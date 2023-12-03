# YouTube-Playlist-Organizer
The YouTube Playlist Organizer is a Python program designed to assist in organizing your learning journey when studying from large YouTube playlists. It automates the process of categorizing and organizing videos based on their subjects, making it easier to track your progress and access specific videos within the playlist.

# Introduction
As a Data Science and Machine Learning enthusiast, I often found it challenging to keep up with my progress while studying from large YouTube playlists, such as the **Alex The Analyst Bootcamp** (https://www.youtube.com/watch?v=rGx1QNdYzvs&list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF). It became difficult to remember which video I had last watched, leading to wasted time searching for the next video or revisiting ones unnecessarily. To solve this problem, I developed the YouTube Playlist Organizer, which utilizes the YouTube Data API to fetch video details and organizes them into a structured study guide.

<p align="center">
  <img src="https://github.com/rasmodev/YouTube-Playlist-Organizer/blob/main/images/main.jpg" alt="App Screenshot">
  <br>
  <b>App Screenshot</b>
</p>


# Features
Fetches video details from a YouTube playlist URL using the YouTube Data API. Categorizes videos based on repetitive terms in their titles. Generates a Word document study guide with categorized videos. Provides easy access to video titles and links within the study guide. Simplifies tracking progress and navigating through large playlists.

# Getting Started
To use the YouTube Playlist Organizer, follow the steps below.

## Prerequisites
Python 3.7 or above installed on your machine. Access to the YouTube Data API. API credentials (API key) for the YouTube Data API.

## Installation
Clone or download the YouTube Playlist Organizer program files from this GitHub repository.
Install the required Python packages

## Authentication
Obtain the necessary API credentials by following these steps: Go to the Google Developers Console (https://console.developers.google.com/). Create a new project or select an existing one. Enable the YouTube Data API for the project. Create API credentials (API key) for the project. Open the Jupyter Notebook **youtube_playlist_organizer.ipynb** in a text editor. Locate the line that says **"YOUR_API_KEY_HERE"** and replace it with your YouTube Data API key obtained earlier.

## Usage
Follow the prompts in the terminal and enter the URL of the YouTube playlist you want to organize. The program will fetch the video details, categorize them, and generate a Word document named **organized_videos.docx** as the organized study guide.

# How It Works
The YouTube Playlist Organizer utilizes the YouTube Data API to fetch video details from the provided playlist URL. It categorizes the videos based on repetitive terms found in their titles (e.g., Excel, Power BI, SQL, Python). Videos with repetitive terms are grouped under their respective headings (A, B, C, D) in the study guide, while videos without repetitive terms are grouped under "Introduction" (for the first video) or "Conclusion" (for the last video).

# Contributing
Contributions to the YouTube Playlist Organizer project are welcome!

# License
The YouTube Playlist Organizer project is released under the MIT license. For more information, please refer to the LICENSE file in the repository.

If you have any questions or need further assistance, feel free to reach out or create an issue in the GitHub repository. Happy organizing!
