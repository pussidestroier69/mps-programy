x = int(input('How many jobs? '))


i = 0

while i < x:
    y = int(input('Quantity in tray: '))
    z = int(input('First tray; '))
    v = int(input('Last tray: '))
    i+=1
    c = (v-z+1)
    c+=c
    o = c*y


print('You packed ', o , ' leaflets, in ' , x , 'jobs.')
