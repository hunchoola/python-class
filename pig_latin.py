text = "hello"
vowels = "aeiou"
con_count = 0
for ch in text:
    if ch not in vowels:
        new = text[1:] + text[0]
print(new + "ay")