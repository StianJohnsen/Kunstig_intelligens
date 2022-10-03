lst_name = [
    [],
    [],
    [],
    [],
    [],
    []
]

with open('Personer.dta', 'r', encoding="latin-1") as file:
    data = file.read()
    data_lst = []
    data_la = data.replace('\n', ';').split(';')
    for i in range(len(data_la)):
        if i % 5 == 0:
            lst_name[0].append(data_la[i])
        elif i % 5 == 1:
            lst_name[1].append(data_la[i])
        elif i % 5 == 2:
            lst_name[2].append(data_la[i])
        elif i % 5 == 3:
            lst_name[3].append(data_la[i])
        else:
            lst_name[4].append(data_la[i])



for i in range(-5,0,1):
    print(lst_name[0][i],lst_name[1][i],lst_name[2][i],lst_name[3][i],lst_name[4][i])



# Svar på oppgave 2 print(len(set(lst_name[3])))

# Oppgave 3

start_dict = {}

for i in lst_name[0]:
    start_dict[i] = 0

for i in lst_name[0]:
    start_dict[i] += 1

sorted_dict = list(sorted(start_dict.items(),key=lambda item:item[1]))
#print('last name\t Occurence')
#for i in range(-1,-11,-1):
#    print(f'{sorted_dict[i][0]:8}\t{sorted_dict[i][1]:8}')
    
#for i in range(10):
    #print(last_name_lst[i])
# for i in five_highest_set_values:
#    print(i,return_key(i))

# print(start_dict.items())
