import requests
import json
import random


response = requests.get("https://v2.jokeapi.dev/joke/Programming")
data = response.text
joke_form = json.loads(data)
joke_sample = joke_form['joke']
sample_list = random.choice(joke_sample)

while True:
    user_input = input("Would you like to hear a joke? ")
    if user_input.upper() == "Y":
        print()
        #print("Joke", parse_json)
        #print(joke_form['joke'])
        print(sample_list)
        print()
    elif user_input.upper() == "N":
        print()
        print("Alright, talk to you later.")
        print()
        break
    else:
        break

#keys_list = list(parse_json.keys())
#print(keys_list) 


