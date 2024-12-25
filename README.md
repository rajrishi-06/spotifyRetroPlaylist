**Spotify Billboard Playlist Creator:**
  This project allows users to create a Spotify playlist from Billboard’s Hot 100 songs for a specific date.
It integrates with the Spotify API for playlist creation and adds the top songs from the Billboard Hot 100 chart for the specified date.

---------------------------------------------------------------------------------------------------------------------------------------
**Features:**
	•	Scrape Billboard’s Hot 100 songs for a given date.
	•	Search for these songs on Spotify.
	•	Create a new Spotify playlist with the found songs.
 
---------------------------------------------------------------------------------------------------------------------------------------
**Installation:**
Prerequisites
	1.	Python 3.8 or above
	2.	Spotify Developer Account
Create a Spotify developer account and generate your Client ID and Client Secret.
	3.	Install Required Python Packages
    **•	Core Packages**
	      •	os - For interacting with the operating system and environment variables.
      	•	dotenv - For managing environment variables from a .env file.
      	•	json - For working with JSON data.
      	•	requests - For making HTTP requests to APIs like Spotify.
	  **•	Web Scraping**
	      •	BeautifulSoup (from bs4) - For parsing and scraping HTML from web pages.
	  **•	Debugging and Development**
      	•	logging - For structured and detailed logging (optional, but useful).
      	•	webbrowser - For opening URLs in the default web browser (used for Spotify authentication).
       
---------------------------------------------------------------------------------------------------------------------------------------
**Clone the Repository:**
git clone https://github.com/your-username/spotify-billboard-playlist.git
cd spotify-billboard-playlist

---------------------------------------------------------------------------------------------------------------------------------------
**Usage:**
	1.	Set Up Environment Variables
Create a .env file in the project root directory and add the following:

CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=http://localhost:8888/callback
USER_ID=your_spotify_user_id
PLAYLIST_ID=your_existing_playlist_id (optional, leave empty if not applicable)

	2.	Run the Program
Run the main.py file and follow the prompts:
python main.py
	3.	Enter the Date
Enter the date in the format YYYY-MM-DD when prompted to scrape songs from that date.

---------------------------------------------------------------------------------------------------------------------------------------
**File Structure:**
spotify-billboard-playlist/
├── billboard.py          # Scrapes Billboard Hot 100 songs for a specific date.
├── spotify.py            # Handles Spotify API interactions (playlist creation, song search).
├── main.py               # Main entry point of the program.
├── .env                  # Environment variables for sensitive data (not tracked by Git).
├── .gitignore            # Files and folders to ignore in Git.
├── README.md             # Project documentation.
├── requirements.txt      # Python dependencies.
└── __pycache__/          # Auto-generated Python cache files (ignored).

---------------------------------------------------------------------------------------------------------------------------------------
**Contributing:**
Feel free to fork the repository and submit pull requests for improvements. All contributions are welcome!

---------------------------------------------------------------------------------------------------------------------------------------
**License:**
This project is licensed under the MIT License.

---------------------------------------------------------------------------------------------------------------------------------------
**Acknowledgments:**
	•	BeautifulSoup for web scraping.
	•	Spotify API for enabling playlist creation and song search.
