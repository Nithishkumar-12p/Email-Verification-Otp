# OTP Email Verification System

This is a simple Python-based script for sending a One-Time Password (OTP) to a user's email address for verification purposes. It's useful for basic authentication systems in student management platforms, registration processes, or internal tools that require email verification.

## 📌 Features

- Generates a 4-digit OTP.
- Sends the OTP to the specified email address using Gmail's SMTP.
- Verifies the OTP entered by the user.
- Easy to integrate into larger Python projects.

## 🛠️ Technologies Used

- Python (built-in `random`, `smtplib`, `email` libraries)
- SMTP for email delivery (Gmail SMTP server)

## 📋 How It Works

1. A random OTP is generated.
2. An email is composed and sent to the specified recipient.
3. The user inputs the received OTP.
4. If the OTP matches, verification is successful.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- A Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) enabled

### Installation

Clone this repository:
git clone https://github.com/Nithishkumar-12p/Email-Verification-Otp

