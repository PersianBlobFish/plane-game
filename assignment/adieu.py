import inflect

p = inflect.engine()
name = input("Name: ")
names = []
while True:
    names.append(name)
    name = input("Name: ")
    if name == '':
        print(f"Adieu, adieu, to {p.join(names)}")
        break
    
