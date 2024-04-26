## Data
[[Phash, Dhash, SIFT]]
## Graphs

![[Metrics_Graph.png]]

![[Time_Graph.png]]

---

Comparing the individual performances of algorithms to the layered architecture proves that the individual algorithms integrated into the layered architecture enhance the system's capabilities of handling the datasets. Each unique strength is brought in by the algorithms—DHash, Phase, and SIFT. When these algorithms are forced to operate together, at the same time, they operate in silos, presenting different inefficiencies and accuracies concerning the diversity in size of the datasets.

For example, DHash provides good performance for small datasets because it can produce the perfect result in that case with far fewer numbers. However, when reaching the large scale of the dataset size, the accuracy falls off with DHash. Therefore, one can observe the performance drop at scale. As was mentioned above, at the very beginning, such time efficiency is decent but over time deteriorates with the growth of complexity and volume of the data.

On the other hand, Phash may present a degree of resilience in some aspects of image similarity detection based on its very underlying mechanisms of being. It, however, is still unfortunately very susceptible to the same challenges of scaling and a consistent accuracy drawback with larger datasets that have been used in this project. The feature extraction used the fully explained standalone SIFT algorithm, which may not be efficient for use when running computations on big data in terms of time.

However, when all these algorithms are combined into a layered structure, a synergetic effect can occur. Combining the strengths of the algorithms will yield a sound system that maintains good performance at all sizes. It portrays the adaptability of the layered architecture.

Further, the processing time was a bit longer, but not such to an extent as in the case of the heavy algorithm SIFT by itself. This therefore, means that the performance obtained from the layered architecture is retained not only in smaller datasets but also displayed in large, complex datasets. It is a good illustration of how different powers and capabilities of algorithms, when combined, often yield much better results than any lone algorithm acting on its own. This behavior can be understood to mean that different combinations of algorithms, despite their own inflexibilities, using this layered approach should be able to be adapted to vastly different use cases.  

Next it would be interesting to explore how the system can be further optimized through parameter tuning or different algorithm choices and to consider the potential enhancements that could be seen from deploying it on more powerful hardware.

---

> [!NOTE] Why we slower
> -  There hardware:
> 	- Nvidia A100 80GB GPU, 128 GB Ram, and Intel Xenon Scalable CPU with 8 virtual core
> - My hardware:
> 	- Nvidia GTX 1080 GPU, 16 GB Ram, and Intel i7 8700k