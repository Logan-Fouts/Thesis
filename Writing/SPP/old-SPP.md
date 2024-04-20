## Intro
This thesis will address the problem that current near duplicate image detection methods are complex and hardly customizable for highly varied data sets and different definitions of what is exactly a near duplicate image. This thesis is being made as part of a course from a Bachelors Program in Software Technology at Linnaeus University. While the shear amount of images online grows, it becomes more important for there to exist effective methods for detecting near duplicates in every increasing different domains.

This work sets out to design a framework that would make designing algorithms more easily customizable and, therefore, accessible and adaptable to each individuals needs. In summary, this framework is an attempt to bridge between complex image processing algorithms  and engineering solutions in practice, with an advanced, versatile tool for users. Subsequent chapters present the design, implementation, and evaluation of a framework that has the potential to change how image processing algorithms are designed and deployed in practice instead of just in theory.
## Preliminary Title
Flexible Algorithm Customization using a Layered Architecture for Efficient and Accurate Detection of Semantic Near-Duplicate Images

## Elevator Pitch
The uncontrollable growth in the creation of photographs is and continues to be a problem requiring ways of efficient and accurate detection/management, particularly for semantically similar images. There exists techniques to accomplish this; however, these tend to be inefficient in varied datasets, less accurate, or complicated to implement. In this paper, we propose a new algorithm using a layered architecture, built by leveraging different techniques together, with the idea of improving accuracy and efficiency while staying adaptable and relatively simple for implementation. Therefore, we plan on experimenting using standard image data sets in controlled experiments and then comparing them with other methods in terms of accuracy, efficiency, adaptability, and other key metrics.

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
	- **Risk:** When going into the coding phase of our project, we may find that the methods we are trying to implement are challenging to get working and may take more time then we have. This could be the algorithm themselves or how to get them to integrate and work together.
	- **Mitigation:** To avoid this pitfall we can utilize an incremental approach. This involves writing small portions of the program at a time to limit complexity. Furthermore, testing can be used throughout the development to identify any issues early on.
- Differing Near duplicate image definitions
> [!NOTE] TODO
> - Write the above section

- Access to data sets
	- **Risk:** To be able to properly compare and contrast our results to others we need to perform experiments with the same data sets. Access to this data may either be impossible or be locked behind paywalls.
	- **Mitigation:** In order to mitigate this risk we can strategically collect data sets that are listed in papers we intend to compare against. While reading of the used data sets, access to each can be verified. As a backup idea, generated image data sets could be used.
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

**Copyright infringement**- could be an area on its own.

#### Research Area
The idea of duplicate image detection done in a new efficient and accurate manner falls nicely in the field of image processing within computer science. More specifically this project aims to contribute information and potentially a new useful technique to the duplicate image detection research area.

#### Current Knowledge and Why Change
Research shows a plethora of current and past solutions for duplicate image detection. These range from basic hashing techniques like min-hash to more intensive methods such as Convolutional Neural Networks (CNNs). These methods each have their strengths and weaknesses, with some having speed over accuracy, others providing accuracy at the expense of speed, and many showing greater or lesser adaptability to different datasets. This range of pros and cons for each method elicits a notable gap. Despite so many current techniques their is an absence of a method that seamlessly combines high efficiency with accuracy across varied datasets. Furthermore, current best solutions are highly complex and hard to implement. To fill in this gap, a layered architecture is proposed, where each layer utilizes its own distinct method to progressively filter input images as they pass from the top to bottom layers. This nuanced approach hopes to be adaptable to various datasets without requiring modifications, while ensuring a balance between efficiency and accuracy that enhances its usability in real-world applications.

To motivate why this gap should be filled, different potential positive effects can be discussed. Achieving more efficient and reliable duplicate image detection could greatly increase the quality of information on the internet, impacting society by more reliably providing access to accurate information and minimizing the spread of misinformation. Furthermore, this project hopes to help contribute to cleansing the internet of the copyright violations and illegal content that is currently abundant, ensuring individuals keep possession of their creations and preventing misuse of online platforms. Finally, the use of this project/idea by not only corporations but also individuals could lead to a significant reduction in resource consumption, as duplicates would no longer take up precious compute power and storage resources. This conserves financial resources and also allows for more effective use of storage and processing. In summary it could help to contribute to a greener world.

| Feature                        | DHash                                          | Geometric Min Hash                                    | VGG Net                                                     |
| ------------------------------ | ---------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------- |
| **Accuracy**                   | Low to Medium, effective for simple duplicates | Medium to High, captures geometric similarities       | Very high, even on complex images                           |
| **Adaptability to Variations** | Limited, works on exact or nearly exact images | Moderate, best for images with spatial variations     | High, can handle a wide range of variations due to training |
| **Approach**                   | Difference hashing for image comparison        | Hashing based on geometric features                   | Convolutional Neural Network (CNN)                          |
| **Efficiency**                 | Very high, fast enough for real-time           | High for reasonably large datasets                    | Low, computationally expensive                              |
| **Implementation Complexity**  | Low, simple to implement                       | Moderate, requires understanding of geometric hashing | High, requires deep learning expertise                      |

### Related work
### Knowledge Gap/Challenge/Problem
Though many techniques are available for image duplicate detection, there exists a lack of an effective methodology with high accuracy and efficiency across diverse datasets. Even the most promising methods usually suffer from their complexity, and the implementation itself becomes quite a difficult task.
### Knowledge Contribution/Action
This paper introduces the idea for a new algorithm based on a layered architecture of combining various near duplicate image detection techniques. Thus increasing the accuracy and effectiveness of detecting near-duplicate images, all while aiming for a simple and easy to understand algorithm.

This research may offer a framework, to flexibly integrate any added algorithms together that can be used for a number of datasets and application areas. A new framework allows for a certain level of personalization, able to be modified and deployable in a range of scenarios.
### Empirical Evidence/Evaluation
We plan to evaluate our solution by use of a controlled experiment, which will be guided by methodology seen in related work. This will be compared with standard methods such as accuracy, precision, recall, and efficiency by using accessible standard image datasets.

**Evaluation Strategy:** Directly compare under controlled conditions the selected metrics; evaluate with different image datasets to demonstrate the effectiveness and adaptability of this new solution.

**Performance Metrics:** These will be the accuracy, computational efficiency, performance across differing datasets, and other commonly used metrics for performance in this research field (ROC for example). These metrics can be used to see how this solutions works in comparison to other current solutions.