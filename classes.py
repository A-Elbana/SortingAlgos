import random
from manim import Rectangle, VGroup, BraceBetweenPoints, Tex, UP, RIGHT, Write, Unwrite, BLACK, Circle, WHITE


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


class GapIndicator:
    def __init__(self, gap:int, n:int, width, st_position, scene):
        self.gap = gap
        self.n = n
        self.width = width
        self.st_position = st_position
        self.scene = scene
        self.moves:int = 0
        self.Indicators = VGroup()
        self.no_label = False
    
    def createIndicator(self):
        if self.gap == 1:
            return
        indicator = BraceBetweenPoints(self.st_position, self.st_position + RIGHT*(self.width)*self.gap, UP, buff = 0)
        if not self.no_label:
            indicator_text = Tex(f"$k = {self.gap}$", font_size=35).next_to(indicator, UP)
            if indicator_text.width > indicator.width:
                self.no_label = True
            else:
                indicator = VGroup(indicator, indicator_text)
        
        self.Indicators.add(indicator)
        self.scene.play(Write(indicator), run_time=0.5)

    def moveIndicators(self):
        if self.gap == 1:
            return
        self.moves += 1
        self.scene.play(self.Indicators.animate.shift(RIGHT*(self.width)), run_time=0.25)
        if self.moves%self.gap == 0:
            self.createIndicator()
    
    def __del__(self):
        self.scene.play(Unwrite(self.Indicators), run_time=1)

class Node(Circle):
    def __init__(self, **kwargs):
        # Initialize the outer circle using Circle's __init__
        params = kwargs.copy()
        params.pop("text")
        super().__init__(**params)

        radius = kwargs.get("radius")
        # Add the inner circle as a submobject
        self.add(
            VGroup(
                Circle(radius=radius, color=BLACK, z_index=0).set_opacity(1),
                Tex(kwargs.get("text")).scale_to_fit_height(radius),
            )
        )


class arrElement(Rectangle):
    def __init__(
        self,
        value: int = 0,
        color=WHITE,
        height=2,
        width=4,
        grid_xstep=None,
        grid_ystep=None,
        mark_paths_closed=True,
        close_new_points=True,
        **kwargs,
    ):
        # Initialize the rectangle with given parameters
        super().__init__(
            color,
            height,
            width,
            grid_xstep,
            grid_ystep,
            mark_paths_closed,
            close_new_points,
            **kwargs,
        )
        self.value = value
        # Add the value as a Tex object inside the rectangle
        self.add(Tex(value).scale_to_fit_height(self.width - 0.5 * self.width))