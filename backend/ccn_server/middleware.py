from modules.blockchain import Blockchain
from modules.midddlewareAccounts import MiddleWareAccounts
from flask import Flask, jsonify,request
from uuid import uuid4
import config as cfg
import requests
from time import time

app = Flask(__name__)
node_address = str(uuid4()).replace('-','')
Accounts = MiddleWareAccounts()
Adminblockchain = Blockchain()

def raiseInavlidErrorBasedOnKeys(json, keys):

    for eachKey in keys:
        if eachKey not in json:
            return False
    return True

def mineBlock(blockchain, data):
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, previous_hash,data=data)

    return {"error":False,"chain":blockchain}


@app.route('/register_user', methods = ['POST'])
def register_user():
    json = request.get_json()

    if not raiseInavlidErrorBasedOnKeys(json,["face","thumbLeft","thumbRight","username"]):
        return jsonify({"error":True,"msg":"Insufficient Request Parameters"}), 400

    result = Accounts.register_user(face = json["face"],
    thumbLeft=json["thumbLeft"],
    thumbRight=json["thumbRight"],username=json["username"])

    if result["error"]:
        return jsonify(result),400
    return jsonify(result),200


@app.route('/get_transaction_history', methods = ['GET'])
def get_chain():
    
    jsonRequest = request.get_json()

    if "face" not in jsonRequest or "thumbLeft" not in jsonRequest or "thumbRight" not in jsonRequest:
        return jsonify({"error":True,"msg":"Insufficient Request Parameters"}), 400

    response = Accounts.getAccountDetailsByBiometric(face = jsonRequest["face"],
    thumbLeft=jsonRequest["thumbLeft"],thumbRight=jsonRequest["thumbRight"])

    if response["error"]:
        return jsonify({"error":True,"msg":response["msg"]}), 400

    key = response["username"]
    if key not in Accounts.transactions:
        return jsonify({}),200

    blockchain = Accounts.transactions[key]
    print("Blockchain = ", blockchain)


    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

@app.route('/add_wallet_coins_admin', methods = ['POST'])
def add_wallet_coins_admin():
    json=request.get_json()

    if "adminAPIKey" not in json:
        return jsonify({"error":True,"msg":"Admin API Key not available"}),401
    
    if json["adminAPIKey"] != cfg.ADMIN_API_KEY:
        return jsonify({"error":True,"msg":"Admin API Key is not valid."}),401

    if not raiseInavlidErrorBasedOnKeys(json = json,keys = ["username","balance"]):
        return jsonify({"error":True,"msg":"Insufficient Request Parameters."}),400

    username = json["username"]
    balanceAmount = json["balance"]

    result = Accounts.add_admin_balance(username=username,balanceAmount=balanceAmount)

    if result["error"]:

        result = mineBlock(blockchain = Adminblockchain, data = result)
        return jsonify({"result":"Mining Failed"}),400

    result = mineBlock(blockchain = Adminblockchain, data = result)

    return jsonify({"result":"Success"}),201

@app.route('/admin_ops', methods = ['GET'])
def view_admin_ops():
    json=request.get_json()

    if "adminAPIKey" not in json:
        return jsonify({"error":True,"msg":"Admin API Key not available"}),401
    
    if json["adminAPIKey"] != cfg.ADMIN_API_KEY:
        return jsonify({"error":True,"msg":"Admin API Key is not valid."}),401

    if not raiseInavlidErrorBasedOnKeys(json = json,keys = ["adminAPIKey"]):
        return jsonify({"error":True,"msg":"Insufficient Request Parameters."}),400


    response = {'chain': Adminblockchain.chain,
                'length': len(Adminblockchain.chain)}
    

    return jsonify(response),201


@app.route('/does-wallet-exist', methods = ['GET'])
def doesWalletExist():
    json = request.get_json()

    if not raiseInavlidErrorBasedOnKeys(json,["face","thumbLeft","thumbRight","wallets"]):
        return jsonify({"error":True,"msg":"Insufficient Request Parameters"}), 400

    response = Accounts.getAccountDetailsByBiometric(face = json["face"],
    thumbLeft=json["thumbLeft"],thumbRight=json["thumbRight"])

    if response["error"]:
        return jsonify({"error":True,"msg":response["msg"]}), 400

    wallets_existing = json["wallets"]

    walletResponse = requests.post(url=cfg.MIDDLEWARE_TO_BLOCKCHAIN_URLS["URL_FOR_EXISTING_WALLETS"],
    json = {**cfg.WALLETS_REQUEST,
    "wallets":wallets_existing}).json()

    if walletResponse["error"]:
        return jsonify(walletResponse),400
    return jsonify(walletResponse),200

@app.route('/get-central-wallet', methods = ['GET'])
def getCentralWallet():
    json = request.get_json()

    if not raiseInavlidErrorBasedOnKeys(json,["face","thumbLeft","thumbRight"]):
        return jsonify({"error":True,"msg":"Insufficient Request Parameters"}), 400

    response = Accounts.getAccountDetailsByBiometric(face = json["face"],
    thumbLeft=json["thumbLeft"],thumbRight=json["thumbRight"])

    if response["error"]:
        return jsonify({"error":True,"msg":response["msg"]}), 400

    walletResponse = requests.get(url=cfg.MIDDLEWARE_TO_BLOCKCHAIN_URLS["URL_FOR_CENTRAL_WALLET"],
    json = cfg.WALLETS_REQUEST).json()

    if walletResponse["error"]:
        return jsonify(walletResponse),400
    return jsonify(walletResponse),200
    

@app.route('/add_transaction_step_01', methods = ['POST'])
def add_transaction_step01():
    json = request.get_json()

    if not raiseInavlidErrorBasedOnKeys(json,["face","thumbLeft","thumbRight","payment"]):
        return jsonify({"error":True,"msg":"Insufficient Request Parameters"}), 400

    response = Accounts.getAccountDetailsByBiometric(face = json["face"],
    thumbLeft=json["thumbLeft"],thumbRight=json["thumbRight"])

    if response["error"]:
        return jsonify({"error":True,"msg":response["msg"]}), 400


    userName = response["username"]

    middleWareResponse = Accounts.make_a_payment(face = json["face"],
    thumbLeft = json["thumbLeft"],
    thumbRight = json["thumbRight"],
    paymentObject = json["payment"])

    if not middleWareResponse:
        return jsonify({"error": True,"msg":"Insufficient Bank Balance"}),401

    else:
        if Accounts.createPaymentSession(username=userName,paymentObject=json["payment"]):
            return jsonify({"error": False,"msg":"Payment Session Created. Kindly Verify with your Right Thumb Impression","timeStamp":int(time()*1000)}),201
        else:
            return jsonify({"error": True,"msg":"Process Failed due to some Technical Error. Kindly Contact Admin."}),400

@app.route('/add_transaction', methods = ['POST'])
def add_transaction():
    json = request.get_json()

    if not raiseInavlidErrorBasedOnKeys(json,["apiKey","chainName","face","thumbLeft","thumbRight","payment","paymentType"]):
        return jsonify({"error":True,"msg":"Insufficient Request Parameters"}), 400

    response = Accounts.getAccountDetailsByBiometric(face = json["face"],
    thumbLeft=json["thumbLeft"],thumbRight=json["thumbRight"])

    

    if response["error"]:
        return jsonify({"error":True,"msg":response["msg"]}), 400


    if json["paymentType"] == "internal":

        result = Accounts.completeInternalPayment(paymentObject = json["payment"])

        senderName = json["payment"]["sender"]
        recieverName = json["payment"]["reciever"]

        if senderName in Accounts.transactions and recieverName in Accounts.transactions:

            chain = Accounts.transactions[senderName]
            newchain = mineBlock(blockchain=chain, data = result)
            print("Goes into this")
            Accounts.transactions[senderName] = newchain["chain"]

            chain = Accounts.transactions[recieverName]
            newchain = mineBlock(blockchain=chain, data = result)
            Accounts.transactions[recieverName] = newchain["chain"]

        elif senderName not in Accounts.transactions and recieverName in Accounts.transactions:

            chain = Blockchain()
            print("Goes into not sender name")
            newchain = mineBlock(blockchain=chain, data = result)
            Accounts.transactions[senderName] = newchain["chain"]

            chain = Accounts.transactions[recieverName]
            newchain = mineBlock(blockchain=chain, data = result)
            Accounts.transactions[recieverName] = newchain["chain"]

        elif senderName in Accounts.transactions and recieverName not in Accounts.transactions:

            chain = Accounts.transactions[senderName]
            print("Goes into not reciever name")
            newchain = mineBlock(blockchain=chain, data = result)
            Accounts.transactions[senderName] = newchain["chain"]

            chain = Blockchain()
            newchain = mineBlock(blockchain=chain, data = result)
            Accounts.transactions[recieverName] = newchain["chain"]

        else:

            chain = Blockchain()
            print("Goes into else name")
            newchain = mineBlock(blockchain=chain, data = result)
            Accounts.transactions[senderName] = newchain["chain"]

            chain = Blockchain()
            newchain = mineBlock(blockchain=chain, data = result)
            Accounts.transactions[recieverName] = newchain["chain"]


        return jsonify(result),201

    else:

        results = Accounts.deductWalletAmount(paymentObject=json["payment"])
        if results["error"]:
            return jsonify(results),400

        centralWalletResponse = requests.get(cfg.MIDDLEWARE_TO_BLOCKCHAIN_URLS["URL_FOR_CENTRAL_WALLET"],
        json = cfg.WALLETS_REQUEST).json()

        if centralWalletResponse["error"]:
            return jsonify(centralWalletResponse),400

        finalResult = requests.post(
            cfg.MIDDLEWARE_TO_BLOCKCHAIN_URLS["URL_FOR_MAKING_TRANSACTION"],json = {
                "sender": centralWalletResponse["address"],
                "reciever": json["payment"]["reciever"],
                "amount": json["payment"]["amount"],
                **json
            }).json()

        if finalResult["error"]:
            return jsonify(finalResult),400
        else:
            return jsonify(finalResult),201





    


# Running the app

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 6000,debug = True)


# if __name__ == "__main__":
#     app.config['SERVER_NAME'] = "127.0.0.1:6000"
#     app.run(host = '127.0.0.1', port = 6000,debug = True)

