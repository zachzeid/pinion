import boto3
from database import System, Session

def get_iam_details(iam_role):
    # Assuming iam_role is ARN of the IAM role
    session = boto3.Session()
    iam = session.client('iam', aws_access_key_id='ACCESS_KEY', aws_secret_access_key='SECRET_KEY')

    users = iam.list_users()['Users']
    groups = iam.list_groups()['Groups']
    
    return users, groups

def add_aws_account(iam_role):
    session = Session()
    users, groups = get_iam_details(iam_role)

    new_system = System(
        name='AWS Account',
        type='AWS',
        iam_users=users,
        iam_groups=groups
    )
    session.add(new_system)
    session.commit()

# Example usage
add_aws_account('arn:aws:iam::123456789012:role/example')
