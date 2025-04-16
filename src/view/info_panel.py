import tkinter as tk

class InfoPanel:
    def __init__(self, master: tk.Tk):
        self.frame = tk.Frame(master, padx=10, pady=10)

        self.step_label = tk.Label(self.frame, text="Step: 0")
        self.hunters_label = tk.Label(self.frame, text="Hunters: 0")
        self.knights_label = tk.Label(self.frame, text="Knights: 0")
        self.bronze_label = tk.Label(self.frame, text="Bronze Collected: 0")
        self.silver_label = tk.Label(self.frame, text="Silver Collected: 0")
        self.gold_label = tk.Label(self.frame, text="Gold Collected: 0")

        self.step_label.pack(anchor="w")
        self.hunters_label.pack(anchor="w")
        self.knights_label.pack(anchor="w")
        self.bronze_label.pack(anchor="w")
        self.silver_label.pack(anchor="w")
        self.gold_label.pack(anchor="w")

    def update_info(self, step: int, hunters: int, knights: int, bronze: int, silver: int, gold: int):
        self.step_label.config(text=f"Step: {step}")
        self.hunters_label.config(text=f"Hunters: {hunters}")
        self.knights_label.config(text=f"Knights: {knights}")
        self.bronze_label.config(text=f"Bronze Collected: {bronze}")
        self.silver_label.config(text=f"Silver Collected: {silver}")
        self.gold_label.config(text=f"Gold Collected: {gold}")



