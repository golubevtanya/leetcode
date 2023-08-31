#Stepik, Task 2.1
#Check correctness of brackets

#All kind of unicode characters can appear in input.
#If the input is correct, return "Success".
#if the input is wrong, return the number if the first element
#in the input string, where the error occurs. Which is:
#either the index of the first closing bracket, that has no
#openingone  before one or closing the wrong openong bracket,
#or the index of the first opening bracket, that has no
#corresponding closing one.

def check_brackets(s: str) -> str:
    arr = [] #initiate stack
    di = {'}':'{',']':'[',')':'('} #initiate dictionary of paired brackets
    for i,ch in enumerate(s):
        if ch in di: #if the closing bracket comes
            if len(arr)==0 or di[ch]!=arr[-1][0]: #if no brackets came before or
                                                  #the wrong opening one stands before 
                return i+1 #exit the fubction, return index+1 to attribute to 1-indexing
            elif di[ch]==arr[-1][0]: #if the right opening one stands before - pop it
                arr.pop()
        if ch in di.values(): #append opening brackets to stack
            arr.append([ch,i+1])
    if len(arr)!=0: #if all opening brackets are closed, the stack is empty
        return arr[0][1]
    else:
        return "Success"