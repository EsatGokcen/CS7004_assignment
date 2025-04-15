import tkinter as tk

class Controls:
    def __init__(self, master: tk.Tk):
        self.frame = tk.Frame(master, padx=10, pady=10)

        self.start_button = tk.Button(self.frame, text="Start", command=self.start)
        self.pause_button = tk.Button(self.frame, text="Pause", command=self.pause)
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)

        self.start_button.pack(fill="x")
        self.pause_button.pack(fill="x", pady=5)
        self.reset_button.pack(fill="x")

        # Placeholder callbacks, to be set from main_window
        self.on_start = lambda: None
        self.on_pause = lambda: None
        self.on_reset = lambda: None

    def start(self):
        self.on_start()

    def pause(self):
        self.on_pause()

    def reset(self):
        self.on_reset()
