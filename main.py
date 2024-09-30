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

# create a function to fetch a cat fact from the api
def fetch_cat_fact():
    response = requests.get(api_link)
    if response.status_code == 200:
        return response.json().get('fact')
    else:
        return None

# create a function to check user input

def user_input():
    while True:
        inp = input("Do you wish to learn facts about cats (y/n)? ")
        if inp.lower() == 'n':
            return 'n'
        elif inp.lower() == 'y':
            return 'y'
        else:
            print("You can only enter 'y' or 'n'.")
# main program function

def main():
    print("Welcome to Cats Facts.\nHere you will get to know random facts about cats.\n")
    
    # main loop
    while True:
        ask = user_input()
        if ask == 'n':
            return "Thank you, have a nice day! "
        elif ask == 'y':
            try:
                facts_num = int(input("How many facts do you wish to know (Max: 10)? "))
                if facts_num > 10:
                    print("You are not allowed to request too many facts at once")
                    continue
            except ValueError:
                print("Please enter a valid number. ")
                continue
            
            # storage of facts for current request
            facts_store = []
            
            for _ in range(facts_num):
                fact = fetch_cat_fact() #fetch cat fact
                if fact is not None:
                    facts_store.append(fact)
                    
            if facts_store:  # Check if any facts were collected
                print("\nHere are your cat facts:")
                for fact in facts_store:
                    print(f"- {fact}")
            else:
                print("No facts were retrieved. Please try again later.")
print(main())
