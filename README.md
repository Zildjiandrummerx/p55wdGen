# Password and Passphrase Generator with Salt and Pepper

This Python script generates secure passwords and passphrases, enhances security by using salt and pepper techniques, and manages a pepper file with another script. It provides flexibility in generating passwords and passphrases of specified lengths or word counts.

## Features

- **Password Generation**: Generate random passwords of customizable lengths.
- **Passphrase Generation**: Create passphrases using a selection of words without repetition.
- **Salt and Pepper**: Enhance security with dynamically generated salt and a pepper value read from a file.
- **Timestamped Pepper File**: Automatically manage and update a pepper file used in hashing.
- **SHA-256 Encryption**: Encrypt generated passwords and passphrases for secure storage.

## Usage

1. **Main Script (`main.py`)**:
   - Run `main.py` and choose between generating a password or passphrase.
   - Follow prompts to specify length or word count.
   - Outputs include raw generated password/passphrase, SHA-256 encrypted hash, salt, pepper value, and combined hash with salt and pepper.

2. **Pepper Management Script (`pepper.py`)**:
   - Run `pepper.py` to manage the creation and update of the pepper file (`pepper.txt`).
   - Automatically creates a new pepper file with a timestamped filename in the format `dumpYYYYMMDD_HHMMSS.txt`.
   - Handles scenarios where the pepper file is missing or needs recreation.

## Requirements

- Python 3.x
- No additional dependencies

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   
2. Run main.py to generate passwords or passphrases, and pepper.py to manage the pepper file.

## Example Output

$ python main.py

Do you want a password or a passphrase? (Enter 'password' or 'passphrase')
password

Enter the desired password length (12-50):
30

RAW Password: :p.#^<sZ<&RH}3Mz4/u_Q(@J.n2S1z
SHA-256 Encrypted: eaf8c5f2aa35cf38483fcccb547f857338d1c1ea9365f76b9d7c2412654a74cf
Salt: I34EuGk6BOXvSTZX
Pass + Salt: 134a3dbf6cf14d7bd6030b4fe572333872069601600c7df0cbd3c151c30e0418
Pepper: 5iPYjNutX6xsogcckqxOxKfVkOLpzoL8BjZulFHy2hzBwJqTJq
Pass + Salt + Pepper: 0b79cb5303c7b7e7612c7f1c2a04ed335fc70ab0b51f61cdceb31fd06105001a
Generated on: 2024/06/24 - 18:10:39
