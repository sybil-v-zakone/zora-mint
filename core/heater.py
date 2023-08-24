import random

from loguru import logger
from web3 import Web3

from config import zora_rpc, sleep_time, nfts_to_mint
from core.client import ZoraMintClient
from models.database import Database
from utils import sleep


class Heater:
    def __init__(self):
        self.db = Database()

    def warmup(self):
        # wallet: client class
        clients = {}
        for item in self.db.data:
            proxy_kwargs = {"proxies": {"https": f"http://{item.proxy}", "http": f"http://{item.proxy}"}} if item.proxy else {}
            client = ZoraMintClient(
                w3=Web3(Web3.HTTPProvider(endpoint_uri=zora_rpc, request_kwargs=proxy_kwargs)),
                private_key=item.private_key,
                address=item.address,
                proxy=proxy_kwargs
            )
            clients[item.private_key] = client

        while self.db.accounts_remaining > 0:
            active_wallet = random.choice(self.db.data)

            active_client = clients[active_wallet.private_key]

            random_nft = random.choice(active_wallet.nfts_to_mint)

            logger.info(f"Wallet: {active_client.public_key}")

            try:
                tx_res, tx_message = active_client.mint(random_nft, nfts_to_mint[random_nft])

                active_wallet.nfts_to_mint.remove(random_nft)
                if tx_res:
                    logger.success(tx_message)
                else:
                    logger.error(tx_message)
                    active_wallet.error_contracts.append(random_nft)

                self.db.update()

                sleep(sleep_time)

            except Exception as ex:
                logger.error(ex)

        logger.success("Script has ended its work")
        if len(self.db.data) != self.db.accounts_remaining:
            logger.info("Database still contains wallets that had issues while minting")
