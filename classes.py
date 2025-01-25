import random
from manim import Rectangle

class Element(Rectangle):
    index = 0
    def __init__(self, index, width_):
        super().__init__(width=width_)
        self.index = index
        

    def __gt__(self, operand):
        if self.height > operand.height:
            return True
        else:
            return False
    def __st__(self, operand):
        if self.height < operand.height:
            return True
        else:
            return False
        
    def __ne__(self, operand):
        if self.height != operand.height:
            return True
        else:
            return False

    def set_index(self, index):
        if index >= 0:
            self.index = index






# Implementation using Durstenfeld-Fisher-Yates shuffle algorithm
class RNGenerator:
    def __init__(self, max_value) -> None:
        """Generator class

        Usage
        -
            Helps to iteratively generate a unique random number.
        """
        # Set max value of generator
        self.max_value = max_value
        self.numbers = list(range(1, max_value + 1))
        self.index = max_value

    def next(self) -> int:
        """Generates next unique random number using Durstenfeld-Fisher-Yates method.

        Returns:
            `int`: A unique random number.
        """
        if self.index == 0:
            raise ValueError("No more unique numbers to generate.")
        
        random_index = random.randint(0, self.index - 1)
        self.numbers[random_index], self.numbers[self.index - 1] = self.numbers[self.index - 1], self.numbers[random_index]
        self.index -= 1
        return self.numbers[self.index]
    




# # Inefficient random number generator
# class RNGenerator:
    
#     used_numbers = set()
#     def __init__(self, max_value) -> None:
#         """Generator class

#         Usage
#         -
#             Helps to iteratively generate a unique random number.
#         """
#         # Set max value of generator
#         self.max_value = max_value
#         pass

#     def next(self) -> int:
#         """Generates next unique random number.

#         Returns:
#             `int`: A unique random number.
#         """
#         while len(self.used_numbers) < self.max_value:
#             random_number = random.randint(1,self.max_value)
#             if random_number not in self.used_numbers:
#                 self.used_numbers.add(random_number)
#                 return random_number