from pywallet import wallet
import hashlib
from datetime import datetime

def create_wallet():

    seed = wallet.generate_mnemonic()
    w = wallet.create_wallet(network="BTC", seed=seed, children=1)
    w["coin"] = "UCW"
    w["balance"] = 0
    try:
        w["wif"] = w["wif"].decode("utf-8")
    except:
        del(w["wif"])
        pass

    #Add Wallet to DB as well

    return w






class Wallets:

    def __init__(self):

        self.wallets = {}
        self.centralwalletResponse = self.addWalet()
        self.centralWalletAddress = self.centralwalletResponse["address"]
        self.centralWallet = self.centralwalletResponse["public"]


    def _setErrorMessage(self,msg):
        operation = {}
        operation["error"] = True
        operation["msg"] = msg
        return operation

    def getCentralWallet(self):
        return self.centralWallet,self.centralWalletAddress

    
    def addWalet(self):

        wallet = create_wallet()

        if "address" not in wallet or "private_key" not in wallet or "coin" not in wallet or "balance" not in wallet:
            operation = self._setErrorMessage("Insufficient Datapoints to create wallet. Must have all the addresses.")
            return operation

        if wallet["address"] in self.wallets:

            operation = self._setErrorMessage("Wallet can't be created as public address already in use. Try pinging again.")
            return operation

        publicWallet = {}
        publicWallet["private_key"] = hashlib.sha256(wallet["private_key"].encode()).hexdigest()
        publicWallet["balance"] = wallet["balance"]
        publicWallet["coin"] = wallet["coin"]
        publicWallet["isActive"] = True


        self.wallets[wallet["address"]] = publicWallet

        return {"error":False,"address": wallet["address"],"private":wallet,"public":publicWallet}

    
    def transfer_coins(self, fromWallet,toWallet,balanceTransfer):
        
        fromAddress = fromWallet
        toAddress = toWallet

        if fromAddress not in self.wallets:
            return self._setErrorMessage("Sender Address doesn't exist.")
        
        if  toAddress not in self.wallets:
            return self._setErrorMessage("Reciever Address doesn't exist.")


        fromWallet = self.wallets[fromAddress]
        toWallet = self.wallets[toAddress]


        now = datetime.now()

        if fromWallet["balance"] >= balanceTransfer and fromWallet["isActive"] and toWallet["isActive"]:

            fromWallet["balance"] -= balanceTransfer
            toWallet["balance"] += balanceTransfer
            self.wallets[fromAddress] = fromWallet
            self.wallets[toAddress] = toWallet

            return {
                "error":False,
                "fromWallet":fromWallet,
                "toWallet":toWallet,
                "operation": {
                    "transfer_from": fromAddress,
                    "transfer_to": toAddress,
                    "amount": balanceTransfer,
                    "coin": "UCW",
                    'timestamp': str(now),
                    "date": now.strftime("%m/%d/%Y, %H:%M:%S"),
                    "success": True
                }
                }
        return {
            "error":False,
            "fromWallet":fromWallet,
            "toWallet":toWallet,
            "operation": {
                    "transfer_from": fromAddress,
                    "transfer_to": toAddress,
                    "amount": balanceTransfer,
                    "coin": "UCW",
                    'timestamp': str(now),
                    "date": now.strftime("%m/%d/%Y, %H:%M:%S"),
                    "success":False,
                    "msg": "Insufficient Balance in Sender's Account or One of the Account is not Active For Transaction."
                }

            }

    def getAllPublicAddresses(self):

        return list(self.wallets.keys())


    def updateWalletBalance(self,address,newBalance):

        if address not in self.wallets:
            return self._setErrorMessage("Invalid Wallet Address")
        try:
            balance = float(newBalance)
        except ValueError:
            return self._setErrorMessage("Invalid Balance amount, must be a numeric value.")

        self.wallets[address]["balance"] = balance
        return {"error":False,"msg":"Success"}








        

        


