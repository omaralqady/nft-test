from scripts.utils import get_account
from brownie import SimpleCollectible

uri = "https://test/"


def deploy():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(uri, {"from": account})
    tx.wait(1)
    return simple_collectible


def main():
    deploy()
