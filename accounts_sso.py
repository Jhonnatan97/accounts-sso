
from file_handler import FileHandler
import boto3

boto3.setup_default_session(profile_name='sso-bpp')

client2 = boto3.client('organizations')
accounts = []

collum_title = ["Account", "IdAccount"]
row_list = []
row_list2 = []

response = client2.list_accounts()
accounts.extend(response['Accounts'])
while 'NextToken' in response.keys():
    response = client2.list_accounts(NextToken=response['NextToken'])
    accounts.extend(response['Accounts'])
print('roles found: ' + str(len(accounts)))
for i in accounts:
    name = i['Name']
    idAccount = str(i['Id'])
    print('Account:', name, '-', idAccount)
    row = str(name)
    row1 = str(idAccount)
    row_list.append([row, row1])

# file_handler = FileHandler()
# file_handler.create_csv('contas_sso_23_01', collum_title)
# file_handler.save_csv('contas_sso_23_01', row_list)
