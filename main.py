from spotify import Spotify
from billboard import Billboard


def main():
    spot = Spotify()
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

    billboard = Billboard()
    song_titles = billboard.scrape_songs(date)

    if not song_titles:
        print("No songs found to add to the playlist.")
        return

    print(f"Scraped Songs: {song_titles}")

    spot.create_playlist(date)

    if spot.add_songs_to_playlist(song_titles):
        print("Songs added to playlist successfully")
    else:
        print("Error adding songs to the playlist")


if __name__ == "__main__":
    main()