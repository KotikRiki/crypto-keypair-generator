<p align="center">
  <picture>
    <img alt="Crypto Keypair Generator" src="figures/logo.png" width="50%">
  </picture>
</p>

<h1 align="center">Crypto Keypair Generator</h1>

[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](https://github.com/KoTiRiKi/crypto-keypair-generator/actions) [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## ⚠️ Important Notice
If you are using this script to generate keypairs, ensure your mnemonic phrases are valid BIP-39 sequences. Invalid or incomplete phrases may lead to errors or insecure keypairs. Use in a secure, offline environment and never share private keys publicly. 

## 📰 News
- 📅 **[2025-07-28 13:59 CEST]** Initial release of the Crypto Keypair Generator on GitHub!

## 🔭 Overview
![Overview](figures/overview.png)

The **Crypto Keypair Generator** is a Python script that generates Ethereum (EVM) and Solana keypairs (addresses and private keys) from BIP-39 mnemonic phrases. It supports multiple operations, such as deriving private keys or addresses for EVM-compatible chains and Solana, with results saved to text files.

**⚠️ Security Warning**: This script handles sensitive cryptographic data (mnemonic phrases and private keys). Never use it in an insecure environment, share private keys publicly, or store them unencrypted. Use at your own risk.

## 🚀 Features
<img width="953" height="157" alt="Снимок экрана 2025-07-28 в 15 18 12" src="https://github.com/user-attachments/assets/f70670db-9a05-4907-9d42-a726144b0666" />

- ✅ Generate EVM private keys from mnemonic phrases.
- ✅ Generate EVM addresses from mnemonic phrases or private keys.
- ✅ Generate Solana private keys from mnemonic phrases.
- ✅ Generate Solana addresses from mnemonic phrases.
- ✅ Read mnemonics from `mnemonics.txt` and save results to dedicated files.

## 📦 Requirements
The following Python packages are required, listed in `requirements.txt`:
| Package          | Version       | 
|-------------------|:-------------:|
| `eth-account`    | Latest         |
| `mnemonic`       | Latest         |
| `bip-utils`      | >=2.9.0        |
| `base58`         | Latest         |

To install them, run:
```bash
pip install -r requirements.txt
```

## 📋 Installation

### 1. Clone the repository:
```bash
git clone https://github.com/KoTiRiKi/crypto-keypair-generator.git
cd crypto-keypair-generator
```

### 2. Set up a virtual environment (recommended):
```bash
python -m venv venv
```

#### Activate it:
- On **Windows**:
```bash
venv\Scripts\activate
```

- On **macOS/Linux**:
```bash
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎮 Usage

### 1. Prepare the mnemonic file:
Create a file named `mnemonics.txt` in the project directory.
Add one or more BIP-39 mnemonic phrases (e.g., 12-word phrases), each on a new line.

**Example**:
```
retire fashion finish extend loop situate version picnic paddle sibling earn humor
```

### 2. Run the script:
```bash
python seed_to_private_evm_solana.py
```

Select an action by entering a number (1–5):
1. Generate EVM private keys → `private_keys_evm.txt`.
2. Generate EVM addresses from private keys → `addresses_evm.txt`.
3. Generate EVM addresses from mnemonics → `addresses_evm.txt`.
4. Generate Solana private keys → `private_keys_solana.txt`.
5. Generate Solana addresses → `addresses_solana.txt`.

### 3. Check output files:
Results are saved to the respective files based on the selected action.

## 💡 Example
If `mnemonics.txt` contains:
```
retire fashion finish extend loop situate version picnic paddle sibling earn humor
```
Running option 3 will generate an EVM address and save it to `addresses_evm.txt`.

## 🔒 Security Notes
- **Private Key Safety**: Never share `private_keys_evm.txt`, `private_keys_solana.txt`, or `mnemonics.txt` publicly or commit them to Git.
- **Environment**: Run this script in a secure, offline environment.
- **File Deletion**: Clear output files manually after use.

## 🐞 Troubleshooting

### Error: `Microsoft Visual C++ 14.0 or greater is required.`
<img width="979" height="512" alt="image_2025-07-28_16-09-37" src="https://github.com/user-attachments/assets/f61e1c26-b07e-4823-84b4-754c98754979" />
<img width="979" height="512" alt="image_2025-07-28_16-10-00" src="https://github.com/user-attachments/assets/5934f73d-6c7d-451a-9bad-b32941fad3c9" />


This error appears because the `ed25519-blake2b` package used by `bip_utils` needs C++ compilation. This requires Microsoft C++ Build Tools.

✅ **To fix it:**

1. Go to: [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Download and install **Build Tools for Visual Studio**
3. In the installer, select **"C++ build tools"**
4. Make sure the component **"MSVC v14.x"** is checked (e.g., MSVC v14.3x - VS 2022 C++ x64/x86 build tools)
   <img width="1229" height="535" alt="image_2025-07-28_16-58-20" src="https://github.com/user-attachments/assets/922880b9-6cdf-4aab-a0be-a0636c5776e8" />

5. Restart your terminal (CMD/PowerShell) and try again:

```bash
pip install bip_utils
```

💡 **Alternative (temporary)**:

If you're using only **EVM** (Ethereum) and **not Solana**, you can:

- Comment out or remove `seed_to_solana_keypair()` from the code
- Remove `bip_utils` from `requirements.txt`
- Use only `eth_account`

However, for full functionality including Solana, installing the build tools is required.

## 🤝 Contributing
Feel free to submit issues or pull requests on GitHub. Contributions are welcome! 🎉

## 📜 License
This project is licensed under the MIT License.


seed to private seed to addresses evm sol 
