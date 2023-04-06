from web3 import Web3

def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/10a0474ab06f4b108a7929249580de4c'))
    address = '0x60b2d33b8530437312ac9634C287be6e86BD035a'
    privateKey = '0x1322fef684cfca05f4221f0ce88ffd18704fc77e31a8b19a60dc3407ece17eed'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId

