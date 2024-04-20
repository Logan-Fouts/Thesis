## Deep Learning-Based Feature Extraction

- **Convolutional Neural Networks (CNNs)**: CNNs are particularly effective at extracting hierarchical features from images, which can be useful for identifying near-duplicates even when images have significant variations.
- **Siamese Networks**: These networks are designed to learn similarity metrics and can be trained specifically to identify near-duplicates by comparing feature vectors.
- **Bimodal Fusion**: It emphasizes the effectiveness of combining different types of features - both low-level visual features (like color, texture, shape) and high-level semantic features (like objects, scenes, contextual information).
## Multi-Block Image Description

The multi-block approach produces multiple binary codes for each image, so they should be combined. (*G-PCA-HASH, page 7*)

1. **Aggregated Distance Measurement**:
    - **Concatenation**: One straightforward way to combine multiple binary codes is by concatenating them into a single, longer binary code. Once concatenated, the distance between two images can be computed using standard metrics like Hamming distance (which measures the number of differing bits between two binary strings). The idea here is that by combining the codes, you get a more comprehensive representation of each image, potentially leading to more accurate distance measurements.
    - **Average or Weighted Sum of Distances**: Another approach is to compute the distance for each block separately using a suitable metric (again, Hamming distance is a common choice for binary codes) and then take an average or a weighted sum of these distances. This method acknowledges that each block captures different features and treats them independently before aggregating the results.
    
2. **Hybrid or Combined Feature Distance**:
    - **Feature Fusion**: Before computing the distance, features from different blocks can be fused in a more sophisticated manner. This could involve techniques like feature weighting (where some features are given more importance than others), or more complex mathematical operations that combine features in a way that maximizes the discriminatory power of the resulting representation.
    - **Distance Fusion**: Compute distances separately for each block and then apply a fusion method to these distances. This could be a simple mathematical operation like averaging, or it could involve more complex decision-making processes, where the contribution of each block’s distance is adjusted based on its reliability or relevance to the specific task.

---
## Determining Adaptable Threshold

1. **Determining the Adaptation Criteria**: One of the main challenges is defining the criteria or conditions under which the threshold should adapt. This could be based on image content, context, or specific features. However, establishing robust and reliable criteria that work across diverse datasets is complex.
    
2. **Computational Complexity**: Adaptable thresholding techniques can be computationally more intensive than fixed thresholding, especially if they require additional processing to analyze image characteristics before adjusting the threshold.
    
3. **Overfitting**: There's a risk of overfitting, where the adaptable threshold performs very well on specific types of images or datasets but fails to generalize to broader or unseen data.
    
4. **Response to Diverse Image Alterations**: Adapting the threshold effectively for a wide range of image alterations (like scaling, cropping, color adjustments, filters, etc.) is challenging. Different alterations can require different threshold adaptations, making it difficult to develop a universally effective method.
    
5. **Real-Time Processing**: Implementing adaptable thresholding in real-time applications can be challenging due to the additional processing time required to analyze and adjust the threshold dynamically.
    
6. **Data Dependency**: The effectiveness of adaptable thresholding can be heavily dependent on the training data. If the training data is not representative of the real-world scenarios in which the algorithm will be used, the adaptability may not perform as expected.
    
7. **Balancing Sensitivity and Specificity**: Adjusting the threshold for sensitivity (true positive rate) can inadvertently affect specificity (true negative rate), leading to a trade-off between missing near-duplicates (false negatives) and incorrectly identifying non-duplicates as duplicates (false positives).
    
8. **Parameter Tuning**: Adaptable thresholding often involves multiple parameters that need to be finely tuned, which can be a time-consuming and sensitive process.
    
9. **Lack of Standard Benchmarks**: There might be a lack of standardized benchmarks or datasets to evaluate and compare adaptable thresholding techniques effectively, making it hard to gauge their performance relative to fixed thresholding methods.

## Hashing and Feature Extraction

1. **Balancing Compactness with Information Retention**: A key challenge is to design hashing algorithms that create compact representations (hash codes) without losing significant information. Achieving this balance is difficult, especially when dealing with high-dimensional data like images.
    
2. **Robustness to Image Variations**: Many hashing algorithms struggle with robustness, particularly when images undergo various transformations (like rotation, scaling, color changes) or when there are subtle differences between near-duplicates.
    
3. **Computational Efficiency**: Efficient computation is essential, especially for large-scale applications. Some advanced feature extraction and hashing algorithms can be computationally intensive, making them impractical for real-time applications or for use on devices with limited processing power.
    
4. **Generalization**: Algorithms that perform well on certain types of images or specific datasets may not generalize well to others. This limitation can be a significant hurdle in creating universally applicable hashing and feature extraction methods.
    
5. **Handling of Adversarial Attacks**: With the rise of adversarial machine learning, there's an increasing need for hashing and feature extraction algorithms to be robust against deliberate manipulations designed to fool the system.
    
6. **Selection of Features**: Deciding which features of an image to extract and how to best represent them for the purpose of hashing is a complex task. Different types of images may require different approaches, and there is no one-size-fits-all solution.
    
7. **Quantization Errors**: When converting real-valued features to binary hash codes, quantization errors can occur. These errors can significantly affect the accuracy of duplicate detection.
    
8. **Dependency on Training Data**: Machine learning-based hashing algorithms depend heavily on the quality and diversity of the training data. Biased or limited training data can lead to algorithms that do not perform well in real-world scenarios.
    
9. **Scalability**: As the size of image databases continues to grow, scalability becomes a concern. Algorithms need to handle an increasing amount of data efficiently without a loss in performance.

## Geometric min hash: 
main algorithm to determine feature extraction is divided into 2 parts, central and secondary features. Central features is normal min-hash but unique visual words are used (unique features of image). With this unique list of features spatial and scale information is obtained which is used to guide the selection of the secondary features. We can think of it like we zoom in into the main features that was extracted and produce a more clooser look at these regions to produce a more detailed feature list. This would result in a more richer hash which is used for comparision. 

[See MinHash Notes](MinHash.md)

---
#Degree-Project
#Software-Technology
#Algorithms 