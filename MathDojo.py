class MathDojo:

    def __init__(self):
        self.result = 0
    
    def add(self, num , *nums):
        if len(nums) == 1:
            self.result = num + nums[0]
        elif len(nums) > 1:
            for x in (0,len(nums)-1):
                self.result += nums[x]    
            self.result += num
        else:
            self.result = num 

        return self
    

    def subtract(self, num , *nums):
        if len(nums) == 1:
            self.result = num - nums[0]
        elif len(nums) > 1:
            self.result = num
            for x in nums:
                self.result -= x
        else:
            self.result = num

        return self
        



md = MathDojo()

print(md.add(2).result)
print(md.add(2,3).result)
print(md.add(2,2,5,5).result)

print("*************")

print(md.subtract(2).result)
print(md.subtract(3,2).result)
print(md.subtract(20,10,5,1).result)


x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	


