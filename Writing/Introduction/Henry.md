# Layered architecture approach to solve near duplicate image detection 

## Abstract
This comes at no surprise, complex problem equals complex solutions, but what is interesting is what if an approach would be to combine all possible solutions together? Reaping the benefits while discourage the negatives, something that seems like a dream is easier then thought. By utilizing a framework that basically is a layered architecture we hope to combine different near duplicate image detection algorithms and see if there can be some benefit. This allows for easy setup of algorithms and exhaustive testing can be done to quickly give a combination that suites the context needs the most. 


> [!NOTE] About the abstract
> >**I like the first part, I would just say instead:**
>> - **Original**- "This comes at no surprise, complex problem equals complex solutions, but what is interesting is what if an approach would be to combine all possible solutions together?"
>>
> > - **Updated**- This comes at no surprise, complex problem equals complex solutions, but what if it doesn't have to always be this way. What if an approach was taken where current solutions are combined to not only reap benefits from each, but to see if the whole is greater than the sum of its parts.
>> 	- *Remove*- "Reaping the benefits while discouraging the negatives, something that seems like a dream is easier then thought."
> ---
> > **We need to add these parts to complete the abstract:**
>> - What methods you have done to address the problems
> > - A short summary of your result


## Introduction 

Today people's life is ever so infused with techonlogy it could almost be consdered as a foundamental to human life at this point [^1]. With an ever so increasing fuzement of software and people data is increasing at a asthonsing rate [^2]. In a study by the International Data Coporation (IDC) showed the digital fingerprint of the world is around 1.8ZB in 2012 and by 2020 it should exceed 40ZB where latest claims by 2025 we are going to reach 175ZB [^3]. A study contucted by Microsoft in 2012 showed that between 50% to 85% of their data is considered as near duplicated data [^4].
Most of this data is in form of video and images, this comes of course with the burdon of memory allocation and storage which heavily affects cost [^5]. To make an easy perspective: when buying a iphone, one quickly discoveres the price difference based on memeory within the same version of the iphone [^6]. Most people are heavily affected by their missuse of storage and will at some point have to clean their devices or buy in on cloud solutions where the risk of theft is increasing [^7]. The use of smart solutions to deal with near image detection would offer great increase in memory management which could help cleanup lots of data.

From another perspective of the ever increasing data and the problem that comes with it, we face problems in the shadows of the Internet where illegal content being spread [^8], copyright violations where small changes of original content can be applied to avoid current copyright detection and reuploaded [^9]. By having near duplication detection solutions illegal content can be found easier, by better near detection copyright violations could be detected sooner [^10]. 



## Related work

In the paper, Bimodal Fusion of Low-Level Features and High-Level Semantic Features for Near-Duplicate Video Clip Detection, a new approach for near duplicate video clip detection is explored that leverages bimodal fusion, which involves combining low-level features with high-level semantic information. Inspired by this idea of combining different algorithms to extract more information, our purposed approach is a layered architecture including different algorithms at each level for near duplicate image detection. Since this new approach provided promising results, we intend to reform and expand upon it in a different direction.

Research from Chum et al. builds upon the classic min-hash algorithm, traditionally used for efficient similarity detection by visual word hashing. They identify unique central features that give spatial and scale information which is used to perform secondary feature extraction, constructing a richer set of geometric features. This method results in a higher discriminative representation of visual words that leverages the inherent strengths of the min-hash technique. The GmH approach demonstrates substantial improvements in recall and reduces the false positive rate making it into a powerful algorithm for image processing, particularly in near duplicate detection. Similar to GmH, our methodology begins with high-level feature extraction, followed by low-level extraction. However, our approach differs in that we aim to integrate various algorithms while GmH focuses on enhancing the min-hash algorithm. This should show improved results for near-duplicate image detection. GmH may in the end be one step of our algorithm that could be used.

The work done in this article shows promising results by combining three distinct algorithms, dHash, SIFT, and LSH model in a horizontal manner. The initial two algorithms, dHash and SIFT are used for feature extraction resulting in several hashes, these are combined into one condensed hash representation a fingerprint image. LSH receives the hash representation from the previous step, where it employs a final feature extraction which put respective features into respective buckets, reduces the search space. Finally, hamming distance is applied to find matching fingerprints, their approach shows a significant promise of 99.99% accuracy. Their method is similar to ours in that they utilize the advantages of multiple algorithms, however, ours diverges as we adopt a more modular approach to the integration of algorithms by using a layered architecture. We believe this offers improved flexibility to choose different algorithms which can lead to better performance and accuracy throughout differing application areas.

## Method

Both public and private sector would benefit heavily by improved techniques in near duplicate detection (NDD) in legal mannors and memory storage. With this we turn the page to NDD with focus on image as pointed out its the biggest impact on memory but also frudulent activities, this study then focuses primarilly on near image duplicate detection (NIDD). The first problem faced when trying to combat NIDD is the question itself: *"what is a near image duplication?"* this can be considered anything and purly depends on the context. The most importance of NIDD solutions is accuracy and performance [^11], huge budget solution can impose a vast large language model with image feature extraction capabilities but this would not fit all cases in terms of security and cost. Further exploring different solutions for NIDD quickly draws a clear picture, this is a complex problem with multiple solutions out there. Most of the solution stems from each other, ranging from sophisticated convulution nueral networks (cnn) to simple hashing algorithms (dhash for example). There exists hybrid solutions where complex mathematical combination of hashing or transfer learning is applied to achive improved algorightms [^12]. 

All algorithms has strengths and weaknesses, some are simple and offer performance at the cost of accuracy, some wise versa. The whole area is gray in that it is context dependant, the algorithms offer great solution for their specific needs, example the fingerprint model which is fine tuned to fit the fingerprint dataset [^13] where other models would classify fingerprint as similar [^14]. To make matters harder most solutions we have seen and exposed ourself to in this study has shown a lack of parameters to algorithms to achive their results as well no real implementation information. 


[^1]: [insert reference to combat IT and human life]
[^2]: [insert reference to backup data increasement]
[^3]: [IDC study]
[^4]: [microsoft study]
[^5]: [insert reference for memory = expenses]
[^6]: [iphone price memory difference]
[^7]: [reference that can show cloud services exposes users data to higher levels of theft]
[^8]: [illegal content spread on the Internet]
[^9]: [copyright violation, especially regarding how current stuff can be jsut edited and reuploaded]
[^10]: [difficult one, but would be nice to have a way to show how NND can help with illigal content to be found and copyright vilation detection]
[^11]: [reference for accuracy and perfomance being the most imporant things for NIDD]
[^12]: [multiple references to different combined algorightms (fingrprint e.g.)]
[^13]: [fingerprint article]
[^14]: [other model that would put fingerprints as same]
