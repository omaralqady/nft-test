from scripts.utils import LOCAL_BLOCKCHAINS, get_account
from scripts.deploy import deploy
from brownie import network
import pytest


def test_can_deploy():
    if network.show_active() not in LOCAL_BLOCKCHAINS:
        pytest.skip()
    simple_collectible = deploy()

    assert simple_collectible.ownerOf(0) == get_account()
