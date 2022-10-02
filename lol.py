
from xml.etree.ElementPath import get_parent_map


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



# for i in range(-5,0,1):
# print(lst_name[0][i],lst_name[1][i],lst_name[2][-i],lst_name[3][i],lst_name[4][i])
# print(lst_name[0][-5])


# Svar på oppgave 2 print(len(set(lst_name[3])))

# Oppgave 3

start_dict = {}

for i in lst_name[0]:
    if i in start_dict:
        start_dict[i] += 1
    if i not in start_dict:
        start_dict[i] = 1

sorted_dict = list(sorted(start_dict.items(),key=lambda item:item[1]))
#print('last name\t Occurence')
#for i in range(-1,-11,-1):
    #print(f'{sorted_dict[i][0]:8}\t{sorted_dict[i][1]:8}')
    
#for i in range(10):
    #print(last_name_lst[i])
# for i in five_highest_set_values:
#    print(i,return_key(i))

# print(start_dict.items())


# Oppgave 4

class heap:
    def __init__(self):
        self.lst = []
        self.top_index = 0
        self.index = 0
        self.bottom_index = len(self.lst)-1

    def get_left_child_index(self,parent_index):
        return 2*parent_index+1
    
    def get_right_child_index(self,parent_index):
        return 2*parent_index+2

    def get_parent_index(self,child_index):
        return (child_index-1)//2
    
    def has_left_child(self,index):
        return self.get_left_child_index(index) < self.size
    
    def has_right_child(self,index):
        return self.get_right_child_index(index) < self.size
    
    def has_parent(self,index):
        return self.get_parent_index(index) >= 0
    
    def get_left_child(self,index):
        return self.lst[self.get_left_child_index(index)]
    
    def get_right_child(self,index):
        return self.lst[self.get_right_child_index(index)]

    def get_parent(self,index):
        return self.lst[self.get_parent_index(index)]
    
    def swap(self,index_1,index_2):
        self.lst[index_1],self.lst[index_2] = self.lst[index_2],self.lst[index_1]
        
    def add(self,item):
        self.lst.append(item)
        self.index += 1
        self.heapify_up()

    def pop_lst(self):
        self.swap(self.top_index,self.bottom_index)
        self.bottom_index -= 1
        self.heapify_down()
        '''Vi bytter plass på index 0 og index størst
        Endrer størrelsen på listen til len -1'''

    def heapify_up(self):
        self.index = self.bottom_index
        #print(self.get_parent(self.index),self.lst[self.index])
        print(self.index,self.get_parent_index(self.index))
        while(self.has_parent(self.index) and self.get_parent(self.index) < self.lst[self.index]):
            self.swap(self.get_parent_index(self.index),self.index)
            self.index = self.get_parent_index(self.index)

    def heapify_down(self):
        self.index = self.top_index
        while(self.has_left_child(self.index)):
            self.bigger_child_index = self.get_right_child_index(self.index)
            if(self.has_left_child(self.index) and self.get_left_child(self.index) > self.get_right_child(self.index)):
                self.bigger_child_index = self.get_right_child_index(self.index)
            if (self.lst[self.index] > self.lst[self.bigger_child_index]):
                break 
            else:
                self.swap(self.index,self.bigger_child_index)
    
    def return_lst(self):
        return self.lst



test_heap = heap()

for i in (10,15,20,17,8):
    test_heap.add(i)

print(test_heap.return_lst())