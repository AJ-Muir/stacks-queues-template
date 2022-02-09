# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         AJ Muir
# ASSIGNMENT:   Project 2: Stacks and Queues

from Queue import Queue
from Stack import Stack


# Return a new queue in reverse order
# Hint: can use a stack to help
def reverse(q_orig):
    q_new = Queue([])
    s_new = Stack([])
    i=0
    while i<len(q_orig):
        s_new.push(q_orig[i])
        i+=1
    q_orig.clear()
    j=0
    while j<len(s_new):
        q_new.enq(s_new[i])
        j+=1
    return q_new

def main():
    q = Queue(list(range(1, 5)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()