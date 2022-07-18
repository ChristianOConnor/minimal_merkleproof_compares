const whiteListAddresses = require('./address_list.json');
const merkleTreeFunc = require("./merkleTreeModule");
const merkleTree = merkleTreeFunc(true, whiteListAddresses);
const claimingAddress = "0x35C86Dc00C3f40aA53Ff1B371B1f235Bd7Ce6e64";
const rootHash = merkleTree[0].getRoot();

function isEqualToClaimAddress(value) {
  return value == claimingAddress
}

const claimingAddressFromMerkleTree = whiteListAddresses.findIndex(isEqualToClaimAddress);
const processedAddress = merkleTree[1][claimingAddressFromMerkleTree];
const hexProof = merkleTree[0].getHexProof(processedAddress);
const leafs = merkleTree[0].getHexLeaves();
console.log(leafs);
console.log('');

console.log('here is the root hash: ' + rootHash.toString("hex"));
console.log(merkleTree[0].verify(hexProof, processedAddress, rootHash));