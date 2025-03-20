import requests
import threading
import time
import random
import argparse

# Function to get arguments from the command line
def parse_arguments():
    parser = argparse.ArgumentParser(description="Directory brute force tool without proxies.")
    
    # Arguments for target URL, wordlist path, and threads
    parser.add_argument('-u', '--url', required=True, help="Target URL (e.g. https://google.com)")
    parser.add_argument('-w', '--wordlist', required=True, help="Path to wordlist file (e.g. ./wordlist.txt)")
    parser.add_argument('-t', '--threads', type=int, default=10, help="Number of threads (default: 10)")

    return parser.parse_args()

TARGET_URL = None
WORDLIST = None
THREADS = 10

# Get command line arguments
args = parse_arguments()

# Set variables from arguments
TARGET_URL = args.url
WORDLIST = args.wordlist
THREADS = args.threads

def check_directory(word):
    url = f"{TARGET_URL}/{word}"

    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print(f"[+] Found: {url} - {response.status_code}")
        elif response.status_code == 403:
            print(f"[!] Forbidden: {url}")
        elif response.status_code == 301 or response.status_code == 302:
            print(f"[>] Redirected: {url} → {response.headers['Location']}")

        # Random delay between requests to avoid looking like a bot
        time.sleep(random.uniform(0.5, 2.0))  # Sleep for 0.5 to 2 seconds
    except requests.RequestException as e:
        print(f"[-] Error with {url}: {e}")

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
