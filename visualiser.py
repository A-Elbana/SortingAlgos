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
        self.play(ordered_group.animate(lag_ratio=0.3).set_fill(GREEN), ordered_group.animate(lag_ratio=0.5).set_color(GREEN))
        self.wait(5)


class SelectionSort(Scene):
    """Manim Scene Class
    """
    def construct(self):
        n=30 # Number of elements
        rn = RNGenerator(n) # Generator object
        shifting = 0.1 # Padding between bars

        # Get bar width relative to frame size
        bar_width = (self.camera.frame_width - shifting * n - 3) / (n)

        # Generate Title
        text = Tex(r"Selection Sort $O(n^2)$", font_size=55).to_edge(DOWN)
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

        # Run Selection Sort
        for i in range(n):
            curr_min = i
            self.play(array[i].animate.set_fill(RED), run_time = 0.1)
            for j in range(i+1, n):
                curr_item = j
                self.play(array[curr_item].animate.set_fill(YELLOW_D), array[curr_item].animate.set_color(YELLOW_D), run_time = 0.07)
                if array[curr_item].height < array[curr_min].height:
                    self.play(array[curr_min].animate.set_fill(WHITE), array[curr_min].animate.set_color(WHITE), run_time = 0.1)
                    curr_min = curr_item
                    self.play(array[curr_min].animate.set_fill(RED), run_time = 0.1)
                    continue
                self.play(array[curr_item].animate.set_fill(WHITE), array[curr_item].animate.set_color(WHITE), run_time = 0.07)
            
            pj = array[i].get_bottom()
            pj1 = array[curr_min].get_bottom()
            # Switch positions visually
            self.play(
                array[i].animate.shift(pj1-pj),
                array[curr_min].animate.shift(pj-pj1), run_time = 0.07
            )
            array[i], array[curr_min] = array[curr_min], array[i]
            self.play(array[i].animate.set_fill(GREEN), run_time = 0.07)
        
        # Create a new Vector group of the now ordered elements to play a staggered animation
        ordered_group = VGroup(*array)
        self.play(ordered_group.animate(lag_ratio=0.3).set_color(GREEN))
        self.wait(5)




def swap(a:Rectangle,b:Rectangle,scene):
    # Switch positions visually
    if a.height != b.height:
        # Make sure we are not switching the same bar. (Example: When our new bar position is not changed)
        pj = a.get_bottom()
        pj1 = b.get_bottom()
        scene.play(
            a.animate.shift(pj1-pj),
            b.animate.shift(pj-pj1), run_time = 0.07
        )

from collections import deque

class MergeSort(Scene):
    """Manim Scene Class
    """
    def construct(self):
        n=30 # Number of elements
        rn = RNGenerator(n) # Generator object
        shifting = 0.1 # Padding between bars

        # Get bar width relative to frame size
        bar_width = (self.camera.frame_width - shifting * n - 3) / (n)

        # Generate Title
        text = Tex(r"Merge Sort $O(n \log(n))$", font_size=55).to_edge(DOWN)
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
        arraydict = {obj.height:index for index, obj in enumerate(array)} # This will help us retrieve current position by only using the onjects height
        # /Setup

        # Run Merge Sort
        
        def merge(a:deque[Rectangle],b:deque[Rectangle]):
            merged = deque([])
            
            c = list(a+b)
            curr_pos = n + 1
            for item in c:
                curr_pos = min(arraydict[item.height], curr_pos)
            mergedVGroup = VGroup(*c)
            self.play(mergedVGroup.animate.set_fill(BLUE), run_time=0.1)
            while a and b:
                self.play(b[0].animate.set_fill(RED),a[0].animate.set_fill(RED), run_time=0.1)
                if a[0].height < b[0].height:
                    swap(array[curr_pos], array[arraydict[a[0].height]], self)
                    
                    # Update dictionary by switching indices
                    arraydict[a[0].height], arraydict[array[curr_pos].height] =  arraydict[array[curr_pos].height], arraydict[a[0].height]

                    # Update bars array by switching indices
                    array[arraydict[array[curr_pos].height]], array[arraydict[a[0].height]] = array[arraydict[a[0].height]], array[arraydict[array[curr_pos].height]]

                    # Traverse to next bar position
                    curr_pos += 1
                    merged.append(a[0])
                    self.play(b[0].animate.set_fill(BLUE),a[0].animate.set_fill(BLUE), run_time=0.1)
                    a.popleft()
                else:
                    swap(array[curr_pos], array[arraydict[b[0].height]], self)

                    # Update dictionary by switching indices
                    arraydict[b[0].height], arraydict[array[curr_pos].height] =  arraydict[array[curr_pos].height], arraydict[b[0].height]

                    # Update bars array by switching indices
                    array[arraydict[array[curr_pos].height]], array[arraydict[b[0].height]] = array[arraydict[b[0].height]], array[arraydict[array[curr_pos].height]]
                    
                    # Traverse to next bar position
                    curr_pos += 1
                    merged.append(b[0])
                    self.play(b[0].animate.set_fill(BLUE),a[0].animate.set_fill(BLUE), run_time=0.1)
                    b.popleft()
                
            
            while a:
                swap(array[curr_pos], array[arraydict[a[0].height]], self)
                # Update dictionary by switching indices
                arraydict[a[0].height], arraydict[array[curr_pos].height] =  arraydict[array[curr_pos].height], arraydict[a[0].height]

                # Update bars array by switching indices
                array[arraydict[array[curr_pos].height]], array[arraydict[a[0].height]] = array[arraydict[a[0].height]], array[arraydict[array[curr_pos].height]]

                # Traverse to next bar position
                curr_pos += 1
                merged.append(a[0])
                a.popleft()
            while b:
                swap(array[curr_pos], array[arraydict[b[0].height]], self)
                # Update dictionary by switching indices
                arraydict[b[0].height], arraydict[array[curr_pos].height] =  arraydict[array[curr_pos].height], arraydict[b[0].height]

                # Update bars array by switching indices
                array[arraydict[array[curr_pos].height]], array[arraydict[b[0].height]] = array[arraydict[b[0].height]], array[arraydict[array[curr_pos].height]]
                
                # Traverse to next bar position
                curr_pos += 1
                merged.append(b[0])
                b.popleft()
            
            self.play(mergedVGroup.animate.set_fill(WHITE), run_time=0.1)
            return merged
        def mergeSort(array) -> deque[Rectangle]:
            if len(array) == 1:
                return deque(array)
            arr1 = array[:len(array)//2]
            arr2 = array[len(array)//2 :]

            arr1 = mergeSort(arr1)
            arr2 = mergeSort(arr2)

            return merge(arr1, arr2)

        list(mergeSort(array))
        
        # Create a new Vector group of the now ordered elements to play a staggered animation
        ordered_group = VGroup(*array)
        self.play(ordered_group.animate(lag_ratio=0.2).set_color(GREEN))
        self.wait(5)
