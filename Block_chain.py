import hashlib
import json
from datetime import datetime


class Block:
    def __init__(self, data):
        self.data = data
        self.hash = ""
        self.prev_hash = ''
        self.nonce = 0
        self.total_time = ''


def hash(block):
    data = json.dumps(block.data) + block.prev_hash + str(block.nonce)
    data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()


class BlockChain:
    def __init__(self, owner):
        self.chain = []
        self.owner = owner

        # Tạo khối gốc (Genesis block)
        genesis_block = Block('Genesis Block')
        genesis_block.hash = self.mine_block(genesis_block)
        self.chain.append(genesis_block)

    def mine_block(self, block):

        start = datetime.now()
        block.hash = hash(block)
        while not block.hash.startswith("0000"):
            block.nonce += 1
            block.hash = hash(block)
        end = datetime.now()
        block.total_time = str(end - start)
        return block.hash

    def add(self, data):
        new_block = Block(data)
        new_block.prev_hash = self.chain[-1].hash
        new_block.data.append({"from": "", "to": self.owner, "amount": 200})

        # Đào block để tìm giá trị nonce và hash hợp lệ
        new_block.hash = self.mine_block(new_block)
        self.chain.append(new_block)

    def print(self):
        for block in self.chain:
            print('Data : ', block.data)
            print('Prev_Hash : ', block.prev_hash)
            print('Hash : ', block.hash)
            print('Nonce : ', block.nonce)
            print('Total_time : ', block.total_time)
            print()

    def is_valid(self):

        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i-1]

            if not current_block.hash.startswith("0000"):
                return False

            if current_block.hash != hash(current_block):
                return False

            if current_block.prev_hash != prev_block.hash:
                return False

        return True

    def get_balance(self, person):
        balance = 0
        for block in self.chain:
            if type(block.data) != list:
                continue
            for transfer in block.data:
                if (transfer['from'] == person):
                    balance -= transfer['amount']
                if (transfer['to'] == person):
                    balance += transfer['amount']
        return balance


# Tạo một blockchain và thêm các block
blockchain = BlockChain('Meo')
blockchain.add([
    {"from": "Po", "to": "Meo", "amount": 10000},
    {"from": "Meo", "to": "Xam", "amount": 100},
    {"from": "Meo", "to": "Cat", "amount": 300}
])

blockchain.print()
print("is valid: ", blockchain.is_valid())


print(blockchain.get_balance('Meo'))
