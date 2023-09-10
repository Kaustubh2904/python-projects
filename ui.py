import tkinter as tk
import comtypes
from tkinter import ttk
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Function to get the system's audio output volume
def get_system_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return int(volume.GetMasterVolumeLevelScalar() * 100)

# Function to update the volume label and progress bar
def update_volume():
    current_volume = get_system_volume()
    volume_label.config(text=f"Volume: {current_volume}%")
    volume_bar["value"] = current_volume
    window.after(200, update_volume) 

# Create the main window
window = tk.Tk()
window.title("System Volume Monitor")

# Create a label to display the volume
volume_label = tk.Label(window, text="Volume: 0%")
volume_label.pack(pady=10)

# Create a progress bar to visualize the volume
volume_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
volume_bar.pack()

# Initial update
update_volume()

# Start the tkinter main loop
window.mainloop()

