from pywallet import wallet



def create_wallet():

    seed = wallet.generate_mnemonic()
    w = wallet.create_wallet(network="BTC", seed=seed, children=1)
    w["coin"] = "UCW"
    w["balance"] = 0

    #Add Wallet to DB as well
    
    return w


def transfer_coins(fromWallet,toWallet,balanceTransfer):


    if fromWallet["balance"] >= balanceTransfer:
        fromWallet["balance"] -= balanceTransfer
        toWallet["balance"] += balanceTransfer
        return True,{"fromWallet":fromWallet,"toWallet":toWallet}
    return False,{"fromWallet":fromWallet,"toWallet":toWallet}

