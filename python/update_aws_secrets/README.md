# Update AWS Secret Manager

This Python script allows you to create or update an AWS Secret Manager.

**Script capabilities:**

- If the secret does not exist, the script will create it.
- If the secret exists and already contains some key-value pairs, then the key-value pairs you are trying to add will be added to the Secret Manager **without overwriting** existing ones, i.e., the secret will be extended, **not overwritten**.
- If you are trying to update an existing key-value pair, then such a key-value pair will be overwritten.

## Installation

### Installation with virtual environment

Installing the script is very simple. If you want to run it in your virtual environment, follow these steps. These steps will set up your virtual environment, install the necessary dependencies, and allow you to run the script within that environment.

```bash
cd update_aws_secrets

# Create virtual environment for Python
python3 -m venv secrets
source secrets/bin/activate

# Install requirements
pip3 install -r requirements.txt
```

If you need to deactivate the virtual environment, use the following commands.

```bash
deactivate
rm -rf ./secrets
```

### Basic installation

Installation without using a virtual environment is even simpler; you just need to navigate to the folder with the script and install all dependencies using pip. After that, the script will be ready to use.

```
cd update_aws_secrets

# Install requirements
pip3 install -r requirements.txt

python3 update_secrets.py
```

## How to use script

To use the script, you need to specify several variables:

1. Specify the AWS profile name in `aws_profile_name` variable. By default, it uses the default profile from `~/.aws/config`.
2. Specify the name of the AWS Region in which you intend to work in `aws_region` variable. By default, it uses `us-east-1` AWS Region.
3. Specify the name of the secret with key-value pairs in the variable `secret_updates` that you plan to update. The format of this variable is similar to JSON. The object name specifies the name of the secret to be updated. The key and value respectively specify the key and value that will be written to the secret.
4. Login to aws cli

   ```bash
   # Configure aws profile (if you use IAM User)
   aws configure

   # Configure aws profile (if you use AWS SSO)
   aws configure sso
   aws sso login --profile my-profile
   ```

5. Run the script

   ```bash
   # Before you will run this script, please review secrets that is going to create/update
   python3 update_secrets.py
   ```

## Troubleshooting

1. Check if you are logged in to aws cli. You can use the followong [documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html "documentation").
2. Verify that you have sufficient permissions to interact with [AWS Secret Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html "AWS Secret Manager").
