## Research Project

![[DSRM.png]]
*Figure i.i: Our DSRM Flow Chart Heavily Influenced by the DSMR article \cite{dsmr}*
### Overview of Design Science
For out thesis we will use the design science research methodology (DSRM). It is aimed at the creation and evaluation of IT artifacts intended to solve identified problems, offering a rigorous process to design, evaluate, and communicate the artifacts and their attributes \cite{dsmr}. This description closely fits our needs as we would like to design a framework which would be an artifact. Unlike purely empirical methods, such as the observational study, that hope to understand through observation, design science aims to address issues through the design and refinement of practical solutions. The DSRM process has six main steps: problem identification and motivation, definition of the objectives for a solution, design and development, demonstration, evaluation, and communication. This structured approach ensures comprehensive and proper treatment of the research and development of the concrete solutions \cite{dsmr}.

### 1. Problem Identification
The challenge we address is within the definition and identification of near duplicate images (NDI). Depending on the scenario and who you are asking, what exactly defines two images to be near duplicates can change vastly. After reviewing related NDI literature this phenomena is discussed often, a great example is in the classification of images in the \cite{californiaND} paper. Hence, there is a need for a method that could allow easy adaptation and configuration for this seemingly infinite range of situations.

The current methods lack flexibility, rely upon a horizontal approach of combining methods, and/or are simply too computationally expensive to be feasibly ran on integrated or even consumer hardware. The horizontal approach is the closest to our idea, and it is very effective when built correctly to address the issues of complex NDI definitions and scenarios. This can be seen in this paper \cite{GmH}, and furthermore in this paper as well \cite{fingerprintelevation}. Despite the impressive performance, this approach is highly complex requiring deep knowledge in the area therefore, building your own tailored system by combining and tuning methods in this way proves to be quite difficult.

### 2. Objectives of a Solution
Since the combination of many methods shows promise, the goal for our thesis is a modular architecture that allows for integration of various algorithms for NDI detection. This architecture aims to enhance flexibility by optimizing simplicity all while maintaining the efficacy of multi-method approaches.

### 3. Design and Development
We propose a layered architecture approach where different algorithms are placed as an individual layers and are tuned individually first, then refined while combined. The use of many methods allows for better performance much like the horizontal approach, while also providing improvements in terms of easy adaptability/flexibility.

```python
def run_experiments(dataset, size):
    permutation_sets = permutations(list_of_algorithms, size)
    for set in permutation_sets:
        layered = Layers(set)
        results = layered.experiment(dataset)
```

### 4. Demonstration
The prototype will be shown running two vastly different datasets: the Sokoto Coventry Fingerprint Dataset (SOCOFing) and the California-ND. Initially, controlled experiments will be run on "training" subsets of the data for each dataset. This involves tuning individual layers and running automated testing of permutations (combinations) to determine the direction of the optimal configuration. After a configuration is decided upon, then each layer will be tuned by hand to further improve performance. This could mean in terms of execution time or accuracy, but for our situation a balance of the two is targeted in both datasets.

#### Details About The Datasets

![[photo-collage fingers.png]]
*Figure i.i: Example of fingerprints from SOCOFing dataset*

![[photo-collage California.png]]
*Figure i.i: Example of images from California-ND dataset*

SOCOFing \cite{shehu2018sokoto} was created from 600 participants capturing each of their 10 fingers building a subset of 55,273 images in total. The SOCOFing is split into real, easy, medium and hard subsets with a resolution of 96x103 pixels. We will use a subset of the easy section for our demonstration and evaluation due to resource constraints. This dataset is great to be able to capture high detail differences in what are all very similar images. The California-ND data set \cite{californiaND}  contains 701 images from a real user's holiday photo collection with resolution of 1024×768. The target of the data was to represent a real personal photo collection. Participants of 10 has individually created annotations making California a good set for detecting real life near image duplication. 

### 5. Evaluation
Our evaluation will entail the use of both empirical and theoretical argument. The prototype will be compared against traditional and horizontal ND detection methods using metrics like precision, recall, runtime, and resource usage. Comparative analysis will aim to highlight potential advantages and disadvantages of our approach. Furthermore, a detailed theoretical assessment of our vertical approach compared to the horizontal will be conducted. This will provide insight into the less easily proven with data aspects of each. Mainly ease of use/implementation and complexity will be explored.

### 6. Communication
Findings will be documented and shared through scholarly publications in the form of the thesis paper. Additionally, all resources, code, and documentation developed throughout will be available on [GitHub](https://github.com/Logan-Fouts/Thesis).

## Reliability and Validity
Reliability in research refers to the consistency of the results obtained from the study. It explores whether other researchers can produce similar results under the same conditions, using the same methods. In our study, we aim to document in detail all relevant testing and experimentation information in order to allow for others to run them for themselves.

Validity, relates to the accuracy and legitimacy of our findings. To aid in the validity of our study, we engage in rigorous exhaustive testing to find a base algorithm, then tune the layers to fit the domain, maximizing our algorithms ability to identify near duplicate images while limiting wrong classifications.
### Addressing Reliability and Validity Issues
- **Threats to Reliability**: 
	- The main potential threat to reliability comes from non-uniform test environments or inconsistent data sets. To mitigate this, we will use subsets of defined image sets for each algorithm and make sure to have consistent testing conditions across all experiments.
- **Threats to Validity**: 
	- One threat to validity in our study could come from the subjective definition of what constitutes a "near duplicate" image. To deal with this, we will use clearly defined and specific criteria for what constitutes near duplicity for each algorithm targeting a certain domain. When possible we can use a specific example of the ground truth from the articles.
	- Most likely the largest threat to validity would be the use of subsets of the original experiment data due to a lack of compute and time resources. This could lead to skewed or invalid results depending on how the subset is taken. To help minimize this issue and allow for more generalize-ability, subsets will be chosen at random. However, the fact that only a subset is being taken will regardless limit the validity of our results.
	- Quality of algorithm implementation could be a risk for our validity. Assuming one algorithm is implemented far better then another, this would mean a chance that our results would be skewed against the un-optimized algorithm versus optimized ones. This threat is mitigated since the majority of the algorithms we are using are implemented heavily using well known libraries. Furthermore, since we know generally how an algorithm should behave on a data set, we can look out for any irregularities in results.
	- Algorithm Configuration Consistency could be a threat to our validity. Different configurations of the algorithms with different parameters could affect results. To avoid this we will ensure that all algorithms are configured with standard parameters across all test cases and document any changes to account for their impact on our results.

## Ethical Considerations
For our study, we have made the following ethical considerations:

- **Confidentiality**: If the layers were put into production many security issues would need to be ironed out such as securely storing images both in the data bases as well as during processing. However, we do not intend for this to be put into production, simply we are exploring if the idea of layers of image processing is a viable option to allow for greater flexibility as well as reaping the benefits of the filter like flow.

- **Sampling and Bias**: The choice of images and datasets needs to be assessed to avoid biases that could skew the results. For instance, diverse different datasets will be chosen to represent real world scenarios and avoid over fitting, as well as the highlight the flexibility of the layered approach.

- **Risk of Harm**: Our research involves the processing of images and does not entail any human participation, so harm is not a concern.

- **Participation and Consent**: While our study does not involve people directly, use of image datasets will be done following their terms of use. If user-generated content or more personal image are used, it will be done with consent of the owners.