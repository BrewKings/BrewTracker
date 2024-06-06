import sys

class Queue:
    def __init__(self):
        self.__queue = list()
        self.__size = 0

    def enqueue(self, item):
        self.__queue.insert(0,item)
        self.__size += 1

    def dequeue(self):
        if self.__size == 0:
            return Exception("The queue is empty")
        return self.__queue.pop()
    def __repr__(self):
        return "tail: " + str(self.__queue) + " :head"

if __name__ == "__main__":
    args = sys.argv[1:]
    q = Queue()
    # print(args)
    for arg in args:
        q.enqueue(arg)

    print(q)
    print("dequeing")
    for i in range(len(args)):
        print("\titem: " + q.dequeue())
        print("\t "+ str(q))
