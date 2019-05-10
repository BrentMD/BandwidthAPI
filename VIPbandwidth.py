# importing the requests library 
import requests

# Bandwidth Account Variables
userName = raw_input("Bandwidth Username: ")
userPassword = raw_input("Bandwidth Password: ")
subAccountID = raw_input("Sub Account ID: ")
locationID = raw_input("Location ID: ")

# api-endpoint 
URL = ("https://dashboard.bandwidth.com/api/accounts/5004683/sites/" + subAccountID + "/sippeers/" + locationID)
payload = ""
headers = {
    'Content-Type': "application/xml",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

# Get Request using 'requests'
response = requests.get(URL, auth=(userName, userPassword), data=payload, headers=headers)

# Print out of Get request
print(response.text)

# New Lookup
newLookup = raw_input("Would you like to look up another(y,n)? ")
while newLookup == 'y':
    subAccountID = raw_input("Sub Account ID: ")
    locationID = raw_input("Location ID: ")
    response = requests.get(URL, auth=(userName, userPassword), data=payload, headers=headers)
    print(response.text)
    newLookup = raw_input("Would you like to look up another(y,n)? ")