class RandomizedSet:

    def __init__(self):
        # List to store the values
        self.nums = []

        # Dictionary to store value -> index in the list
        self.pos = {}

    def insert(self, val: int) -> bool:
        # If value already exists, return False
        if val in self.pos:
            return False

        # Store the index of the new value in the dictionary
        self.pos[val] = len(self.nums)

        # Add the value to the list
        self.nums.append(val)

        # Value inserted successfully
        return True
        

    def remove(self, val: int) -> bool:
        # If value does not exist, return False
        if val not in self.pos:
            return False

        # Get the index of the value we want to remove
        index_to_remove = self.pos[val]

        # Get the last value from the list
        last_value = self.nums[-1]

        # Put the last value into the position of the value to remove
        self.nums[index_to_remove] = last_value

        # Update the index of the last value in the dictionary
        self.pos[last_value] = index_to_remove

        # Remove the last element from the list
        self.nums.pop()

        # Remove the deleted value from the dictionary
        del self.pos[val]

        # Value removed successfully
        return True
        

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()