class Node(object):
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        # The idea is to keep track of capacity via a doubly linked list
        # while having O(1) runtime for both get and put via a dictionary

        # The complicated part is keeping the two consistent with eachother

        ##################################################################################
        ### This is done by having the dictionary's keys refer DIRECTLY to nodes that  ###
        ### are in the doubly linked list!                                             ###
        ##################################################################################

        # Dictionary
        self.capacity = capacity
        self.cache = {}

        # Doubly Linked List
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        # Connect the surrounding nodes, before you...
        node.prev.next = node.next
        node.next.prev = node.prev
        
        # disconnect the given node from the doubly linked list
        node.next = None
        node.prev = None

    def add_to_front(self, node):
        # Given node is now connected to the front of the doubly linked list (it was most recently used!)
        node.prev = self.head
        node.next = self.head.next

        # Update the head of the linked list
        self.head.next = node

        # Update the previous MRU
        node.next.prev = node



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # Update doubly linked list keeping track of recency
            node = self.cache[key]
            self.remove(node)
            self.add_to_front(node)

            return node.value

        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # We're moving the node in the doubly linked list to the front, IF it exists
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Either we're adding a new node to the front, or recreating the old node
        # with the updated value information
        node = Node(key, value)
        self.add_to_front(node)

        # Update the cache
        self.cache[key] = node

        # Now we have to see whether the cache is over capacity
        if len(self.cache) > self.capacity:
            # We're over capacity, remove the LRU (previous node from dummy tail)
            lru = self.tail.prev
            self.remove(lru)

            # Update the dictionary, so that we stay "O(1)"
            del self.cache[lru.key]






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)