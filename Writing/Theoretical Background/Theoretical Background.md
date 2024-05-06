This section lays the foundational theories involving the integration of multiple near duplicate image processing algorithms within a layered architecture. It explores the growth of image detection technologies, and examines current known methodologies to highlight the exact contributions of this study.

## Historical and Current Technologies

The field of image processing has started off from simple image manipulation techniques, such as cropping, resizing, and color adjustments. In recent times it has grown into complex detection systems that utilize advanced techniques, including heavy artificial intelligence \cite{Gonzalez2018}. Near-duplicate image detection, an area of critical importance within this field, has relied upon mostly hash-based and feature comparison techniques, each with its inherent advantages and disadvantages. Hash based methods tend to be faster and simpler but are not able to understand higher level aspects of images, while feature based methods work well the understand and classify images but are more complicated and computationally expensive.

### Combining Approaches
As can be seen from a brief list of the pros and cons for each method, it seems if there was some way to get benefits from both methods together in one algorithm, then we could potentially have a very strong method. This leads us to the idea of fusing two or more different techniques together. As Szeliski discusses in *Computer Vision: Algorithms and Applications*, integrating multiple image processing techniques can enhance performance beyond what is achievable with isolated applications, suggesting a compounded effect from the diverse methodologies. \cite{Szeliski2010}. As of now, research in this field has used the horizontal approach where algorithms are used on the same layer directly together. For example, in this article \cite{fingerprintelevation}, they combined three different algorithms together, Dhash, SIFT, and LSH, in order to accomplish astonishing results when they compared to previous more traditional methods. However, this horizontal approach is highly complex, difficult to implement, and hard to understand. This means that we do have a way of combining algorithms to bolster the performance as a whole, but the inherent complexities make it so significant understanding and expertise is needed to build it for your own use case. 

### Near Duplicate Image Philosophy
As discussed in the *Handbook of Face Recognition*, near duplicate detection is subjective, dependent on the context and intended application \cite{face-recognition}. The need for all these different algorithms that target the same goal but try accomplish it in different ways and with different criteria for success are indicative of this fact. Depending on the use case, a photo of a person smiling versus not smiling with the same background may not want to be identified as duplicates, but then for fingerprinting, high levels of accuracy are needed to distinguish what fingerprints are the same. An algorithm built for one domain may perform poorly on the other.

### Similarity Measures
An essential part of near duplicate image detection algorithms is the method used to measure similarity between images. The choice of similarity measure can have a great impact the performance of the systems, influencing both their accuracy and computational cost. Below are descriptions of a few of the most common.

- **Euclidean Distance**: This method is typically used in feature-based methods where the features of two images are represented as points in a vector space. The similarity is calculated as the inverse of the distance between the points.

- **Cosine Similarity**: The cosine of the angle between two vectors. This method is is useful when the scale of the vector is not important compared to the direction. This makes it nicer when working with high-dimensional data.

- **Jaccard Index**: Used with hash-based techniques, it measures similarity as the size of the intersection divided by the size of the union of different sets.

- **Hamming Distance**: Seen as a more simple approach, it is used with hash values, to measure the number of different bits between two binary strings.

## Review of Image Detection Techniques

> [!NOTE] Notes about this section
> -  Not sure if this section is also maybe too detailed? I did try to limit it a bit but I am not sure.

An examination of image detection techniques available reveals many different methodologies, from simple deterministic algorithms to complex neural networks. Each with trade-offs in terms of accuracy, efficiency, flexibility, and/or scalability. By understanding current methods, this research can identify areas where improvements can be made and how a layered approach can address them.

To give a quick understanding of the most commonly used methods and their theories, a description of a few will be made in the following section.

### Dhash
Difference Hash (Dhash), is a well known image hashing algorithm used for very quick near-duplicate image identification. It works by converting images into gray scale, resizing them, and then comparing adjacent pixel values to generate a binary hash which is often then converted into a hexadecimal  format.

### MinHash
MinHash (Minimum Hashing) is an algorithm used to give a quick estimate of the Jaccard similarity between two sets. This makes it suitable for tasks such as the detection of duplicate or near-duplicate images. It is founded on the concept of locality-sensitive hashing, used to reduce the dimensionality of high-dimensional data while preserving similarity by keeping dimensions where the highest variability is. MinHash, builds a summary or "sketch" of a set (e.g., the characteristics of an image).

### Convolutional Neural Networks
Convolutional Neural Networks (CNNs) are a class of deep neural networks whose architectures are excellent in analysis of images. Their performance is one of the benchmarks across scopes of image processing. CNNs use an operation called convolution, which deals with data having a grid-like structure. Images are prime examples of this topology as they are a matrix of pixels. They work by processing images through layers that apply differing filters to detect patterns (convolution layers). Some of these layers classify the image based on the extracted features (fully connected layers).

### SIFT
Scale-Invariant Feature Transform (SIFT) is a computer vision algorithm made to find and describe important parts of an image. It's performs very well when handling changes in images, such as scaling, rotation, or lighting changes. SIFT works by grabbing specific spots in an image that are considered unique and then it describes them in a way such that it doesn't change, even if the image does.

![[SIFT-Example.png]]

## Integration of Algorithms in Layered Architectures

The concept of combining multiple algorithms into a single system is not a new idea, it has been explored in various use cases. However, its application in near duplicate image detection seems unexplored. This section reviews the theory of algorithm integration within a layered architecture, discussing potential benefits and negatives.

To attempt to use the benefits of a layered architecture in general the framework follows a few key concepts. The layers act together to form a sort of filter where at the top the fastest methods are placed and they can get progressively slower towards the bottom. This way of building makes it so easier to classify images can be removed at an earlier time so that the heavier more accurate methods at the bottom do not have to do nearly as much work. Furthermore, the methods placed before the most accurate method(s) should be tuned in such a way that they make the least amount of false positives as possible. This is due to the fact that for the images labeled as duplicates, only one will go on to the next layer while the potentially many others will stay out, not giving the strongest method a chance to  correctly classify them as not duplicates. Finally, the main driving idea behind the whole framework is that each method or layer should be a black box. Simply a list of image paths is passed in and classified image paths are returned. Thus, each layer is independent and can be moved and modified independently of the other algorithms that it may be working together with.

A clear potential downside to the filtering idea is however, the way that images that are labeled as duplicates do not move on to the next layer mean that if mislabeled as a duplicate further layers cannot correct this mistake. In addition, the whole idea of filtering to a certain extent relies upon the idea that images that are in fact duplicates can be identified at the same layer. This assumption felt like to significant of a risk to blindly accept, so to mitigate this issue, after each layer is run, a random image from each duplicate group is allowed to continue to run onto the next layer.
## Gap in Existing Research

> [!TODO] 

*Despite considerable advancements in image processing, the integration of disparate algorithms into a unified framework remains a significant challenge. Current solutions often lack flexibility and are not optimized for the varying definitions and conditions of near-duplicate images across different datasets. This research identifies a clear gap in the ability to dynamically adapt image detection techniques to specific user requirements and proposes a new architecture designed to bridge this gap.*

## Conclusion

> [!TODO] 

*This theoretical background sets the stage for the development and implementation of a layered architectural framework aimed at revolutionizing near-duplicate image detection. By building on existing knowledge and introducing innovative integration strategies, this research contributes to both the theoretical and practical advancements in image processing technologies.*
