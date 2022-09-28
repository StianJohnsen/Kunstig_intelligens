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


#Her er rett svar på oppgave 2: print(len(set(lst_name[3])))




