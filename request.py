import requests
import json
import random


response = requests.get("https://v2.jokeapi.dev/joke/Programming")

#print(response.status_code)

#print(response.json())
#Response form of Dictionary
    #type = single                   ----twopart (later) 
    #joke                            ----(setup)
    #                                ----delivery
data = response.text
joke_form = parse_json = json.loads(data)
#print("Joke", parse_json)
print(joke_form['joke'])

#keys_list = list(parse_json.keys())
#print(keys_list) 



