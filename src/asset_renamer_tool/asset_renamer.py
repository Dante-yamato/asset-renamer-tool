"""
This module provides a class, AssetRenamer,
for renaming asset instances in a scene and
return the updated scene lines along with unique asset names.
"""

import re


class AssetRenamer:
    """Class for renaming asset instances in a scene.

    Attributes:
        scene_lines (list): List of strings representing the scene.

        asset_pattern (re.Pattern): Regular expression pattern for
        extracting asset names and instances.

        asset_mapping (dict): Dictionary to store mapping
        of old names to new names.

        final_list (list): List to store the final renamed asset instances.

        unique_assets (set): Set to store unique asset names.

    Methods:
        rename_assets: Rename asset instances sequentially
        and return the updated scene_lines list and unique scene_lines list.
    """

    def __init__(self, scene_lines):
        self.scene_lines = scene_lines
        self.asset_pattern = re.compile(r'([a-zA-Z]+[0-9]+)x([0-9]+)')
        self.asset_mapping = {}
        self.final_list = []
        self.unique_assets = set()

    def rename_assets(self):
        """
        Rename asset instances sequentially.

        Returns: 
            self.final_list(list): Updated asset names.
            self.unique_assets(list): Unique asset names.
        """
        for line in self.scene_lines:
            # Extract asset name and instance using regex
            match = re.match(self.asset_pattern, line)
            if match:
                asset_name, instance = match.groups()
                instance = int(instance)
            else:
                print(f"Invalid asset name provided: {line}")
                continue

            self.unique_assets.add(asset_name)

            if asset_name in self.asset_mapping:
                instance_number = self.asset_mapping[asset_name] + 1
                self.asset_mapping[asset_name] = instance_number
            else:
                self.asset_mapping[asset_name] = 1

            # Create the new line with the updated instance number
            new_line = f'{asset_name}x{self.asset_mapping[asset_name]:02d}'
            self.scene_lines[self.scene_lines.index(line)] = new_line
            self.final_list.append(new_line)

        return sorted(self.final_list), sorted(list(self.unique_assets))
