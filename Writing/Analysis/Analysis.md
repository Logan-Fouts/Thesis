## Comparative Analysis

This section compares the results obtained from our layered architecture framework with existing studies on similar datasets. We focus on comparing the performance metrics such as precision, recall, F1-score, and accuracy.

### California-ND Dataset

#### Existing Benchmark

Eshkol et al. \cite{cali-comparative} utilized the MPEG-7 Color Structure Descriptor for image detection on the California-ND dataset, yielding the following performance metrics:

- **Number of images**: 701
- **Precision:** 54.4%
- **Recall:** 78.2%
- **F1-Score:** 64.16%

#### Our Framework Results

In contrast, our layered approach using a combination of Phash, Dhash, SIFT, and VGG algorithms produced notably higher performance metrics:

- **Number of images**: 701
- **Precision:** Ranges from 98% to 100% based on permutation configurations
- **Recall:** Consistently above 84%
- **F1-Score:** Typically exceeds 90%

The stark improvement in precision and F1-score illustrates the effectiveness of our multi-method, layered architecture in handling the complex variations within the California-ND dataset. The layered approach not only improves accuracy but also maintains high recall rates, demonstrating robustness across varied image conditions.

### SOCOFing Dataset

#### Existing Benchmark

The research on the SOCOFing dataset that we are comparing against uses the horizontal approach, where multiple algorithms operate at the same level, combining their outputs to enhance the detection process. These studies have achieved high performance, often reaching perfect metrics under controlled conditions. The exact results we are comparing against are as follows:

- **Number of images**: 17,000
- **Precision**: 1
- **Recall**: 1
- **F1-Score**: 1
- **Accuracy**: 1
- **Elapsed Time**: 50 minutes

#### Our Framework Results

Our experiments on the SOCOFing dataset, employing a vertical layered architecture framework, yielded the following results for a size of 3000 images:

- **Number of images**: 3,000
- **Precision**: 0.9481
- **Recall**: 0.9821
- **F1-Score**: 0.9648
- **Accuracy**: 0.9320
- **Elapsed Time**: 3 minutes

---

### Empirical Comparative Discussion

Our empirical observations, made using our vertical layered architecture, argue that this approach can give competitive results when compared to horizontal approaches, specifically in the context of the SOCOFing dataset. Moreover, it can be seen that the vertical approach has many advantages over the multi-method approach because it significantly outperforms the more standard approach used on the California-ND dataset. The empirical comparison, therefore, shows the advantages and disadvantages of each approach.

To discuss further, data seen in our results supports the conclusion that horizontal approaches are capable of delivering the maximal performance but at the cost of complex and therefore less flexible configurations. On the other hand, the vertical approach, though without the peak performance seen in the horizontal method, gives comparable performance, easy integration, and management of various algorithms with the ability to be highly adaptable to specific operational needs.

This flexibility is particularly important when rapid deployment, system modifiability, and operational simplicity are needed. The evidence suggests that vertical architecture with the framework as a tool to build it, can offer a ambitious performance appropriate for ever changing real-world applications, especially where systems require updating often to adapt to new data types or detection tasks or where simpler detection system building is desired.

### Theoretical Comparative Discussion

After researching the vertical method in comparison to the horizontal approach, we would like to present our theoretical understanding of both systems.

#### Horizontal Method

**Definition and Architecture:**

The horizontal method defines the relation of different algorithms at the same level. Their output is then aggregated. The usual methods to handle this are feature concatenation, ensemble averaging, or voting systems.

**Strengths:**

1. **Performance Optimization:** By using multiple algorithms simultaneously, horizontal methods can optimize for the best possible performance, achieving high accuracy and efficiency. The combination of outputs directly seems to allow for a greater understanding of an image.

2. **Image Understanding and Reliability:** This approach does not have the issue where some layers may never touch certain images if they are processed incorrectly before. Each method creates and combines an output for every image, thereby increasing the system's reliability.

**Weaknesses:**

1. **Complexity:** Managing multiple algorithms and how they are combined can significantly increase the system's complexity. This requires a deep understanding of each selected method's internal workings.

3. **Scalability Issues:** When new algorithms are needed and added, this would require significant reconfiguration of the system, making it more difficult to modify and adapt.

#### Vertical Method

**Definition and Architecture:**

Our vertical method structures the system as a set of layers, where each layer applies an algorithm. The output of one layer feeds directly into the next as a list of unclassified images. This allows for refinement of results as images are filtered out.

**Strengths:**

1. **Modularity and Flexibility:** Vertical architectures are inherently modular, making it easier to add or modify layers without needing to reconfigure the entire system.

2. **Ease of Implementation and Maintenance:** Since the layers are black boxes, each can be implemented and optimized independently, simplifying development and maintenance.

3. **Adaptability:** Vertical methods, since more modular, can adapt easier to different types of data or changing requirements, as changes can be made to specific layers instead of the whole system.

**Weaknesses:**

1. **Error Propagation:** Errors in early layers can propagate through to the rest, in worst cases potentially compounding and destroying the overall system accuracy. This is mitigated to an extent by passing images from each duplicate group to the next layer for further processing.

2. **Understanding of Images:** Since layers are separate from each other, they can not directly benefits from the understanding of the previous layers. This results in the layered approach performing in our results slightly worse than the horizontal approach.

#### Comparative Theoretical Implications

There are good reasons for choosing either horizontal or vertical methods, depending on the needs and constraints of the application. Ideal applications for horizontal methods are those where very high performance is critical and implementation time and maintenance are not a significant concern. In contrast, vertical methods are more flexible and easier to manage, being more appropriate for applications requiring frequent alteration or adaptation to new data types or processing techniques. Although potentially less performative, the vertical approach and the framework provide a structured way to easily integrate diverse algorithms and adapt to changes.