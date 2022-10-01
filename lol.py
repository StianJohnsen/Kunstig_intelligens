


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
        self.size = 0
        self.length = len(self.lst) - 1


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
        self.size += 1
        self.heapify_up()



    def heapify_up(self):
        self.index = self.size - 1
        while(self.has_parent(self.index) and self.get_parent(self.index) < self.lst[self.index]):
            self.swap(self.get_parent_index(self.index),self.index)
            self.index = self.get_parent_index(self.index)

    def heapify_down(self):
        self.index = 0
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



class heap_sort(heap):
    def __init__(self,heap_lst):
        super().__init__()
        self.heap_lst = heap_lst

        #print(self.lst)


    def build_max_heap(self):
        for i in self.heap_lst:
            self.add(i)


    def pop_lst(self):
        self.first_index = 0
        self.last_index = self.length
        while self.last_index > 0:
            self.swap(self.first_index,self.last_index)
            self.last_index -= 1
            self.heapify_down()






test_heap = heap_sort([2,1,0,100,4])
test_heap.build_max_heap()
print(test_heap.return_lst())
test_heap.pop_lst()
print(test_heap.return_lst())





