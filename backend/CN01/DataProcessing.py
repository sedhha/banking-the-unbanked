import json
import requests
import hashlib
from Account import Account


# PLACEHOLDER
# here is where we will make a request once we have server
# response = requests.get("URL")
# data = json.loads(response.text) # list of dictionaries
# PLACEHOLDER
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

# access list of accounts
accountList = []
for i in range(0, len(data)):
    accountList.append(Account(data[i]['fingerprint'], data[i]['isActive'], data[i]['accountBalance']))

# now have access to account information to validate and perform transactions
print(accountList)

