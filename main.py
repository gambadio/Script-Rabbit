import tkinter as tk
from tkinter import ttk
from integrated_app import IntegratedApp
import sv_ttk
import darkdetect
import sys
import pywinstyles

def apply_theme_to_titlebar(root):
    """Apply theme to the window title bar (Windows only)"""
    if sys.platform != "win32":
        return
        
    version = sys.getwindowsversion()

    if version.major == 10 and version.build >= 22000:
        # Windows 11
        pywinstyles.change_header_color(root, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa")
    elif version.major == 10:
        # Windows 10
        pywinstyles.apply_style(root, "dark" if sv_ttk.get_theme() == "dark" else "normal")
        # Hack to update title bar color
        root.wm_attributes("-alpha", 0.99)
        root.wm_attributes("-alpha", 1)

def setup_window(root):
    """Setup the main window properties"""
    root.title("Script Rabbit")
    # Set a minimum size for the window
    root.minsize(800, 600)
    # Center the window on the screen
    window_width = 1000
    window_height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    
    # Setup window properties
    setup_window(root)
    
    # Apply Sun Valley theme
    sv_ttk.set_theme(darkdetect.theme().lower())  # Use system theme (dark/light)
    
    # Apply theme to title bar on Windows
    apply_theme_to_titlebar(root)
    
    # Create the application
    app = IntegratedApp(root)
    
    # Start the application
    root.mainloop()