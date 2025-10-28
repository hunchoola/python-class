import requests

word = input("Enter a word to get its definition: ")

url = (f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

try:
    response = requests.get(url)

    data = response.json()

    definition = data[0]['meanings'][0]['definitions'][0]['definition']

    print(f"\nDefinition of '{word}':")
    print(definition)


except Exception:
    print("An error occurred:")
