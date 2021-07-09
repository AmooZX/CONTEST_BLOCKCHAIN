import os.path
from os import listdir
from random import randrange
import fonction.recurrent as fctrct

from classes import Chain, Wallet, Block

chain = Chain()

path = os.path.join(os.getcwd(), "content\\wallets\\")
if len(listdir(path)) < 3:
    wallet1 = Wallet()
    wallet2 = Wallet()
    wallet3 = Wallet()
else:
    wallets_name = fctrct.get_wallets_name()
    wallet1 = Wallet(wallets_name.pop(randrange(len(wallets_name))))
    wallet2 = Wallet(wallets_name.pop(randrange(len(wallets_name))))
    wallet3 = Wallet(wallets_name.pop(randrange(len(wallets_name))))

path = os.path.join(os.getcwd(), "content\\blocs\\")
if len(listdir(path)) < 3:
    chain.add_block()
    chain.add_block()
    chain.add_block()

block1 = chain.get_block("00")

blocks_hash = fctrct.get_blocks_hash()
block2 = chain.get_block(blocks_hash.pop(randrange(len(blocks_hash))))

print("\n0.------ "
      "Retrieving the last transaction number "
      "------\n")
print(chain.last_transaction_number)
print("\n1. "
      "------ Transaction n°1: "
      "------\n")
transaction_amount = 10
print("Before transaction :")
print("Transmitter ->", wallet1.unique_id, "->", wallet1.balance)
print("Receiver ->", wallet2.unique_id, "->", wallet2.balance)
print(
    "\n",
    "Transaction :",
    chain.add_transaction(block2, wallet1, wallet2, transaction_amount),
    "\n")
print("After transaction :")
print("Transmitter ->", wallet1.unique_id, "->", wallet1.balance,
      "(-{})".format(transaction_amount))
print("Receiver ->", wallet2.unique_id, "->", wallet2.balance,
      "(+{})".format(transaction_amount))
print("\n2. ------ "
      "Transaction n°2: no more token "
      "------\n")
print(chain.add_transaction(block2, wallet1, wallet2, 500))
print("\n3. ------ "
      "Transaction n°3: no more place"
      "------\n")
result = None
expected_response = "Impossible transaction: " \
                    "no more place on the select block"
while result != expected_response:
    result = chain.add_transaction(
        block1, wallet1, wallet2, 0)
print("Block Weigth: {} octets".format(block1.get_weight()))
print("\n4. ------ "
      "Transaction n°4: unknown wallet "
      "------\n")
print(chain.add_transaction(block2, Wallet("Test"), wallet2, 500))
print(chain.add_transaction(block2, wallet1, Wallet("Test"), 500))
print(chain.add_transaction(block2, Wallet("Test"), Wallet("Test"), 500))
print("\n5. ------ "
      "Rebuilding the chain each time chain initialized "
      "------\n")
del chain
chain = Chain()
print(" -> ".join([block.hash for block in chain.blocks]))
print("\n6. ------ "
      "Retrieving the last transaction number"
      "------\n")
print(chain.last_transaction_number)
print("\n7. ------ "
      "Retrieving a transaction by number"
      "------\n")
print(chain.find_transaction(100))
print(chain.find_transaction(-1))
print(chain.find_transaction(chain.last_transaction_number + 1))
print("\n7. ------ "
      "Retrieving a transaction with blocknumber"
      "------\n")
print(block2.get_transaction(chain.last_transaction_number))
print(block2.get_transaction(-1))
print(block2.get_transaction(chain.last_transaction_number + 1))