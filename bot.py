#!/usr/bin/python3
import os
import requests
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
import sys
import subprocess
import boto3
import botocore
from botocore.config import Config
from dotenv import load_dotenv
load_dotenv()

#Helper functions

def get_instance_state(ec2, instance_id):
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response["Reservations"][0]["Instances"][0]
        return instance["State"]["Name"]
    except botocore.exceptions.ClientError as e:
        print("Error:", e)
        return None

def check_instance_status(instance_id):
    region_name = "us-east-1"  # Replace with your region
    profile_name = "htduong02"  # Replace with your profile name

    htduong02_config = Config(
        region_name=region_name,
        signature_version="v4",
        retries={"max_attempts": 10, "mode": "standard"},
    )

    session = boto3.session.Session(profile_name=profile_name)
    ec2 = session.client("ec2", config=htduong02_config)

    instance_state = get_instance_state(ec2, instance_id)

    if instance_state == "running":
        try:
            response = ec2.describe_instance_status(InstanceIds=[instance_id])
            if response.get("InstanceStatuses"):
                instance_status = response["InstanceStatuses"][0]
                if instance_status["InstanceState"]["Name"] == "running":
                    return True
        except botocore.exceptions.ClientError as e:
            print("Error:", e)

    return False

def run_bot(bot_url):
    azure_c8k_1 = os.getenv("azure_c8k_1")
    azure_c8k_2 = os.getenv("azure_c8k_2")
    azure_c8k_admin = os.getenv("azure_c8k_admin")
    azure_c8k_pass = os.getenv("azure_c8k_pass")

    aws_c8k_1 = os.getenv("aws_c8k_1")
    aws_c8k_2 = os.getenv("aws_c8k_2")
    aws_c8k_admin = os.getenv("aws_c8k_admin")
    aws_c8k_pass =os.getenv("aws_c8k_pass")
   
    # AWS Instance ID:
    cnc_instance_id = os.getenv("cnc_instance_id")
    c8k1_instance_id = os.getenv("c8k1_instance_id")
    c8k2_instance_id = os.getenv("c8k2_instance_id")

    # Azure VM Name:
    # place holder

    # hard-code team bot parameters, it is better to leverage environment variable in production setup
    TEAMS_BOT_TOKEN = os.getenv("TEAMS_BOT_TOKEN")
    TEAMS_BOT_EMAIL = os.getenv("TEAMS_BOT_EMAIL")
    TEAMS_BOT_APP_NAME = os.getenv("TEAMS_BOT_APP_NAME")

    bot_email = TEAMS_BOT_EMAIL
    teams_token = TEAMS_BOT_TOKEN
    bot_app_name = TEAMS_BOT_APP_NAME

    # List of authorized users who can talk with cnbu bot.
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

    awscnc = os.getenv("awscnc")
    awspass = os.getenv("awspass")
    awscnc_user = os.getenv("awscnc_user")
    awscnc_version = os.getenv("awscnc_version")

    azurecnc = os.getenv("azurecnc")
    azurepass = os.getenv("azurepass")
    azurecnc_user = os.getenv("azurecnc_user")
    azurecnc_version = os.getenv("azurecnc_version")

    # Create a Bot Object
    print(bot_app_name)
    bot = TeamsBot(
        bot_app_name,
        teams_bot_token=teams_token,
        teams_bot_url=bot_url,
        teams_bot_email=bot_email,
        approved_users=approved_users,
        webhook_resource_event=[
            {"resource": "messages", "event": "created"},
            {"resource": "attachmentActions", "event": "created"},
        ],
    )


    # A simple command that returns a basic string that will be sent as a reply
    def do_something(incoming_msg):
        """
        Sample function to do some action.
        :param incoming_msg: The incoming message object from Teams
        :return: A text or markdown based reply
        """
        return "i did what you said - {}".format(incoming_msg.text)

    def azure(incoming_msg):
        """
        Turn on Cloud Controller in Azure. 
        """
        subprocess.call(['./backends/azurecnc.sh'])
        return "Azure lab started, please wait 5 to 10 minutes."

    def stopazure(incoming_msg):
        """
        Turn off Azure Cloud Controller
        """
        subprocess.call(['./backends/stopazurecnc.sh'])
        return "Azure lab stopped! See you again!"

    def aws(incoming_msg):
        """
        Turn on AWS Cloud Controller lab
        """
        subprocess.call(['./backends/awscnc.sh'])
        return "AWS lab started, please wait 5 to 10 minutes."

    def stopaws(incoming_msg):
        """
        Turn off AWS Cloud Controller lab
        """
        subprocess.call(['./backends/stopawscnc.sh'])
        return "AWS lab stopped! See you again!"
    
    def gcp(incoming_msg):
        return "Sorry GCP lab is not setup, please come back later"

    def infoaws(incoming_msg):
        return "AWS Controller: {}, Version: {}, User: {}, Password {}".format(awscnc, awscnc_version, awscnc_user,awspass)

    def infoazure(incoming_msg):
        return "Azure Controller: {}, Version: {}, User: {}, Password {}".format(azurecnc,azurecnc_version,azurecnc_user, azurepass)
    
    def csraws(incoming_msg):
        return "AWS - User: {}, Password: {}, C8k-1: {}, C8k-2: {}".format(aws_c8k_admin,aws_c8k_pass,aws_c8k_1,aws_c8k_2)

    def csrazure(incoming_msg):
        return "Azure - User: {}, Password: {}, C8k-1: {}, C8k-2: {}".format(azure_c8k_admin, azure_c8k_pass,azure_c8k_1, azure_c8k_2)

    def stataws(incoming_msg):
        if check_instance_status(cnc_instance_id):
            statcnc = "Running"
        else:
            statcnc = "Not running"
        if check_instance_status(c8k1_instance_id):
            statc8k1 = "Running"
        else:
            statc8k1 = "Not running"
        if check_instance_status(c8k2_instance_id):
            statc8k2 = "Running"
        else:
            statc8k2 = "Not running"

        return "AWS Controller: {}, C8k-1: {}, C8k-2: {}".format(statcnc, statc8k1, statc8k2)

    def statazure(incoming_msg):
        return "Sorry! this function is not available. Please come back later."

    def greeting(incoming_msg):
        # Loopkup details about sender
        sender = bot.teams.people.get(incoming_msg.personId)

        # Create a Response object and craft a reply in Markdown.
        response = Response()
        response.markdown = "Hello {}, I'm a chat bot. ".format(sender.firstName)
        response.markdown += "See what I can do by asking for **/help**."
        return response

    # Set the bot greeting.
    bot.set_greeting(greeting)

    # display help message
    bot.set_help_message(
        "Welcome to the CNBU Bot! You can use the following commands. Remember to direct the message directly to me by typing @cnbu /command\n")
    # Add new commands to the box.

    bot.add_command("/aws", "Start AWS Cloud Controller", aws)
    bot.add_command("/stopaws", "Stop AWS Cloud Controller", stopaws)
    bot.add_command("/azure", "Start Azure Cloud Controller", azure)
    bot.add_command("/stopazure", "Stop Azure Cloud Controller", stopazure)
    bot.add_command("/gcp", "Start GCP Cloud Controller",gcp)
    bot.add_command("/infoaws","Show me AWS lab login credentials",infoaws)
    bot.add_command("/infoazure","Show me Azure lab login credetials",infoazure)
    bot.add_command("/csraws","AWS C8000V login credentials",csraws)
    bot.add_command("/csrazure","Azure C8000V login credentials",csrazure)
    bot.add_command("/statusaws","AWS running status",stataws) 
    bot.add_command("/statusazure","Azure running status",statazure)
    bot.run(host="0.0.0.0", port=5000)

def main():
    bot_url = os.getenv("bot_url")
    run_bot(bot_url)
if __name__ == "__main__":
    main()