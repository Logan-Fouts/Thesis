With the ever-increasing digital world, this thesis from Linnaeus University's Bachelor Programme in Software Technology, hopes to contribute information to the intricate challenge of near-duplicate image detection across the various domains and use cases. Traditional methods alone cannot be expected to work properly in this ever-diversifying dataset, this together with the fluid definitions of what might be considered as a near-duplicate image. As Vonikakis et al. stated in their paper *Photo Cluster*, "ND detection in personal photolibraries is a very challenging task, mainly due to the semantic gap, which may result in different interpretations between observers" \cite{photocluster}. Current solutions that aim to address this problem often are highly complicated tending to be less flexible.

As the sheer number of images grows, the need for more generalizable methods of detection on differing datasets and definitions of ND becomes clear. This work is an endeavor to engineer a new layered architecture-based framework—one that makes it easier to combine image processing algorithms for more flexible and effective solutions.

In this respect, the thesis proposes a possible solution to the missing link between the theoretical algorithmic complexity and the engineering solution with a flexible architectural approach. The following chapters look into more detail into the design of the architecture, describe practical implementation, and outline evaluation—all with a single aim: contributing a way as to how modern solutions for image processing could be built.

Before we continue, a few key definitions should be made. 
1. NDI means near duplicate image, hence ND means near duplicate.
2. Horizontal approach means on the same level algorithms are combined in some manner such as concatenating hashes.
3. Vertical approach means algorithms are layers that are stacked on top of each other.

## Background
In modern times, society is finding that the amount of images existing is ever-increasing. These images are not all insignificant selfies, some may provide information for health care, important law enforcement concerns, surveillance logs, or any number of other important information. Thus, the necessity to efficiently manage and process these images in each unique domain is growing.

### Application Areas
Image processing in general is a very useful tool across many different areas for a plethora of different use cases. Below are just a few areas in which customized refined algorithms could provide benefits with motivation:

- **Surveillance and Security:** Processing of images could more effectively remove old surveillance logs that are considered normal while avoiding any that have potential abnormalities. Furthermore, images from videos can be processed for automated monitoring without the need for human eyes.
  
- **Digital Libraries:** In places where users store lots of various ranges of media such as pictures and videos, duplicate detection could prove a handy tool. The use of this detection could greatly reduce storage resource utilization which could help to reduce overall computational resource utilization.
  
- **Social Media:** Refined duplicate detection could be used heavily in this area to mitigate many issues. These include spam, copyright infringement, posting of illegal images, etc. This would have a direct effect on improving user experience within the platform.

### Research Area
The idea of duplicate image detection done in a new efficient and accurate manner falls nicely in the field of image processing within computer science. More specifically, this project aims to contribute information and a new useful tool to the duplicate image detection research area. The framework built for the technique may be considered as part of the software engineering field.

### Current Knowledge and Why Change
Research for duplication image detection solutions include current and previous works that range from basic hashing techniques to more intense ones, such as Convolutional Neural Networks (CNNs). All these have their strengths and weaknesses, usually with trade-offs between execution speed, accuracy, and in some cases, the ability to apply on other datasets. In order to try to have the benefits while minimizing negatives, solutions nowadays are mostly a combination on these individual methods. The main way in which this is accomplished seems to be a horizontal approach, but this proves to be highly complex and more difficult to get working. Two examples of implementations using this approach are \cite{GmH} and \cite{fingerprintelevation}. In our approach, a layered architecture as the core of the framework is proposed, where known methods are applied at each layer to progressively filter out images in hopes that suitable solutions for each problem domain can be made. Our approach aims to allow specifically tailored algorithms to be made in a more simple manner for whatever the users input domain and NDI definitions are. This idea is analogous to a real world filter and we will refer to it as the vertical approach.

In the table below a few of the most common and interesting algorithms in the NDI detection field are analyzed. Further information is provided in the Theoretical Background chapter.

| Feature                        | DHash                                                                      | Geometric Min Hash                                                      | VGG Net                                                                               |
| ------------------------------ | -------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Accuracy**                   | Low to Medium, effective for simple duplicates                             | Medium to High, captures geometric similarities                         | Very high, even on complex images                                                     |
| **Adaptability to Variations** | Limited, works on exact or nearly exact images                             | Moderate, best for images with spatial variations                       | High, can handle a wide range of variations due to training                           |
| **Approach**                   | Difference hashing for image comparison                                    | Hashing based on geometric features                                     | Convolutional Neural Network (CNN)                                                    |
| **Efficiency**                 | Very high, fast enough for real-time                                       | High for reasonably large datasets                                      | Low, computationally expensive                                                        |
| **Implementation Complexity**  | Low, simple to implement                                                   | Moderate, requires understanding of geometric hashing                   | High, requires deep learning and AI expertise                                         |
| **Dataset Domain**             | Best for straightforward, less complex image sets (e.g., documents, icons) | Effective in datasets with spatial transformations (rotations, scaling) | Diverse datasets with high detail variability (e.g., natural images, medical imaging) |

*Figure i.i: Comparative Analysis of Image Detection Techniques*

### Related work
In the paper, Bimodal Fusion of Low-Level Features and High-Level Semantic Features for Near-Duplicate Video Clip Detection \cite{bimodalfusion}, a new approach for ND video clip detection is explored that is leveraged in order to increase accuracy. This technique is called bimodal fusion and it involves combining low-level features with high-level semantic information. Inspired by this idea of combining different algorithms to extract more information, our purposed approach is a layered architecture including different algorithms at each level for NDI detection. Since this new approach provided promising results, we intend to reform and expand upon it in a different direction.

Research from Chum et al. \cite{GmH} builds upon the classic min-hash algorithm, traditionally used for efficient similarity detection by visual word hashing. They identify unique central features that give spatial and scale information which is used to perform secondary feature extraction, constructing a richer set of geometric features. This method results in a higher discriminative representation of visual words that leverages the inherent strengths of the min-hash technique. The GmH approach demonstrates substantial improvements in recall and reduces the false positive rate making it into a powerful algorithm for image processing, particularly in ND detection. Similar to GmH, our methodology begins with high-level feature extraction, followed by low level extraction. However, our approach differ in that we aim to integrate various algorithms while GmH focuses on enhancing the min-hash algorithm. This should show improved results for near-duplicate image detection. GmH may in the end be one step of our algorithm that could be used.

The work done in this article \cite{fingerprintelevation}, shows promising results by combining three distinct algorithms, dHash, SIFT and LSH model in a horizontal manner. The initial two algorithms, dHash and SIFT are used for feature extraction resulting in several hashes, these are combined into one condensed hash representation a fingerprint image. LSH receives the hash representation from previous step, where it employs a final feature extraction which put respective features into respective buckets, reduces the search space. Finally hamming distance is applied to find matching fingerprints, their approach shows a significant promise of 99.99% accuracy. Their method is similar to ours in that they utilizes the advantages of multiple algorithms, however ours diverges as we adopt a more modular approach to the integration of algorithm by using a layered architecture. We believe this offers improved flexibility to choose different algorithms which can lead to better performance and accuracy throughout differing application areas.

## Motivation
"As data expands daily, an unprecedented increase in the amount of digital data has prompted the need to upgrade data storage devices. A study conducted by the International Data Corporation (IDC), in 2012, showed that the amount of digital information produced worldwide is approximately 1.8 ZB, and by 2020 that amount would exceed 40ZB. Moreover, almost three-quarters of digital information is duplicated" \cite{lightweight-dedup}. This solution could have significant societal, ethical, and economic benefits. Further improvements in the detection of duplicate images would be an improvement in the current quality of information on the Internet, making access to the correct form more reliable and even lessening the amount of misinformation. Ethically, it complies with copyright enforcement, and hence the reduction of illegal contents on the web \cite{bimodalfusion}. Implementation for each specific domain could minimize economic waste of computing resources in a more ecologically disposed online world both for companies and individuals \cite{shandizfast}. All these considered together, this approach aims not only to allow easily tailored automatic content management, but also to ensure a more informed, properly-managed, ethically-clear, and resource-effective world is facilitated.

## Problem formulation
The central challenge addressed by this thesis revolves around the complexities and inflexibilities inherent in current methods of near-duplicate image detection. As the digital world expands, the need for effective and more easily adapted detection technologies grows as well. Current technologies often struggle to accommodate the variability in data sets and the lack of a uniform definition for what constitutes a NDI. This thesis proposes a novel approach aimed at resolving these issues.

### Knowledge Gap
Despite all the progress in image processing techniques and the current horizontal approach, a gap remains in the development of a method that can dynamically combine algorithms into a pipeline that is adapted to various data sets and definitions of near-duplicate images while remaining relatively simple to understand. The existing solutions often require complex configurations that do not lend themselves to easy customization for diverse application domains. This gap highlights the necessity for a more flexible architectural framework that can simplify the customization process of combining many algorithms for specific user requirements.

### Research Objectives
The primary objective of this research is to design and evaluate a versatile architecture that simplifies the process of developing and deploying image detection algorithms. By integrating various algorithmic layers, this architecture aims to offer a solution that can be easily adapted to meet individual and domain-specific needs. This approach hopes to bridge the gap between complex theoretical image processing algorithms and practical engineering solutions, providing a more digestible approach that supports extensive customization.

### Problem Statements
The problem can be summarized into a few main questions that guide our research and development:
1. Can a layered architecture be used to provide a flexible and reasonable way to combine image processing algorithms?
2. In what ways can the proposed framework improve the efficacy and flexibility of near-duplicate detection compared to existing methods?

## Results
We plan to evaluate our solution through design science including controlled experiments, which will be guided by methodologies seen in related work. Our results will be compared with standard metrics such as accuracy, precision, recall, and efficiency that were detailed in articles we plan on targeting as use cases. Finally, with great theoretical knowledge, we will assess the easy of use and understanding for our method compared to others.

### Evaluation Method
Direct comparisons will be made under controlled conditions using selected metrics; evaluation will be conducted with different image datasets to demonstrate the effectiveness and adaptability of this new solution in relation to results gathered from each specific article.

### Performance Metrics
The metrics used for this evaluation will include:
- F1 Score
- Computational Efficiency
- Performance across differing datasets

These metrics will be utilized to assess how this solution compares with other current solutions for each use case, as recall precision and F1 score are the most common metrics used for NDI bench marking \cite{photocluster}.

### Expected Outcomes
If we can elicit good results across diverse input domains and definitions of NDI's, then we can assert that we have created a flexible approach to combining image processing techniques. Then we can further discuss if our method is more "easy" through theoretical assessment.

## Scope/Limitation
### Development of the Layered Architecture
This involves the development of a modular framework based on a layered architecture that will allow for easy composition of various NDI detection algorithms. The approach should be flexible to allow for adaptation to specific needs within different datasets and use cases.

### Evaluation through Controlled Experiments
In this evaluation, the effectiveness and performance of our proposed idea will be compared with traditional methods of image detection, as well as any found examples of horizontal combinations of algorithms. The goal is to see if a layered approach can be highly flexible as well and remain less complex than previous approaches.

### Limitations
#### Algorithm Selection
Existing image detection algorithms form the basis of our study. Our research covers customization and combinations of these algorithms under the new architecture, but there will be no development of completely unique detection algorithms within this thesis scope.

#### Data Constraints
Given the time and resources are very limited, the experiments will be conducted with a small and limited subset of publicly available datasets. Even though datasets will be selected to be representative of the different kinds of images and settings, these will not span all conceivable scenarios.

#### Generalizability of the Results
The level of generalizability that could be accorded to the results will mainly be based on the specific algorithms and datasets used in our research. For example, although valid for indicating the potential of the framework, these results should not be generalized to all cases of image data or detection scenarios.

#### Production Deployment
The thesis does not discuss the deployment of the project into any production environment. Most issues in scalability, continuous integration, and real-time processing are acknowledged but not the focus. With these boundaries set, the aim of the thesis is to take a focused look at the proposed architecture, understanding that there are practical limits met during its research.

## Target group
The primary target group for our thesis is a broad set of people and organizations that stand to benefit from advanced, customizable NDI detection technologies. Some interested parties could include, academic researchers, software developers, digital content managers, security analysts, and social media organizations who require adaptable tools for managing large datasets of images across various domains. By addressing some of the needs of these groups, the thesis hopes to provide an idea that has many practical applications.

## Outline
This paper is structured as follows:
- Chapter 1, Introduction: This chapter acts as the introductory part to the research problem; it outlines the significance and provides objectives.
- Chapter 2, Method: Involves a description of the methodological framework, research methods, and ethical considerations that were involved in the study.
- Chapter 3, Theoretical Background: We present a comprehensive account of the theoretical foundations to our study, which take care of existing knowledge gaps.
- Chapter 4, Research Project Implementation: This chapter elaborates on the aims of developing an evaluation method used to guide the design and implementation that follows.
- Chapter 5, Results: In this chapter, we present the first results of applying the developed technique.
- Chapter 6, Analysis: Herein, the analysis of the results obtained from the application of the technique across three case studies is provided.
- Chapter 7, Discussion: This chapter will discuss the design of the framework with theory and data.
- Chapter 8, Conclusions and Future Work: The final chapter will state the main findings of this research, discuss them, and suggest possible future research.
- Chapter 9, References: Lists all the cited sources used in the study to give the readers reference to the resources for further reading.