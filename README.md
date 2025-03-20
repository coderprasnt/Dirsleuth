➡️  DirSleuth<br>
A free, fast and customizable directory discovery tool written in Python

DirSleuth is a lightweight directory brute-forcing tool that helps uncover hidden directories and files on a web server. It's designed for speed and efficiency, using multi-threading to make quick work of large wordlists.

## 🚀 Features
- ✅ Fast multi-threaded scanning
- ✅ Supports custom wordlists
- ✅ Handles redirects, forbidden, and OK responses
- ✅ Lightweight and easy to use
- ✅ Customizable User-Agent and headers

## 🔧 How to Install

Clone the repository:
```bash
git clone https://github.com/coderprasnt/dirsleuth.git
```

Navigate to the folder:
```bash
cd dirsleuth
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Create a `wordlist.txt` with common directory names (or use an existing one).

## ▶️ How to Use

Basic Usage:
```bash
python dirsleuth.py
```

Example:
```bash
python dirsleuth.py -u https://example.com -w wordlist.txt -t 10
```

| Argument | Description | Example |
| -------- | ----------- | ------- |
| `-u`      | Target URL   | `https://google.com` |
| `-w`      | Path to wordlist | `./wordlist.txt` |
| `-t`      | Number of threads (default: 10) | `10` |

## 💪 Merits
- ✅ Fast due to multi-threading
- ✅ Easy to customize
- ✅ Handles 301/302 redirects gracefully
- ✅ Can bypass simple firewalls by randomizing User-Agent

## 🤦‍♂️ Demerits
- ❌ No SSL verification (can be risky)
- ❌ Might trigger WAF (Web Application Firewall) if aggressive
- ❌ No rate limiting (can get IP banned)
- ❌ Doesn’t handle JavaScript-based paths

## 🛡️ Use Cases
- ✔️ Penetration Testing – Find hidden files and directories
- ✔️ Security Audits – Check for misconfigurations
- ✔️ Bug Bounties – Discover exposed assets
- ✔️ CTF Challenges – Great for finding hidden flags

## 📜 Legal Disclaimer
- ⚠️ This tool is for educational purposes only.
- ⚠️ Do not use on unauthorized websites.
- ⚠️ Use responsibly and within the scope of permission.

## 👨‍💻 Author
- 💻 Coderprasant
- 🔗 GitHub: [@coderprasant](https://github.com/coderprasnt)

## 🌟 Contribute
Feel free to open an issue or create a pull request if you'd like to contribute! 😎
