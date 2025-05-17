# 📧 Python Email Sender Script

This repository provides a simple Python script for sending emails using Gmail's SMTP server. It's ideal for automation, testing, or learning how email works in Python.

## 🧰 Features

- ✅ Send emails through Gmail SMTP
- 🧾 MIME-formatted email (supports plain text)
- 👥 Supports multiple recipients (easily extendable)
- 📦 Simple, lightweight, and dependency-free (uses standard Python libraries)

## 📁 File Structure
send_mail.py # Main Python script for sending email

## 🔒 Requirements

- Python 3.x
- Gmail account with **App Passwords** enabled

## 🔧 Setup Instructions

1. **Enable 2-Step Verification** on your Gmail account:
   - https://myaccount.google.com/security

2. **Create an App Password**:
   - Go to [App Passwords](https://myaccount.google.com/apppasswords)
   - Select "Mail" as the app and "Other (Custom name)" as the device
   - Generate and copy the password

3. **Edit the Script**:
   In `send_mail.py`, replace the placeholders:

   ```python
   sender_email = "your_email@gmail.com"
   app_password = "your_generated_app_password"
   x = {"recipient@example.com"}  # Add your recipient(s)

   python send_mail.py
