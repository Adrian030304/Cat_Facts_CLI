#I will be making http requests and towards api 
import requests

#now I will create the link I will be using for the api url
api_link = "https://catfact.ninja/fact"

# this is an important endpoint for our get request , is is the above link of the api
# output --> a json response from the api
# request made -> you get a response back that contains all the info from the server

# requests.get() send a get request to the server , it has many arguments which can be filled up but the most important one to take not of is 
# the api endpoint link

http_response = requests.get(api_link) #returns a response object

# we notice that an object is being returned together with its status which is 200 for being ok , this means that the request was successful    
# will create a code logic which will display the result based on the status code
if http_response.status_code == 200:
    cat_fact = http_response.json().get("fact")
    print(cat_fact)
else:
    print("You can't check the facts about cats for now. Try again later.")