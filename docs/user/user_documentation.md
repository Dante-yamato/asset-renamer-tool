Asset Renamer Tool - User Documentation
=======================================
Introduction
------------
Welcome to the Asset Renamer Tool user documentation. This tool is designed to help users efficiently rename asset instances in a scene. The graphical user interface (GUI) allows for an intuitive and user-friendly experience.

Features
--------
1. Opening a Scene

To get started, follow these steps:

Run the script (run.py).
Click the "Open Scene File" button.
Select the scene file you want to process using the file dialog.
The content of the scene file will be displayed in the text area.

2. Running the Asset Renamer

Once you've opened a scene file, you can proceed to run the asset renamer:

Click the "Run Asset Renamer" button.
The tool will process the scene content and update the instances of each asset sequentially.
A new window will appear, showing the updated scene and a list of unique asset names.

3. Viewing Results

The results window will display:

The updated scene with sequentially numbered instances.
A list of unique asset names found in the scene.

Requirements
-------------
The Asset Renamer Tool has the following requirements:

Python 3.x (Tested on Python 3.7+)
No additional installations are necessary, as the tool uses the standard tkinter library for the GUI.

Example
-------
Let's illustrate the tool with a simple example:

Original Scene:
plantClover01x01
plantClover02x02
plantClover01x07
plantClover01x09

After running the asset renamer, the updated scene might look like this:

Updated Scene:
plantClover01x01
plantClover01x02
plantClover01x03
plantClover02x01

And the unique assets found:

Unique Assets:
plantClover01
plantClover02

Troubleshooting
---------------
If you encounter any issues or have questions, please refer to the CONTRIBUTING.md file for information on reporting problems or seeking assistance.