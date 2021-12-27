// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract FundMe {
    uint256 total_balance;
    address payable wallet;
    mapping(address => uint256) public balances;
    address[] public donors;

    constructor() {
        wallet = payable(msg.sender);
    }

    modifier ownerOnly {
        require(msg.sender == wallet, "Only owner should call");
        _;
    }

    function donate() payable public {
        balances[msg.sender] += msg.value;
        total_balance += msg.value;
        donors.push(msg.sender);
    }

    function sendTo(address payable receiver) payable public {
        receiver.transfer(msg.value);
    }

    function withDraw() public ownerOnly{
        wallet.transfer(total_balance);
        total_balance = 0;
    }
}