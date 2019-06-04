# importing the requests library 
import requests
# import ElementTree to work with the XML data
import xml.etree.ElementTree as ET

# Bandwidth Account Variables
userName = raw_input("Bandwidth Username: ")
userPassword = raw_input("Bandwidth Password: ")

# api-endpoint 
URL = ("https://dashboard.bandwidth.com/api/accounts/5004683/sites/")
payload = ""
headers = {
    'Content-Type': "application/xml",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
# Begin Lookup
newLookup = 'y'
while newLookup == 'y':
    subAccountID = raw_input("Sub Account ID: ")
    locationID = raw_input("Location ID: ")
    response = requests.get(URL + subAccountID + "/sippeers/" + locationID, auth=(userName, userPassword), data=payload, headers=headers)
    print(response.text)
    ##drNumber = raw_input("Disaster Route Number:")
    # Adding the FinalDestinationUri to the SipPeer
    ##root = ET.fromstring(response.content)
    ##SipPeer = root.find('SipPeer')
    ##FinalDestinationUri = ET.SubElement(SipPeer, 'FinalDestinationUri')
    ##FinalDestinationUri.text = drNumber
    ##print ET.tostring(root)
    newLookup = raw_input("Would you like to look up another(y,n)? ")


