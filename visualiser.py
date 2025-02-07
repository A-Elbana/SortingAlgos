from math import floor, log2
from manim import Rectangle, Tex, Scene, Write, UP, DR, UL, DL, LEFT, GREEN, DARK_BLUE, ORIGIN, RIGHT, VGroup, RED, YELLOW_D, Unwrite, BLUE, BLUE_B, BLUE_E, Arrow, DOWN, WHITE, Text, BraceBetweenPoints, Point, PI, Graph, ManimColor, Transform, Circle, BLACK, UR

# Import the double-ended queue
from collections import deque, defaultdict

from classes import Element, GapIndicator, Node, RNGenerator, arrElement
import constants

def generateName():
    return Tex("Github: A-Elbana/SortingAlgos", font_size=38).to_edge(UP+LEFT).set_color_by_gradient(GREEN,GREEN,DARK_BLUE)

def swap(a:Element,b:Element,scene, run_time = 0.07, **kwargs):
    # Switch positions visually
    radix = kwargs.get("radix") or False
    if (a != b) or radix:
        # Make sure we are not switching the same bar. (Example: When our new bar position is the same as the old one)
        bottom_a = a.get_bottom()
        bottom_b = b.get_bottom()
        scene.play(
            a.animate.shift(bottom_b-bottom_a),
            b.animate.shift(bottom_a-bottom_b),
            run_time = run_time
        )

def swap_using_top(a:Element, b:Element, scene, run_time=0.07):
    # Switch positions visually using the top of the Mobject
    if (a != b) :
        # Make sure we are not switching the same bar. (Example: When our new bar position is the same as the old one)
        top_a = a.get_top()
        top_b = b.get_top()
        scene.play(
            a.animate.shift(top_b - top_a),
            b.animate.shift(top_a - top_b),
            run_time=run_time
        )

class BubbleSort(Scene):
    """Manim Scene Class
    """
    def construct(self):
        n=constants.N # Number of elements
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
        array=[Element(idx, bar_width) for idx in range(n)]
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
                if array[j]>array[j+1]:
                    # Highlight elements being processed
                    self.play(array[j].animate.set_fill(RED), array[j+1].animate.set_fill(RED),array[j].animate.set_color(RED), array[j+1].animate.set_color(RED), run_time = 0.1)

                    swap(array[j], array[j+1], self)
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
        self.play(ordered_group.animate(lag_ratio=0.3).set_fill(GREEN), ordered_group.animate(lag_ratio=0.3).set_color(GREEN))
        self.wait(5)


class SelectionSort(Scene):
    """Manim Scene Class
    """
    def construct(self):
        n=constants.N # Number of elements
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
        array=[Element(idx, bar_width) for idx in range(n)]
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
                if array[curr_item] < array[curr_min]:
                    self.play(array[curr_min].animate.set_fill(WHITE), array[curr_min].animate.set_color(WHITE), run_time = 0.1)
                    curr_min = curr_item
                    self.play(array[curr_min].animate.set_fill(RED), run_time = 0.1)
                    continue
                self.play(array[curr_item].animate.set_fill(WHITE), array[curr_item].animate.set_color(WHITE), run_time = 0.07)
            
            swap(array[i], array[curr_min], self)
            array[i], array[curr_min] = array[curr_min], array[i]
            self.play(array[i].animate.set_fill(GREEN), run_time = 0.07)
        
        # Create a new Vector group of the now ordered elements to play a staggered animation
        ordered_group = VGroup(*array)
        self.play(ordered_group.animate(lag_ratio=0.3).set_color(GREEN))
        self.wait(5)





class HeapSort(Scene):
    LAYOUT_CONFIG = {"vertex_spacing": (-1, 1)}
    VERTEX_TYPE = Node
    VERTEX_CONF = {
        "radius": 0.25,
        "color": BLUE_B,
        "fill_opacity": 0.1,
        "stroke_color": WHITE,
        "z_index": 2,
        "text": "0",
    }

    def construct(self):
        self.n = 7
        n = 7
        rn = RNGenerator(9)
        elementWidth = 0.8 * (self.camera.frame_width - 3) / (10)
        self.array = [
            arrElement(width=elementWidth, height=elementWidth, value=rn.next())
            for _ in range(n)
        ]

        # Generate Title
        title = Tex(r"Heap Sort $O(n \log(n))$", font_size=55).to_edge(DOWN)

        # Generate Credits
        githubName = generateName()
        self.play(Write(githubName), Write(title))

        # Display initial steps
        steps = Tex(r"Turn the array into a binary tree.", font_size=34).next_to(
            ORIGIN, DOWN * 3.5, buff=0.5
        )
        group = VGroup(*self.array).arrange(DOWN, buff=0).to_edge(LEFT)
        self.play(
            Write(group), githubName.animate.to_corner(DR), title.animate.to_corner(UR)
        )
        self.play(Write(steps))

        # Initialize the heap with the first element
        self.VERTEX_CONF["text"] = str(self.array[0].value)
        self.q = deque(["0"])
        self.nodes = ["0"]
        heap = Graph(
            ["0"], [], vertex_type=self.VERTEX_TYPE, vertex_config=self.VERTEX_CONF
        )
        self.play(Write(heap))

        # Add remaining elements to the heap
        for i in range(1, n):
            e: arrElement = group[i]
            self.play(
                e.animate.set_fill(GREEN, 0.5),
                e.submobjects[0].animate.set_opacity(1),
                run_time=0.25,
            )
            self.add_node_to_tree(heap, str(e.value))
            self.play(
                e.animate.set_fill(GREEN, 0),
                e.submobjects[0].animate.set_opacity(1),
                run_time=0.25,
            )
            self.wait(0.25)

        # Convert the binary tree into a max heap
        self.display_message(steps, r"Convert the binary tree into a max heap.", True)
        self.display_message(
            steps, r"We use the heapify algorithm on the non-leaf nodes."
        )
        self.max_heapify(heap)

        # Start sorting process
        self.display_message(
            steps, r"Now that we have a max heap, we can start sorting.", True
        )
        self.display_message(
            steps, r"We know that the root is the largest element in the heap."
        )
        self.wait(2)
        self.play(
            heap.vertices["0"].submobjects[0][0].animate.set_color(DARK_BLUE),
            run_time=0.25,
        )

        # Swap and remove the root element
        self.display_message(
            steps,
            r"We can pop that element and place it at the end of the array.",
            True,
        )
        self.display_message(
            steps, r"We swap it with the last element and remove it from the heap.", True
        )
        self.swapVerts(heap, "0", self.nodes[-1])
        self.wait(3)
        self.remove_node_from_tree(heap, self.nodes[-1])
        self.nodes.pop()
        self.wait(3)

        # Fix the heap property
        self.display_message(
            steps, r"Now the binary tree violates the max-heap property.", True
        )
        self.display_message(
            steps, r"We can fix this by calling heapify on the root.", True
        )
        self.max_heapify(heap)

        # Repeat until the heap is empty
        self.display_message(
            steps, r"We repeat the previous steps until the heap is empty.", True
        )
        for i in range(n - 1):
            self.swapVerts(heap, "0", self.nodes[-1])
            self.remove_node_from_tree(heap, self.nodes[-1])
            self.nodes.pop()
            if self.nodes:
                self.max_heapify(heap)

        # Display sorted array
        self.display_message(steps, r"The array is now sorted.", True)
        sorted_array = VGroup(*self.array)
        self.play(
            sorted_array.animate.arrange(RIGHT, buff=0).move_to(ORIGIN),
            Unwrite(steps),
            githubName.animate.next_to(sorted_array.copy().arrange(RIGHT, buff=0).move_to(ORIGIN), UP),
            title.animate.next_to(sorted_array.copy().arrange(RIGHT, buff=0).move_to(ORIGIN), DOWN),
            run_time=1,
        )
        self.play(sorted_array.animate(lag_ratio=0.3).set_color(GREEN), run_time=1)

        self.wait(5)

    def max_heapify(self, heap: Graph):
        def heapify_down(heap, node):
            left_child = f"{node}/0"
            right_child = f"{node}/1"
            largest = node
            if left_child in heap.vertices and int(
                heap.vertices[left_child].submobjects[0][1].tex_string
            ) > int(heap.vertices[largest].submobjects[0][1].tex_string):
                largest = left_child

            if right_child in heap.vertices and int(
                heap.vertices[right_child].submobjects[0][1].tex_string
            ) > int(heap.vertices[largest].submobjects[0][1].tex_string):
                largest = right_child

            if largest != node:
                self.play(
                    heap.vertices[node]
                    .submobjects[0][0]
                    .animate.set_color(ManimColor("#9A3020")),
                    run_time=0.25,
                )
                self.swapVerts(heap, node, largest)

                heapify_down(heap, largest)

        for i in self.nodes[(len(self.nodes) // 2) - 1 :: -1]:
            heapify_down(heap, str(i))

    def display_message(self, mobject: Tex, text, wait=False):
        to = Tex(text, font_size=34).move_to(mobject.get_center())
        self.play(Transform(mobject, to), run_time=0.5)
        if wait:
            self.wait(3)

    def swapVerts(self, heap, a, b):
        swap(
            self.array[self.vertex_to_index(a)],
            self.array[self.vertex_to_index(b)],
            self,
            0.25,
        )
        self.array[self.vertex_to_index(a)], self.array[self.vertex_to_index(b)] = (
            self.array[self.vertex_to_index(b)],
            self.array[self.vertex_to_index(a)],
        )
        a = heap.vertices[a]
        b = heap.vertices[b]
        temp = b.submobjects[0][1].copy()
        a.submobjects[0][1].tex_string, b.submobjects[0][1].tex_string = (
            b.submobjects[0][1].tex_string,
            a.submobjects[0][1].tex_string,
        )
        self.play(
            a.submobjects[0][0].animate.set_color(BLACK),
            Transform(
                b.submobjects[0][1],
                a.submobjects[0][1].copy().move_to(b.submobjects[0][1].get_center()),
            ),
            Transform(
                a.submobjects[0][1], temp.move_to(a.submobjects[0][1].get_center())
            ),
        )

    @staticmethod
    def vertex_to_index(vertex_id):
        if vertex_id == "0":
            return 0
        ids = vertex_id.split("/")
        idx = 0
        for i in range(1, len(ids)):
            idx = (idx * 2) + (1 + int(ids[i]))
        return idx

    def add_node_to_tree(self, g: Graph, text: str):
        # Find the last vertex in a binary tree
        last_vertex_id = self.q[0]

        # Check both left and right child positions
        if f"{last_vertex_id}/0" not in g.vertices:
            new_vertex_id = f"{last_vertex_id}/0"
        else:
            new_vertex_id = f"{last_vertex_id}/1"
            self.q.popleft()

        self.q.append(new_vertex_id)
        self.nodes.append(new_vertex_id)
        g.add_edges(
            (last_vertex_id, new_vertex_id),
            vertex_type=self.VERTEX_TYPE,
            vertex_config={**self.VERTEX_CONF, "text": text},
            positions={new_vertex_id: g.vertices[last_vertex_id].get_center()},
        )
        self.play(
            g.animate.change_layout(
                "tree",
                root_vertex="0",
                layout_config=self.LAYOUT_CONFIG,
            ),
            run_time=0.5,
        )

    def remove_node_from_tree(self, g: Graph, node_id):
        if node_id == "0":
            self.play(g.animate.remove_vertices(node_id), run_time=0.5)
            return
        self.play(
            g.animate.remove_vertices(node_id),
            g.animate.change_layout(
                "tree",
                root_vertex="0",
                layout_config=self.LAYOUT_CONFIG,
            ),
            run_time=0.5,
        )





class MergeSort(Scene):
    """Manim Scene Class
    """
    def construct(self):
        n=constants.N # Number of elements
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
        array=[Element(idx, bar_width) for idx in range(n)]
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

        # Run Merge Sort
        
        def merge(a:deque[Element],b:deque[Element]):
            merged = deque([])
            
            #--------Visuals--------
            c = list(a+b)
            curr_pos = a[0].index
            mergedVGroup = VGroup(*c)
            self.play(mergedVGroup.animate.set_fill(BLUE), run_time=0.1)
            #--------/Visuals--------

            while a and b:
                self.play(b[0].animate.set_fill(RED),a[0].animate.set_fill(RED), run_time=0.1) #--------Visuals/--------
                if a[0].height < b[0].height:
                    #--------Visuals--------
                    swap(array[curr_pos], array[a[0].index], self)
                    
                    # Update dictionary by switching indices
                    a[0].index, array[curr_pos].index =  array[curr_pos].index, a[0].index

                    # Update bars array by switching indices
                    array[array[curr_pos].index], array[a[0].index] = array[a[0].index], array[array[curr_pos].index]
                    

                    # Traverse to next bar position
                    curr_pos += 1
                    self.play(b[0].animate.set_fill(BLUE),a[0].animate.set_fill(BLUE), run_time=0.1)
                    #--------/Visuals--------
                    merged.append(a[0])
                    a.popleft()
                else:
                    #--------Visuals--------
                    swap(array[curr_pos], array[b[0].index], self)

                    # Update indices
                    b[0].index, array[curr_pos].index =  array[curr_pos].index, b[0].index

                    # Update bars array by switching indices
                    array[array[curr_pos].index], array[b[0].index] = array[b[0].index], array[array[curr_pos].index]
                    
                    # Traverse to next bar position
                    curr_pos += 1
                    self.play(b[0].animate.set_fill(BLUE),a[0].animate.set_fill(BLUE), run_time=0.1)
                    #--------/Visuals--------
                    merged.append(b[0])
                    b.popleft()
                
            
            while a:
                #--------Visuals--------
                swap(array[curr_pos], array[a[0].index], self)
                # Update indices
                a[0].index, array[curr_pos].index =  array[curr_pos].index, a[0].index

                # Update bars' array by switching indices
                array[array[curr_pos].index], array[a[0].index] = array[a[0].index], array[array[curr_pos].index]

                # Traverse to next bar position
                curr_pos += 1
                #--------/Visuals--------
                merged.append(a[0])
                a.popleft()
            while b:
                #--------Visuals--------
                swap(array[curr_pos], array[b[0].index], self)

                # Update indices
                b[0].index, array[curr_pos].index =  array[curr_pos].index, b[0].index

                # Update bars array by switching indices
                array[array[curr_pos].index], array[b[0].index] = array[b[0].index], array[array[curr_pos].index]
                
                # Traverse to next bar position
                curr_pos += 1
                #--------/Visuals--------
                merged.append(b[0])
                b.popleft()
            
            self.play(mergedVGroup.animate.set_fill(WHITE), run_time=0.1) #--------Visuals/--------
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
        n=constants.N # Number of elements
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

        # Run Quick Sort
        def partition(arr:list[Rectangle], low:int, high:int):
            # Choose pivot using the median-of-three method
            helper = [ low, (high+low+1) // 2, high]
            medianOfThree = [arr[low].height,arr[(high+1+low)//2].height, arr[high].height]

            # Use unrolled Bubble Sort to sort the array (O(1))
            for i in range(2):
                for j in range(2-i):
                    if medianOfThree[j] > medianOfThree[j+1]:
                        medianOfThree[j], medianOfThree[j+1] = medianOfThree[j+1], medianOfThree[j]
                        arr[helper[j]], arr[helper[j+1]] = arr[helper[j+1]], arr[helper[j]]
                        swap(arr[helper[j]], arr[helper[j+1]], self, 0.1)
            self.wait(0.25)
            
            if (high-low) <= 2:
                self.play(arr[low].animate.set_fill(GREEN),arr[(high+1+low)//2].animate.set_fill(GREEN),arr[high].animate.set_fill(GREEN), run_time=0.13)
                return (high+1+low)//2
            pivot_pos = (high+1+low)//2
            # Setup pointers used to parse and arrange array into two sub-arrays (Greater than pivot and smaller than pivot)
            l_idx = low
            #--------Visuals--------
            l_idx_indicator = VGroup()
            l_idx_arrow = Arrow(start= arr[l_idx].get_bottom() + 1.4*DOWN, end=arr[l_idx].get_bottom()+0.4*DOWN, color=WHITE)
            l_idx_indicator.add(l_idx_arrow)
            l_idx_indicator.add(Text("l_idx",font_size=20,color=BLUE_B).next_to(l_idx_arrow, DOWN))
            #--------/Visuals--------


            r_idx = high - 1
            #--------Visuals--------
            r_idx_indicator = VGroup()
            r_idx_arrow = Arrow(start= arr[r_idx].get_bottom() + 1.4*DOWN, end=arr[r_idx].get_bottom()+0.4*DOWN, color=WHITE)
            r_idx_indicator.add(r_idx_arrow)
            r_idx_indicator.add(Text("r_idx",font_size=20,color=RED).next_to(r_idx_arrow, DOWN))
            #--------/Visuals--------

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

            #--------Visuals--------
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



class RadixSort(Scene):
    """Manim Scene Class
    """
    def construct(self):
        n = constants.N_RADIX
        max_num = (10**constants.DIGITS_RADIX) - 1
        rn = RNGenerator(max_num) # Generator object
        box_width = (self.camera.frame_width - 3) / (10 if n <= 10 else n)

        # Generate Title
        text = Tex(r"Radix Sort $O(n * d)$", font_size=55).to_edge(DOWN)
        self.play(Write(text))

        # Generate Credits
        githubName = generateName()
        self.play(Write(githubName))


        # Setup box for each element and buckets
        array=[Rectangle(width=box_width, height=box_width) for _ in range(n)]

        positions = defaultdict(int) # Hashmap to help speed up the lookup process of the indices of each number

        for i in range(len(array)):
            rn_num = rn.next()
            number = Tex(*[a for a in str(rn_num)]).scale_to_fit_height(box_width - 0.6 * box_width)
            number.move_to(array[i])
            array[i] = VGroup(array[i], number)

            # Shift box to the right of the previous element
            array[i].shift(RIGHT*(box_width)*i)
            positions[rn_num] = i # Input numbers' positions in hashmap/dict

            # Align the bottom edge of each box
            array[i].align_to((0,0,0),DOWN)
        group=VGroup(*array)
        group.move_to(ORIGIN)
        self.play(Write(group))
        self.play(group.animate.to_edge(UL).scale(0.8), githubName.animate.scale(0.75).to_corner(DR,buff=0.25), Unwrite(text))
        
        # Create Buckets
        bucket_width = 0.8 * (self.camera.frame_width - 3) / (10)
        buckets=[Rectangle(width=bucket_width, height=bucket_width).set_color(BLUE_E).set_fill(BLUE_E, opacity=1) for _ in range(10)]

        # Scale and Order Buckets
        for i in range(10):
            number = Tex(f"${i}$").scale_to_fit_height(bucket_width - 0.5 * bucket_width)
            number.move_to(buckets[i])
            buckets[i] = VGroup(buckets[i], number)
            buckets[i].shift(DOWN*(bucket_width+0.3)*(i%5))
            
            # Align the left edge of each bucket
            buckets[i].align_to((0,0,0),LEFT)

            # Move bucket to new column if it is greater than 4
            if i > 4:
                buckets[i].align_to(((self.camera.frame_width - bucket_width) / 2 ,0,0),LEFT)
        b_group=VGroup(*buckets)
        # Move Buckets to bottom-left corner
        b_group.to_corner(DL)
        self.play(Write(b_group))
        #/Setup


        # Run Radix Sort

        # Loop through the number of digits
        for d in range(constants.DIGITS_RADIX):
            # Hashmap to keep track of elements in each bucket
            buckets_map = defaultdict(deque)
            # Loop through each element
            for i in range(len(array)):
                number = int(array[i][1].tex_string)

                # Get corresponding Bucket (By Extracting d'th digit)
                b_index = number % (10**(d+1)) // (10**d)

                

                # Copy Element for visualisation purposes
                copy_rect = array[i].copy()

                
                
                
                # Add element to bucket
                buckets_map[b_index].append(copy_rect)

                #--------Visuals--------
                digit_highlight = None
                try:
                    digit_highlight = copy_rect[1][-(1+d)]
                    self.play(digit_highlight.animate.set_color(GREEN), run_time=0.2)
                    self.play(VGroup(* buckets_map[b_index]).animate.arrange().next_to(buckets[b_index]) )
                except:
                    self.play(VGroup(* buckets_map[b_index]).animate.arrange().next_to(buckets[b_index]) )
                    
                
                
                #--------/Visuals--------
            
            # Initialize a Swap Pointer (This part could be implemented in many different ways)
            swap_pointer = 0
            for n in range(10):
                self.play(buckets[n][0].animate.set_color(GREEN), run_time=0.15)
                for element in list(buckets_map[n]):
                    # Extract number from Mobject
                    number = int(element[1].tex_string)
                    # Get number's current position from hashmap
                    num_index = positions[number]
                    # Get number-to-be-replaced's current position from hashmap
                    num_2 = int(array[swap_pointer][1].tex_string)

                    # Swap positions
                    array[num_index], array[swap_pointer] = array[swap_pointer], array[num_index]
                    
                    #--------Visuals--------
                    
                    swap(array[num_index], array[swap_pointer], self, 0.3, radix = True)
                    self.play(Unwrite(element),array[swap_pointer].animate.set_color(BLUE), run_time=0.1)
                    
                    #--------/Visuals--------

                    # Update positions in hashmap
                    positions[num_2] = positions[number]
                    positions[number] = swap_pointer

                    # Increment Pointer
                    swap_pointer += 1
                self.play(buckets[n][0].animate.set_color(BLUE_E), run_time=0.15)
            self.play(group.animate.set_color(WHITE), run_time=0.2)
        # Create a new Vector group of the now ordered elements to play a staggered animation
        ordered_group = VGroup(*array)
        self.play(Unwrite(b_group),run_time=0.1)
        self.play(ordered_group.animate.move_to(ORIGIN).scale(1.25))
        self.play(githubName.animate.scale(1/0.75 +0.2).next_to(ordered_group, UP), Write(Tex(r"Radix Sort $O(n * d)$", font_size=55).next_to(ordered_group, DOWN)))
        self.play(ordered_group.animate(lag_ratio=0.3).set_fill(GREEN).set_color(GREEN))
        self.wait(5)


def play(self, *args, run_time=0.1):
    if args:
        self.play(*args, run_time=run_time)

class InsertionSort(Scene):
    """Manim Scene Class
    """
    
    def construct(self):
        n= min(15, constants.N) # Number of elements
        rn = RNGenerator(n) # Generator object
        shifting = 0.1 # Padding between bars

        # Get bar width relative to frame size
        bar_width = (self.camera.frame_width - shifting * n - 3) / (n)

        # Generate Title
        title = Tex(r"Insertion Sort $O(n^{2})$", font_size=55).to_edge(DOWN)

        # Generate Credits
        githubName = generateName()
        self.play(Write(githubName), Write(title))

        # Setup bar for each element
        array=[Rectangle(width=bar_width) for _ in range(n)]
        for i in range (0, n):
            # Stretch bar height appropriately to fit in frame. Height range: [(half screen height)/n, (half screen height)].
            array[i].stretch_to_fit_height(rn.next() /(n*1.0) * self.camera.frame_height * 0.4)

            # Shift bar to the right by its width + the shifting which acts as padding
            array[i].shift(RIGHT*(bar_width+shifting)*i)
            
            # Align the bottom edge of each bar
            array[i].align_to((0,0,0),DOWN)
        group=VGroup(*array)
        group.move_to(ORIGIN)
        group.set_fill(WHITE,opacity=1)
        self.play(*[Write(o) for o in array])
        gt = Text("<", font_size=35, weight="BOLD").rotate(PI/2).save_state()
        lt = Text("<", font_size=35, weight="BOLD").rotate(-PI/2).save_state()
        w = lt.width
        # /Setup


        # Move Title
        self.play(title.animate.to_edge(UP+RIGHT), run_time=0.25)
        
        
        
        # Run Insertion Sort
        for i in range(1,len(array)):
            
            temp = array[i]
            temp_in = temp.get_bottom()
            j = i

            c = i
            gapped:list[Rectangle] = []
            while (c >= 1):
                gapped.append(array[c - 1])
                c -= 1
            highlight = list(map(lambda x: x.animate.set_fill(BLUE_E), gapped))
            highlight.append(temp.animate.shift(DOWN*(temp.height + w + 4*shifting)).set_fill(YELLOW_D))
            
            play(self, *highlight, run_time=0.5)


            while (j >= 1):
                self.play(temp.animate.shift(array[j-1].get_bottom()- temp_in), run_time=0.25)
                if (array[j - 1].height > temp.height):
                    gt.restore().move_to(array[j-1].get_bottom() + (w + shifting)*DOWN)
                    self.play(Write(gt), run_time=0.25)
                    self.play(Unwrite(gt), run_time=0.25)
                    new_temp_in = array[j - 1].get_bottom()
                    self.play(array[j-1].animate.shift(temp_in - array[j-1].get_bottom()).set_fill(RED), run_time=0.25)
                    
                    temp_in = new_temp_in
                    array[j] = array[j - 1]
                    
                    j -= 1
                    
                else:
                    lt.restore().move_to(array[j-1].get_bottom() + (w + shifting)*DOWN)
                    self.play(Write(lt), run_time=0.25)
                    self.play(Unwrite(lt), run_time=0.25)
                    self.play(temp.animate.shift(temp_in - array[j-1].get_bottom()), array[j-1].animate.set_fill(GREEN), run_time=0.25)
                    break
                    
            array[j] = temp
            
            remove_highlight = list(map(lambda x: x.animate.set_fill(WHITE), gapped))
            remove_highlight.append(temp.animate.shift(UP*(temp.height + w + 4*shifting)).set_fill(WHITE))
            play(self, *remove_highlight, run_time=0.5)
                
            
        
        self.play(VGroup(*array).animate.set_color(GREEN), run_time=1, lag_ratio=0.3)
        self.wait(2)
class ShellSort(Scene):
    """Manim Scene Class
    """
    
    def construct(self):
        n= min(15, constants.N) # Number of elements
        rn = RNGenerator(n) # Generator object
        shifting = 0.1 # Padding between bars

        # Get bar width relative to frame size
        bar_width = (self.camera.frame_width - shifting * n - 3) / (n)

        # Generate Title
        title = Tex(r"Shell Sort $O(n^{\frac{4}{3}})$", font_size=55).to_edge(DOWN)

        # Generate Credits
        githubName = generateName()
        self.play(Write(githubName), Write(title))

        # Setup bar for each element
        array=[Rectangle(width=bar_width) for _ in range(n)]
        for i in range (0, n):
            # Stretch bar height appropriately to fit in frame. Height range: [(half screen height)/n, (half screen height)].
            array[i].stretch_to_fit_height(rn.next() /(n*1.0) * self.camera.frame_height * 0.4)

            # Shift bar to the right by its width + the shifting which acts as padding
            array[i].shift(RIGHT*(bar_width+shifting)*i)
            
            # Align the bottom edge of each bar
            array[i].align_to((0,0,0),DOWN)
        group=VGroup(*array)
        group.move_to(ORIGIN + DOWN)
        group.set_fill(WHITE,opacity=1)
        self.play(*[Write(o) for o in array])
        gt = Text("<", font_size=35, weight="BOLD").rotate(PI/2).save_state()
        lt = Text("<", font_size=35, weight="BOLD").rotate(-PI/2).save_state()
        w = lt.width
        # /Setup


        # Move Title
        self.play(title.animate.to_edge(UP+RIGHT), run_time=0.25)
        
        
        
        # Run Shell Sort

        # Using Hibbard's sequence (https://oeis.org/A000225)
        gaps = [2**i - 1 for i in range(floor(log2(len(array))),0, -1)]

        for gap in gaps:
            if gap == 1:
                inssort = Text("Ordinary Insertion Sort", font_size=35).next_to(group, UP)
                self.play(Write(inssort), run_time=0.5)
            gapIndicator = GapIndicator(gap, n, bar_width + shifting, [array[0].get_x(), self.camera.frame_height * 0.2, 0] + DOWN, self)
            gapIndicator.createIndicator()
            for i in range(gap,len(array)):
                
                temp = array[i]
                temp_in = temp.get_bottom()
                j = i

                c = i
                gapped:list[Rectangle] = []
                while (c >= gap):
                    gapped.append(array[c - gap])
                    c -= gap
                highlight = list(map(lambda x: x.animate.set_fill(BLUE_E), gapped))
                highlight.append(temp.animate.shift(DOWN*(temp.height + w + 4*shifting)).set_fill(YELLOW_D))
                
                play(self, *highlight, run_time=0.5)


                while (j >= gap):
                    self.play(temp.animate.shift(array[j-gap].get_bottom()- temp_in), run_time=0.25)
                    if (array[j - gap].height > temp.height):
                        gt.restore().move_to(array[j-gap].get_bottom() + (w + shifting)*DOWN)
                        self.play(Write(gt), run_time=0.25)
                        self.play(Unwrite(gt), run_time=0.25)
                        new_temp_in = array[j - gap].get_bottom()
                        self.play(array[j-gap].animate.shift(temp_in - array[j-gap].get_bottom()).set_fill(RED), run_time=0.25)
                        
                        temp_in = new_temp_in
                        array[j] = array[j - gap]
                        
                        j -= gap
                        
                    else:
                        lt.restore().move_to(array[j-gap].get_bottom() + (w + shifting)*DOWN)
                        self.play(Write(lt), run_time=0.25)
                        self.play(Unwrite(lt), run_time=0.25)
                        self.play(temp.animate.shift(temp_in - array[j-gap].get_bottom()), array[j-gap].animate.set_fill(GREEN), run_time=0.25)
                        break
                    
                array[j] = temp
                
                remove_highlight = list(map(lambda x: x.animate.set_fill(WHITE), gapped))
                remove_highlight.append(temp.animate.shift(UP*(temp.height + w + 4*shifting)).set_fill(WHITE))
                play(self, *remove_highlight, run_time=0.5)
                if i < len(array) - 1:
                    gapIndicator.moveIndicators()
            del gapIndicator
            if gap == 1:
                self.play(Unwrite(inssort), run_time=0.75)
        
        self.play(VGroup(*array).animate.set_color(GREEN), run_time=1, lag_ratio=0.3)
        self.wait(2)