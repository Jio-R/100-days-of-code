from os import makedirs, chdir

day = input('Enter day to make: ')

if input("Day %s, proceed? (y/n): " % day).lower() == "n":
    exit()

paths = ["./day-%s/day-%s-exercises/" % (day,day), "./day-%s/day-%s-project/" % (day,day)]

[makedirs(i) for i in paths]
chdir(paths[1])

with open('main.py', 'x') as f:
    f.write("#paste instructions here")
    f.close()

print('Made %s, %s, and %s' % (paths[0], paths[1], paths[1]+"main.py/"))
