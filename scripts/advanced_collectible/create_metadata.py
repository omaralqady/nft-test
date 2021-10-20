from brownie import AdvancedCollectible, network
from scripts.utils import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os

ipfs_localhost = "http://127.0.0.1:5001"

# hashes will always be the same in IPFS, therefore once uploaded, there is no
# need to re-upload on different runs/deploys
breed_to_image = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}


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
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"

            image_uri = None
            if os.getenv("UPLOAD_TO_IPFS") == "true":
                image_uri = upload_to_ipfs(image_path)
            image_uri = image_uri if image_uri else breed_to_image[breed]

            collectibe_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectibe_metadata, file)

            if os.getenv("UPLOAD_TO_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        endpoint = ipfs_localhost + "/api/v0/add"

        res = requests.post(endpoint, files={"file": image_binary})
        ipfs_hash = res.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
