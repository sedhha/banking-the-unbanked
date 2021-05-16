# creates dummy data to simulate data intake information
import json
import hashlib

nameList = ['Global Bank Account', 'Shivam Sahil', 'Olivia Carey', 'Alan Lai', 'Alex Lai', 'Jahangir Iqbal']
data = []

for name in nameList:
    temp = {}
    temp['name'] = name # can probably remove this since fingerprint is an identifier for an account
    temp['fingerprint'] = hashlib.sha256(name.encode()).hexdigest()
    temp['isActive'] = True

    if name == 'Global Bank Account':
        temp['accountBalance'] = 1000000
    else:
        temp['accountBalance'] = 0

    data.append(temp)

print(data)

# create dummy data
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

# check on dumping dummy data
with open("data_file.json", "r") as read_file:
    checkData = json.load(read_file)

print(checkData == data)