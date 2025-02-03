
<a id="readme-top"></a>


[![LinkedIn][linkedin-shield]][linkedin-url]




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation and usage">Installation and Usage</a></li>
      </ul>
    </li>
    <li><a href="#Visualizations">Visualizations</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#disclaimer">Disclaimer</a></li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![][product-screenshot]

This project visualizes various sorting algorithms using Manim. It aims to provide a clear and interactive understanding of how these algorithms work. Users can explore different algorithms and compare their performance. The project is designed to be a valuable resource for students, educators, and developers seeking to learn about sorting algorithms through visual representations.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


* [![Python](https://skillicons.dev/icons?i=py&theme=dark)](https://python.org)
* [Manim](https://github.com/ManimCommunity/manim)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

* Python 3.9+ [All Releases Here](https://www.python.org/downloads/)
* Manim [Follow Instructions On Official Website](https://www.manim.community/)
* [TeX/LaTeX](https://miktex.org/download) (If you don't want to install LaTeX on your system, change `Tex()` Mobjects to `Text()` to render text normally)
  
<a id="installation"></a>
<a id="readme-top"></a>

### Installation and Usage


1. Clone the repo
   ```sh
   git clone https://github.com/A-Elbana/SortingAlgos
   ```
2. Make sure manim is properly installed by running the following command in your terminal:
   ```sh
   manim
   ```
3. Run your desired algorithm and render it using manim by running the following in your terminal:
   ```sh
   manim -pqh visualiser.py {AlgorithmName}
   ```
   This will render a video in 1080p60. For lower quality use the `-pql` flag.<br>
   For available `{AlgorithmName}` refer to the table below.

#### Here's a list of all the algorithms currently available. 
>Feel free to open an issue to suggest new algorithms to add!

| Algorithm        | `{AlgorithmName}`|
|:-------------:|:-------------:|
| Bubble Sort| `BubbleSort` |
| Selection Sort| `SelectionSort` |
| Merge Sort| `MergeSort` |
| Quick Sort| `QuickSort` |
| Radix Sort| `RadixSort` |
| Insertion Sort| `InsertionSort` |
| Shell Sort| `ShellSort` |

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- VISUALIZATIONS -->
## Visualizations

## Bubble Sort
##### Time Complexity: $O(n^2)$
##### Space Complexity: $O(1)$


https://github.com/user-attachments/assets/e81deff2-9268-4e58-8e9f-0c057e96b832


### Explanation:

1. Start from the beginning of the array.

2. Compare the <span style="color:red">current element</span> with the <span style="color:red">next element</span>.

3. If the current element is greater than the next element, swap them.![][SB]

4. Continue this process until the end of the array is reached.

5. After one pass, the largest element will be at the end of the array. Repeat the process for the remaining unsorted elements.![][FP]

---

## Selection Sort
##### Time Complexity: $O(n^2)$
##### Space Complexity: $O(1)$

https://github.com/user-attachments/assets/e0bbfa89-6433-4534-8d08-22112c2e2979

### Explanation:

1. Start from the beginning of the array.
![][begin]

2. Traverse the following elements. (<span style="color:#F4D345">Yellow</span> Indicator)

3. Keep track of the minimum element encountered so far. (Marked in <span style="color:red">red</span>)
![][MSF]

4. After traversing through all of the unsorted portion, swap the found minimum element with the first element of the unsorted portion.![][SM]


5. Repeat the process for the remaining unsorted portion of the array.

---

## Merge Sort
##### Time Complexity: $\Theta (n \log(n))$
##### Space Complexity: $O(n)$
##### Methodology: $Divide \ and \ Conquer$ (Bottom-Top)

https://github.com/user-attachments/assets/b5bd3f20-3fdb-449b-bccf-6ff082a6d6ee

### Explanation:

1. Divide the array recursively into two halves until it can't be divided anymore.
2. Recursively sort each half using merge sort.
![][SortSub]

3. If the array contains only one element, it is already sorted. (Base Case)
4. When comparing two halves `a` and `b` of one or more elements:
- *Without loss of generality*, assume `a` has more elements than `b`. `a` and `b` should both be internally sorted, so we treat them as `queues` and compare the head of each queue. The smaller element is pushed to an auxiliary array `c` and popped from its queue.
- Repeat the previous process till either `a` or `b` becomes empty.
- Push the remaining elements of the non-empty half to the end of `c`
- `c` is now the merged array of `a` and `b`, and will be one of the halves of the next recursive call in the call stack.
![][Merge]

5. Repeat steps 1-4 until the entire array is sorted.


---

## Quick Sort
##### Time Complexity: $O(n \log(n))$
##### Space Complexity: $O(\log(n))$ (Average Case)
##### Methodology: $Divide \ and \ Conquer$ (Top-Bottom)

https://github.com/user-attachments/assets/33ea5bb4-a73c-4f52-9a6f-281befa3b298

### Explanation:
1. Choose the <span style="color:#F4D345">`Pivot`</span>:<br>To choose the pivot, the [median-of-three](https://stackoverflow.com/questions/7559608/median-of-three-values-strategy#answer-7560859) method is used.![][medianofthree]
2. Move <span style="color:#F4D345">`Pivot`</span> to the end of the array and initialize <span style="color:#58C4DD">`l_idx`</span> and <span style="color:red">`r_idx`</span>.![][ptep]
3. The two pointers <span style="color:#58C4DD">`l_idx`</span> and <span style="color:red">`r_idx`</span> will traverse through the array from left and from right until a value (at each respective index) greater than the <span style="color:#F4D345">`Pivot`</span> and smaller than the <span style="color:#F4D345">`Pivot`</span> is found. Then the two elements at <span style="color:#58C4DD">`l_idx`</span> and <span style="color:red">`r_idx`</span> are exchanged.![][pe]
4. Repeat the previous step until <span style="color:#58C4DD">`l_idx`</span> is greater than <span style="color:red">`r_idx`</span>.![][pc]
5. Exchange element at <span style="color:#58C4DD">`l_idx`</span> (greater than pivot) with the pivot (which is at the end of the array).![][ptf]
6. Now the <span style="color:#F4D345">`Pivot`</span> is in its <span style="color:green">correct and final</span> position in the main array. Repeat steps `1-5` on the generated sub-arrays until sorted.![][Rec]


---

## Radix Sort
##### Time Complexity: $O(n * d)$
##### Space Complexity: $O(n+k)$ (For visualization purposes. However, it can be implemented more efficiently. Refer to [this example](https://stackoverflow.com/questions/43587853/duplicate-removal/43588349#answer-43588349)) 


https://github.com/user-attachments/assets/dcc503cc-9bf6-49a3-b6d4-56233a762f56



### Explanation:
1. Determine the maximum number of `digits` (Predefined in `DIGITS_RADIX`)
2. Create buckets (According to the `base` used)
3. Distribute elements based on n-th digit
4. Collect elements (Resort the array according to buckets' arrangement)
6. Repeat steps `3-4` for each digit until sorted.

---
## Insertion Sort
##### Time Complexity: $O(n^2)$ (Worst-case, Average-case. Best-case is $O(n)$ when the array is nearly sorted.)
##### Space Complexity: $O(1)$ (In-place sorting algorithm)






https://github.com/user-attachments/assets/1a051ddd-0c4b-4535-b857-5a38498de981



### Explanation:
1. **Iterate through the array:**  
   Starting from the second element, consider each element in the array one by one.

2. **Find the correct insertion position:**  
   Compare the current element with the elements before it. Shift larger elements one position to the right to create space.

3. **Insert the element:**  
   Once the correct position is identified, insert the current element.



4. **Repeat for all elements:**  
   Continue this process until every element is inserted in its proper position, resulting in a sorted array.



---

## Shell Sort
##### Time Complexity: $O(n^2)$ (Worst-case. With optimized gap sequences, the average performance can be significantly better.)
##### Space Complexity: $O(1)$ (In-place sorting algorithm)

https://github.com/user-attachments/assets/1550270e-301f-426a-816c-0f9a6479ec71

### Explanation:
1. **Select an initial gap:**  
   Start with a `gap` value (commonly half the length of the array) to determine which elements to compare. However, there are sets of sequences that may affect the time complexity of the algorithm. You can check these sequences [here](https://en.wikipedia.org/wiki/Shellsort#Gap_sequences). Refer to this [link](https://oeis.org/A000225) for the one used in this visualisation.

2. **Gapped Insertion Sort:**  
   For the current `gap`, perform a modified insertion sort where elements that are `gap` positions apart are compared and swapped if necessary.

3. **Reduce the gap:**  
   After sorting with the current `gap`, reduce the gap (often by halving it) and repeat the gapped insertion sort on the now partially sorted array.
4. Repeat steps `2-3` until the `gap` is reduced to `1`.
5. **Final pass:**  
   When the `gap` is reduced to 1, perform a final standard insertion sort to ensure the entire array is fully sorted.



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Abdelrahman Elbana - manelbana079@gmail.com

Project Link: [https://github.com/A-Elbana/SortingAlgos](https://github.com/A-Elbana/SortingAlgos)

Linkedin: https://www.linkedin.com/in/abdelrahmanwisam/

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Geeksforgeeks - Bubble Sort Algorithm](https://www.geeksforgeeks.org/bubble-sort-algorithm/)
* [Merge Sort Explanation](https://www.youtube.com/watch?v=4VqmGXwpLqc)
* [Selection Sort Explanation](https://youtu.be/g-PGLbMth_g?si=2WM32az9L8182Ksy)
* [Quick Sort Explanation](https://www.youtube.com/watch?v=Hoixgm4-P4M)
* [CS Dojo - Radix Sort Explanation](https://www.youtube.com/watch?v=XiuSW_mEn7g)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Disclaimer -->
## Disclaimer
*While this visualization tool demonstrates the steps involved in each sorting algorithm, the actual time taken for the animation to complete should not be considered a direct measure of the algorithm's performance. Some algorithms may have visually longer or more complex animations, which can affect the perceived execution time. For a true performance comparison, refer to the provided metrics based on computational complexity, not animation duration.*

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[forks-shield]: https://img.shields.io/github/forks/A-Elbana/SortingAlgos.svg?style=for-the-badge
[forks-url]: https://github.com/A-Elbana/SortingAlgos/network/members
[stars-shield]: https://img.shields.io/github/stars/A-Elbana/SortingAlgos.svg?style=for-the-badge
[stars-url]: https://github.com/A-Elbana/SortingAlgos/stargazers

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/abdelrahmanwisam/
[product-screenshot]: images/cover.png
[medianofthree]: images/QuickSort/median-of-three.svg
[ptep]: images/QuickSort/PivotToEnd-Pointers.png
[ptf]: images/QuickSort/PivotToFinalPosition.png
[pc]: images/QuickSort/Pointers-Cross.png
[pe]: images/QuickSort/Pointers-Exchange.png
[Rec]: images/QuickSort/Recursion.svg
[FP]: images/BubbleSort/FirstPass.png
[SB]: images/BubbleSort/SwapBigger.png
[Begin]: images/SelectionSort/Begin.png
[MSF]: images/SelectionSort/MinSoFar.png
[SM]: images/SelectionSort/SwapMin.png
[Merge]: images/MergeSort/Merge.png
[SortSub]: images/MergeSort/SortSub.png
