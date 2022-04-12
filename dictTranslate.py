import json
from difflib import get_close_matches

data = json.load(open("data.json"))



def translate(w):
    w = w.lower()
    if w in data: 
        return "\n".join(data[w])
    elif len(get_close_matches(w, data.keys())) > 0:
        words = ", ".join(get_close_matches(w, data.keys()))
        return "Do you mean one of these words: \n " + words
        
    else:
        return "The word doesn't exist. Please double check it."


