class Calculator:
    # adds all numbers together using built in feature
    def add(self, *nums):
        return sum(nums)
    # subtracts in order for first to last
    def subtract(self,*nums):
        result = nums[0]
        for n in nums[1:]:
            result-=n
        return result
    #multiplies all numbers
    def multiply(self, *nums):
        result =1
        for n in nums:
            result*=n
        return result
    # divides first by second number
    def divide(self, a, b):
        return a/b
    # divides first by second
    def exponentiate(self, a, b):
        return a ** b
    