#Stepik, Task 2.2
#Tree Hight

#A tree is given as a list of parents:
#a parent of each node i is stored in an array under index i.
#The root node is denoted with -1.
#Find the height of a tree.
#The input is garuanteed to be correct.

def get_tree_height(arr: List[int]) -> int:
    #The intuition is to go up the tree, remembering the heights
    #of the visited elements. Return the maximum height.

    #Until we reach the root, we do not know the height.
    stack  = []
    #Store the visited elements for later storing a dictionary
    #of node's height.
    memo = {}

    height = 0 #in case the tree is empty
    for i in range(N):
        h = 1
        #Fill the stack going up till the root.
        while arr[i]!=-1: 
            if i in memo:
                h += memo[i]
                break
            stack.append(i)
            i = int(arr[i])
        
        #Empty the stack saving the heights of visited nodes into a dict.
        while stack: 
            i = stack.pop()
            memo[i] = h
            h += 1

        #Store the maximum height.
        height = max(height,h) 
    return height