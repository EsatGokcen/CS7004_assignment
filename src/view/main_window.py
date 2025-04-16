import tkinter as tk
from src.view.grid_view import GridView
from src.view.info_panel import InfoPanel
from src.view.control_panel import Controls

class MainWindow:
    def __init__(self, map_obj):
        self.root = tk.Tk()
        self.root.title("Knights of Eldoria")

        # UI Components
        self.info_panel = InfoPanel(self.root)
        self.info_panel.frame.grid(row=0, column=0, sticky="nw")

        self.controls = Controls(self.root)
        self.controls.frame.grid(row=1, column=0, sticky="sw")

        self.grid_view = GridView(self.root, map_obj)
        self.grid_view.frame.grid(row=0, column=1, rowspan=2)

    def run(self):
        self.root.mainloop()
