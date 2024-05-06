With the every increasing digital world, this thesis from Linnaeus University's Bachelor Programme in Software Technology, hopes to contribute information to the intricate challenge of near-duplicate image detection across the various domains and use cases. Traditional methods alone cannot be expected to work properly in this ever-diversifying dataset, together with the fluid definitions of what might be considered as a near-duplicate image. And the current solutions that aim to address this problem often are highly complicated.

As the sheer number of images grows, the need for more generalizable methods of detection on differing datasets and definitions of near duplicates becomes clear. This work is an endeavor to engineer a new architecture—one that makes it easier to combine image processing algorithms for more flexible and effective solutions.

In this respect, the thesis proposes a possible solution to the missing link between the theoretical algorithmic complexity and the engineering solution with a flexible architectural approach. The following chapters look into more detail into the design of the architecture, describe practical implementation, and outline evaluation—all with a single aim: contributing an idea as to how solutions for image processing could be implemented. 

~~This thesis will address the problem that current near duplicate image detection methods are complex and hardly flexible for varied data sets and different definitions of what constitutes a near duplicate image. This thesis is being made as part of a course from a Bachelors Program in Software Technology at Linnaeus University. While the sheer amount of images online grows, it becomes more important for there to exist effective and simple methods for detecting near duplicates in an ever-increasing amount of different domains.~~

~~This work sets out to design an architecture that will make designing algorithms easily customize-able and, therefore, accessible and adaptable to each individual's needs. In summary, this is an attempt to bridge between complex image processing algorithms and engineering solutions in practice, with an advanced, versatile architecture. Subsequent chapters present the design, implementation, and evaluation of a framework that has the potential to change how some image processing solutions are designed and deployed in practice.~~

---
## Background

In modern times, society is finding that the amount of images existing is ever-increasing. These images are not all insignificant selfies, some may provide information for healthcare, important law enforcement concerns, surveillance logs, or any number of other important information. Thus, the necessity to efficiently manage and process these images in each unique domain is growing.

### Application Areas

Image processing in general is a very useful tool across many different areas for a plethora of different use cases. Below are just a few areas in which customized refined algorithms could provide benefits with motivation:

- **Surveillance and Security:** Processing of images could more effectively remove old surveillance logs that are considered normal while avoiding any that have potential abnormalities. Furthermore, images from videos can be processed for automated monitoring without the need for human eyes.
- **Digital Libraries:** In places where users store lots of various ranges of media such as pictures and videos, duplicate detection could prove a handy tool. The use of this detection could greatly reduce storage resource utilization which could help to reduce overall computational resource utilization.
- **Social Media:** Refined duplicate detection could be used heavily in this area to mitigate many issues. These include spam, copyright infringement, posting of illegal images, etc. This would have a direct effect on improving user experience within the platform.

### Research Area

The idea of duplicate image detection done in a new efficient and accurate manner falls nicely in the field of image processing within computer science. More specifically, this project aims to contribute information and potentially a new useful technique to the duplicate image detection research area. The tool built for the technique may be considered as part of the software engineering field.

| Feature                    | DHash                                                                      | Geometric Min Hash                                                      | VGG Net                                                                               |
| -------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Accuracy                   | Low to Medium, effective for simple duplicates                             | Medium to High, captures geometric similarities                         | Very high, even on complex images                                                     |
| Adaptability to Variations | Limited, works on exact or nearly exact images                             | Moderate, best for images with spatial variations                       | High, can handle a wide range of variations due to training                           |
| Approach                   | Difference hashing for image comparison                                    | Hashing based on geometric features                                     | Convolutional Neural Network (CNN)                                                    |
| Efficiency                 | Very high, fast enough for real-time                                       | High for reasonably large datasets                                      | Low, computationally expensive                                                        |
| Implementation Complexity  | Low, simple to implement                                                   | Moderate, requires understanding of geometric hashing                   | High, requires deep learning and AI expertise                                         |
| Dataset Domain             | Best for straightforward, less complex image sets (e.g., documents, icons) | Effective in datasets with spatial transformations (rotations, scaling) | Diverse datasets with high detail variability (e.g., natural images, medical imaging) |

*Table 1: Comparative Analysis of Image Detection Techniques*

---
## Related work

In the paper, *Bimodal Fusion of Low-Level Features and High-Level Semantic Features for Near-Duplicate Video Clip Detection*, a new approach for near duplicate video clip detection is explored that leverages bimodal fusion, which involves combining low-level features with high-level semantic information. Inspired by this idea of combining different algorithms to extract more information, our purposed approach is a layered architecture including different algorithms at each level for near duplicate image detection. Since this new approach provided promising results, we intend to reform and expand upon it in a different direction.

Research from Chum et al. builds upon the classic min-hash algorithm, traditionally used for efficient similarity detection by visual word hashing. They identify unique central features that give spatial and scale information which is used to perform secondary feature extraction, constructing a richer set of geometric features. This method results in a higher discriminative representation of visual words that leverages the inherent strengths of the min-hash technique. The GmH approach demonstrates substantial improvements in recall and reduces the false positive rate making it into a powerful algorithm for image processing, particularly in near duplicate detection. Similar to GmH, our methodology begins with high-level feature extraction, followed by low-level extraction. However, our approach differs in that we aim to integrate various algorithms while GmH focuses on enhancing the min-hash algorithm. This should show improved results for near-duplicate image detection. GmH may in the end be one step of our algorithm that could be used.

The work done in this article shows promising results by combining three distinct algorithms, dHash, SIFT, and LSH model in a horizontal manner. The initial two algorithms, dHash and SIFT are used for feature extraction resulting in several hashes, these are combined into one condensed hash representation a fingerprint image. LSH receives the hash representation from the previous step, where it employs a final feature extraction which put respective features into respective buckets, reduces the search space. Finally, hamming distance is applied to find matching fingerprints, their approach shows a significant promise of 99.99\% accuracy. Their method is similar to ours in that they utilize the advantages of multiple algorithms, however, ours diverges as we adopt a more modular approach to the integration of algorithms by using a layered architecture. We believe this offers improved flexibility to choose different algorithms which can lead to better performance and accuracy throughout differing application areas.

## Motivation

This solution could have significant societal, ethical, and economic benefits. Further improvements in the detection of duplicate images would be an improvement in the current quality of information on the Internet, making access to the correct form more reliable and even lessening the amount of misinformation. Ethically, it complies with copyright enforcement, and hence the reduction of illegal contents on the web. Implementation for each specific domain could minimize economic waste of computing resources in a more ecologically disposed online world both for companies and individuals. All these considered together, this approach aims not only to more effectively allow content management online but also to ensure a more informed, properly-managed, ethically-clear, and resource-effective world is facilitated.

### ~~Knowledge Gap/Challenge/Problem~~

~~Research for duplication image detection solutions includes current and previous works that range from basic hashing techniques to more intense ones, such as Convolutional Neural Networks (CNNs). All these have their strengths and weaknesses, usually with trade-offs between execution speed, accuracy, and in some cases, the ability to apply on other datasets. Currently, there exists a horizontal approach to combining methods together but this proves to be highly complex and more difficult to get working. In our approach, a layered architecture, known methods are applied at each layer to progressively filter out images in hopes that suitable solutions for each problem domain can be made. Our approach aims to allow specifically tailored algorithms to be made in a more simple manner for whatever the users input domain and near duplicate image definitions are.~~~~
~~
### ~~Knowledge Contribution/Action~~

~~This paper introduces the idea of using a layered architecture of combining various near duplicate image detection techniques together in a filter-like structure. Thus, we will be taking more simple and less flexible algorithms and combining them for a more flexible result, while aiming for easy-to-understand algorithms.~~~~
~~
### Empirical Evidence/Evaluation

We plan to evaluate our solution by use of controlled experiments, which will be guided by methodology seen in related work. Our results will be compared with standard methods such as accuracy, precision, recall, and efficiency that were detailed in articles we plan on targeting as use cases.

**Evaluation Strategy:** Directly compare under controlled conditions the selected metrics; evaluate with different image datasets to demonstrate the effectiveness and adaptability of this new solution in relation to results gathered from each specific article.

**Performance Metrics:** These will be the accuracy, computational efficiency, performance across differing datasets, and other commonly used metrics for performance in this research field (ROC for example). These metrics can be used to see how this solution works in comparison to other current solutions for each use case.

If we can elicit good results for diverse input domains and definitions of near duplicate images, then we can say that we have created a more easily understood flexible approach to combining image processing techniques.

---
## Problem formulation

The central challenge addressed by this thesis revolves around the complexities and inflexibilities inherent in current methods of near-duplicate image detection. As the digital world expands, the need for effective and more easily adapted detection technologies grows as well. Current technologies often struggle to accommodate the variability in data sets and the lack of a uniform definition for what constitutes a "near-duplicate" image. This thesis proposes a novel approach aimed at resolving these issues.

### Knowledge Gap

Despite all the progress in image processing techniques, a gap remains in the development of a method that can dynamically combine algorithms into a pipeline that is adapted to various data sets and definitions of near-duplicate images while remaining relatively simple to understand. The existing solutions often require complex configurations that do not lend themselves to easy customization for diverse application domains. This gap highlights the necessity for a more flexible architectural framework that can simplify the customization process of combining many algorithms for specific user requirements.

### Research Objectives

The primary objective of this research is to design and evaluate a versatile architecture that simplifies the process of developing and deploying image detection algorithms. By integrating various algorithmic layers, this architecture aims to offer a solution that can be easily adapted to meet individual and domain-specific needs. This approach hopes to bridge the gap between complex theoretical image processing algorithms and practical engineering solutions, providing a more digestible approach that supports extensive customization.

### Problem Statements

The problem can be summarized into a few main questions that guide our research and development:

1. **Can a layered architecture be used to provide a flexible and reasonable way to combine image processing algorithms?**
2. **In what ways can the proposed architecture improve the efficiency and flexibility of near-duplicate detection compared to existing methods?**
3. ~~**How can this new framework be implemented to ensure it is accessible and usable by a broad spectrum of users, from researchers to commercial developers?**~~
## Results
### Empirical Evidence/Evaluation

We plan to evaluate our solution by use of controlled experiments, which will be guided by methodology seen in related work. Our results will be compared with standard methods such as accuracy, precision, recall, and efficiency that were detailed in articles we plan on targeting as use cases.

**Evaluation Strategy:** Directly compare under controlled conditions the selected metrics; evaluate with different image datasets to demonstrate the effectiveness and adaptability of this new solution in relation to results gathered from each specific article.

**Performance Metrics:** These will be the accuracy, computational efficiency, performance across differing datasets, and other commonly used metrics for performance in this research field (ROC for example). These metrics can be used to see how this solution works in comparison to other current solutions for each use case.

If we can elicit good results for diverse input domains and definitions of near duplicate images, then we can say that we have created a more easily understood flexible approach to combining image processing techniques.

## Scope/Limitation

**Scope**
- Development of the Layered Architecture: This is the development of this modular architecture that will allow easy composition of various near duplicate image detection algorithms. The approach should be flexible to allow for adaptation to certain needs within different datasets and use cases.
- **Evaluation through Controlled Experiments:** In this evaluation, the effectiveness and performance of our proposed idea will we compared with traditional methods of image detection as well as an any found examples of horizontal combinations of algorithms. The goal is to see if a layered approach can be highly flexible as well and remain less complex than previous approaches.

**Limitations:**
- **Algorithm Selection:** Existing image detection algorithms form the basis of our study. Our research covers customization and combinations of these algorithms under the new architecture, but there will be no development of completely unique detection algorithm in this thesis scope.

**Data constraints:** Given the time and resources are very limited, the experiments will be conducted with a small and limited subset of publicly available datasets. Even though data sets will be selected to be representative of the different kinds of images and settings, these will not span all conceivable scenarios.
- **Generalizability of the Results:** The level of generalizability that could be accorded to the results would mainly be based on the specific algorithms and datasets used in our research. For example, although valid for indicating the potential of the framework, these results should not be generalized to all cases of image data or detection scenarios.

- **Production Deployment**: The thesis does not discuss the deployment of the project into any production environment.

Most of the issues in scalability, continuous integration, and real-time processing are acknowledged but not focused on. With these boundaries set, the aim of the thesis is to take a focused look at the proposed architecture, understanding that there are practical limits met during its research.

## Target group

The primary target group for our thesis is a broad set of people and organizations that stand to benefit from advanced, customizable near duplicate image detection technologies. Some interested parties could include, academic researchers, software developers, digital content managers, security analysts, and social media organizations who require adaptable tools for managing large datasets of images across various domains. By addressing some of the needs of these groups, the thesis hopes to provide an idea that has many practical applications.

## Outline

> [!TODO]
> Here you outline the rest of the report. It shall contain which chapters that will follow, and what each of them is about.
> 
> **Example:**
> 
> This report is organized as follows. In Chapter 2 we discuss the methodological framework, research methods, and ethical considerations. Chapter 3 provides a full account of the theoretical background and discusses the knowledge gap used in the project. In Chapter 4 we discuss the objectives for an evaluation technique, which guides the design of a technique that we present in Chapter 5. Chapters 6 and 7 describe the validation of the technique. First, we demonstrate the technique on three cases in Chapter 6. In Chapter 7, we describe the case study design for the stakeholder interviews. Chapter 8 presents and discusses experiences and results from the demonstration and interviews. These are analyzed and discussed further in Chapter 9, where we also discuss threats to the validity of the work. In Chapter 10 we Conclude and discuss Future work.
> 