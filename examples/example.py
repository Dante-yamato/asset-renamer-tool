from src.asset_renamer_tool.asset_renamer import AssetRenamer

def run_example():
    # Example scene as a list of strings
    example_scene_lines = [
        "plantClover01x01",
        "plantClover02x02",
        "plantClover01x07",
        "plantClover01x09",
        "plantFern01x001",
        "plantFern03x01",
        "plantFern01x01",
        "plantFern01x03",
    ]

    # Create an AssetRenamer object
    asset_renamer = AssetRenamer(example_scene_lines)

    # Rename assets and retrieve the results
    updated_scene, unique_assets = asset_renamer.rename_assets()

    # Display the results
    print("Updated Scene:")
    for line in updated_scene:
        print(line)

    print("\nUnique Assets:")
    print(unique_assets)

# Run the example when the script is executed
if __name__ == "__main__":
    run_example()