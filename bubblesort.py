import math
from manim import *
import random


class RNGenerator:
    
    used_numbers = set()
    def __init__(self, max_value) -> None:
        """Generator class

        Usage
        -
            Helps to iteratively generate a unique random number.
        """
        # Set max value of generator
        self.max_value = max_value
        pass

    def next(self) -> int:
        """Generates next unique random number.

        Returns:
            `int`: A unique random number.
        """
        while len(self.used_numbers) < self.max_value:
            random_number = random.randint(1,self.max_value)
            if random_number not in self.used_numbers:
                self.used_numbers.add(random_number)
                return random_number



class BubbleSort(Scene):
    """Manim Scene Class
    """
    def construct(self):
        n=30 # Number of elements
        rn = RNGenerator(n) # Generator object
        shifting = 0.1 # Padding between bars

        # Get bar width relative to frame size
        bar_width = (self.camera.frame_width - 3) / (n + shifting * n)

        # Generate Title
        text = Tex(r"Bubble Sort $O(n^2)$", font_size=55).to_edge(DOWN)
        self.play(Write(text))

        # Generate Title
        text = Tex("By Abdelrahman Elbana", font_size=50).to_edge(UP+LEFT).set_color_by_gradient(GREEN,GREEN,DARK_BLUE)
        self.play(Write(text))

        # Setup bar for each element
        array=[Rectangle(width=bar_width) for _ in range(n)]
        for i in range (0, n):
            # Stretch bar height appropriately to fit in frame. Height range: [(half screen height)/n, (half screen height)].
            array[i].stretch_to_fit_height(rn.next() /(n*1.0) * self.camera.frame_height * 0.5)

            # Shift bar to the right by its width + the shifting which acts as padding
            array[i].shift(RIGHT*(bar_width+shifting)*i)
            
            # Align the bottom edge of each bar
            array[i].align_to((0,0,0),DOWN)
        group=VGroup(*array)
        group.move_to(ORIGIN)
        group.set_fill(WHITE,opacity=1)
        self.play(*[Write(o) for o in array])
        # /Setup

        # Run Bubble Sort
        for i in range(n):
            for j in range(n-i-1):
                if array[j].height>array[j+1].height:
                    # Highlight elements being processed
                    self.play(array[j].animate.set_fill(RED), array[j+1].animate.set_fill(RED),array[j].animate.set_color(RED), array[j+1].animate.set_color(RED), run_time = 0.1)

                    pj = array[j].get_bottom()
                    pj1 = array[j+1].get_bottom()
                    # Switch positions visually
                    self.play(
                        array[j].animate.shift(pj1-pj),
                        array[j+1].animate.shift(pj-pj1), run_time = 0.07
                    )
                    # Swap array positions
                    array[j], array[j+1] = array[j+1], array[j]

                    # Revert highlighting (Instantaneous, no animation)
                    array[j].set_fill(WHITE)
                    array[j+1].set_fill(WHITE)
                    array[j].set_color(WHITE)
                    array[j+1].set_color(WHITE)
        
        # Create a new Vector group of the now ordered elements to play a staggered animation
        ordered_group = VGroup(*array)
        self.play(ordered_group.animate(lag_ratio=0.5).set_fill(GREEN), ordered_group.animate(lag_ratio=0.5).set_color(GREEN))
        self.wait(5)
