import json
from functools import wraps

from loguru import logger
from tqdm import tqdm
import random
import time

from web3 import Web3

from config import eth_rpc


def read_file_by_lines(file_path) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            return [line.strip() for line in file]
    except FileNotFoundError as e:
        logger.error(f"{str(e)} while try to open \"{file_path}\"")
    except Exception as e:
        logger.error(f"{str(e)} while open txt file: \"{file_path}\"")


def read_from_json(file_path):
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        logger.error(f"File '{file_path}' not found.")
        exit()
    except Exception as e:
        logger.error(f"Error while reading a JSON file '{file_path}': {e}.")
        exit()


def sleep(sleep_range: list):
    try:
        for _ in tqdm(range(random.randint(*sleep_range)), colour="#ff8e76"):
            time.sleep(1)
    except Exception as e:
        logger.error(f"Sleep error: {str(e)}")


def gas_delay(gas_threshold: int, delay_range: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                current_eth_gas_price = get_eth_gas_fee()
                threshold = Web3.to_wei(gas_threshold, "gwei")
                if current_eth_gas_price > threshold:
                    random_delay = random.randint(delay_range[0], delay_range[1])

                    logger.warning(
                        f"Current gas fee '{current_eth_gas_price}' wei > Gas threshold '{threshold}' wei. Waiting for {random_delay} seconds..."
                    )

                    with tqdm(total=random_delay, desc="Waiting", unit="s", dynamic_ncols=True, colour="#FFD700") as pbar:
                        for _ in range(random_delay):
                            time.sleep(1)
                            pbar.update(1)
                else:
                    break

            return func(*args, **kwargs)

        return wrapper

    return decorator


def get_eth_gas_fee():
    w3 = Web3(Web3.HTTPProvider(eth_rpc))
    return w3.eth.gas_price
