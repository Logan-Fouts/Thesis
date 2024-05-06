## Research Project

~~In order to address the issue of the ambiguous definition of what constitutes a near duplicate image, and the seemingly infinite possible definitions of this, we purpose an interesting technique. This study uses aspects of the design science approach to develop and evaluate new algorithms and potentially a small framework created to easily build them. We will then validate our approach by comparison to current state of the art techniques for near duplicate image detection and their results as well as comparing results of individual algorithms to the combination.~~
  
To address the challenge of defining and identifying near duplicate images, which lacks a uniform exact definition, we propose a technique utilizing a layered architecture. Our methodology is inspired by design science principles, so it facilitates the development and evaluation of a modular architecture. Through this, we hope to integrate various algorithms for near duplicate image detection together. This not only seeks to enhance flexibility but also aims to optimize simplicity. Our prototype will be validated against existing techniques and their results with their datasets, comparing both the efficacy of individual algorithms and their combined effect when deployed within our layered framework. We will as well go into a theoretical discussion to reason about the perceived ease of use and implementation for our approach compared to others. 

>im having some problem with this sentence, it is good but I feel it caputeres a bit falsly: *"This study uses aspects of the design science approach to develop and evaluate new algorithms and potentially a small framework created to easily build them."*\
How are we using aspects of design science to develop & evaluate "new algorithms"
and then potentially creating a small framework, that will be used to build them?

>Instead I understand the text more to this? (the design science is still bit weird for me):\
**design science controlls the develop and evelation of algorithms**
*"This study focuses on combining algorithms together by the use of a small framework that has been build alongside it, with a design science approach we hope to combine and evaluate the layered algorithms"*\
**if design science controlls more the development of framework**
*"This study is focused on combining algorithms together and check if simplicity, performance and accuracy can be achived, with some aspects of design science we have constructed a framework that will help us to achive that."*

## Research methods

### Controlled Experiments

In order to build the algorithms targeted for a specific domain, we will utilize controlled experiments. Initially, layers will be manually tuned by manipulating each parameter independently to optimize performance for the specific input data. Once each layer is tuned, then each combination of layers can be automatically exhaustively tested. From the history of performance data, the best combination can be selected for further comparative analysis. This method allows for clear control over variables, preventing other factors from skewing the results. Furthermore, automation will help to avoid any possible oversights that could occur from manual testing.

> Maybe give a quick outline to give reading understanding how the automation will take place which should also clear up any question of how we do testing (as its all same dataset?) - maybe also just to increase lines ^^

```python
	def run_experiments(dataset, size):
		perumation_sets = permutations(list_of_algorithms, size)
		
		for set in perumation_sets:
			layered = Layers(set)
			results = layered.experiment(dataset)
```
### Comparative Analysis

Our decided algorithms outputs will be bench marked against other more traditional near duplicate image detection techniques. Statistics such as precision, recall, run time, and resource usage will be both recorded then considered while comparing methods. Comparing these metrics will allow us to effectively highlight any pro's or con's of the new algorithms as well as the layered approach. In order to compare, a subset of the same input data will be used and the same metrics will be compared for each. Results from these comparisons will allow us to evaluate if our method is an effective way to allow for flexible near duplicate image detection.

### Prototype Assessment

In order to back up our claim that our vertical method of combining algorithms is "easier" compared to the horizontal method, a review of the two workflows will be done. This assessment hope to highlight the relative simplicity/speed of set up, understand-ability, and operating efficiency with respect to our approach, despite limited practical access to implementations in a horizontal approach.

#### **Theoretical Assessment**

Our theoretical assessment is an analysis of the workflow involved in both the vertical and horizontal methods. We will focus on:
- **Setup/Configuration Complexity**: Count the number of steps, configuration requirements, and the level of knowledge required to build with both approaches.
- **Understand-ability**: This involves taking a look at the difficulty to comprehend and run each approach. This will avoid discuss any front end user interfaces as we aim to reason about the underlying tooling.
- **Integration of Components**: We assess how each method handles the combination of the various algorithms into a single system, and discuss potential benefits and draw backs of each.

>Are we going to try to "theoretically" go over how to implement a more advanced algorithm like maybe geo-minhash and based on this theoretical by exposing the fact they have to combine their hashes in a smart way then having to iterate and check where things are considered "near" duplicate\
compared to ours: you find one that works and you mess with its parameters then you see if it combined with other algorithms could give even better results? (maybe even without that algorithm)?

#### **Practical Assessment**

Due to limited access to the horizontal approach, our practical assessment revolves around our implementation of the vertical method. We can replicate conditions that have been recorded in articles and infer the horizontal method's performance against ours:
- **Operational Efficiency**: We measure the time taken to complete runs on each approach. Metrics such as throughput and resource usage are recorded to evaluate performance and time complexity.
- **Error Rate and Maintenance**: Analyzing the error rate and other rates, we provide insights into the usability and reliability of our method. Comparison is done with reported metrics from horizontal systems, when available.

#### **Outcomes and Future Directions**

The results from both theoretical and practical assessments hope to argue that the vertical approach is a similarly performative option, but an easier and more user-friendly solution for image processing algorithm combination.

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