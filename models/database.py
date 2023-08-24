import json
import random

from loguru import logger

from models.data_item import DataItem
from utils import read_file_by_lines, read_from_json
from config import (
    private_keys_file,
    proxies_file,
    nfts_to_mint,
    database_file,
    database_autocreate,
    use_proxy
)


class Database:
    def __init__(self, create_once=False):
        self.data: list[DataItem] = list[DataItem]()
        if database_autocreate or create_once:
            self.create()
            self.accounts_remaining = len(self.data)
        else:
            try:
                dumped = read_from_json(database_file)
                self.parse_data_items(dumped["data"])
                self.accounts_remaining = dumped['accounts_remaining']
                logger.success(f"Database has been loaded")
            except Exception as ex:
                logger.error(f"Seems like database file is wrongly formatted: {ex}")

    def dump(self):
        try:
            with open(database_file, 'w') as fp:
                json.dump(self, fp=fp, default=lambda o: o.__dict__)
        except Exception as ex:
            logger.error(f"Database to json object error: {str(ex)}")

    def parse_data_items(self, wallets: dict):
        for item in wallets:
            wallet = DataItem(
                private_key=item['private_key'],
                proxy=item['proxy'],
                nfts_to_mint=item['nfts_to_mint'],
                error_contracts=item['error_contracts']
            )
            self.data.append(wallet)

    def create(self):
        try:
            private_keys = read_file_by_lines(private_keys_file)
            proxies = read_file_by_lines(proxies_file)

            if use_proxy and len(private_keys) != len(proxies):
                logger.error("\'use_proxy\' is set to True, but wallets and proxies files\' length doesn't match")
                exit()

            try:
                for key in private_keys:
                    key_index = private_keys.index(key)
                    proxy = proxies[key_index] if use_proxy else None
                    nfts_start_list = list(nfts_to_mint)
                    data_item = DataItem(
                        private_key=key,
                        proxy=proxy,
                        nfts_to_mint=nfts_start_list
                    )
                    self.data.append(data_item)
            except Exception as ex:
                logger.error(f"Error while reading data when creating database: {str(ex)}")

            self.dump()
            logger.success(f"Database has been created")
        except Exception as ex:
            logger.error(f"Database creation failed: {str(ex)}")

    def update(self):
        for item in self.data:
            if len(item.nfts_to_mint) == 0:
                self.accounts_remaining -= 1
            if len(item.nfts_to_mint) == 0 and len(item.error_contracts) == 0:
                self.data.remove(item)  
        self.dump()
        logger.success("Database has been updated")
