Asset Renamer Tool - Developer Documentation
============================================

Introduction
------------
Welcome to the Asset Renamer Tool developer documentation. This document provides details on the structure of the code, the functionality of the classes, and guidelines for contributing to the development of the tool.

Folder Structure
----------------
The project follows a standard Python package structure:
```
asset-renamer-tool/
│
├── src/
│   ├── asset_renamer_tool/
│         ├── __init__.py
│         ├── asset_renamer.py
|         |── scene_asset_gui/
|               |── __init__.py
|               |── asset_renamer_gui.py
|               |── scene_assets.txt
│
├── tests/
│   ├── __init__.py
│   ├── test_asset_renamer.py
│
├── docs/
│   ├── user/
│       ├── user_documentation.md
│   ├── developer/
│       |── developer_documentation.md
│
├── examples/
│   ├── __init__.txt
│   ├── example_scene.txt
│   └── example.py
│
├── .gitignore
├── README.md
|── run.py
└── setup.py
```
src/: Contains the source code of the Asset Renamer Tool.
tests/: Includes test files for the code in the src/ directory.
docs/: Documentation files, including user and developer documentation.
examples/: Example files demonstrating the usage of the tool.

Code Structure
---------------
AssetRenamer Class:

The AssetRenamer class is responsible for renaming asset instances in a scene. It has the following attributes:

scene_lines (list): List of strings representing the scene.
asset_pattern (re.Pattern): Regular expression pattern for extracting asset names and instances.
asset_mapping (dict): Dictionary to store mapping of old names to new names.
final_list (list): List to store the final renamed asset instances.
unique_assets (set): Set to store unique asset names.

Methods:

__init__(self, scene_lines):
Initializes the class instance with the provided scene_lines.

rename_assets(self):
Renames asset instances sequentially and returns the updated asset names and unique asset names.

Code Style
The code follows the PEP 8 style guide. To ensure code consistency.

Testing
Use the tests/ directory for writing test cases. Run tests using a test runner such as pytest. Ensure that all tests pass before submitting changes.