class bubbles(object):
        def __init__(self,nums):
                self.nums=nums
                self.nums_len=len(nums)
        def _sort(self):
                for i in range(self.nums_len-1):
                        for j in range(self.nums_len-i-1):
                                if(self.nums[j]>self.nums[j+1]):
                                        self.nums[j],self.nums[j+1]=self.nums[j+1],self.nums[j]
        def print_nums(self):
                print('the sorted numbers is:')
                for i in range(self.nums_len):
                        print ('%s' %(self.nums[i]))

numbers=bubbles([2,4,3,7,9,5,6])
numbers._sort()
numbers.print_nums()
