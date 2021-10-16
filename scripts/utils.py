from brownie import accounts, network, config

LOCAL_BLOCKCHAINS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    elif id:
        return accounts.load(id)
    elif network.show_active() in LOCAL_BLOCKCHAINS:
        return accounts[0]

    return accounts.add(config["wallets"]["from_key"])
