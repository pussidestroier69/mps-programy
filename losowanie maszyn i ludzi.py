import random
x = ['Dan', 'Lukasz', 'Konrad', 'Madi', 'Ewelina B.', 'Ewelina', 'Gosia', 'Zosia', 'Ula', 'Tomek',]  # people list
y = []  # machine list
while True:
    p = input('how many people at overtimes?')
    if p.isdecimal():
        pp= int(p)
        break
        



i = 0

while i < pp:
    while True:
        c = input('name: ')
        if c.isdecimal():
            cc=str(c)
            x.append(c)
            break
    i+=1
    

i = 0
l = len(x) 

while i < l  :
    while True:
        d = input('machine nr:')
        if d.isdecimal():
            dd=int(d)
            y.append(d)
            break
    i+=1
print('---------------------------------------')
i = 0
random.shuffle(y)
random.shuffle(x)
i = 0
while i < l:
    print(x[i], y[i], sep=' - ')
    i+=1

