from merkletools_instance import MerkleTools


def merkle_run(hashtocheck):
    data = []
    nmt = MerkleTools(hash_type="keccak")
    with open('address_list.txt', mode='r', encoding="utf-8") as in_file:
        for address in in_file:
            nmt.add_leaf(address.strip(), True)
            data.append(address.strip())
    index_of_target = data.index(hashtocheck)
    nmt.make_tree()
    root_value = nmt.get_merkle_root()
    proof = nmt.get_proof(index_of_target)
    target_hash = nmt.get_leaf(index_of_target)

    for tr in range(nmt.get_leaf_count()):
        print(nmt.get_leaf(tr))
    
    print('\n' + 'this is the merkle root: ' + root_value + '\n')
    if nmt.validate_proof(proof, target_hash, root_value):
        print('address is in the tree')
    else:
        exit('address is not in the tree')

merkle_run('0x35C86Dc00C3f40aA53Ff1B371B1f235Bd7Ce6e64')