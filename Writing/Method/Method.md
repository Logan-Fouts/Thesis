## Research Project

In order to address the issue of the ambiguous definition of what constitutes a near duplicate image, and the seemingly infinite possible definitions of this, we purpose an interesting technique. This study uses aspects of the design science approach to develop and evaluate new algorithms and potentially a small framework created to easily build them. We will then validate our approach by comparison to current state of the art techniques for near duplicate image detection and their results as well as comparing results of individual algorithms to the combination.

## Research methods

### Controlled Experiments

In order to build the algorithms targeted for a specific domain, we will utilize controlled experiments. Initially, layers will be manually tuned by manipulating each parameter independently to optimize performance for the specific input data. Once each layer is tuned, then each combination of layers can be automatically exhaustively tested. From the history of performance data, the best combination can be selected for further comparative analysis. This method allows for clear control over variables, preventing other factors from skewing the results. Furthermore, automation will help to avoid any possible oversights that could occur from manual testing.
### Comparative Analysis

Our decided algorithms outputs will be bench marked against other more traditional near duplicate image detection techniques. Statistics such as precision, recall, run time, and resource usage will be both recorded then considered while comparing methods. Comparing these metrics will allow us to effectively highlight any pro's or con's of the new algorithms as well as the layered approach. In order to compare, a subset of the same input data will be used and the same metrics will be compared for each. Results from these comparisons will allow us to evaluate if our method is an effective way to allow for flexible near duplicate image detection.
## Reliability and Validity

Reliability in research refers to the consistency of the results obtained from the study. It explores whether other researchers can produce similar results under the same conditions, using the same methods. In our study, we aim to document in detail all relevant testing and experimentation information in order to allow for others to run them for themselves.

Validity, relates to the accuracy and legitimacy of our findings. To aid in the validity of our study, we engage in rigorous exhaustive testing to find a base algorithm, then tune the layers to fit the domain, maximizing our algorithms ability to identify near duplicate images while limiting wrong classifications.

### Addressing Reliability and Validity Issues

- **Threats to Reliability**: 
	- The main potential threat to reliability comes from non-uniform test environments or inconsistent data sets. To mitigate this, we will use subsets of defined image sets for each algorithm and make sure to have consistent testing conditions across all experiments.
- **Threats to Validity**: 
	- One threat to validity in our study could come from the subjective definition of what constitutes a "near duplicate" image. To deal with this, we will use clearly defined and specific criteria for what constitutes near duplicity for each algorithm targeting a certain domain.
	- Most likely the largest threat to validity would be the use of subsets of the original experiment data due to a lack of compute and time resources. This could lead to skewed or invalid results depending on how the subset is taken. To help minimize this issue and allow for more generalize-ability, subsets will be chosen at random. However, the fact that only a subset is being taken will regardless limit the validity of our results.
	
## Ethical considerations

For our study, we have made the following ethical considerations:

- **Confidentiality**: If the layers were put into production many security issues would need to be ironed out such as securely storing images both in the data bases as well as during processing. However, we do not intend for this to be put into production, simply we are exploring if the idea of layers of image processing is a viable option to allow for greater flexibility as well as reaping the benefits of the filter like flow.

- **Sampling and Bias**: The choice of images and datasets needs to be assessed to avoid biases that could skew the results. For instance, diverse different datasets will be chosen to represent real world scenarios and avoid over fitting, as well as the highlight the flexibility of the layered approach.

- **Risk of Harm**: Our research involves the processing of images and does not entail any human participation, so harm is not a concern.

- **Participation and Consent**: While our study does not involve people directly, use of image datasets will be done following their terms of use. If user-generated content or more personal image are used, it will be done with consent of the owners.