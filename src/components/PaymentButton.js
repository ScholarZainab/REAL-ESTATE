// src/components/PaymentButton.js
import React from "react";
import axios from "axios";

const PaymentButton = () => {
  const handlePayment = async () => {
    try {
      const response = await axios.post("/api/payment/");
      window.location.href = response.data.url; // Redirect to Stripe Checkout
    } catch (error) {
      console.error("Payment failed:", error);
    }
  };

  return (
    <button className="payment-button" onClick={handlePayment}>
      Upgrade to Platinum Listing ($1000)
    </button>
  );
};

export default PaymentButton;
