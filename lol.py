def return_key(val):
    for key, value in start_dict.items():
        if value==val:
            return key
            
    return('Key Not Found')

lst_name = [
    [],
    [],
    [],
    [],
    [],
    []
]


with open('Personer.dta','r',encoding="latin-1") as file:
    
    data = file.read()
    data_la = data.replace('\n',';').split(';')
    for i in range(len(data_la)):  
        if i%5 == 0:
            lst_name[0].append(data_la[i])
        elif i%5 == 1:
            lst_name[1].append(data_la[i])
        elif i%5 == 2:
            lst_name[2].append(data_la[i])
        elif i%5 == 3:
            lst_name[3].append(data_la[i])
        else:
            lst_name[4].append(data_la[i])

#for i in range(-5,0,1):
    #print(lst_name[0][i],lst_name[1][i],lst_name[2][-i],lst_name[3][i],lst_name[4][i])
#print(lst_name[0][-5])


#print(len(set(lst_name[3])))
#Oppgave 3 

start_dict = {}

for i in lst_name[0]:
    start_dict[i] = 0

for i in lst_name[0]:
    start_dict[i]+=1

sorted_values = sorted(start_dict.values())
set_sorted_values = set(sorted_values)
#five_highest_set_values = [x for x in sorted_values[-1:-11:-1]]
#for i in five_highest_set_values:
#    print(i,return_key(i))

#print(start_dict.items())
for i in data_la:
    print(i)