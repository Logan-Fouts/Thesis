## Semantic Near-Duplicate Image Detection Using Deep Learning And Bimodal Fusion
----
~~It seems most are concerned not with getting the highest accuracy, but in efficiency in computation, storage, and retrieval.~~
### Potential Layers
1. d-hash
2. min-hash
3. VGG
### Hypothesis
~~Using deep learning models together with Multi-Modal Fusion techniques we can increase upon the accuracy of current techniques such as min-hash, PCA, and etc.~~
### Define Near Duplicate Images
Near duplicate images are images that are either exact copies or very similar to each other with minimal differences. Some differences could be as follows:
- Image transformations- Alterations made to an image through some sort of software
- Perspective changes
- Lighting
- ~~And other changes that are prevalent in real life like weather/environment~~
### Potential Models
[Good Article](https://spotintelligence.com/2023/11/04/feature-extraction/#What_is_Feature_Extraction_in_Machine_Learning)
-  VGG, ResNet, and Inception
### What Do I Hope To Discover or Test?
We are not looking to create a faster necessarily method but a more reliable accurate method.
- One thing we could do is redefine exactly what we are considering a near duplicate image. Everything I have found defines it as image transformations, but this is not what I want to do. Instead I want different pictures that are similar where small things such as angle or whatnot are a bit different.
- The Research Gap
	- Deep learning Semantic Hashing with Multi modal fusion
		- Hashing techniques that focus on semantic similarity rather than pixel-level similarity, enabling the detection of duplicates that are contextually similar but may not be visually identical.
		- Traditional methods often rely heavily on visual features and simple similarity metrics, which may not fully capture the semantic essence or the contextual information of images. Your research aims to fill the gap in deep semantic understanding and interpretation of images, moving beyond purely visual similarities to recognize semantically related, near-duplicate images.
### Application Fields
- Forensics for law enforcement
- Copyright enforcement
- Social media
- Image storage libraries/software
### Research Gap
#### Min-Hash Technique
- **Research Gap**: Min-Hash efficiently estimates set similarity by focusing on the presence or absence of features, making it well-suited for identifying exact or near-exact duplicates. However, this method primarily captures surface-level similarities and might not delve into the deeper semantic meaning or context of the images. Your approach, by leveraging deep learning, aims to understand and interpret the underlying semantic content and relationships within images. This allows for the detection of images that are not just visually similar but are semantically related, addressing a significant gap in capturing the essence of what makes images truly near-duplicates beyond mere visual overlap.
    
- **Multimodal Data Integration**: The Min-Hash technique does not inherently accommodate multimodal data sources. It operates on a single data modality, typically visual features represented as a set of hashed values. In contrast, your method proposes to utilize bimodal or multimodal fusion, integrating various types of information (e.g., visual content along with textual annotations or metadata) to enhance the accuracy and depth of near-duplicate detection. This approach could significantly improve the detection process by incorporating additional contextual and semantic cues that Min-Hash alone might overlook.
#### Principal Component Analysis Hashing (PCAH)

- **Research Gap**: PCAH focuses on reducing dimensionality to improve computational efficiency but may not capture complex, non-linear relationships in image data. Your approach, emphasizing deep semantic understanding and bimodal fusion, could better capture these complex relationships and offer more nuanced near-duplicate detection.

#### Spectral Hashing (SH)

- **Research Gap**: SH is designed to preserve similarity in the Hamming space, focusing on efficiency in large-scale datasets. However, it might not fully account for semantic similarities or the context of images. Your deep learning-based method could enhance semantic detection capabilities, offering improvements in accurately identifying semantically related near-duplicates.

#### Locality-Sensitive Hashing (LSH)

- **Research Gap**: LSH excels in approximate nearest neighbor search but may not explicitly address semantic similarities or leverage multimodal data for near-duplicate detection. Your work could fill gaps in semantic analysis and multimodal integration, providing a more holistic approach to identifying near-duplicates.

#### Iterative Quantization (ITQ)

- **Research Gap**: ITQ aims to improve the binary coding of high-dimensional data, offering efficient retrieval. While ITQ enhances quantization for hashing, it doesn't inherently focus on semantic content or the fusion of different data types. Your approach introduces an emphasis on deep learning and bimodal fusion to capture and utilize semantic content more effectively.
### Related Stuff
- Google photos has exact duplicate detection, not near duplicate detection [Here](https://sites.google.com/site/picasaresources/google-photos-1/how-to-remove-duplicates-in-google-photos)
### Notes
- Simply the goal is the answer true or false if two images are considered **perceptually** to be duplicates. This is done by finding the best suited threshold between the two possibilities.
- "Image description should be as **compact** as possible for storage efficiency, and duplicate detection needs to be **very fast** and **accurate** with light memory usage." (*G-PCA-HASH, page 1*)
- Current state of the art methods include PCAH, SH, LSH, and ITQ.
- Typical **FAR** (false alarm rate) should be around 0.01 --> 0.1
- We want to retain high percentage of the **energy of the data**
	- The term "energy of the data" refers to the amount of variance or information from the original dataset that is captured and retained in the reduced or transformed dataset.
	- The *G-PCA-HASH* retained around 78.9% --> 87.4%
- Potential Data Sets
	- "Copydays, Peekaboom, Mirflickr, and Tiny images." (*G-PCA-HASH, page 8*)
	- University of Kentucky data set (https://www.robots.ox.ac.uk/~vgg/publications/2008/Chum08a/chum08a.pdf)
	- California ND data set (https://link.springer.com/article/10.1007/s11831-020-09400-w)

### Methodology
#### Before and During
1. Gather test image data-set
2. Processes images into hash-code/binary-representation
	- Image compression potential ideas ([[Detailed Algorithm Notes]])
		- "An m-bit binary coder, h : R^n → {0, 1}^m, of a n-dimensional vector" (*G-PCA-HASH, page 3*)
		- Some form of deep-learning
		- Multi-block Image Description  
3. Determine duplicate threshold
4.  Exhaustive check all images for duplicates
#### After
5. Performance evaluation
6. Document Findings

## References
- [[Revisiting Gist-PCA Hashing for Near Duplicate Image Detection.pdf]] (*G-PCA-HASH*)
---
#Degree-Project
#Software-Technology