class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data, index=None):
        new_node = Node(data)
        if(index != None):
            if (self.head is None and index <= 0):
                print("invalid index")
            else:
                current = self.head
                new_node = Node(data)
                i = 0
                while (current.get_next() is not None and i < index -1 ):
                    current = current.get_next()
                    i += 1
                new_node.set_next(current.get_next())
                current.set_next(new_node)

        elif(self.head is None):

            self.head = new_node
        else:
            current = self.head
            while(current.get_next() is not None):
                current = current.get_next()
            current.set_next(new_node)



    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current is not None and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())