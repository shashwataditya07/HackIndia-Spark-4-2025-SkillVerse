const express = require("express");
const { registerDonation } = require("../controllers/donationController");

const router = express.Router();

// Route for organ donation registration
router.post("/register", registerDonation);

module.exports = router;
