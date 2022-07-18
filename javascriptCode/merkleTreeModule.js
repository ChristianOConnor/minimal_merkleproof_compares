const { MerkleTree } = require("merkletreejs")
const keccak256 = require("keccak256")

const create_merkle_tree_sortPairs_false = (sortPairsBool, whiteListAddresses) => {
    const leafNodes = whiteListAddresses.map((x) => keccak256(x))
    /* for (var addrss in leafNodes) {
        console.log(leafNodes[addrss].toString('hex'))
    } */
    const tree = new MerkleTree(leafNodes, keccak256, { sortPairs: sortPairsBool})
    return [tree, leafNodes]
}

module.exports = create_merkle_tree_sortPairs_false;