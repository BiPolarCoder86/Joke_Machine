import requests
import json
import random


response = requests.get("https://v2.jokeapi.dev/joke/Programming")
data = response.text
parse_json = json.loads(data)
#print(response.status_code)


print("Welcome to the joke machine: ")
print()

while True:
    user_input = input("Would you like to hear a joke? ")
    if user_input.upper() == "Y":
        print()
        #print("Joke", parse_json)
        print(parse_json['joke'])
        print()
    elif user_input.upper() == "N":
        print()
        print("Alright, talk to you later.")
        print()
        break
    else:
        break

    
    #Response form of Dictionary
    #type = single                   ----twopart (later) 
    #joke                            ----(setup)                           ----delivery

#data = response.text
#parse_json = json.loads(data)
#print("Joke", parse_json)
#print(joke_form['joke'])

#keys_list = list(parse_json.values())
#print(keys_list) 





