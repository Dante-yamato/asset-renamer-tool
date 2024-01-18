import tkinter as tk
from tkinter import filedialog
from src.asset_renamer_tool.asset_renamer import AssetRenamer

class AssetRenamerGUI:
    """
    GUI for the Asset Renamer Tool.
    """
    def __init__(self, root):
        """
        Initialize the GUI.

        Parameters:
            root (tk.Tk): The Tkinter root window.
        """
        self.root = root
        self.root.title("Asset Renamer Tool")

        # Create a Text widget for displaying scene lines
        self.scene_text = tk.Text(root, height=10, width=50)
        self.scene_text.pack(pady=10)

        # Button to open a file dialog
        open_button = tk.Button(root, text="Open Scene File", command=self.open_file)
        open_button.pack(pady=10)

        # Button to run the asset renamer
        run_button = tk.Button(root, text="Run Asset Renamer", command=self.run_renamer)
        run_button.pack(pady=10)

    def open_file(self):
        """
        Open a file dialog to select a scene file and display its content in the GUI.
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                scene_content = file.read()
            self.scene_text.delete('1.0', tk.END)  # Clear previous content
            self.scene_text.insert(tk.END, scene_content)

    def run_renamer(self):
        """
        Run the asset renamer tool and display the results in a new window.
        """
        scene_lines = self.scene_text.get("1.0", tk.END).splitlines()
        asset_renamer = AssetRenamer(scene_lines)
        updated_scene, unique_assets = asset_renamer.rename_assets()

        # Display the updated scene and unique assets in a new window
        result_window = tk.Toplevel(self.root)
        result_window.title("Renamer Results")

        updated_scene_text = tk.Text(result_window, height=10, width=50)
        updated_scene_text.pack(pady=10)
        for line in updated_scene:
            updated_scene_text.insert(tk.END, line + "\n")

        unique_assets_label = tk.Label(result_window, text="Unique Assets:")
        unique_assets_label.pack()
        unique_assets_text = tk.Text(result_window, height=5, width=50)
        unique_assets_text.pack(pady=10)
        unique_assets_text.insert(tk.END, "\n".join(unique_assets))
