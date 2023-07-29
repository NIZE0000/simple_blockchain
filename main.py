from modules.blockchain import Blockchain
from flask import Flask, jsonify

def main():

    # Create Blockchain
    blockchain = Blockchain()

    app = Flask(__name__)

    # routing
    @app.route('/blockchains',methods=["GET"])
    def blockchains():
        response = {
            "chain":blockchain.chain,
            "length": len(blockchain.chain)
        }
        return jsonify(response), 200
    
    @app.route('/mining', methods=["POST"])
    def proof_of_work():
        blockchain.proof_of_work()

        response = {
            "chain":blockchain.chain,
            "length": len(blockchain.chain)
        }
        return jsonify(response), 200

    app.run()


if __name__ == "__main__":
    main()