class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = max(capacity, MIN_CAPACITY)
        self.storage = [None] * capacity
        self.load = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

        return self.load / self.get_num_slots()

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        byte_array = str(key).encode('utf-8')
        for byte in byte_array:
            hash = ((hash * 33) ^ byte) % 0x100000000
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        idx = self.hash_index(key)

        if self.storage[idx] != None:
            print("Collision")
            current_node = self.storage[idx]

            while current_node != None:
                if current_node.key == key:
                    current_node.value = value
                    return
                elif current_node.next == None:
                    current_node.next = HashTableEntry(key, value)
                    self.load += 1
                current_node = current_node.next

        else:
            self.storage[idx] = HashTableEntry(key, value)
            self.load +=1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)

        if self.storage[idx] != None:
            if self.storage[idx].key == key:
                self.storage[idx] = self.storage[idx].next
                return
            
            prev_node = self.storage[idx]
            current_node = self.storage[idx].next

            while current_node != None:
                if current_node.key == key:
                    prev_node.next = current_node.next
                    return
                else:
                    prev_node = current_node
                    current_node = current_node.next
            

        else:
            print('no such key')
            

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)

        if self.storage[idx] != None:
            print('Warning! No key!!!')
            current_node = self.storage[idx]

            while current_node != None:
                if current_node.key == key:
                    return current_node.value
                elif current_node.next == None:
                    return None
                current_node = current_node.next

        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_table = list(set(self.storage))

        self.capacity = max(new_capacity, MIN_CAPACITY)
        #create new array
        self.storage = [None] * self.capacity
        self.load = 0

        #loop over and put the old data into new array
        for item in old_table:
            self.put(item.key, item.value)
            if item.next != None:
                current_node = item.next
                while current_node != None:
                    self.put(current_node.key, current_node.value)
                    current_node = current_node.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
