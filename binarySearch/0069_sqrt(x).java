public int findPosition(int[] nums, int target) {
    
    if (nums == null || nums.length == 0) {
        return -1;
    }

    int start = 0, end = nums.length - 1;

    // while start < end: 相邻就退出，start=1, end=2 就退出
    while (start + 1 < end) {
        // start，end=2^ 31，(start+end)/2对32bits int越界
        int mid = start + (end - start) / 2;
        if (nums[mid] == target) {
            start = mid;
        } else if (nums[mid] < target) {
            start = mid;
        } else {
            end = mid;
        }
    }
    
    if (nums[end] == target) {
        return end;
    }
    if (nums[start] == target) {
        return start;
    }

    return -1;
    
}