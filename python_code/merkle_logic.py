from itertools import tee
from web3 import Web3
from eth_utils import keccak
from merkletools_instance import MerkleTools


def merkle_run(hashtocheck):
    data = []
    with open('address_list.txt', mode='r', encoding="utf-8") as in_file:
        for line_in_file in in_file:
            data.append(line_in_file.strip())
        
    tree = MerkleTools(hash_type="keccak")
    tree.add_leaf(data, True)
    tree.make_tree()
    tree.is_ready
    root_value = tree.get_merkle_root()

    index_of_target = data.index(hashtocheck)
    target_hash = tree.get_leaf(index_of_target)
    proof = tree.get_proof(index_of_target)
    print('this is the merkle root hash: ' + root_value)
    print('\n')

    for tr in range(tree.get_leaf_count()):
        print(tree.get_leaf(tr))

    # you can also pass in the hash value of 'hashtocheck', it will hash automatically if the user forgot to hash it
    if tree.validate_proof(proof, target_hash, root_value):
        print('address is in the tree')
    else:
        exit('address is not in the tree')

merkle_run('0x35C86Dc00C3f40aA53Ff1B371B1f235Bd7Ce6e64')