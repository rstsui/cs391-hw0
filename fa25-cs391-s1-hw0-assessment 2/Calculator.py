class Calculator:
    def add(self, *nums):
        return sum(nums)
    def subtract(self,*nums):
        result = nums[0]
        for n in nums[1:]:
            result-=n
        return result
    def multiply(self, *nums):
        result =1
        for n in nums:
            result*=n
        return result
    def divide(self, a, b):
        return a/b
    def exponentiate(self, a, b):
        return a ** b
    