# Installations
# Make sure to install the required packages in your Streamlit environment
# You can use the following commands:
# !pip install streamlit google-api-python-client python-docx python-dotenv

import streamlit as st
from dotenv import dotenv_values
from googleapiclient.discovery import build
from docx import Document

# Load environment variables from the .env file into a dictionary
environment_vars = dotenv_values('.env')

# Get the credential values from the '.env' file
my_api_key = environment_vars.get("API_KEY")

# Enter your API key here
api_key = my_api_key

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

def main():
    st.title("YouTube Playlist Video Organizer")

    # Get the playlist URL from the user
    playlist_url = st.text_input("Enter the playlist URL:")

    # Get repetitive terms from the user
    repetitive_terms = st.text_input("Enter repetitive terms (comma-separated):")
    repetitive_terms = [term.strip().upper() for term in repetitive_terms.split(',')]

    if st.button("Organize Videos"):
        organize_videos(playlist_url, repetitive_terms)

def organize_videos(playlist_url, repetitive_terms):
    # Create a Word document
    doc = Document()

    # Get the playlist ID from the URL
    playlist_id = playlist_url.split("list=")[1]

    # Define the repetitive terms and headings
    headings = {}

    # Get all the video details from the playlist
    videos = []
    next_page_token = None

    while True:
        # Get the playlist items
        playlist_items = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        # Get the video IDs
        video_ids = [item['contentDetails']['videoId'] for item in playlist_items['items']]

        # Get the video details
        video_details = youtube.videos().list(
            part="snippet",
            id=','.join(video_ids)
        ).execute()

        # Add the videos to the list
        for item in video_details['items']:
            title = item['snippet']['title']
            video_id = item['id']
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            # Group videos based on the repetitive terms
            found = False
            for term in repetitive_terms:
                if term in title.upper():
                    if term not in headings:
                        headings[term] = chr(len(headings) + 65)
                    videos.append({"title": title, "url": video_url, "group": headings[term]})
                    found = True
                    break

            # Add videos without repetitive terms to Introduction or Conclusion
            if not found:
                if item == video_details['items'][0]:
                    videos.append({"title": title, "url": video_url, "group": "Introduction"})
                elif item == video_details['items'][-1]:
                    videos.append({"title": title, "url": video_url, "group": "Conclusion"})

        # Check if there are more pages
        next_page_token = playlist_items.get('nextPageToken')

        if not next_page_token:
            break

    # Print the video titles and URLs grouped by the headings
    for group in sorted(headings.values()):
        doc.add_paragraph(f"\n{group}. {list(headings.keys())[list(headings.values()).index(group)]}")
        count = 1
        for video in videos:
            if video['group'] == group:
                doc.add_paragraph(f"{group}.{count} {video['title']} - {video['url']}")
                count += 1

    # Print videos without repetitive terms under Introduction or Conclusion
    for group in ["Introduction", "Conclusion"]:
        doc.add_paragraph(f"\n{group}")
        count = 1
        for video in videos:
            if video['group'] == group:
                doc.add_paragraph(f"{group}.{count} {video['title']} - {video['url']}")
                count += 1

    # Save the document
    doc.save("organized_videos.docx")

if __name__ == "__main__":
    main()