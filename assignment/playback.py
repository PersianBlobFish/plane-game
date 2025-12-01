text = input("")
text = text.split()
for i in range(len(text)-1): 
    text[i] = text[i]+("...")
text = "".join(text)
print(text)