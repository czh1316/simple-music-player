import os

MUSIC_DIR = "assets/music"


class Playlist:
    def __init__(self):
        self.songs = []
        self.current_index = 0
        self.load_songs()

    def load_songs(self):
        if os.path.exists(MUSIC_DIR):
            self.songs = [
                f for f in os.listdir(MUSIC_DIR)
                if f.endswith(".mp3")
            ]

    def get_current_song(self):
        if self.songs:
            return os.path.join(MUSIC_DIR, self.songs[self.current_index])
        return None

    def next_song(self):
        if self.songs:
            self.current_index = (self.current_index + 1) % len(self.songs)

    def prev_song(self):
        if self.songs:
            self.current_index = (self.current_index - 1) % len(self.songs)