class MathDojo(object):
    def init(self):
        self.value = 0
    def add(self, num1, *nums):
        self.value += num1
        if nums:
            for i in nums:
                self.value += i
            return self
    def subtract(self, num1, *nums):
        self.value -= num1
        if nums:
            for i in nums:
             self.value -= i
             return self
md=MathDojo()
print md.add(2).add(2,5).subtract(3,2).value