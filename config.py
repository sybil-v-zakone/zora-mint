# путь до файла с приватниками
private_keys_file = "data/private_keys.txt"

# путь до файла с данными от прокси
proxies_file = "data/proxies.txt"

# путь до файла базы данных
database_file = "data/database.json"

# адреса NFT в сети Zora и количество для бесплатного минта (адрес: количество)
nfts_to_mint = {
    "0x8A43793D26b5DBd5133b78A85b0DEF8fB8Fce9B3": 99,
    "0x53cb0B849491590CaB2cc44AF8c20e68e21fc36D": 3,
    "0x4de73D198598C3B4942E95657a12cBc399E4aDB5": 1,
    "0x266b7E8Df0368Dd4006bE5469DD4EE13EA53d3a4": 3,
    "0xFa177a7eDC2518E70F8f8Ee159fA355D6b727257": 3,
    "0x4073a52A3fc328D489534Ab908347eC1FcB18f7f": 3,
    "0x12B93dA6865B035AE7151067C8d264Af2ae4be8E": 10,
    "0x48D913ee06B66599789F056A0e48Bb45Caf3b4e9": 3,
    "0x8974B96dA5886Ed636962F66a6456DC39118A140": 3,
    "0xC47ADb3e5dC59FC3B41d92205ABa356830b44a93": 2,
    "0x9eAE90902a68584E93a83D7638D3a95ac67FC446": 3,
    "0xbC2cA61440fAF65a9868295Efa5d5D87c55B9529": 4,
    "0xb096832A6ccD9053fe7a0EF075191Fe342D1AB75": 2,
    "0x8f1B6776963bFcaa26f4e2a41289cFc3F50eD554": 2,
    "0xA85B9F9154db5bd9C0b7F869bC910a98ba1b7A87": 3,
    "0xd46760C832960eEBd81391aC5DC8502A778B24Ec": 1,
}

# автогенерация базы данных; True - вкл, False - выкл
database_autocreate = True

# минимальный баланс для совершения минта
min_balance = 0.0001

# время между бриджами, [от, до] (выбирается рандомное число)
sleep_time = [10, 30]

# множитель для расчета цен на газ для транзакции
gas_multiplier = 1.5

# максимальная цена газа в Gwei, при которой будет проводиться бридж
gas_threshold = 20

# диапазон времени задержки между проверками текущей цены газа в секундах
gas_delay_range = [10, 15]

# используемая rpc для Zora
zora_rpc = "https://rpc.zora.energy"

# использумая rpc для Ethereum (mainnet)
eth_rpc = "https://rpc.ankr.com/eth"
