class Animal(object):
    def __init__(self, name = None, cins = None):
        self.name = name
        self.types = ["dog", "cat"]
        self.type = self.types[cins]

class Queue(object):
    def __init__(self, head = None): # initiliaze with a list containing head as its first element
        # self.storage = [head] # again, if you have info inside array which is None, this will break your code!
        self.storage= []

    def enqueue(self, new_element, cins): # append to the end of the queue
        new_animal = Animal(new_element, cins)       
        self.storage.append(new_animal)

    def peek(self): # get the top of the queue
        return self.storage[0]

    def dequeueAny(self): # remove the top element from the queue
        return self.storage.pop(0)
    
    def dequeueCat(self): # remove the top cat from the queue
        counter = 0
        while self.storage[counter].type != "cat":
            counter += 1
        return self.storage.pop(counter)
              
    def dequeueDog(self): # remove the top dog from the queue
        counter = 0
        while self.storage[counter].type != "dog":
            counter += 1
        return self.storage.pop(counter)
    

q = Queue()
q.enqueue("Fistik", 1)
q.enqueue("Armut", 0)
q.enqueue("Kopek", 0)
q.enqueue("Kathy", 1)
print(q.dequeueDog().name)