const Donation = require("../models/Donation");

// Register a new donation
const registerDonation = async (req, res) => {
  try {
    const { fullName, email, organs } = req.body;

    // Validation
    if (!fullName || !email || organs.length === 0) {
      return res.status(400).json({ success: false, message: "All fields are required." });
    }

    // Save to database
    const newDonation = new Donation({ fullName, email, organs });
    await newDonation.save();

    res.status(201).json({ success: true, message: "Donation registered successfully!" });
  } catch (error) {
    console.error("Error:", error);
    res.status(500).json({ success: false, message: "Server error. Please try again later." });
  }
};

module.exports = { registerDonation };
