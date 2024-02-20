text = "abcdefghijklmnop"
print(dir(text))
help(text.isupper())
print(text.isupper())
print("ABC".isupper())
print(text.upper())
print(text.upper().isupper())

new_text = text.upper()
print(text, new_text)
print("bannannnana".count("n"))
print("banabababnan".index("ana"))
print("banababanabnana".replace("ana", "XXYZZ"))
sentence = "Hello, kind-sir; how many! I be of service today?"
replace(",", "").replace(";", "").replace("!", "").replace("-", "")

# elegant way to do this
punctuation = ".,;!?-"
for p in punctuation:
    sentence = sentence.replace(p, "")
print(sentence)

print("this is a sentence and I want the word".split(" "))
text = "Bob goes to school. Bob like to play tennis. I am friends with Bob. Such a nice guy Bob is."
print(text.find("Bob"))
print(text.rfind("Bob"))
# find all the positions of Bob
i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1
