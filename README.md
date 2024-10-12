
<a id="readme-top"></a>

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
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
    <li><a href="#objective">Objective</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#Visualizations">Visualizations</a></li>
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
  
<a id="readme-top"></a>
### Installation and Usage


1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
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

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- VISUALIZATIONS -->
## Visualizations

### Bubble Sort
##### Time Complexity: $O(n^2)$

https://github.com/user-attachments/assets/febdc27f-0c52-4d4c-b51f-27345303b398

---

### Selection Sort
##### Time Complexity: $O(n^2)$



https://github.com/user-attachments/assets/e0bbfa89-6433-4534-8d08-22112c2e2979


---

### Merge Sort
##### Time Complexity: $O(n \log(n))$

https://github.com/user-attachments/assets/b5bd3f20-3fdb-449b-bccf-6ff082a6d6ee


---

### Quick Sort
##### Time Complexity: $O(n \log(n))$




<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Abdelrahman Elbana - manelbana079@gmail.com

Project Link: [https://github.com/A-Elbana/SortingAlgos](https://github.com/A-Elbana/SortingAlgos)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Geeksforgeeks - Bubble Sort Algorithm](https://www.geeksforgeeks.org/bubble-sort-algorithm/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



[forks-shield]: https://img.shields.io/github/forks/A-Elbana/SortingAlgos.svg?style=for-the-badge
[forks-url]: https://github.com/A-Elbana/SortingAlgos/network/members
[stars-shield]: https://img.shields.io/github/stars/A-Elbana/SortingAlgos.svg?style=for-the-badge
[stars-url]: https://github.com/A-Elbana/SortingAlgos/stargazers

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/abdelrahmanwisam/
[product-screenshot]: cover.png
