class ArrayQueue:
    
    DEFAULT_CAPACITY = 10          

    def __init__(self):
    
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._back = 0

    def __len__(self):
        
        return self._size

    def is_empty(self):
        
        return self._size == 0

    def first(self):
        
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    

    def Start(self):
        
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None        
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        self._back = (self._front + self._size - 1) % len(self._data)
        return answer
    
    def End(self):
        
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None         
        self._front = self._front
        self._size -= 1
        self._back = (self._front + self._size - 1) % len(self._data)
        return answer

    def end(self, e):
        
        if self._size == len(self._data):
            self._resize(2 * len(self.data))     
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        self._back = (self._front + self._size - 1) % len(self._data)
        
    def start(self, e):
        
        if self._size == len(self._data):
            self._resize(2 * len(self._data))     
        self._front = (self._front - 1) % len(self._data)
        avail = (self._front + self._size) % len(self._data)
        self._data[self._front] = e
        self._size += 1
        self._back = (self._front + self._size - 1) % len(self._data)

    def sizeagain(self, cap):                  
        
        old = self._data                       
        self._data = [None] * cap              
        walk = self._front
        for k in range(self._size):            
            self._data[k] = old[walk]            
            walk = (1 + walk) % len(old)         
        self._front = 0                          
        self._back = (self._front + self._size - 1) % len(self._data)
        
queue = ArrayQueue()
queue.end(1)
print(f"Start Element: {queue._data[queue._front]}, End Element: {queue._data[queue._back]}")
queue._data
queue.end(2)
print(f"Start Element: {queue._data[queue._front]}, End Element: {queue._data[queue._back]}")
queue._data
queue.Start()
print(f"Start Element: {queue._data[queue._front]}, End Element: {queue._data[queue._back]}")
queue.end(3)
print(f"Start Element: {queue._data[queue._front]}, End Element: {queue._data[queue._back]}")
queue.end(4)
print(f"Start Element: {queue._data[queue._front]}, End Element: {queue._data[queue._back]}")
queue.Start()
print(f"Start Element: {queue._data[queue._front]}, End Element: {queue._data[queue._back]}")
queue.start(5)
print(f"Start Element: {queue._data[queue._front]}, End Element: {queue._data[queue._back]}")
queue.End()
print(f"start Element: {queue._data[queue._front]}, End Element: {queue._data[queue._back]}")
queue.end(6)
print(f"Start Element: {queue._data[queue._front]}, End Element: {queue._data[queue._back]}")