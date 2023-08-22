from web3 import Web3


class DataItem:
    def __init__(
            self,
            private_key: str,
            proxy: str | None,
            nfts_to_mint=None,
            error_contracts=None
    ):
        if nfts_to_mint is None:
            nfts_to_mint = list[str]()

        if error_contracts is None:
            error_contracts = list[str]()

        self.private_key = private_key
        self.address = Web3.to_checksum_address(Web3().eth.account.from_key(private_key=private_key).address)
        self.proxy = proxy
        self.nfts_to_mint = nfts_to_mint
        self.error_contracts = error_contracts
