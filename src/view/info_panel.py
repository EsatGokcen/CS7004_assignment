import tkinter as tk

class InfoPanel:
    def __init__(self, master: tk.Tk):
        self.frame = tk.Frame(master, padx=10, pady=10)

        self.step_label = tk.Label(self.frame, text="Step: 0")
        self.hunters_label = tk.Label(self.frame, text="Hunters: 0")
        self.knights_label = tk.Label(self.frame, text="Knights: 0")
        self.treasure_label = tk.Label(self.frame, text="Treasure Collected: 0")

        self.step_label.pack(anchor="w")
        self.hunters_label.pack(anchor="w")
        self.knights_label.pack(anchor="w")
        self.treasure_label.pack(anchor="w")

    def update_info(self, step: int, hunters: int, knights: int, collected: int) -> None:
        self.step_label.config(text=f"Step: {step}")
        self.hunters_label.config(text=f"Hunters: {hunters}")
        self.knights_label.config(text=f"Knights: {knights}")
        self.treasure_label.config(text=f"Treasure Collected: {collected}")

