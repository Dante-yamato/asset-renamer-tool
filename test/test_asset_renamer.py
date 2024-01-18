import unittest
from src.asset_renamer_tool.asset_renamer import AssetRenamer

class TestAssetRenamer(unittest.TestCase):

    def test_rename_assets(self):
        # Test case with a provided scene
        scene_lines = [
            "plantClover01x01",
            "plantClover02x02",
            "plantClover01x07",
            "plantClover01x09",
            "plantFern01x001",
            "plantFern03x01",
            "plantFern01x01",
            "plantFern01x03",
        ]

        asset_renamer = AssetRenamer(scene_lines)
        updated_scene, unique_assets = asset_renamer.rename_assets()

        # Assert the correctness of the updated scene
        expected_updated_scene = [
            "plantClover01x01",
            "plantClover01x02",
            "plantClover01x03",
            "plantClover02x01",
            "plantFern01x01",
            "plantFern01x02",
            "plantFern01x03",
            "plantFern03x01",
        ]
        self.assertEqual(updated_scene, expected_updated_scene)

        # Assert the correctness of unique assets
        expected_unique_assets = ["plantClover01", "plantClover02", "plantFern01", "plantFern03"]
        self.assertEqual(unique_assets, expected_unique_assets)

if __name__ == '__main__':
    unittest.main()
