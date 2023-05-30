# Script README

This script was developed to interact with AWS (Amazon Web Services) using the Boto3 library. It performs the following tasks:

## Prerequisites
- Python 3 installed
- Boto3 library installed (`pip install boto3`)
- AWS CLI configured with required credentials and profiles

## Settings
1. Install Python 3 if it is not already installed.
2. Install the Boto3 library by running the command `pip install boto3` in the terminal.
3. Configure the AWS CLI with the required credentials and profiles.

## Profile Configuration
1. Before running the script, make sure you've configured the AWS CLI with the required credentials and profiles. This script depends on the profiles defined in the AWS CLI configuration.
2. Open the script file and replace `'your-profile'` with the actual profile name you want to use for the AWS session.

## Running the Script
1. Download the script file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script file is saved.
4. Run the script by running the `python accounts_sso.py` command in the terminal, replacing `4. Run the script by running the `python accounts_sso.py` command in the terminal, replacing `accounts_sso.py` with the actual script file name.
` with the actual script file name.

## Script Overview

The script performs the following actions:

1. Retrieves a list of all AWS accounts associated with the specified profile.
2. Prints the name and ID of each account.

## Alternate GitHub Commands

If you prefer to use alternative GitHub commands to clone the repository:

1. Download the repository:
    - Click the "Code" button on this GitHub page.
    - Select the "Download ZIP" option.
    - Extract the ZIP file on your computer.

2. Navigate to the script directory:
    - Open a terminal or command prompt.
    - Use the `cd` command to navigate to the directory where the script file is located.

3. Run the script:
    - Make sure you have Python 3 installed.
    - Use the `python accounts_sso.py` command to run the script, replacing `accounts_sso.py` with the actual script file name.

## Disclaimer
This script is provided as-is without any warranties. It is your responsibility to review and understand the code before running it in your environment. Use it at your own risk.

**Note:** The script assumes that you have already installed the necessary dependencies and correctly configured the AWS CLI.
