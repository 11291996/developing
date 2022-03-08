class Solution:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
    def findMedianSortedArrays(self):
        short, long = self.nums1, self.nums2 
        total = len(short) + len(long)
        mid = total // 2 
        if len(short) > len(long):
            short, long = long, short 
        left, right = 0, len(short) - 1     
        while True:
            i = (left + right) // 2 #initial mid point of the short 
            #this equation always splits the total elements into half   
            j = mid - i - 2  
            short_left = short[i] if i >= 0 else float('-inf')
            short_right = short[i + 1] if (i + 1) < len(short) else float('inf') 
            long_left = long[j] if j >= 0 else float('-inf')
            long_right = long[j + 1] if (j + 1) < len(long) else float('inf')
            #condition suitable for the median
            if short_left <= long_right and short_right >= long_left:
                #calculate the median 
                #odd
                if total % 2:
                    return min(short_right, long_right)
                #even
                return (max(short_left, long_left) + min(short_right, long_right))/2
            #use binary comparison to satisfy the condition
            elif short_left > long_right:
                #move an index to the left -> i decrease and j increase
                right = i - 1 
            else:
                #move an index to the right -> i increase and j decrease
                left = i + 1 

if __name__ == '__main__':
    nums1 = [1,3,5,6]
    nums2 = [2,4,7]
    case1 = Solution(nums1, nums2)
    print(case1.findMedianSortedArrays())