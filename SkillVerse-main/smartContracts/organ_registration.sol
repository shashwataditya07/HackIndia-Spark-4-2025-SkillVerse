pragma solidity ^0.8.0;

// SPDX-License-Identifier: MIT
contract HealthcareRecords {
    struct MedicalRecord {
        string ipfsHash;
        address owner;
    }
    
    struct Donor {
        string bloodType;
        string hlaTyping;
        string organ;
        bool available;
        bool functionTestPassed;
        bool physicalTestPassed;
        string medicalHistory;
    }
    
    struct Recipient {
        string bloodType;
        string hlaTyping;
        string organNeeded;
        bool matched;
        string medicalHistory;
    }
    
    mapping(address => MedicalRecord) public records;
    mapping(address => Donor) public donors;
    mapping(address => Recipient) public recipients;
    
    event RecordStored(address indexed user, string ipfsHash);
    event DonorRegistered(address indexed donor);
    event RecipientRegistered(address indexed recipient);
    event MatchFound(address indexed donor, address indexed recipient);
    
    function storeRecord(string memory _ipfsHash) public {
        records[msg.sender] = MedicalRecord(_ipfsHash, msg.sender);
        emit RecordStored(msg.sender, _ipfsHash);
    }
    
    function registerDonor(
        string memory _bloodType,
        string memory _hlaTyping,
        string memory _organ,
        bool _functionTestPassed,
        bool _physicalTestPassed,
        string memory _medicalHistory
    ) public {
        require(_functionTestPassed, "Function test failed");
        require(_physicalTestPassed, "Physical test failed");
        
        donors[msg.sender] = Donor(
            _bloodType, 
            _hlaTyping, 
            _organ, 
            true, 
            _functionTestPassed, 
            _physicalTestPassed, 
            _medicalHistory
        );
        
        emit DonorRegistered(msg.sender);
    }
    
    function registerRecipient(
        string memory _bloodType,
        string memory _hlaTyping,
        string memory _organNeeded,
        string memory _medicalHistory
    ) public {
        recipients[msg.sender] = Recipient(
            _bloodType, 
            _hlaTyping, 
            _organNeeded, 
            false, 
            _medicalHistory
        );
        
        emit RecipientRegistered(msg.sender);
    }
    
    function matchDonorRecipient(address donorAddress, address recipientAddress) public {
        require(donors[donorAddress].available, "Donor not available");
        require(!recipients[recipientAddress].matched, "Recipient already matched");
        require(keccak256(abi.encodePacked(donors[donorAddress].bloodType)) == keccak256(abi.encodePacked(recipients[recipientAddress].bloodType)), "Blood type mismatch");
        require(keccak256(abi.encodePacked(donors[donorAddress].hlaTyping)) == keccak256(abi.encodePacked(recipients[recipientAddress].hlaTyping)), "HLA typing mismatch");
        
        donors[donorAddress].available = false;
        recipients[recipientAddress].matched = true;
        
        emit MatchFound(donorAddress, recipientAddress);
    }
}