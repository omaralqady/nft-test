from brownie import accounts, network, config, LinkToken, VRFCoordinatorMock

LOCAL_BLOCKCHAINS = ["development", "ganache-local"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"

contract_to_mock = {"link_token": LinkToken, "vrf_coordinator": VRFCoordinatorMock}


def get_network_config(property):
    return config["networks"][network.show_active()][property]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    elif id:
        return accounts.load(id)
    elif network.show_active() in LOCAL_BLOCKCHAINS:
        return accounts[0]

    return accounts.add(config["wallets"]["from_key"])


def get_contract(contract_name):
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAINS:
        if len(contract_type) <= 0:
            deploy_mocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )

    return contract


def deploy_mocks():
    print(f"The active network is: {network.show_active()}")
    print("Deploying mocks...")
    account = get_account()
    link_token = LinkToken.deploy({"from": account})
    VRFCoordinatorMock.deploy(link_token.address, {"from": account})
    print("Mocks deployed")
