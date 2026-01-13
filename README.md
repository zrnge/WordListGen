# 📜 WordListGen
WordListGen is an advanced, customizable password wordlist generator written in Python. It is designed for security professionals, penetration testers, and researchers who need to generate targeted password lists based on personal attributes and common transformation techniques.

# Features

1. Case variations (lowercase, uppercase, capitalized)
2. Leetspeak substitutions
3. Word combinations and permutations
4. Number enrichment (common patterns and ranges)
5. Date-based variations (e.g., birthdays)
6. Symbol prefixing and suffixing
7. Maximum length filtering
8. Output to file

# Requirements

- Python 3.7 or later
- No external dependencies (standard library only)

# Installation

Clone the repository and ensure the script is executable:
``
git clone https://github.com/zrnge/WordListGen.git
cd WordListGen
chmod +x WordListGen.py
``
# Usage

``
./WordListGen.py --name <NAME> [OPTIONS]
``

| Argument       | Description                                |
| -------------- | ------------------------------------------ |
| `--name`       | Primary base word (required)               |
| `--job`        | Job title or related keyword               |
| `--birthday`   | Date in `DDMMYY` format                    |
| `--leet`       | Enable leetspeak variations                |
| `--numbers`    | Append and prepend number patterns         |
| `--symbols`    | Append and prepend symbols                 |
| `--max-length` | Maximum password length (default: 32)      |
| `--output`     | Output file name (default: `wordlist.txt`) |

# Examples

``
./wordlistgen.py \
  --name Ayub \
  --job Analyst \
  --birthday 120398 \
  --leet \
  --numbers \
  --symbols \
  --output passwords.txt
  ``

  # Disclaimer

  This tool is intended strictly for educational purposes and authorized security testing. Unauthorized use against systems you do not own or have explicit permission to test is illegal and unethical.


