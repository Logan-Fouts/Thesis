[[Project Idea]]
## Research Article Notes

### Revisiting Gist-PCA Hashing for Near Duplicate Image Detection

- Early duplicate image detectors were based on the hashing based approaches adapted from document processing. While image search engines retrieve similar or relevant images in a ranked order by measuring distances in high-dimensional feature space, the near duplicate image detectors have been developed to find perceptually/visually identical images by counting hash key collisions between binary codes
- Recently learning based approaches have been getting more attention for approximate nearest neighbor search because it represents images or high dimensionality feature vectors as compact binary codes while preserving their neighborhood structure and/or relative distances. 
  - These approaches depend on PCA for dimensionality reduction and then encode the projected vectors into binary codes using various quantization techniques. 
    - Quantization refers to the conversion of these vectors into a binary format.
- Here they are doing image-to-image transformation near duplicate detection. My goal is non image-to-image near duplicate detection.

### Bimodal fusion of low-level visual features and high-level semantic features for near-duplicate video clip detection

- **Bimodal Fusion**: It emphasizes the effectiveness of combining different types of features - both low-level visual features (like color, texture, shape) and high-level semantic features (like objects, scenes, contextual information). This approach can enhance the accuracy of duplicate detection.

---

\#Degree-Project
#Software-Technology