from eth_account import Account
from mnemonic import Mnemonic
import base58
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

def all_lines(filepath: str):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines if line.strip()] or False
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return False

def add_line(filepath: str, line: str):
    with open(filepath, 'a') as file:
        file.write(line + '\n')

def clear_file(filepath: str):
    with open(filepath, 'w') as file:
        file.truncate(0)

def seed_to_evm_keypair(seed_phrase, account_index=0):
    try:
        Account.enable_unaudited_hdwallet_features()
        account = Account.from_mnemonic(
            seed_phrase.strip(),
            account_path=f"m/44'/60'/{account_index}'/0/0"
        )
        return {
            "address": account.address,
            "private_key": "0x" + account.key.hex(),
            "chain": "evm"
        }
    except Exception as e:
        print(f"Ошибка EVM: {str(e)}")
        return None

def seed_to_solana_keypair(seed_phrase, account_index=0):
    try:
        seed_bytes = Bip39SeedGenerator(seed_phrase.strip()).Generate()
        bip44_chg = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA) \
            .Purpose() \
            .Coin() \
            .Account(account_index) \
            .Change(Bip44Changes.CHAIN_EXT)
        private_key = bip44_chg.PrivateKey().Raw().ToBytes()
        public_key = bip44_chg.PublicKey().RawCompressed().ToBytes()[1:]  # Убираем префикс

        private_key_full = private_key + public_key
        public_key_base58 = base58.b58encode(public_key).decode()
        private_key_base58 = base58.b58encode(private_key_full).decode()

        return {
            "address": public_key_base58,
            "private_key": private_key_base58,
            "chain": "solana"
        }
    except Exception as e:
        print(f"Ошибка Solana: {str(e)}")
        return None

if __name__ == '__main__':
    print("[1] Mnemonic -> Private Key (EVM)")
    print("[2] Private Key -> Address (EVM)")
    print("[3] Mnemonic -> Address (EVM)")
    print("[4] Mnemonic -> Private Key (Solana)")
    print("[5] Mnemonic -> Address (Solana)")
    try:
        action = int(input("\n> "))
    except ValueError:
        print("Ошибка: Введите число от 1 до 5.")
        exit()

    mnemonics = all_lines(filepath="mnemonics.txt")
    if not mnemonics:
        print("Файл mnemonics.txt пуст или не существует.")
        exit()

    if action in [1, 3, 4, 5]:
        if action == 1:
            clear_file(filepath="private_keys_evm.txt")
            for mnemonic in mnemonics:
                wallet = seed_to_evm_keypair(mnemonic)
                if wallet:
                    add_line(filepath="private_keys_evm.txt", line=wallet["private_key"])
        elif action == 3:
            clear_file(filepath="addresses_evm.txt")
            for mnemonic in mnemonics:
                wallet = seed_to_evm_keypair(mnemonic)
                if wallet:
                    add_line(filepath="addresses_evm.txt", line=wallet["address"])
        elif action == 4:
            clear_file(filepath="private_keys_solana.txt")
            for mnemonic in mnemonics:
                wallet = seed_to_solana_keypair(mnemonic)
                if wallet:
                    add_line(filepath="private_keys_solana.txt", line=wallet["private_key"])
        elif action == 5:
            clear_file(filepath="addresses_solana.txt")
            for mnemonic in mnemonics:
                wallet = seed_to_solana_keypair(mnemonic)
                if wallet:
                    add_line(filepath="addresses_solana.txt", line=wallet["address"])
    elif action == 2:
        private_keys = all_lines(filepath="private_keys_evm.txt")
        if private_keys:
            clear_file(filepath="addresses_evm.txt")
            for private_key in private_keys:
                try:
                    account = Account.from_key(private_key.strip())
                    add_line(filepath="addresses_evm.txt", line=account.address)
                except Exception as e:
                    print(f"Ошибка для ключа: {str(e)}")
        else:
            print("Файл private_keys_evm.txt пуст или не существует.")
    else:
        print("Ошибка: Неверный выбор действия. Введите число от 1 до 5.")
