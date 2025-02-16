from random import random

class Queue:
    def __init__(self):
        self.a_in = []
        self.a_out = []
        self.costly = 0
        self.cheap = 0
        
    def enqueue(self, d):
        self.cheap += 1
        self.a_in.append(d)

    def dequeue(self):
        if (self.a_out == []):
            if (self.a_in == []): # There's nothing to dequeue
                self.cheap += 1
                return None
            
            self.costly += 1 # There is something to dequeue, which is costly
            for d in self.a_in:
                self.a_out.append(d)
            self.a_in = []

        return self.a_out.pop(0)
    
def main():
    """
    Summary: Loops through asking a user to determine the probability that an enqueue will occurr in a double array queue. The program will simulate the array 100,000 times with that probability and determine what percentage of operations were costly vs. cheap.
    """
    q = Queue()
    t = True

    while t:
        try:
            print("\n")
            prob = float(input("Enter the probability of an enqueue between 0.34 and 0.66 \nSelect 0 to end \nProbability of an enqueue: "))

            if .34 <= prob <= .66:
                for n in range(100000):
                    if random() > prob:
                        q.enqueue(n)
                    else:
                        q.dequeue()

                cheap = q.cheap
                costly = q.costly
                percentage = round(costly/(cheap+costly)*100, 0)
                print(f"There were {costly} costly moves and {cheap} cheap moves. {percentage}% of the moves were costly.")

            elif prob == 0:
                return None
            
            else:
                print("Invalid number.")

        except:
            print("Invalid input. Try again.")
    
# =========================================

main()