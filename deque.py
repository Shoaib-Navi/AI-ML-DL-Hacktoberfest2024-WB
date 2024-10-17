class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        """Add an item to the front of the deque"""
        self.items.insert(0, item)

    def add_rear(self, item):
        """Add an item to the rear of the deque"""
        self.items.append(item)

    def remove_front(self):
        """Remove and return the front item of the deque"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop(0)

    def remove_rear(self):
        """Remove and return the rear item of the deque"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()

    def peek_front(self):
        """Peek at the front item without removing it"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[0]

    def peek_rear(self):
        """Peek at the rear item without removing it"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[-1]

    def size(self):
        """Return the number of items in the deque"""
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Example usage:
if __name__ == "__main__":
    deque = Deque()
    
    deque.add_rear(10)
    deque.add_rear(20)
    deque.add_front(5)
    
    print("Deque after adding elements:", deque)  # Output: [5, 10, 20]
    
    print("Removed from front:", deque.remove_front())  # Output: 5
    print("Removed from rear:", deque.remove_rear())    # Output: 20
    
    print("Deque after removals:", deque)  # Output: [10]
    
    print("Peek front:", deque.peek_front())  # Output: 10
    print("Is deque empty?", deque.is_empty())  # Output: False
    print("Deque size:", deque.size())  # Output: 1

