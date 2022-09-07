class fib_iterator():
    def __init__(self):
        self.index = 0
        self.fib_list = [0,1] 
    
    def __iter__(self):
        return self

    def last_item(self):
        return self.fib_list[len(self.fib_list)-1]
    
    def next_last_item(self):
        if len(self.fib_list) > 2:
            return self.fib_list[len(self.fib_list)-2]
        else:
            return self.fib_list[0]


    def __next__(self):
        if self.index >= len(self.fib_list):
            raise StopIteration
        index = self.index
        self.index += 1 
        return self.fib_list

    def make_fib_list(self):
        while self.last_item() < 1000:
            if (self.last_item() + self.next_last_item()) < 1000:
                self.fib_list.append(self.last_item() + self.next_last_item())
        return self.fib_list

heisann = fib_iterator()

print (heisann.make_fib_list())