class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
    
    def enqueue(self, animal, type):
        if type == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    
    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        return self.cats.pop(0)
    
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        return self.dogs.pop(0)
    
    def dequeueAny(self):
        if len(self.cats) == 0:
            return self.dogs.pop(0)
        else:
            return self.cats.pop(0)

cq = AnimalShelter()
cq.enqueue("Cat1", "Cat")
cq.enqueue("Cat2", "Cat")
cq.enqueue("Dog1", "Dog")
cq.enqueue("Cat3", "Cat")
cq.enqueue("Dog2", "Dog")
print(cq.dequeueCat())
print(cq.dequeueAny())