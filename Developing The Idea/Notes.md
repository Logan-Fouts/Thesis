## How to write related work
- Summary
- Position (Relate their work to yours)
- Motivation (Why is it important)
This should show the research gap.

## Preliminary Title
Improving visually duplicate image detection with deep learning and ~~multi-modal fusion~~

## Elevator Pitch
Background: Current image analysis often struggles to accurately identify near duplicate images due to the complexity and variability of real-world scenes, and the inherit complexity in defining what is a near duplicate. This shortcoming results in inadequate solutions for detecting copyright infringements and other legal concerns, as well as leading to unnecessary consumption of significant storage resources.

Challenge: ~~Accurately extracting and utilizing low-level features from the main objects in images for more accurate duplicate detection remains relatively unexplored.~~

Action: ~~Implement a program that will identifies main objects, classifies them, and extracts low-level features to~~ generate a unique hash for each object that can then be used to decide if images are to be considered duplicates or not.

Evaluation: The effectiveness of the approach will be assessed by comparing the accuracy of this duplicate detection method against existing benchmarks and other strategies.

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
