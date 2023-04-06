from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/10a0474ab06f4b108a7929249580de4c'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(f"Your address: {address}\nYour key: {privateKey}")