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

        # Hook up control callbacks (stubbed for now)
        self.controls.on_start = self.start_simulation
        self.controls.on_pause = self.pause_simulation
        self.controls.on_reset = self.reset_simulation

        # Simulation state (stub)
        self.simulation_step = 0

    def start_simulation(self):
        print("Simulation started")  # Replace with real logic

    def pause_simulation(self):
        print("Simulation paused")  # Replace with real logic

    def reset_simulation(self):
        print("Simulation reset")  # Replace with real logic

    def run(self):
        self.root.mainloop()
