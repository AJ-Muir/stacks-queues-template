# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         FIXME
# ASSIGNMENT:   Technical HW: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(q):
    len = 0                         #length of longest duplicates
    highest = 1                     #counts duplicates to find highest
    while q.is_empty() == False:
        s = q.deq()                 #
        if s == q.front():
            highest+=1
        else:
            highest = 1
        if highest > len:
            len = highest
    #q.clear()
    return len

def main():
    print("out 2:", count_longest( Queue( [ l for l in "hello" ] ) ))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee"])))


# Don't run main on import
if __name__ == "__main__":
    main()

