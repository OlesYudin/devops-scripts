# Update AWS Secret Manager

This script update key-value of AWS secret manager.

## Installation

```bash
cd update_aws_secrets

# Create virtual environment for Python
python3 -m venv secrets 
source secrets/bin/activate

# Install requirements
pip3 install -r requirements.txt 

# Before you will run this script, please review secrets that is going to create/update
python3 update_secrets.py
```

## Remove virtual environment
```bash
deactivate
rm -rf ./secrets
```