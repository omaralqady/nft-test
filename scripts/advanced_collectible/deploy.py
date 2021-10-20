from scripts.utils import (
    OPENSEA_URL,
    get_account,
    get_network_config,
    get_contract,
    fund_with_link,
)
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
    fund_with_link(advanced_collectible.address)
    tx = advanced_collectible.createCollectible({"from": account})
    tx.wait(1)
    print("Token has been created")
    return advanced_collectible, tx


def main():
    deploy()
