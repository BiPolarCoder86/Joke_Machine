import requests
import json
import random


response = requests.get("https://v2.jokeapi.dev/joke/Programming")
data = response.text
joke_form = json.loads(data)
#print("Joke", parse_json)
print(joke_form['joke'])
#print(response.status_code)

#print(response.json())
#Response form of Dictionary
    #type = single                   ----twopart (later) 
    #joke                            ----(setup)
    #                                ----delivery


#keys_list = list(parse_json.keys())
#print(keys_list) 


