alphabet = "abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"

f = open("secret.txt")
text = f.read()


lines = text.split("\n")
for line in Lines:


    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"

    f = open("secret.txt")
    text = f.read()

    lines = text.split("\n")
    for line in lines:
        decoded_line = ""
        for char in line:
            if char in alphabet:
                index = (alphabet.index(char) + 3) % 26
                decoded_line += alphabet[index]
            else:
                decoded_line += char
        print(decoded_line)
