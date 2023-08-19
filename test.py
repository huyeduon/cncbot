from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import os

TEAMS_BOT_TOKEN = os.getenv("TEAMS_BOT_TOKEN")
TEAMS_BOT_EMAIL = os.getenv("TEAMS_BOT_EMAIL")
TEAMS_BOT_APP_NAME = os.getenv("TEAMS_BOT_APP_NAME")

print("TEAMS_BOT_TOKEN :", TEAMS_BOT_TOKEN )
print("TEAMS_BOT_EMAIL :", TEAMS_BOT_EMAIL)
print("TEAMS_BOT_APP_NAME :", TEAMS_BOT_APP_NAME )



azure_c8k_1 = os.getenv("azure_c8k_1")
azure_c8k_2 = os.getenv("azure_c8k_2")
azure_c8k_admin = os.getenv("azure_c8k_admin")
azure_c8k_pass = os.getenv("azure_c8k_pass")

aws_c8k_1 = os.getenv("aws_c8k_1")
aws_c8k_2 = os.getenv("aws_c8k_2")
aws_c8k_admin = os.getenv("aws_c8k_admin")
aws_c8k_pass =os.getenv("aws_c8k_pass")

print(azure_c8k_1)
print(azure_c8k_2)
print(azure_c8k_admin)
print(azure_c8k_pass)
print(aws_c8k_1)
print(aws_c8k_2)
print(aws_c8k_admin)
print(aws_c8k_pass)

cnc_instance_id = os.getenv("cnc_instance_id")
c8k1_instance_id = os.getenv("c8k1_instance_id")
c8k2_instance_id = os.getenv("c8k2_instance_id")

print(cnc_instance_id)
print(c8k1_instance_id)
print(c8k2_instance_id)


user1 = os.getenv("user1")
user2 = os.getenv("user2")
user3 = os.getenv("user3")
user4 = os.getenv("user4")
user5 = os.getenv("user5")
user6 = os.getenv("user6")
user7 = os.getenv("user7")
user8 = os.getenv("user8")
    
approved_users = [
        user1,
        user2,
        user3,
        user4,
        user5,
        user6,
        user7,
        user8
    ]

for user in approved_users:
    print(user)