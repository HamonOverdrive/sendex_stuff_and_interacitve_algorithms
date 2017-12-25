class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        # size attribute INSTANCE to linked list that i can add to or subtract from if ex: pop, append, etc
        self.size = 0
        self.head = None
        # adding tail helps create append into linear O(1)
        self.tail = None

    def isEmpty(self):
        return self.head == None

    # its possible I could add a size attribute here......
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1

        # if addition of temp is first item in list tail will point to it
        if temp.getNext() == None:
            self.tail = temp

    # # replaced this size method for a size attribute instance
    # def size(self):
    #     current = self.head
    #     count = 0
    #     while current != None:
    #         count = count + 1
    #         current = current.getNext()
	#
    #     return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    # appends new item at end of unordered list it is O(n)
    def append(self,item):
        current = self.tail
        # found = False
        # make a node object from the current item argument
        temp = Node(item)

        # this condition makes append O(1) constant
        if self.size > 0:
            self.size += 1
            current.setNext(temp)
            current = current.getNext()
            print(current.getData())

        # this is for when O(n) linear
        # while current != None and not found:
        #     if current.getNext() == None:
        #         self.size += 1
        #         found = True
        #         # sets current next to new appended node which is at end of list
        #         current.setNext(temp)
        #         # current changes to end of list item checks state of list and end of unordered list is correct and has next as none
        #         current = current.getNext()
        #     else:
        #         current = current.getNext()

        # if empty list handles first append HANDLES BEGINNING SPECIAL CASE
        if current == None:
            self.size += 1
            temp.setNext(self.head)
            self.head = temp

    def insert(self,item,num):
        current = self.head
        previous = None
        count = 0
        found = False
        # at end switch if it becomes one then it means inserted at the end due to num length being to large
        skip_switch = 0
        # make a node object from the current item argument
        temp = Node(item)

        # handle special case if position number is larger than current list size
        # problem after this if statement ran it would go down to the last else statement and create another node. SOLVED
        if num > self.size:
            self.append(item)
            skip_switch = 1
            print(self.index(6), self.size)

        # while loop checks for index num of list breaks out once found
        while current != None and not found:
            if count == num:
                found = True
            else:
                previous = current
                current = current.getNext()
                count += 1
        # first if handles if list is empty second else handles if between two nodes
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
            self.size += 1
        # if the number switches is at 1 it will return and skip adding a unnecessary node
        elif skip_switch == 1:
            return
        else:
            temp.setNext(current)
            previous.setNext(temp)

    # index method?
    def index(self,num):
        current = self.head
        count = 0
        if num > self.size:
            a = "ERROR: index out bounds!"
            return a
        while current != None:
            if count == num:
                return current.getData()
            count += 1
            current = current.getNext()

    def pop(self):
        current = self.head
        previous = None
        found = False
        # find the end of the list
        while not found:
            if current.getNext() == None:
                found = True
            else:
                previous = current
                current = current.getNext()

        # first if statement handles if only one item on list
        if previous == None:
            self.size -= 1
            single = current.getData()
            # del current so node does not stay in memory when popped
            del current
            self.head = current.getNext()
            return single
        else:
            self.size -= 1
            x = current.getData()
            # del current so node does not stay in memory when popped
            del current
            previous.setNext(None)
            return x


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

# # Index Example?
# print(mylist.index(20))

# # Insert Example checker
# print(mylist.insert(3, 3))
# print(mylist.index(2))
# print(mylist.index(3))
# print(mylist.index(4))
# # checks special case insert if num is larger than length
# mylist.insert(24,14)
# print(mylist.index(6))
# print(mylist.size)

# # Append example
# mylist.append(2)
# print(mylist.size)
# print(mylist.search(2))

# # pop example
# print(mylist.size)
# print(mylist.pop())
# print(mylist.size)


# # all the below add search remove and size examples
# print(mylist.size())
# print(mylist.search(93))
# print(mylist.search(100))
#
# mylist.add(100)
# print(mylist.search(100))
# print(mylist.size())
#
# mylist.remove(54)
# print(mylist.size())
# mylist.remove(93)
# print(mylist.size())
# mylist.remove(31)
# print(mylist.size())
# print(mylist.search(93))

