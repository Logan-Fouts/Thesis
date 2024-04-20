
> [!NOTE] Note
> This is a revised version of our SPP.
> - Updated it to be more about the flexibility of the layered approach
> - Talked about comparative analysis with subsets of others experiments
> - Should be good to go to show Rafael
> - Went ahead and updated the [latex](https://www.overleaf.com/read/srnrdvgdddsv#e126f6)	

**Authors:** Logan Fouts, Henry Pap  
**LNU Supervisor:**  Rafael Messias Martins
**Supervision status according to student:**
- [ ] Currently working with (Ongoing project)
- [ ] Agreed but not started
- [ ] Wish to work with (or unclear of status)
- [ ] No preference, help me find one

## Preliminary Title
Layered Architecture Leveraged For Flexible Algorithm Building For Efficient and Accurate Detection of Visually Near-Duplicate Images.

## Elevator Pitch
The uncontrollable growth in the creation of photographs is and continues to be a problem requiring ways of efficient and accurate detection/management, particularly for visually similar images. There exists techniques to accomplish this; however, these tend to be highly dataset dependent, less accurate, or are complicated. Thus, we propose a new approach using a layered architecture, built by leveraging different techniques together. Therefore, we plan on experimenting taking some existing benchmarks for specific datasets and seeing how well we a layered architecture of algorithms could work for each.

## Steps/Milestones/Actions
1. **Select duplicate detection methods**
   - Research the current best methods and, for each layer of our system, select one that will be well suited.
2. **Decide upon a methodology for conducting our experiments.**
   - Find a well-defined structured methodology that we can follow for conducting experiments.
3. **Implement a layered architecture for duplicate detection.**
   - Translate the methods chosen previously into a unified layered approach.
4. **Conduct experiments and collect results.**
   - Execute a series of experiments on the implementation, collecting results for each.
5. **Evaluate our performance against existing solutions and benchmarks.**
   - Compare how our model performed compared to how other established solutions do in the same setups. These evaluations will include items such as accuracy, false positive/negative rate, execution time, etc.

## Risks
- **Implementation complexity**
  - **Risk:** When going into the coding phase of our project, we may find that the methods we are trying to implement are challenging to get working and may take more time than we have. This could be the algorithms themselves or how to get them to integrate and work together.
  - **Mitigation:** To avoid this pitfall we can utilize an incremental approach. This involves writing small portions of the program at a time to limit complexity. Furthermore, testing can be used throughout the development to identify any issues early on.
- **Differing Near duplicate image definitions**
  - **Risk:** While trying to combine different strategies, we may find that some are not so compatible. Thus, ending in poor results from experiments. This could be due to the fact that some may use differing definitions of what exactly is a near duplicate image.
  - **Mitigation:** While researching options for algorithms in each layer, we will ensure that the purposed techniques target labeling duplicate images based off of similar properties. If these share similar or the exact same definitions of what a near duplicate is, then we can consider them to be compatible.
- **Access to data sets**
  - **Risk:** To be able to properly compare and contrast our results to others we need to perform experiments with the same data sets. Access to this data may either be impossible or be locked behind paywalls.
  - **Mitigation:** In order to mitigate this risk, we can strategically collect data sets that are listed in papers we intend to compare against. While reading of the used data sets, access to each can be verified. As a backup idea, generated image data sets could be used.
- **Computational limitations**
  - **Risk:** The layered approach including potentially a heavy deep learning model may turn out to be very computationally heavy for our resources.
  - **Mitigation:** While in the process of choosing methods for each layer, we can vet each to make sure it is not only well suited for the specific layer but also computationally manageable for our hardware.

## The longer story

### Background and Motivations
In modern times, society is finding that the amount of images existing is ever-increasing. These images are not all insignificant selfies, some may provide information for health care, important law enforcement concerns, surveillance logs, or any number of other important information. Thus, the necessity to efficiently and reliably manage and process these images in each domain is growing.

#### Application Areas
- **Surveillance and Security:** Processing of images could more effectively remove old surveillance logs that are considered normal while avoiding any that have potential abnormalities. Furthermore, images from videos can be processed for automated monitoring without the need for human eyes.
- **Digital Libraries:** In places where users store lots of media such as pictures and videos, duplicate detection could prove a handy tool. The use of this detection could greatly reduce storage resource utilization which could help to reduce overall computational resource utilization.
- **Social Media:** Duplicate detection could be used heavily in this area to mitigate many issues. These include spam, copyright infringement, posting of illegal images, etc. This would have a direct effect on improving user experience within the platform.

#### Research Area
The idea of duplicate image detection done in a new flexible, efficient, and accurate manner falls nicely in the field of image processing within computer science. More specifically, this project aims to contribute information and potentially a new useful technique to the duplicate image detection research area.

#### Current Knowledge and Why Change
Research for duplication image detection solutions include current and previous works that range from basic hashing techniques to more intense ones, such as Convolutional Neural Networks (CNNs). All these have their strengths and weaknesses, usually with trade-offs between execution speed, accuracy, and in some cases, the ability to apply on other datasets. There exists no present existing method that may offer an efficient combination of all strengths that each algorithm possesses while at the same time minimizing weaknesses. In this approach, a layered architecture is proposed, where known methods are applied at each layer to progressively filter out images in hopes that a suitable solution for the complexities of real-world scenarios is found. Furthermore, our approach aims to allow easier access to customizable image processing algorithms and any number of combinations of such.

This solution could have significant societal, ethical, and economic benefits. Further improvements in detection of the duplicate image would be an improvement in the current quality of information on the Internet, making access to the correct form more reliable and even lessening the amount of misinformation. Ethically, it complies with copyright enforcement, and hence the reduction of illegal contents on the web. Implementation can cause economic waste of computing resources in a more ecologically disposed online world both for companies and individuals. All these added together, this approach has aimed not only to manage content online but also to make sure a more informed, properly-managed, ethically-clear, and resource-effective world is facilitated.

### Comparative Analysis of Near Duplicate Image Detection Techniques

| Feature                    | DHash                                                                      | Geometric Min Hash                                                      | VGG Net                                                                               |
| -------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Accuracy                   | Low to Medium, effective for simple duplicates                             | Medium to High, captures geometric similarities                         | Very high, even on complex images                                                     |
| Adaptability to Variations | Limited, works on exact or nearly exact images                             | Moderate, best for images with spatial variations                       | High, can handle a wide range of variations due to training                           |
| Approach                   | Difference hashing for image comparison                                    | Hashing based on geometric features                                     | Convolutional Neural Network (CNN)                                                    |
| Efficiency                 | Very high, fast enough for real-time                                       | High for reasonably large datasets                                      | Low, computationally expensive                                                        |
| Implementation Complexity  | Low, simple to implement                                                   | Moderate, requires understanding of geometric hashing                   | High, requires deep learning and AI expertise                                         |
| Dataset Domain             | Best for straightforward, less complex image sets (e.g., documents, icons) | Effective in datasets with spatial transformations (rotations, scaling) | Diverse datasets with high detail variability (e.g., natural images, medical imaging) |

#### Related work
In the paper, *Bimodal Fusion of Low-Level Features and High-Level Semantic Features for Near-Duplicate Video Clip Detection*, a new approach for near duplicate video clip detection is explored that is leveraged in order to increase accuracy. This technique is called bimodal fusion and it involves combining low-level features with high-level semantic information. Inspired by this idea of combining different algorithms to extract more information, our purposed approach is a layered architecture including different algorithms at each level for near duplicate image detection. Since this new approach provided promising results, we intend to reform and expand upon it in a different direction.

The work done by *GmH* builds upon the classic min-hash algorithm, traditionally used for efficient similarity detection by visual word hashing. They identify unique central features that give spatial and scale information which is used to perform secondary feature extraction, constructing a richer set of geometric features. This method results in a higher discriminative representation of visual words that leverages the inherent strengths of the min-hash technique. The GmH approach demonstrates substantial improvements in recall and reduces the false positive rate making it into a powerful algorithm for image processing, particularly in near duplicate detection. Similar to GmH, our methodology begins with high-level feature extraction, followed by low level extraction. However, our approach differ in that we aim to integrate various algorithms while GmH focuses on enhancing the min-hash algorithm. This should show improved results for near-duplicate image detection. GmH may in the end be one step of our algorithm that could be used.

The work done by *fingerprint elevation* shows very nice results by combining three distinct algorithms, dHash, SIFT and LSH model. The initial two algorithms, dHash and SIFT are used for feature extraction resulting in several hashes, these are combined into one condensed hash representation a fingerprint image. LSH receives the hash representation from previous step, where it employs a final feature extraction which put respective features into respective buckets, reduces the search space. Finally hamming distance is applied to find matching fingerprints, their approach shows a significant promise of 99.99\% accuracy. Their method is similar to ours in that they utilizes the advantages of multiple algorithms, however ours diverges as we adopt a more modular approach to the integration of algorithm by using a layered architecture. We believe this offers improved flexibility to choose different algorithms which can lead to better performance and accuracy throughout differing application areas.

#### Knowledge Gap/Challenge/Problem
Though many techniques are available for image duplicate detection, there exists a lack of an effective methodology with high accuracy and efficiency across diverse datasets. Even the most promising methods usually suffer from their complexity, and the implementation itself becomes quite a difficult task.

#### Knowledge Contribution/Action
This paper introduces the idea for a new algorithm based on a layered architecture of combining various near duplicate image detection techniques. Thus increasing the flexibility of detecting near-duplicate images across differing domains, all while aiming for a simple and easy to understand algorithms.

This research may offer a framework, to flexibly integrate any added algorithms together that can be used for a number of datasets and application areas. A new framework allows for a certain level of personalization, able to be modified and deployable in a range of scenarios.

#### Empirical Evidence/Evaluation
We plan to evaluate our solution by use of a controlled experiments, which will be guided by methodology seen in related work. This will be compared with standard methods such as accuracy, precision, recall, and efficiency by using accessible standard image datasets.

**Evaluation Strategy:** Directly compare under controlled conditions the selected metrics; evaluate with different image datasets to demonstrate the effectiveness and adaptability of this new solution.

**Performance Metrics:** These will be the accuracy, computational efficiency, performance across differing datasets, and other commonly used metrics for performance in this research field (ROC for example). These metrics can be used to see how this solutions works in comparison to other current solutions.