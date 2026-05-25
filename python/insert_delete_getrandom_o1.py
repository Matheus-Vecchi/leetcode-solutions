# ======================================
# LeetCode Problem: insert delete getrandom o1
# Language: python3
# Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
# Synced by: LinkCode
# Date: 25/05/2026, 15:09:05
# ======================================


import random


class RandomizedSet:

    def __init__(self):
        self.array = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.array)
            self.array.append(val)
            return True
        
        return False


    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False

        self.hashmap[self.array[-1]] = self.hashmap[val]
        if len(self.array) > 1:
            self.array[self.hashmap[val]] = self.array[-1]
        del self.hashmap[val]

        self.array.pop()

        return True

    def getRandom(self) -> int:
        if self.array:
            return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()