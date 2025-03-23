lista1 = []

# while, except value
for _ in range(5):
    while True:
        try:
            nums = int(input('Adj meg egy számot 1 és 1000 között: '))
            if 1 <= nums <= 1000:
                lista1.append(nums)
                break
            else:
                print('A számnak 1 és 1000 közé kell esnie!')
        except ValueError:
            print('Hiba! Kérlek csak számot adj meg!')
# even numbers
par = []
for i in lista1:
    if i % 2 == 0:
        par.append(i)
# numbers above 500
big = []
for ii in lista1:
    if ii > 500:
        big.append(ii)
# numbers above average
up = []
for iii in lista1:
    if iii > sum(lista1) / len(lista1):
        up.append(iii)

# prints
print(f'''Az általad megadott számok: {lista1}. 
A legkisebb szám a(z) {min(lista1)}, a legnagyobb a(z) {max(lista1)}. 
A számok átlaga: {sum(lista1) / len(lista1):.2f}! 
A listában {len(par)} páros szám található és {len(big)} darab szám van 500 felett!
A listában {len(up)} darab szám van az átlag felett, amik a következők: {up}.''')