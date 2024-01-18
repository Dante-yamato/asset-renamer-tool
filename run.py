"""Run this file to test the code"""
from src.asset_renamer_tool.scene_asset_gui.asset_renamer_gui import AssetRenamerGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = AssetRenamerGUI(root)
    root.mainloop()
