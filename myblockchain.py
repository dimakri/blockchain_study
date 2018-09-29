import os
import json
from time import time
from hashlib import sha256
from uuid import uuid1


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.create_new_block(previous_hash=1, proof=100)  # ?????

    def add_new_node(self):
        random_node_id = uuid1()
        self.nodes.add(random_node_id)

    def create_new_block(self, proof, previous_hash=None):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transaction": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash,  # # self.hash(self.chain[-1])
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def resolve_conflict(self):
        pass

    def validate(self):
        pass

    def create_transaction(self, sender, receiver, ammount):
        transaction = {"sender": sender, "receiver": receiver, "ammount": ammount}
        self.current_transactions.append(transaction)

    def validate_blockchain(self):
        print(type(self.chain))
        print(len(self.chain))
        last_block = self.chain[0]
        current_block_index = 1

        while current_block_index < len(self.chain):
            block = self.chain[current_block_index]
            # print(block(self.chain[current_block_index]))
            if self.block_hash(last_block) != block["previous_hash"]:
                return False
            if not self.check_proof(last_block["proof"], block["proof"]):
                return False
            last_block = block
            current_block_index += 1
            return True

            # print(self.block_hash(last_block), block["previous_hash"])
            # print(last_block, block)
            # print(self.block_hash(block), last_block)

    @staticmethod
    def block_hash(block):
        block = json.dumps(block).encode()
        block_hash = sha256(block).hexdigest()
        return block_hash

    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_block):
        proof = 0
        last_proof = last_block["proof"]
        last_hash = last_block["previous_hash"]
        while self.check_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def check_proof(self, last_proof, proof):
        nice_try = f"{proof}{last_proof}".encode()
        proof_hash = sha256(nice_try).hexdigest()
        return proof_hash[:4] == "0000"
        # if proof_hash[:4]=="0000":
        #     retunr proof_hash


b = Blockchain()
# b.create_new_block()
# print(b.last_block())
# a = 0
# while a < 2:
#     last_block = b.last_block()
#     last_proof = b.last_block()["proof"]
#     proof = b.proof_of_work(last_block)
#     # print(proof)
#     b.create_new_block(proof, b.block_hash(last_block))
#     print(b.last_block())
#     a += 1


# b.create_new_block()


def mine(blockchain):
    bc = blockchain
    proof = bc.proof_of_work(bc.last_block())
    bc.create_new_block(proof, bc.block_hash(bc.last_block()))
    bc.create_transaction(0, "myname", 1)
    print("Last block is: ", b.last_block())
    print("You have mined a new block!!!")


# for a in range(0, 30):
#     mine(b)
# for a in range(0, 4):
#     mine(b)
# mine(b)
# mine(b)
# mine(b)
# mine(b)
# mine(b)
# b.validate_blockchain()
# a = set()
# a.add(1)
# a.add(3)
# a.add(2)
# a.add(1)
# a.add(1)
# print(uuid1())
# print(b.chain)
# print(b.chain[1])

