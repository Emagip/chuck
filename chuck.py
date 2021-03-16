import requests
people = requests.get("https://api.chucknorris.io/jokes/random")
people_json  = people.json()
print("One day Chuck Noris have said: ",people_json['value'])
