
> [!NOTE] Think About
> False positives would be very bad for our arhitecture
> - dhash has a low false positive rate
> - Design science methodology
## Do this right now quickly
- **Minimal viable project**
- Maybe we use ==Design science methodology==
## How to write related work
- Summary
- Position (Relate their work to yours)
- Motivation (Why is it important)
This should show the research gap.
###  ~~Articles chosen (TBD)~~
- ~~[[Bimodal Fusion of Low-Level Visual Features and High-Level Semantic Features For Near-Duplicate Video Clip Detection.pdf]]~~
	- ~~This gives us the idea to combine different techniques together~~
- ~~[[Near Duplicate Image Detection min-Hash and tf-idf Weighting.pdf]] or [[Geometric_min-Hashing_Finding_a_thick_needle_in_a_haystack.pdf]]~~
	- ~~Layer 1 solution~~
- ~~[[Revisiting Gist-PCA Hashing for Near Duplicate Image Detection.pdf]]~~
	- ~~Layer 2 solution~~
- ~~[[Pulse Coupled NN based Near-Duplicate Detection of Images (PCNN - NDD).pdf]] or Use VGG~~
	- ~~Layer 3 solution~~~~
~~

## ~~Preliminary Title~~
~~Improving visually duplicate image detection with deep learning and multi-modal fusion~~

## ~~Elevator Pitch~~
~~Background: Current image analysis often struggles to accurately identify near duplicate images due to the complexity and variability of real-world scenes, and the inherit complexity in defining what is a near duplicate. This shortcoming results in inadequate solutions for detecting copyright infringements and other legal concerns, as well as leading to unnecessary consumption of significant storage resources.~~

~~Challenge: Accurately extracting and utilizing low-level features from the main objects in images for more accurate duplicate detection remains relatively unexplored.~~

~~Action: Implement a program that will identifies main objects, classifies them, and extracts low-level features to generate a unique hash for each object that can then be used to decide if images are to be considered duplicates or not.~~

~~Evaluation: The effectiveness of the approach will be assessed by comparing the accuracy of this duplicate detection method against existing benchmarks and other strategies.~~

## Why
- [This](https://books.google.se/books?hl=en&lr=&id=qcHsCgAAQBAJ&oi=fnd&pg=PA107&dq=layered+approach+in+Image+Processing&ots=qNZqrM3zSk&sig=MrRYL1LCsTTyzBjzCcnUlAlXewA&redir_esc=y#v=onepage&q=layered%20approach%20in%20Image%20Processing&f=false) book discusses a layered approach for image processing but is from 1993.
- Other layered approaches use layers to extract different features while all of our layers are just trying to identify duplicates
- We are targeting a more **flexible** approach?
	- We allow for differing speed/accuracy depending on how many and what layers we use.
- Versatile for varied image types/conditions
- Adaptation to the newest best technologies and algorithms

## Focus point
### Choose a target audience for the project
- Probably law/copyright enforcement, but could be private individuals as well
### ~~Image aspects to consider~~
- ~~Overall image classification.~~
- ~~Probably grey scale the image.~~
- ~~Probably no object location just simply object exists in the image.~~


## Focus point next steps 
- find datasets 
- find relative studies to create compare 
- find other definitions of NDD 
- find different algorithms to include ()
- tweak algorithms to find suiting paramas 
- build presets of parameters/algorithms 
- self build datasets (as backup)
- improve overall user experience 


### Questions to ask for next steps

- when should we start implementing?
- what should we focus on?
- how extensive should our experiments be?
- do we need to justify the reason why we go with layered architecure?j
