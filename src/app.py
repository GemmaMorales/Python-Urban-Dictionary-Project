import requests, os, sys
import json
# Retrieve your API credentials from the .env file
if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
    print("ERROR! Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)

# Get credentials from the .env file
API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")

if len(sys.argv) == 1:
    user_input = input("What term do you want to look for?")
else:
    user_input = sys.argv[1]

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

querystring = {"term":user_input}

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "ed651e5f44msh05112fd96c9e4f0p1c4bbejsn5b09dd186da5"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response = response.json()

data = []
for x in response["list"]:
    data.append(x["definition"])
    print('\n'.join(data))
    
#print(response["list"][0]["definition"])

with open("src/" + user_input + ".json", "w+") as json_file:
    test = json.dumps(data)
    json_file.write(test)
    json_file.close()

# print("This is the name of the script: ", sys.argv[0])
# print("Number of arguments: ", len(sys.argv))
# print("The arguments are: " , str(sys.argv))
