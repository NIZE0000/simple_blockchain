import datetime
import hashlib
import json

class Blockchain:
    """
        Blockchain class for create the chain 
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

        # Convert distionary object to json
        encode_block = json.dumps(block,sort_keys=True).encode

        # Create a new SHA-256 hash object
        sha256_hash = hashlib.sha256()

        # Update the hash object with the data to be hashed (encoded as bytes)
        sha256_hash.update(encode_block)

        # Get the hexadecimal representation of the hash
        hex_digest = sha256_hash.hexdigest()
        
        return hex_digest

