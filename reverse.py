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
    q_new = Queue([])                   # Queue that will be returned
    s_new = Stack([])                   # Stack to help reverse Queue
    while q_orig.is_empty() == False:   # Will q_orig has elements left
        s_new.push(q_orig.deq())        # q_orig deques into s_new (pushes)
    q_orig.clear()                      # destroys q_orig
    while s_new.is_empty() == False:
        q_new.enq(s_new.pop())          # s_new pops into q_new (enqueues)
    s_new.clear()                       # destroys s_new
    return q_new                        

def main():
    q = Queue(list(range(1, 5)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()