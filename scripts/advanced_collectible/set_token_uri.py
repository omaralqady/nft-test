from brownie import network, AdvancedCollectible
from scripts.utils import OPENSEA_URL, get_account, get_breed

dog_metadata = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def main():
    print(f"Working on: {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]

    num_of_collectibles = advanced_collectible.tokenCtr()
    print(f"{num_of_collectibles} uploaded so far!")

    for token_id in range(num_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    # to check if the token URI was set or not yet
    if not advanced_collectible.tokenURI(token_id).startswith("https://"):
        print(f"Setting token URI of {token_id}")
        set_token_uri(token_id, advanced_collectible, dog_metadata[breed])


def set_token_uri(token_id, nft_contract, token_uri):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, token_uri, {"from": account})
    tx.wait(1)
    print(
        f"You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wait up to 20 minutes and hit refresh")
