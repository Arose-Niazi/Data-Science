import requests as req
import json
import re
import myToken


res = req.get("https://api.github.com/user", params={
    "access_token": myToken.myToken().TOKEN
})

data = json.loads(res.content)
print(data)



params = {
    "limit": 300
}
res = req.get("https://pokeapi.co/api/v2/pokemon?", params=params)

print("Response Code:", res.status_code)
print("Content:", res.content)
pokemons = json.loads(res.content)
pokemons = pokemons['results']
for pokemon in pokemons:
    print(pokemon['name'])

with open('data.txt', 'w') as outfile:
    for pokemon in pokemons:
        json.dump(pokemon, outfile)
        outfile.write("\n")
name = ""
for pokemon in pokemons:
    name = name + pokemon['name'] + "\n"
match = re.search(r"pid", name)
print(match.start())

texts = [
    "life science",
    "life sciences",
    "life. Science",
    "this data science problem"
]

for t in texts:
    x = re.match("\w+\s+science", t)
    print(x)
    if x != "None":
        print(x.string)