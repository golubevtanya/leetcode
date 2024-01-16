'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''

import random
class RandomizedSet:

    def __init__(self):
        #we need two data structures to have O(1) search both by index
        #and by value
        self.di = dict()
        self.ind = []

    def insert(self, val: int) -> bool:
        if val in self.di:
            return False
        else:
            self.ind.append(val)
            self.di[val] = len(self.ind)-1
            return True
        
    def remove(self, val: int) -> bool:
        if val in self.di:
            i = self.di[val]
            #move the element to be deleted to the end
            #then it will take O(2)=O(1) to delete an element from an array
            self.ind[i], self.ind[-1] = self.ind[-1], self.ind[i]
            self.di[self.ind[i]] = i
            #it is important to delete an element from a dictionary after 
            #updating the dictionary - for the cirner case with 1 element
            del self.di[val]
            self.ind.pop()
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        i = random.randint(0, len(self.ind)-1)
        return self.ind[i]
        