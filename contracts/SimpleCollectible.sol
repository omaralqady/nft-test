// SPDX-License-Identifier: MIT

pragma solidity 0.8.9;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract SimpleCollectible is ERC721URIStorage {
    uint256 public tokenCtr;

    constructor() public ERC721("Doggie", "DOG") {
        tokenCtr = 0;
    }

    function createCollectible(string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newId = tokenCtr;
        _safeMint(msg.sender, newId);
        _setTokenURI(newId, tokenURI);
        tokenCtr = tokenCtr + 1;
        return newId;
    }
}
