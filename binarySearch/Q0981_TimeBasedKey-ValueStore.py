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