import boto3
import json

# General variables
aws_profile_name = "default" # Specify name of AWS profile. Can be found in ~/.aws/config
aws_region = "eu-west-1" # Specify AWS region where you want to update secrets. By default, secrets will be updated in 'eu-west-1' region


session = boto3.Session(profile_name=aws_profile_name)

def update_secrets(secret_updates, region_name="eu-west-1"):

    # Create AWS Secrets Manager client
    secret_manager_client = session.client('secretsmanager', region_name=region_name)
    
    for secret_id, new_key_values in secret_updates.items():
        try:
            # Get current value of secret
            response = secret_manager_client.get_secret_value(SecretId=secret_id)
            current_secret_value = json.loads(response['SecretString'])
        except secret_manager_client.exceptions.ResourceNotFoundException:
            # If secret in AWS Secret Manager not exist - create new secret with empty value
            current_secret_value = {}

            try:
                secret_manager_client.create_secret(Name=secret_id, SecretString=json.dumps(current_secret_value))
                print(f"Created a new secret with id: {secret_id}")
            except Exception as e:
                print(f"Error creating secret: {e}")
                continue

        # Update or add new key-value in secret
        for key, value in new_key_values.items():
            current_secret_value[key] = value

        # Update secret with new key-value's
        try:
            secret_manager_client.put_secret_value(
                SecretId=secret_id,
                SecretString=json.dumps(current_secret_value)
            )
            print(f"Updated secret with id: {secret_id}")
        except Exception as e:
            print(f"Error updating secret {secret_id}: {e}")
            continue

if __name__ == "__main__":
    # Example
    secret_updates = {
        "test_1": {
            "key_1": "value_1",
            "key_2": "value_2",
            "key_3": "value_3"
        },
        "test_2": {
            "key_1": "value_1",
            "key_2": "value_2",
            "key_3": "value_3",
            "key_4": "value_4"
        }
    }

    update_secrets(secret_updates, region_name=aws_region)