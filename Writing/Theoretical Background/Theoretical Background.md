This section lays the foundational theories involving the integration of multiple near duplicate image processing algorithms within a layered architecture. It explores the growth of image detection technologies, and examines current known methodologies to highlight the exact contributions of this study.

## Historical and Current Technologies

The field of image processing has started off from simple image manipulation techniques, such as cropping, resizing, and color adjustments. In recent times it has grown into complex detection systems that utilize advanced techniques, including heavy artificial intelligence networks \cite{Gonzalez2018}. NDI detection, an area of critical importance within this field, has relied upon largely hash-based and feature extraction and comparison techniques, each with its inherent advantages and disadvantages. Hash based methods tend to be faster and simpler but are not able to *understand* higher level aspects of images, while feature based methods work well to understand and classify images but tend to be more complicated and more computationally expensive. In general, one method on its own cannot accommodate the complexities inherit in many NDI domains \cite{dupsinlarge}.

### Combining Approaches
![[Horizontal.png]]
*Figure i.i: Horizontal Approach Simplified Flow*

Each method has its pros and cons, it seems if there was some way to have benefits from many methods together in one algorithm, a very strong approach could be made. This leads us to the idea of fusing two or more different techniques together. As Szeliski discusses in *Computer Vision: Algorithms and Applications*, integrating multiple image processing techniques can enhance performance beyond what is achievable with isolated applications, suggesting a compounded effect from the diverse methodologies. \cite{Szeliski2010}. As of now, research in this field of NDI detection has used a horizontal approach where algorithms are used on the same layer directly together with combining hashes, features, and etc, see the figure above. For example, Dongre et al. \cite{fingerprintelevation} combined three different algorithms together, Dhash, SIFT, and LSH, in order to accomplish astonishing results when compared to previous methods. Their approach can be seen simplified in **Figure i.i**. However, this horizontal approach despite being highly accurate is also highly complex, difficult to implement, and hard to understand. This means that we do have a way of combining algorithms to bolster the performance as a whole, but the inherent complexities make it so significant understanding and expertise is needed to build it for your own use cases.

### Near Duplicate Image Philosophy
As discussed in the *Handbook of Face Recognition*, near duplicate detection is subjective, and dependent on the context and intended application \cite{face-recognition}. The need for all these different algorithms that target the same goal but try to accomplish it in different ways are indicative of this fact. A photo of a person smiling versus not smiling with the same background may not want to be identified as duplicates, but then for fingerprinting, high levels of accuracy are needed to distinguish what fingerprints are from the same person. An algorithm built for one domain may perform poorly on another. Data sets like California ND, provide a non-binary ground truth in annotations. In simple words they include multiple different peoples opinions on what images are and are not duplicates. **Figure i.i** below is a graph showing the distribution of agreement for image pairs from the 10 people. This is a great example of how varied definitions of near duplicates images may be even within the same data set \cite{californiaND}.

![[Cali-Results.png]]
*Figure i.i: Adapted Results from California-ND Article*
### Similarity Measures
An essential part of near duplicate image detection algorithms is the method used to measure similarity between images. The choice of similarity measure can have a great impact the performance of the systems, influencing both their accuracy and computational cost. Below are paraphrased overviews of a few common techniques as outlined by Murty et al. \cite{similarity-measures}.

- **Euclidean Distance**: This method is typically used in feature-based methods where the features of two images are represented as points in a vector space. The similarity is calculated as the inverse of the distance between the points.

- **Cosine Similarity**: The cosine of the angle between two vectors. This method is is useful when the scale of the vector is not important compared to the direction. This makes it nicer when working with high-dimensional data.

- **Jaccard Index**: Used with hash-based techniques, it measures similarity as the size of the intersection divided by the size of the union of different sets.

- **Hamming Distance**: Seen as a more simple approach, it is used with hash values, to measure the number of different bits between two binary strings.

## Review of Image Detection Techniques

An examination of image detection techniques available reveals many different methodologies, from simple deterministic algorithms to complex neural networks. By understanding current methods, this research can identify areas where improvements can be made and how a layered approach can address and utilize them.

To give a quick understanding a few commonly used methods and their theories are explained briefly in the following section.

### Dhash
Difference Hash (Dhash), is a well known image hashing algorithm used for very quick near-duplicate image identification. It works by converting images into gray scale, resizing them, and then comparing adjacent pixel values to generate a binary hash which is often then converted into a hexadecimal format. Then, typically the hamming distance is used as the similarity measure \cite{Dhash}.

### MinHash
MinHash (Minimum Hashing) is an algorithm used to give a quick estimate of the Jaccard similarity between two sets. This makes it suitable for tasks such as the detection of duplicate or near-duplicate images. It is founded on the concept of locality-sensitive hashing, used to reduce the dimensionality of high-dimensional data while preserving similarity by keeping dimensions with the highest variability. MinHash, builds a summary or "sketch" of a set (e.g., the characteristics of an image). Standard MinHash then takes a set intersection using the sketches as its similarity measure \cite{MinHash-TIDF}.

### Convolutional Neural Networks
Convolutional Neural Networks (CNNs) are a class of deep neural networks whose architectures are excellent in analysis of images. Their performance is one of the benchmarks across scopes of image processing. CNNs use an operation called convolution, which deals with data having a grid-like structure. Images are prime examples of this topology as they are a matrix of pixels. They work by processing images through layers that apply differing filters to detect patterns (convolution layers). Some of these layers classify the image based on the extracted features (fully connected layers). The performance of these models are heavily dependent on the depth of the system. As Krizhevsky et al. observed in their experiments with CNN's, "It is notable that our network’s performance degrades if a single convolutional layer is removed. For example, removing any of the middle layers results in a loss of about 2% for the top-1 performance of the network. So the depth really is important for achieving our results" \cite{CNNs}.

### SIFT
Scale-Invariant Feature Transform (SIFT) is a computer vision algorithm made to find and describe important parts of an image. It's performs very well when handling changes in images, such as scaling, rotation, or lighting changes. SIFT works by grabbing specific spots in an image that are considered unique and then it describes them in a way such that it can be identified in separate images. We can say these key points are "invariant to scale changes" \cite{fingerprintelevation}.

![[SIFT-Example.png]]
*Figure i.i: Sift Feature Matching Example*
## Research Gap

The gap we intend to fill is the integration of NDI detection algorithms in a layered architecture for optimized simplicity while retaining benefits associated with the use of multiple methods. The resulting artifact will be a simple framework for building NDI detection systems in this manner. A visual representation of this approach is shown in **Figure i.i** below.

![[Vertical.png]]
*Figure i.i: Vertical Approach Simplified Flow*

The concept of combining multiple algorithms into a single system is not a new idea, it has been explored in various use cases. However, its application in near duplicate image detection seems unexplored. This section reviews the theory of NDI detection algorithm integration within a layered architecture, discussing theoretical benefits and negatives.

To attempt to use inherent benefits from a layered architecture, the framework follows a few key concepts. The layers act together to form a sort of filter where at the top the fastest methods are placed and they can get progressively slower towards the bottom. This way of building makes it so easier to classify images can be removed at an earlier time so the heavier more accurate methods at the bottom do not have to do as much work. Furthermore, the methods placed before the most accurate method(s) should be tuned in such a way that they make the least amount of false positives as possible. This is due to the fact that for the images labeled as duplicates, only one will go on to the next layer while the potentially many others will stay out, not giving the strongest method a chance to  correctly classify them as not duplicates. Finally, the main driving idea behind the whole framework is that each method or layer should be a black box. Simply a list of image paths is passed in and classified image paths are returned. Thus, each layer is independent and can be moved and modified independently of the other algorithms that it may be working with.

A clear potential downside to the filtering idea is that images who are labeled as duplicates do not move on to the next layer. This means that if mislabeled as a duplicates, further layers cannot correct this mistake. In addition, the whole idea of filtering relies upon the idea that all images that are duplicates can be identified at the same layer. This assumption was to significant of a risk to accept, so to mitigate this issue, after each layer is run, a random image from each duplicate group is allowed to continue to run onto the next layer.

## Conclusion

This theoretical background helps to set the stage for development of the layered architectural framework aimed at simplifying while retaining multi-method performance for NDI detection. By building on existing knowledge and introducing our own ideas, this research contributes to theoretical and practical advancements in the NDI field.
