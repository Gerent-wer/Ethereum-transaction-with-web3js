from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()
private_key = os.getenv("PRIVATE_KEY")

w3 = Web3(Web3.HTTPProvider('https://polygon-mumbai.gateway.tenderly.co'))

account = w3.eth.account.from_key(private_key)

balance = w3.eth.get_balance(account.address)
print(f"Current balance: {w3.from_wei(balance, 'ether')} ETH")

tx = {
    'nonce': w3.eth.get_transaction_count(account.address),
    'chainId': 80001,
    'to': '0xC9d59a78FE51D0A084B9C1F3Ca29Ec0Afa2fadc6',
    'value': w3.to_wei(0.01, 'ether'),
    'gas': 212560,
    'gasPrice': w3.to_wei('20', 'gwei'),
    'data': Web3.to_hex(text='Dima Ivashchenko')
}

signed_tx = account.sign_transaction(tx)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(f'Transaction hash: {tx_hash.hex()}')
