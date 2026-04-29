import tkinter as tk
from player import audio
from player.playlist import Playlist

playlist = Playlist()


def play_selected():
    selected = listbox.curselection()
    if selected:
        playlist.current_index = selected[0]

    song = playlist.get_current_song()
    if song:
        audio.load_music(song)
        audio.play()


def pause():
    audio.pause()


def next_song():
    playlist.next_song()
    listbox.selection_clear(0, tk.END)
    listbox.selection_set(playlist.current_index)
    play_selected()


def prev_song():
    playlist.prev_song()
    listbox.selection_clear(0, tk.END)
    listbox.selection_set(playlist.current_index)
    play_selected()


def run_app():
    global listbox

    root = tk.Tk()
    root.title("Music Player")
    root.geometry("400x400")

    listbox = tk.Listbox(root, width=50, height=15)
    listbox.pack(pady=10)

    for song in playlist.songs:
        listbox.insert(tk.END, song)

    tk.Button(root, text="播放", command=play_selected).pack()
    tk.Button(root, text="暂停", command=pause).pack()
    tk.Button(root, text="上一首", command=prev_song).pack()
    tk.Button(root, text="下一首", command=next_song).pack()

    root.mainloop()