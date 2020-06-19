'''
981. Time Based Key-Value Store
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
 

Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

'''

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._values = collections.defaultdict(list)
        self._times = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self._values[key].append(value)
        self._times[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        times = self._times.get(key)
        if not time:
            return ''
        if times[0] > timestamp:
            return ''
        # there is timestamp(s) in times array, binary search
        index = bisect.bisect(times, timestamp) - 1
        return self._values.get(key)[index]
