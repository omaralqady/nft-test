from scripts.utils import OPENSEA_URL, get_account, get_network_config, get_contract
from brownie import AdvancedCollectible


def deploy():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        get_network_config("keyhash"),
        get_network_config("fee"),
        {"from": account},
    )
    return advanced_collectible


def main():
    deploy()
