from scripts.utils import LOCAL_BLOCKCHAINS, get_account, get_contract
from scripts.advanced_collectible.deploy import deploy
from brownie import network
import pytest


def test_can_deploy():
    if network.show_active() not in LOCAL_BLOCKCHAINS:
        pytest.skip()
    advanced_collectible, tx = deploy()
    requestId = tx.events["requestedCollectible"]["requestId"]
    random_num = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_num, advanced_collectible.address, {"from": get_account()}
    )

    assert advanced_collectible.tokenCtr() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_num % 3
