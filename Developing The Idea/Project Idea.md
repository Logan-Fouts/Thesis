## Semantic Near-Duplicate Image Detection Using Deep Learning And Bimodal Fusion

----
### What Do I Hope To Discover or Test?
- Adaptable threshold techniques
	- Develop an adaptive threshold approach that happens during the hashing process itself.
- New Algorithms for hashing and feature extraction
	- Hybrid hashing using strengths of current approaches and the strengths of deep learning.
- Semantic Hashing
	- Hashing techniques that focus on semantic similarity rather than pixel-level similarity, enabling the detection of duplicates that are contextually similar but may not be visually identical.

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