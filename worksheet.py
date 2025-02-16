from random import randrange

def test(initialSize, probRemove):
    accCheap, accCosty = 0, 0
    s = initialSize
    m = 2*s
    for i in range(100000):
        if (randrange(100) < probRemove):
            if (s > 0):
                s -= 1
        else:
            if (s == m):
                m = m*2
                s += 1
                accCosty += 1
            else:
                s += 1
                accCheap += 1
    print("Initial size:", initialSize, "Prob Remove:", probRemove, "out of 100")
    print("Costly: {:7} ({:3.1}%)".format(accCosty,100*accCosty/(accCosty+accCheap)))
    print("Cheap: {:7} ({:3.1}%)".format(accCheap,100*accCheap/(accCosty+accCheap)))

def main():
    test(1, 0)
    test(100, 0)
    test(1000, 0)
    test(10000, 0)
    print("===================")
    test(1, 50)
    test(100, 50)
    test(1000, 50)
    test(10000, 50)

main()

# It's extremely difficult, or maybe impossible, to get 1% of the operations to be costly. To maximize the costly moves, I've made the initial size very small and the probability of removal zero. In this way, we've maximized the number of times the array needs to double in size, thus maximizing the costly moves.
# These results are notable in demonstrating the efficiency of dynamic arrays. The vast majority of moves are "cheap," and memory isn't taxed since the array grows only when necessary.