from collections import defaultdict


# My solution
# class TimeMap:

#     def __init__(self):
#         self.store = defaultdict(list)  # "key": [val, timestamp]
        

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.store[key].append([value, timestamp])


#     def get(self, key: str, timestamp: int) -> str:
#         res = ""
#         for k, vls in self.store.items():
#             if k == key:
#                 for v in vls:
#                     if v[1] <= timestamp:
#                         res = v[0]
#         return res


# Brute Force solution | Time: O(1) for set() and O(n) for get(), Space: O(m * n),
# where n = total number of unique timestamps associated with a key and m = total number of keys.
# class TimeMap:

#     def __init__(self):
#         self.keyStore = {}

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.keyStore:
#             self.keyStore[key] = {}
#         if timestamp not in self.keyStore[key]:
#             self.keyStore[key][timestamp] = []
        
#         self.keyStore[key][timestamp].append(value)

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.keyStore:
#             return ""
#         seen = 0

#         for time in self.keyStore[key]:
#             if time <= timestamp:
#                 seen = max(seen, time)
#         return "" if seen == 0 else self.keyStore[key][seen][-1]


# Binary Search solution | Time: O(1) for set() and O(log n) for get(), Space: O(m * n),
# where n = total number of unique timestamps associated with a key and m = total number of keys.
class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])
        l = 0
        r = len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res



if __name__ == "__main__":
    timeMap = TimeMap()

    # timeMap.set("alice", "happy", 1);
    # print(timeMap.get("alice", 1))
    # print(timeMap.get("alice", 2))
    # timeMap.set("alice", "sad", 3);  
    # print(timeMap.get("alice", 3))


    # timeMap.set("key1", "value1", 10)
    # print(timeMap.get("key1", 1))
    # print(timeMap.get("key1", 10))
    # print(timeMap.get("key1", 11))

    timeMap.set("test", "one", 10)
    timeMap.set("test", "two", 20)
    timeMap.set("test", "three", 30)
    print(timeMap.get("test", 15))
    print(timeMap.get("test", 25))
    print(timeMap.get("test", 35))