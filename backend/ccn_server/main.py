from modules.blockchain import Blockchain
import modules.walletOperations as wallet
from flask import Flask, jsonify,request
from uuid import uuid4

app = Flask(__name__)


blockchain = Blockchain()

app = Flask(__name__)
node_address = str(uuid4()).replace('-','')
blockchain = Blockchain()
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender=node_address,reciever='Shivam',amount=1)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions':block['transactions']}
    return jsonify(response), 200

# Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': True}
    else:
        response = {'message': False}
    return jsonify(response), 200

@app.route('/add_transaction', methods = ['POST'])
def add_transactions():
    json=request.get_json()
    transaction_keys=['sender','reciever','amount']
    if not all (key in json for key in transaction_keys):
        return 'Some elements of transaction are missing',400
    index=blockchain.add_transaction(json['sender'],json['reciever'],json['amount'])
    response={'message':f'This transaction will be added to Block. {index}'}
    return jsonify(response),201

@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
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
    nodes=json.get('nodes')
    if nodes is None:
        return 'No node',400
    for node in nodes:
        blockchain.add_node(node)
    response={'message': 'All the nodes are now connected. The Blockchain contains:',
              'total_nodes':list(blockchain.nodes)}
    return jsonify(response),201
    


# Running the app
app.run(host = '0.0.0.0', port = 5000)

