from modules.blockchain import Blockchain
from flask import Flask, jsonify

def main():

    # Create Blockchain
    blockchain = Blockchain()

    app = Flask(__name__)

    # routing
    @app.route('/blockchain',methods=["GET"])
    def blockchains():
        response = {
            "chain":blockchain.chain,
            "length": len(blockchain.chain)
        }
        return jsonify(response), 200
    
    @app.route('/mining', methods=["GET"])
    def mining_block():

        previous_block = blockchain.get_previous_block()

        nonce = blockchain.proof_of_work(previous_block["nonce"])

        previous_hash = blockchain.hash(previous_block)

        block = blockchain.create_block(previous_hash, nonce)

        response = {
            "message": "Mining Suceed",
            "index": block["index"],
            "timestamp": block["timestamp"],
            "nonce": block["nonce"],
            "previous_hash": block["previous_hash"]
        }

        return jsonify(response), 200


    @app.route('/is_chains_valid', methods=["GET"])
    def is_chains_valid():
        is_valid = blockchain.is_chain_valid(blockchain.chain)
        if is_valid:
            response = {"message": "Blockchain is valid"}
        else:
            response = {"message": "Problem, Blockchain invalid"}
        return jsonify(response), 200
        
    app.run()


if __name__ == "__main__":
    main()