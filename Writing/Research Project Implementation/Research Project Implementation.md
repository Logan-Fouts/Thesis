This chapter aims to unfold the implementation of our new framework as well as the steps took to evaluate and compare the effectiveness of our multi-method vertical approach for NDI detection. The objective of our implementation was to create a robust and simple architecture by which the integration of algorithms could be performed effectively to detect ND from datasets.

### Implementation of Existing NDI Detection Algorithms

#### Selection of Algorithms
Algorithms who are readily available in libraries and who are also effective in their techniques were selected as the tools for the framework. The libraries used are imagehash \cite{imhash}, cv2 \cite{opencv}, and tensor flow \cite{tensorflow}. The following are the algorithms we are using.

- **Dhash (Difference Hash)**: Difference in brightness of neighboring pixels.
- **Phash (Perceptual Hash)**: Phash allows for visual examination of image contents with the intention of finding relations between images in a more human vision like approach.
- **Ahash (Average Hash)**: Finds duplicates through comparison of averages in pixel intensity.
- **SIFT (Scale-Invariant Feature Transform)**: Identification and description of local features in images.
- **VGG (Visual Geometry Group)**: Deep learning for recognizing patterns in images. Classification layer is left out.
- **SSIM (Structural Similarity Index Measure)**: Structural similarity measure of two images.

### Framework Design

![[component diagram.png]]
*Figure i.i: Component diagram of the framework architecture \cite{umlComponentDiagrams}*

The framework is written in python due to its use in machine learning. It is structured around classes that allow for flexible integration of various image detection algorithms. A detailed component diagram in **Figure i.i** gives a visual as to what the system looks like. The main components include:

- **Algorithms inside python classes**: Each detection algorithm is encapsulated in a Python class that provides a `process` function. This function accepts a list of image paths and updates two lists. One for images labeled as duplicates and another for those not labeled yet. This allows each algorithm to act as a black box where we do not need to know or really care what is going on inside. We are only concerned with input and output. These layers may or may not have parallel processing utilized inside of them.
- **Initialization parameters**: Each algorithm class constructor (`__init__`) takes named arguments as parameters to the algorithm, allowing for easy hyper parameter tuning of each algorithm. Default values are set in case no parameters are provided by the user. These values were selected to be middle of the road options.
- **Compatibility layer**: This wraps each algorithmic layer, ensuring methods are callable in the same way between all the algorithms. Methods like run, get_results, print_results, etc are included in the wrapper. The goal is to abstract away complexities from the end user.
- **Layered architecture**: This is the most important feature of the implementation. Algorithms are passed in as a list of layers, and each is subsequently wrapped in the compatibility layer before use. In a filter like way, processes are completed layer by layer, sending selected images from one layer to another, therefore progressively refining the two labeled sets of image paths. All of this is done inside its own class. This class also utilizes a union find data structure to clean the sets between runs to ensure we do not process more duplicates then necessary. From the groups of related duplicates 1 image from each is selected to continue on to minimize inherit issues in the layered methodology.
- **Accuracy calculator**: This is an integrated component within the architecture, computing the accuracy at the end of the processing. This is passed to the layered architecture as a method since each domain has its own specific requirements for calculating the metrics. The results from this method are then used to calculate the precision, recall, f1 score, and accuracy.
- **Organize images**: The layered architecture allows for the automatic organization of processed images to specific group folders based on the classification of the images. This is done by grouping related sets together via the union find data structure implementation.
- **Error handling**: Throughout the program in areas where errors could occur, proper handling is done to gracefully resolve the issue.
- **Easy expansion**: Due to the black box idea for each layer, plunging in of other algorithms directly or even through external APIs should be easy to implement. The greater the amount and the more advanced the algorithms the better the framework may get. This is an important detail, as me and my partner had limited time. So we are here to show if the simple layered approach works well for NDI detection with the algorithms we had on hand, not to see the real end game potential possible when combined with more advanced algorithms that are out there.

No graphical interface has been implemented but all a user needs to do to build with this approach is import the required modules, instantiate and put them into a list, and provide the desired path to images folder. An example can be seen in **Figure i.i.**
```python
# Import modules
from Layers.layers import Layers
from Phash.phash import Phash
from SURF.surf import SURF
from SIFT.sift import SIFT

image_paths = get_image_paths(path)

layers = [Phash(), SURF(), SIFT()]
layered_architecture = Layers(raw_layers=layers, accuracy_calculator=None)

layered_architecture.run(test_paths)
```
*Figure i.i: Example setup of an algorithmic suite*

> [!TODO] Permutations/Median ?
> - Henry knows more about this then I do, so maybe you can write a section here about how you did it and whatnot.
> 
> - Also anything else Henry wrote like cali median stuff
> 
> - Maybe Logan need to write about union find a bit

### Dataset Utilization for Demonstration
Two different datasets were used to show the abilities of the new framework. These are the SOCOFing and California-ND datasets.

- **Recursive Image Collection**: The images are collected recursively from the specified directory so as to form a comprehensive list of all image paths for processing. 
- **Subset Selection**: For illustration purposes and due to constraints, random subsets of these images have been selected to illustrate the capabilities of our framework when tested under the same conditions as the articles we plan on comparing against.
- **Exhaustive testing of permutations**: Using a training subset of the data, all combination of algorithms are tested. The suite with the best recorded metrics is selected for further optimization by hand.
- **Manual Tuning**: The selected suite of algorithms are tuned by hand on the training subset of data to achieve a balance between accuracy and time taken.
- **Final suites tested**: Once tuned each suite is ran on increasing larger and larger testing sets of the data. The simple code can be seen in Figure i.i below.

```python
 for i in range(300, 3300, 300):
    run_experiment(i, "DataSet")
```
*Figure i.i: Example of running increasingly large experiments*

- **Individual method measurement**: From the selected suite of algorithmic layers each algorithm is run by itself and its result are recorded to allow for better discussion. 

#### Data Collection and Analysis
All experiments were conducted with the following hardware and software setup: 11th Gen Intel i7-1165G7 CPU, 16 GB RAM, and Linux kernel 6.8.9-arch1-1. A collection of outputs of the automated testing is maintained in text files. Each includes used algorithms with presets and the processing outcomes with execution times. These files are used for the comparative analysis and creation of relevant graphs using matplotlib \cite{mpl} in order to provide insightful visuals. This includes both the permutation and final tests.