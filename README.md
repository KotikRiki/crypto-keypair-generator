📝 Crypto Keypair Generator
🌟 Overview
The Crypto Keypair Generator is a Python script that generates Ethereum (EVM) and Solana keypairs (addresses and private keys) from BIP-39 mnemonic phrases. It supports multiple operations, such as deriving private keys or addresses for both EVM-compatible chains and Solana, with results saved to text files.
⚠️ Security Warning: This script handles sensitive cryptographic data (mnemonic phrases and private keys). Never use it in an insecure environment, share private keys publicly, or store them unencrypted. Use at your own risk.
🚀 Features

Generate EVM private keys from mnemonic phrases.
Generate EVM addresses from mnemonic phrases or private keys.
Generate Solana private keys from mnemonic phrases.
Generate Solana addresses from mnemonic phrases.
Read mnemonics from a file (mnemonics.txt) and output to dedicated files.

📦 Requirements
The following Python packages are required, listed in requirements.txt:



Package
Version



eth-account
Latest


mnemonic
Latest


bip-utils
>=2.9.0


base58
Latest


To install them, run:
pip install -r requirements.txt

📋 Installation

Clone the repository:git clone https://github.com/KoTiRiKi/crypto-keypair-generator.git
cd crypto-keypair-generator


Install dependencies:pip install -r requirements.txt



🎮 Usage

Prepare the mnemonic file:

Create a file named mnemonics.txt in the project directory.
Add one or more BIP-39 mnemonic phrases (e.g., 12-word phrases), each on a new line.
Example mnemonics.txt:retire fashion finish extend loop situate version picnic paddle sibling earn humor




Run the script:

Execute the script:python seed_to_private_evm_solana.py


Choose an action by entering a number (1–5):

1: Generate EVM private keys → private_keys_evm.txt.

2: Generate EVM addresses from private keys → addresses_evm.txt.

3: Generate EVM addresses from mnemonics → addresses_evm.txt.

4: Generate Solana private keys → private_keys_solana.txt.

5: Generate Solana addresses → addresses_solana.txt.




Check output files:

Results are saved to the respective files based on the selected action.



💡 Example
If mnemonics.txt contains:
retire fashion finish extend loop situate version picnic paddle sibling earn humor

Running option 3 will generate an EVM address and save it to addresses_evm.txt.
🔒 Security Notes

Private Key Safety: Never share private_keys_evm.txt, private_keys_solana.txt, or mnemonics.txt publicly or store them in a Git repository.
Environment: Run this script in a secure, offline environment.
File Deletion: Clear output files manually after use.

🤝 Contributing
Feel free to submit issues or pull requests on GitHub. Contributions are welcome!
📜 License
This project is licensed under the MIT License.
