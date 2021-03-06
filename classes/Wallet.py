import uuid
import json
import os.path
import fonction.recurrent as fctrct

class Wallet:

    def __init__(self, unique_id=""):
        loaded = self.load(unique_id)

        if not loaded and not unique_id:
            self.unique_id = self.generate_unique_id()
            self.balance = 100
            self.history = []
            self.save()
        elif not loaded:
            self.unique_id = "WRONG"
            self.balance = 0
            self.history = []

    def generate_unique_id(self):
        wallets = fctrct.get_wallets_name()
        id = str(uuid.uuid4())
        while id in wallets:
            id = str(uuid.uuid4())
        return id

    def add_balance(self, balance):
        self.balance += balance
        self.save()

    def sub_balance(self, balance):
        self.balance -= balance
        self.save()

    def send(self, receiver, amount):
        self.sub_balance(amount)
        receiver.add_balance(amount)

    def save(self):
        content = json.dumps(self.__dict__)
        path = os.path.join(
            os.getcwd(), "content\\wallets\\", self.unique_id + ".json"
        )
        with open(path, "w+") as f:
            f.write(content)
            f.close()

    def load(self, unique_id):
        path = os.path.join(
            os.getcwd(), "content\\wallets\\", unique_id + ".json"
        )
        if os.path.isfile(path):
            with open(path, "r") as f:
                content = json.loads(f.read())
                f.close()
                for k, v in content.items():
                    setattr(self, k, v)
        return os.path.isfile(path)