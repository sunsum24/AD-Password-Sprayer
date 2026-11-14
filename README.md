# Active Directory Password Spraying Tool

A Python-based script designed for Red Team engagements to test a single password against a list of Active Directory usernames.

## The Problem
Brute-forcing a single account with thousands of passwords triggers Account Lockout Policies. Password spraying flips this: it tries a single, highly likely password (e.g., `Summer2026!`) against hundreds of users.

## The Solution
This script iterates through a list of usernames and attempts to authenticate using a single password. 
**Crucially, it includes a 2-second delay between attempts** to prevent locking out accounts in the target environment.

## Usage
1. Ensure you have `requests` installed: `pip install requests`
2. Run the script:
`python sprayer.py <target_url> <userlist.txt> <password>`

## Disclaimer
This tool is strictly for authorized penetration testing and educational purposes. Unauthorized access to systems is illegal.
