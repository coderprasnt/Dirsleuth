# This is a free tool dev by coderprasnt

import requests
import threading

TARGET_URL = 'https://google.com/'  # Replace with target URL
WORDLIST = 'wordlist.txt'  # Path to wordlist
THREADS = 10

def check_directory(word):
    url = f"{TARGET_URL}/{word}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[+] Found: {url}")
        elif response.status_code == 403:
            print(f"[!] Forbidden: {url}")
        elif response.status_code == 301 or response.status_code == 302:
            print(f"[>] Redirected: {url} → {response.headers['Location']}")
    except requests.RequestException as e:
        print(f"[-] Error: {e}")

def main():
    with open(WORDLIST, 'r') as file:
        words = file.read().splitlines()

    threads = []
    for word in words:
        if len(threads) >= THREADS:
            for t in threads:
                t.join()
            threads = []

        t = threading.Thread(target=check_directory, args=(word,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
