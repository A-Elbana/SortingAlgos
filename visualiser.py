from manim import *
import random
N = 30 # Number of elements

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


def generateName():
    githubName = Tex("Github: A-Elbana/SortingAlgos", font_size=38).to_edge(UP+LEFT).set_color_by_gradient(GREEN,GREEN,DARK_BLUE)

    return githubName


class BubbleSort(Scene):
    """Manim Scene Class
    """
    def construct(self):
        n=N # Number of elements
        rn = RNGenerator(n) # Generator object
        shifting = 0.1 # Padding between bars

        # Get bar width relative to frame size
        bar_width = (self.camera.frame_width - 3) / (n + shifting * n)

        # Generate Title
        text = Tex(r"Bubble Sort $O(n^2)$", font_size=55).to_edge(DOWN)
        self.play(Write(text))

        # Generate Credits
        githubName = generateName()
        self.play(Write(githubName))

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
                    array[j].set_color(WHITE)
                    array[j+1].set_color(WHITE)
                    if j+1 == n-i-1:
                        array[j+1].set_fill(GREEN)
        
        # Create a new Vector group of the now ordered elements to play a staggered animation
        ordered_group = VGroup(*array)
        self.play(ordered_group.animate(lag_ratio=0.3).set_fill(GREEN), ordered_group.animate(lag_ratio=0.5).set_color(GREEN))
        self.wait(5)


class SelectionSort(Scene):
    """Manim Scene Class
    """
    def construct(self):
        n=N # Number of elements
        rn = RNGenerator(n) # Generator object
        shifting = 0.1 # Padding between bars

        # Get bar width relative to frame size
        bar_width = (self.camera.frame_width - shifting * n - 3) / (n)

        # Generate Title
        text = Tex(r"Selection Sort $O(n^2)$", font_size=55).to_edge(DOWN)
        self.play(Write(text))

        # Generate Credits
        githubName = generateName()
        self.play(Write(githubName))

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
                self.play(array[curr_item].animate.set_fill(YELLOW_D), run_time = 0.07)
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




def swap(a:Rectangle,b:Rectangle,scene, run_time = 0.07, sim_anim = []):
    # Switch positions visually
    if a.height != b.height:
        # Make sure we are not switching the same bar. (Example: When our new bar position is not changed)
        pj = a.get_bottom()
        pj1 = b.get_bottom()
        scene.play(
            a.animate.shift(pj1-pj),
            b.animate.shift(pj-pj1),
            *sim_anim,
            run_time = run_time
        )

# Import the double-ended queue data structure
from collections import deque

class MergeSort(Scene):
    """Manim Scene Class
    """
    def construct(self):
        n=N # Number of elements
        rn = RNGenerator(n) # Generator object
        shifting = 0.1 # Padding between bars

        # Get bar width relative to frame size
        bar_width = (self.camera.frame_width - shifting * n - 3) / (n)

        # Generate Title
        text = Tex(r"Merge Sort $O(n \log(n))$", font_size=55).to_edge(DOWN)
        self.play(Write(text))

        # Generate Credits
        githubName = generateName()
        self.play(Write(githubName))

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



class QuickSort(Scene):
    """Manim Scene Class
    """
    def construct(self):
        n=N # Number of elements
        rn = RNGenerator(n) # Generator object
        shifting = 0.1 # Padding between bars

        # Get bar width relative to frame size
        bar_width = (self.camera.frame_width - shifting * n - 3) / (n)

        # Generate Title
        title = Tex(r"Quick Sort $O(n \log(n))$", font_size=55).to_edge(DOWN)
        self.play(Write(title))

        # Generate Credits
        githubName = generateName()
        self.play(Write(githubName))

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


        # Move Title
        self.play(title.animate.to_edge(UP+RIGHT), run_time=0.5)

        # # Run Quick Sort
        def partition(arr:list[Rectangle], low:int, high:int):
            # Choose pivot using the median-of-three method
            helper = [ low, (high+low+1) // 2, high]
            medianOfThree = [arr[low].height,arr[(high+1+low)//2].height, arr[high].height]

            # Use unrolled Bubble Sort to sort the array
            for i in range(2):
                for j in range(2-i):
                    if medianOfThree[j] > medianOfThree[j+1]:
                        medianOfThree[j], medianOfThree[j+1] = medianOfThree[j+1], medianOfThree[j]
                        arr[helper[j]], arr[helper[j+1]] = arr[helper[j+1]], arr[helper[j]]
                        swap(arr[helper[j]], arr[helper[j+1]], self, 0.1)
            self.wait(0.5)
            
            pivot_pos = (high+1+low)//2
            # Setup pointers used to parse and arrange array into two sub-arrays (Greater than pivot and smaller than pivot)
            l_idx = low
            l_idx_indicator = VGroup()
            l_idx_arrow = Arrow(start= arr[l_idx].get_bottom() + 1.4*DOWN, end=arr[l_idx].get_bottom()+0.4*DOWN, color=WHITE)
            l_idx_indicator.add(l_idx_arrow)
            l_idx_indicator.add(Text("l_idx",font_size=20,color=BLUE_B).next_to(l_idx_arrow, DOWN))

            r_idx = high - 1
            r_idx_indicator = VGroup()
            r_idx_arrow = Arrow(start= arr[r_idx].get_bottom() + 1.4*DOWN, end=arr[r_idx].get_bottom()+0.4*DOWN, color=WHITE)
            r_idx_indicator.add(r_idx_arrow)
            r_idx_indicator.add(Text("r_idx",font_size=20,color=RED).next_to(r_idx_arrow, DOWN))
            

            #--------Visuals--------
            # Label used to indicate where the pivot is located
            pivot_title = Text("Pivot",font_size=25).move_to(arr[pivot_pos].get_bottom() + 0.4*DOWN)
            self.play(arr[pivot_pos].animate.set_fill(YELLOW_D), Write(pivot_title), run_time=0.15)
            self.wait(0.5)
            pj = arr[pivot_pos].get_bottom()
            pj1 = arr[high].get_bottom()
            self.play(
                arr[pivot_pos].animate.shift(pj1-pj),
                arr[high].animate.shift(pj-pj1),
                pivot_title.animate.shift(pj1-pj),
                run_time = 0.5
            )
            #--------/Visuals--------
            
            # Move pivot to the end of the array
            arr[high], arr[pivot_pos] = arr[pivot_pos], arr[high] # pivot = arr[high]

            #--------Visuals--------
            pivot_arrow_1 = Arrow(start= arr[l_idx].get_bottom() + 1.3*DOWN, end=arr[l_idx].get_bottom(), color=WHITE,buff=0).align_to(pivot_title.get_center(), UP)

            pivot_arrow_2 = Arrow(start= pivot_arrow_1.get_start(), end=[pivot_title.get_x(),pivot_arrow_1.get_bottom()[1],pivot_arrow_1.get_z()],stroke_width=6,max_stroke_width_to_length_ratio=float('inf'), color=WHITE,buff=0, max_tip_length_to_length_ratio=0)

            pivot_arrow_2.shift(UP * 0.02)
            pivot_arrow_3 = Arrow(start= pivot_arrow_2.get_end(), end=pivot_title.get_bottom() + 0.1 * DOWN, color=WHITE,buff=0, max_tip_length_to_length_ratio=0)

            
            self.play(Write(l_idx_indicator),Write(r_idx_indicator), run_time=0.2)
            #--------/Visuals--------

            while l_idx <= r_idx:
                # Revert pointers to the edges of the sub-array (This is done for clarity purposes when visualizing and is not necessary in the algorithm)

                l_idx = low # <- Removable
                r_idx = high - 1 # <- Removable

                #--------Visuals--------
                self.play(r_idx_indicator.animate.move_to([arr[r_idx].get_x(),r_idx_indicator.get_y(),0]),l_idx_indicator.animate.move_to([arr[l_idx].get_x(),l_idx_indicator.get_y(),0]), run_time=0.2)
                #--------/Visuals--------

                # Parse the sub-array from the left until a number greater than the pivot is found
                while arr[l_idx].height < arr[high].height:
                    l_idx += 1

                    #--------Visuals--------
                    self.play(l_idx_indicator.animate.move_to([arr[l_idx].get_x(),l_idx_indicator.get_y(),0]), run_time=0.1)
                    #--------/Visuals--------
                
                # Parse the sub-array from the right until a number less than the pivot is found
                while arr[r_idx].height > arr[high].height:
                    r_idx -= 1

                    #--------Visuals--------
                    self.play(r_idx_indicator.animate.move_to([arr[r_idx].get_x(),r_idx_indicator.get_y(),0]), run_time=0.1)
                    #--------/Visuals--------
                
                # If both pointers haven't crossed eachother. Switch the elements' positions.
                if l_idx <= r_idx:
                    #--------Visuals--------
                    self.play(arr[l_idx].animate.set_fill(BLUE),arr[r_idx].animate.set_fill(BLUE), run_time=0.1)
                    self.wait(0.3)
                    swap(arr[l_idx],arr[r_idx],self,0.1)
                    self.play(arr[l_idx].animate.set_fill(WHITE),arr[r_idx].animate.set_fill(WHITE), run_time=0.1)
                    #--------/Visuals--------

                    # Swapping array elements.
                    arr[r_idx], arr[l_idx]= arr[l_idx], arr[r_idx]

            #--------/Visuals--------
            self.wait(0.4)
            self.play(Unwrite(l_idx_indicator),Unwrite(r_idx_indicator), run_time=0.2)
            
            pivot_arrow_1.move_to([arr[l_idx].get_x(), pivot_arrow_1.get_y(), 0])

            pivot_arrow_2.put_start_and_end_on(start=[arr[l_idx].get_x(), pivot_arrow_2.get_y(), 0], end=pivot_arrow_2.get_end())
            #--------/Visuals--------

            # Check if l_idx isn't pointing at pivot's position
            if l_idx != high:
                #--------Visuals--------
                self.play(Write(pivot_arrow_1), Write(pivot_arrow_2),Write(pivot_arrow_3), run_time=0.13)
                self.wait(0.5)
                swap(arr[l_idx],arr[high],self,0.1)
                #--------/Visuals--------

                # Bring back the pivot to its correct and final position.
                arr[l_idx] , arr[high] = arr[high], arr[l_idx]
            
            #--------Visuals--------
            self.play(Unwrite(pivot_title),Unwrite(pivot_arrow_1), Unwrite(pivot_arrow_2),Unwrite(pivot_arrow_3),arr[l_idx].animate.set_fill(GREEN), run_time=0.13)
            #--------/Visuals--------

            # Deallocate memory
            pivot_title = pivot_arrow_1 = pivot_arrow_2 = pivot_arrow_3 = None
            del pivot_title
            del pivot_arrow_1
            del pivot_arrow_2
            del pivot_arrow_3

            return l_idx


        def quick_sort(arr, low, high):
            if low < high:
                # Split array into two sub-arrays with the partition_index beng an item at its final correct position
                partition_index = partition(arr, low, high)

                # Recursively run the algorithm on each of the two sub-arrays
                quick_sort(arr, low, partition_index - 1)
                quick_sort(arr, partition_index + 1, high)

        
        quick_sort(array, 0, len(array) - 1)
        # Create a new Vector group of the now ordered elements to play a staggered animation
        ordered_group = VGroup(*array)
        self.play(ordered_group.animate(lag_ratio=0.2).set_color(GREEN))
        self.wait(5)
