
import json
from berryfield import berryfield
from bear import bear
from tourist import tourist

def update(grid, allbears, alltourists):
    for i in range(a.numrows):
        for j in range(a.numcolumns):
            #places bears and tourists in dictionary
            a.grid[(i,j)]['bear_there']=False
            for k in allbears:
                if k.pos()==(i,j) and k.onfield:
                    a.grid[(i,j)]['bear_there']=True
            a.grid[(i,j)]['tourist_there']=False
            for y in alltourists:
                if y.pos()==(i,j) and y.onfield:
                    a.grid[(i,j)]['tourist_there']=True
def turn():
    for i in allbears:
        i.take_turn(a.grid[i.pos()]['tourist_there'],a.numrows, a.numcolumns)
        a.grid[i.pos()]['berries']=0
        
def seebears():
    for i in alltourists:
        for k in allbears:
            if k.onfield and i.onfield:
                if abs(k.row-i.row)<=4 or abs(k.column-i.column)<=4:
                    i.bears_seen+=1
                if k.row==i.row and k.column==i.column and k.killed:
                    i.onfield=False
            if not k.onfield:
                a.grid[k.pos()]['bear_there']=False
            if not i.onfield:
                a.grid[i.pos()]['tourist_there']=False
def print_bears():
    print('Active Bears:')
    for k in allbears:
        if k.onfield:
            print(k)
    print('')
def print_tourists():
    print('Active Tourists:')
    for k in alltourists:
        if k.onfield:
            print(k)


json_file=input('Enter the json file name for the simulation => ')
#json_file='bears_and_berries_1.json'
print(json_file)
f=open(json_file)
data=json.loads(f.read())

allbears=[]
for i in range(len(data['active_bears'])):
    allbears.append(bear(data['active_bears'][i][0], data['active_bears'][i][1], data['active_bears'][i][2], True))
for i in range(len(data['reserve_bears'])):
    allbears.append(bear(data['reserve_bears'][i][0], data['reserve_bears'][i][1], data['reserve_bears'][i][2], False))
alltourists=[]
for i in range(len(data['active_tourists'])):
    alltourists.append(tourist(data['active_tourists'][i][0], data['active_tourists'][i][1], True))
for i in range(len(data['reserve_tourists'])):
    alltourists.append(tourist(data['reserve_tourists'][i][0], data['reserve_tourists'][i][1], False))

a=berryfield(data['berry_field'])
update(a,allbears,alltourists)
print('Starting Configuration')
print('\nField has {} berries.'.format(a.count_berries()))
print(a)
for i in range(1,20):
    a.grow()
    turn()
    seebears()
    if i%5==0:
        print('')
        print('Turn:',i)
    update(a,allbears,alltourists)
    if i%5==0:
        print('\nField has {} berries.'.format(a.count_berries()))
        print(a)
    print_bears()
    print_tourists()




