const mongoose = require("mongoose");

const donationSchema = new mongoose.Schema({
  fullName: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  organs: { type: [String], required: true },
});

module.exports = mongoose.model("Donation", donationSchema);
