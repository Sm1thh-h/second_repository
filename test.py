# for i in range(1,100):
#     print(i)

names = ["James", "Judah", "Iscariot"]

for name in names:
    if name.startswith("J"):
        print(name)

a = []
for i in range(1,10):
    if i % 2 == 0:
        a.append(i)
    print(a)

    
names = ["James", "Judah", "Iscariot"]
even_number = [i for i in names if i.startswith("J")]
print(even_number)
