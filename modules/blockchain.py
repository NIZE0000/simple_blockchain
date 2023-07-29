import datetime
import hashlib
import json

class Blockchain:
    """
        Blockchain class for manage the chain 
    """
        
    def __init__(self):

        self.chain = []

        self.transaction = 0

        # create genesis block
        self.create_block(nonce=1, previous_hash="0")

    def create_block(self, nonce, previous_hash):

        block = {
            "index": len(self.chain)+1,
            "timestamp": str(datetime.datetime.now()),
            "nonce": nonce,
            "data": self.transaction,
            "previous_hash": previous_hash
        }

        self.chain.append(block)

        return block
    
    # return previous block
    def get_previous_block(self):
        return self.chain[-1]
    
    # hashing function SHA256
    def hash(self, block):

        # Convert distionary object to json and sorting 
        encode_block = json.dumps(block,sort_keys=True).encode()

        # Get the hexadecimal representation of the hash
        hex_digest = hashlib.sha256(encode_block).hexdigest()
        
        return hex_digest
    
    # proof of work function
    def proof_of_work(self, previous_nonce):
        
        new_nonce = 1
        check_proof = False

        while check_proof == False:
            
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()

            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_nonce += 1

        return new_nonce

    def is_chain_valid(self,chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash(previous_block):
                return False
            
            previous_nonce = previous_block["nonce"]
            nonce = nonce["nonce"]

            hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] != "0000":
                return False
            
            previous_block = block
            block_index += 1

        return True


if __name__ == "__main__":
    blockchain = Blockchain()

    print(blockchain.hash(blockchain.chain[0]))
    blockchain.proof_of_work(1)
    print(blockchain.hash(blockchain.chain))

    