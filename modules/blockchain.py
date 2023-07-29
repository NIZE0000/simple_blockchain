import datetime
import hashlib
import json

class Blockchain:
    """
        Blockchain class for manage the chain 
    """
        
    def __init__(self):

        self.chain = []

        # create genesis block
        self.create_block(nonce=1, previous_hash="0")

    def create_block(self, nonce, previous_hash):

        block = {
            "index": len(self.chain)+1,
            "timestamp": str(datetime.datetime.now()),
            "nonce": nonce,
            "previouse_hash": previous_hash
        }

        self.chain.append(block)

        return block
    
    # return previous block
    def get_previous_block(self):
        return self.chain[-1]
    
    # hashing function SHA256
    def hash(self, block):

        # Convert distionary object to json and sorting 
        encode_block = json.dumps(block,sort_keys=True).encode

        # Create a new SHA-256 hash object and hashing
        sha256_hash = hashlib.sha256(encode_block)

        # Get the hexadecimal representation of the hash
        hex_digest = sha256_hash.hexdigest()
        
        return hex_digest

    # proof of work function
    def proof_of_work(self, previous_nonce):
        
        new_nonce = 1
        check_proof = False

        while check_proof is False:
            
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()

            if hash_operation[:4] == "0000":
                check_proof == True
            else:
                new_nonce += 1

        return new_nonce