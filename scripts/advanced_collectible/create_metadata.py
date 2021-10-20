from brownie import AdvancedCollectible, network
from scripts.utils import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path


def main():
    advanced_collectible = AdvancedCollectible[-1]
    num_of_collectibles = advanced_collectible.tokenCtr()
    print(f"{num_of_collectibles} collectibles created so far!")

    for token_id in range(num_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectibe_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists!")
        else:
            print(f"Creating metadata file: {metadata_file_name}")
            collectibe_metadata["name"] = breed
            collectibe_metadata["description"] = f"A cute {breed} puppy"
