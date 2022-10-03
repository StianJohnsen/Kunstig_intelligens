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
        self.sorted_lst = []
        self.first_index = 0
    
    def build_max_heap(self):
        for i in self.heap_lst:
            self.add(i)
    
    def reheapify(self,input_lst):
        new_heap = heap_sort(input_lst)
        new_heap.build_max_heap()
        self.lst = new_heap.return_lst()
        

    def do_heap_sort(self):
        while len(self.lst) > 0:
            self.swap(self.first_index,self.length)
            self.sorted_lst.append(self.lst[-1])
            self.lst = self.lst[:-1]
            self.reheapify(self.lst)

    def return_sorted_lst(self):
        return self.sorted_lst[::-1]

with open("Personer.dta") as file:
    data_line = file.read().replace(";"," ").splitlines()
heap_instance = heap_sort(data_line)
heap_instance.build_max_heap()
heap_instance.do_heap_sort()
for i in range(0,80001,20000):
    print(heap_instance.return_sorted_lst()[i])
