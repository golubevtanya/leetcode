#Stepik, Task 2.3
#Network Packet Handling

#Processor handles packets one after another, in their arrival order.
#If processor is busy with one of the previous requests,
#the packet will be kept in memory of size n.
#The packet that comes when memory is full will not be handled.
#Input contains if size n and two arrays with arrival and duration time.
#We are sure that the input always comes in the right format.
#Arrival time: the time at which the packet arrives
#Duration time: the time it takes for processor to handle the packet
#Return the time, at which processor will start handling each packet
#-1 if the packet will not be handled
from collections import deque                                   

class Processor:
    def __init__(self, size: int):
        self.size = size
        self.deq = deque([])
        
    def add(self, ar: int, dur: int):
        #When a new package arrives, check if some packets were already processed
        #and can be discarded from the memory.

        while self.deq and self.deq[0]<=ar:
            self.deq.popleft()
            
        #start the handling proceess, if there is available memory.
        if len(self.deq)<size:
            
            #The handling will start when the processor will be free from the previous tasks
            #or at the time of packet's arrival, if it arrives after finishing of the previous tasks.
            time = max(time, ar)

            #By the end of the packet processing, processor will be at the time of handling start + 
            #duration of process handling. We append this value to the stack.
            self.deq.append(time+dur)
            return time
        else:
            return -1

def packer_handling (size:int, arrival: List[int], duration: List[int]) -> List[int]:
    ans = []
    Proc = Processor(size)
    for a,d in zip(arrival, duration):
        ans.append(Proc.add(a,d))
    return ans