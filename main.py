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

# loop through the requests for users to get as many facts as they wish for

ask = input("Do you wish to learn facts about cats? (y/n) ")
# add explanation about facts
print("Cat facts are little trivia pieces of information about cats.")

facts_store = []

while True:
    if ask.lower() == 'n':
        print("Thank you, have a nice day! ")
        break
    elif ask.lower() == 'y':
        # specify how many facts can be displayed in one request
        facts_num = int(input("How many facts do you wish to know? "))
        for _ in range(facts_num):
            http_response = requests.get(api_link)
            if http_response.status_code == 200:
                cat_fact = http_response.json().get("fact")
                # store the cat facts
                facts_store.append(cat_fact)
            else:
                print("You can't check the facts about cats for now. Try again later.")
                print("Error: Code error " + str(http_response.status_code))
                ask = input("Would you like to try again? ")
        if facts_store:
            for fact in facts_store:
                print(f"- {fact}")
        # clean the list of facts
        facts_store = []
    else:
        print("Please enter 'y' for yes or 'n' for no.")
    ask = input("\nDo you still want to know more facts about cats? (y/n)  ")