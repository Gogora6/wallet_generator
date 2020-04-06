from generate import KeyGenerator
from ethereum import EthereumWallet
from bitcoin import BitcoinWallet


def generate_ethereum_wallet():
    private_key = KeyGenerator().generate_key()
    ethereum_wallet = EthereumWallet.generate_address(private_key)
    print('Ethereum Wallet :   ', ethereum_wallet)


def generate_bitcoin_wallet():
    private_key = KeyGenerator().generate_key()
    bitcoin_wallet = BitcoinWallet.generate_address(private_key)
    print('Bitcoin Wallet :   ', bitcoin_wallet)


