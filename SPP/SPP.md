## Preliminary Title
Layered Architecture for Efficient and Accurate Detection of Semantic Near-Duplicate Images.

## Elevator Pitch
### Background
### Challenge
### Action
### Evaluation

## Steps/Milestones/Actions
1. Define criteria for near duplicate images
	- Use previous research to decide upon what factors will be considered when classifying two images.
2. Select duplicate detection methods
	- Research the current best methods and, for each layer of our system, select one that will be well suited.
3. Decide upon a methodology for conducting our experiments.
	- Find a well defined structured methodology that we can follow for conducting experiments.
4. Implement a layered architecture for duplicate detection.
	- Translate the methods chosen previously into a unified layered approach.
5. Conduct experiments and collect results.
	- Execute a series of experiments on the implementation, collecting results for each.
6. Evaluate our performance against existing solutions and benchmarks.
	- Compare how our model performed compared to how other established solutions do in the same setups. These evaluations will include items such as accuracy, false positive/negative rate, execution time, etc.
7. ~~potentially - performance increase, some images might be unnecessary to compare etc.~~
8. ~~maybe talk about future work~~ 

## Risks
- Implementation complexity
	- **Risk:** When going into the coding phase of our project, we may find that the methods we are trying to implement are challenging to get working. This could be the algorithm themselves or how to get them to integrate and work together.
	- **Mitigation:** To avoid this pitfall we can utilize an incremental approach. This involves writing small portions of the program at a time to limit complexity. Furthermore, testing can be used throughout the development to identify any issues early on.
- Access to data sets
	- **Risk:** To be able to properly compare and contrast our results to others we need to perform experiments with the same data sets. Access to this data may either be impossible or be locked behind paywalls.
	- **Mitigation:** In order to mitigate this risk we can strategically collect data sets that are listed in papers we intend to compare against. While reading of the used data sets, access to each can be verified.
- Computational limitations
	- **Risk:** The layered approach including potentially a heavy deep learning model may turn out to be very computationally heavy for our resources.
	- **Mitigation:** While in the process of choosing methods for each layer, we can vet each to make sure it is not only well suited for the specific layer but also computationally manageable for our hardware.

## The longer story
### Background and Motivations
In modern times, society is finding that the amount of images existing is ever-increasing. These images are not all insignificant selfies, some may provide information for health care, including important law enforcement concerns, surveillance logs, or any number of other important information. Thus, the necessity to efficiently and reliably manage and process these images is growing. 

#### Application Areas
Image processing in general is a very useful tool across many different areas for a plethora of different use cases. Below are a few primary areas with motivation. 

**Healthcare:** Images may need to be compared for duplication to limit redundant scans, to optimize storage, or even identify health concerns against existing known images of such.

**Surveillance and Security:** Processing of images could more effectively remove old surveillance logs that are considered normal while avoiding any that have potential abnormalities. Furthermore, images from videos can be processed for automated monitoring without the need for human eyes.

**Digital Libraries:** In places where users store lots of media such as pictures and videos, duplicate detection could prove a handy tool. The use of this detection could greatly reduce storage resource utilization which could help to reduce overall computational resource utilization.

**Social Media:** Duplicate detection could be used heavily in this area to mitigate many issues. These include spam, copyright infringement, posting of illegal images, etc. This would have a direct effect on improving user experience within the platform.

#### Research Area
The idea of duplicate image detection done in a new efficient and accurate manner falls nicely in the field of image processing within computer science. More specifically this project aims to contribute information and potentially a new useful technique to the duplicate image detection research area.
### Related work
### Knowledge Gap/Challenge/Problem
### Knowledge Contribution/Action
### Empirical Evidence/Evaluation