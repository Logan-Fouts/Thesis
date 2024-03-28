## Preliminary Title
Improving visually duplicate image detection with deep learning and multimodal fusion
## Elevator Pitch
Background: Current image analysis often struggles to accurately identify near duplicate images due to the complexity and variability of real-world scenes, and the inherit complexity in defining what is a near duplicate. This shortcoming results in inadequate solutions for detecting copyright infringements and other legal concerns, as well as leading to unnecessary consumption of significant storage resources.

Challenge: Accurately extracting and utilizing low-level features from the main objects in images for more accurate duplicate detection remains relatively unexplored.

Action: Implement a program that will identifies main objects, classifies them, and extracts low-level features to generate a unique hash for each object that can then be used to decide if images are to be considered duplicates or not.

Evaluation: The effectiveness of the approach will be assessed by comparing the accuracy of this duplicate detection method against existing benchmarks and other strategies.


## Focus point
### Choose a target audience for the project
- Probably law/copyright enforcement.
### Image aspects to consider
- Overall image classification.
- Probably grey scale the image.
- Probably no object location just simply object exists in the image.

## Steps
- Define what should be considered near duplicate images
- Identify our idea for detecting duplicate images that fills a research gap

project-steps
- Define what should be considered near duplicate images
- choose one or several methods to detect image features 
- combine and produce a identity from result of those methods (likely a hash) (per image)
- cross checking these sets of images to detect near duplicate on the benchmark of step 1 
- compare results on previous solutions
- potentially - performance increase, some images might be unecessary to compare etc. 
- maybe talk about future work 