from modules.blockchain import Blockchain
from modules.walletOperations import Wallets
from flask import Flask, jsonify,request
from uuid import uuid4
import config as cfg

app = Flask(__name__)
node_address = str(uuid4()).replace('-','')
# blockchain = Blockchain()
central_BC_transaction = Blockchain()
wallet_transaction = Blockchain()
wallet_Data = Blockchain()
bcWallets = Wallets()

def getChainByName(chainName):

    if chainName == "central":
        return central_BC_transaction

    elif chainName == "wallet":
        return wallet_transaction

    else:
        return wallet_Data

def authenticate_api(apiKey):
    if apiKey != cfg.API_KEY:
        return False
    return True

def sanitation_check(jsonRequest):

    if jsonRequest is None:
        response = {"error": True, "msg":"Invalid Body","errorCode": 400}
        jsonRequest = {}
    if "apiKey" not in jsonRequest or "chainName" not in jsonRequest:
        response = {"error": True, "msg":"apiKey and chainName are must for request to procceed.","errorCode": 400}
    if not authenticate_api(jsonRequest["apiKey"]):
        response = {"error": True, "msg":"Invalid API Key","errorCode": 401}
    else:
        response = {"error": False, "msg":"Invalid API Key","errorCode": 200}

    return response



@app.route('/get_chain', methods = ['GET'])
def get_chain():
    jsonRequest = request.get_json()

    sanitationResponse = sanitation_check(jsonRequest = jsonRequest)
    if sanitationResponse["error"]:
        return jsonify(sanitationResponse), sanitationResponse["errorCode"] 

    blockchain = getChainByName(jsonRequest["chainName"])

    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    jsonRequest = request.get_json()

    sanitationResponse = sanitation_check(jsonRequest = jsonRequest)
    if sanitationResponse["error"]:
        return jsonify(sanitationResponse), sanitationResponse["errorCode"] 

    blockchain = getChainByName(jsonRequest["chainName"])


    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': True}
    else:
        response = {'message': False}
    return jsonify(response), 200

@app.route('/add_wallet', methods = ['POST'])
def add_wallet():
    json=request.get_json()

    sanitationResponse = sanitation_check(jsonRequest = json)
    if sanitationResponse["error"]:
        return jsonify(sanitationResponse), sanitationResponse["errorCode"] 

    result = bcWallets.addWalet()

    if result["error"] == True:
        return jsonify(result),400

    return jsonify(result),201

@app.route('/add_wallet_coins_admin', methods = ['POST'])
def add_wallet_coins_admin():
    json=request.get_json()

    sanitationResponse = sanitation_check(jsonRequest = json)

    if sanitationResponse["error"]:
        return jsonify(sanitationResponse), sanitationResponse["errorCode"]

    if "adminAPIKey" not in json:
        return jsonify({"error":True,"msg":"Admin API Key not available"}),401
    
    if json["adminAPIKey"] != cfg.ADMIN_API_KEY:
        return jsonify({"error":True,"msg":"Admin API Key is not valid."}),401

    if json["publicAddress"] not in bcWallets.wallets:
        return jsonify({"error":True,"msg":"Wallet Address doesn't exist."}),400

    result = bcWallets.updateWalletBalance(address=json["publicAddress"],newBalance=json["newBalance"])

    if result["error"]:
        return jsonify(result),400

    return jsonify(result),200

    

@app.route('/add_transaction', methods = ['POST'])
def add_transactions():
    json=request.get_json()

    sanitationResponse = sanitation_check(jsonRequest = json)
    if sanitationResponse["error"]:
        return jsonify(sanitationResponse), sanitationResponse["errorCode"] 

    blockchain = wallet_transaction

    transaction_keys=['sender','reciever','amount'] #Wallet Address
    if not all (key in json for key in transaction_keys):
        return 'Some elements of transaction are missing',400

    result = bcWallets.transfer_coins(fromWallet=json["sender"],toWallet=json["reciever"],balanceTransfer=json["amount"])

    if result["error"]:
        return result["msg"],400

    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, previous_hash,data=result["operation"])

    if not result["operation"]["success"]:
        return jsonify({"error":True,"msg": result["operation"]["msg"]}),400

    return jsonify({"error":False,"msg":"Transaction Success."}),201

@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
    json=request.get_json()

    sanitationResponse = sanitation_check(jsonRequest = json)
    if sanitationResponse["error"]:
        return jsonify(sanitationResponse), sanitationResponse["errorCode"] 

    blockchain = getChainByName(json["chainName"])


    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'Node has different chains so it was replaced by longest one.',
                    'new_chain':blockchain.chain}
    else:
        response = {'message':'All good. The chain is largest one.',
                    'actual_chain':blockchain.chain}
    return jsonify(response), 200

@app.route('/connect_node',methods=['POST'])
def connect_node():
    json=request.get_json()
    sanitationResponse = sanitation_check(jsonRequest = json)
    if sanitationResponse["error"]:
        return jsonify(sanitationResponse), sanitationResponse["errorCode"] 

    blockchain = getChainByName(json["chainName"])


    nodes=json.get('nodes')
    if nodes is None:
        return 'No node',400
    for node in nodes:
        blockchain.add_node(node)
    response={'message': 'All the nodes are now connected. The Blockchain contains:',
              'total_nodes':list(blockchain.nodes)}
    return jsonify(response),201
    


# Running the app

if __name__ == "__main__":

    app.run(host = '0.0.0.0', port = 5000,debug = True)

