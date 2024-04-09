
# Min hash

MinHash will give us the estimated Jaccard Similarity which will cut down process time. [^2]

>*To approximate the Jaccard Similarity between two sets, we will take their MinHash signatures, and simply* **count the number of components which are equal**. If you divide this count by the signature length, you have a pretty good approximation to the Jaccard Similarity between those two sets. [^2]

where signature referes to the computed hash itself. [^2]

Computing the shingels is a considerable hard task for min-hash when it comes to images and its suggested to use it with conjuction with another feature extraction approach. [^3]

The problem lies in the picking of pixels are representors of shingels. So we are first going to focus on creating min-hash for words and lets see if that leads us anyplace..



for words its eaiser like `"I like bananas"` could be grouped to `"I like" "like banans"` *(i think)*.



```bash
h(x) = (ax + b) % c
```

>The coefficients a and b are randomly chosen integers less than the maximum value of x. c is a prime number slightly bigger than the maximum value of x. [^2]

**Jaccard Similarity**:
> *Lets say you and I are both subscribers to Netflix, and we’ve each watched roughly 100 movies on Netflix. The list of movies I’ve seen is a set, and the list of movies you’ve seen is another set. To measure the similarity between these two sets, you can use the Jaccard Similarity,* **which is given by the intersection of the sets divided by their union**. That is, count the number of movies we’ve both seen, and divide that by the total number of unique movies that we’ve both collectively seen. [^2]


[^1]: [chapter3 minhash.pdf](../Current%20Research/Research/research-dump-henry/chapter3%20minhash.pdf)
[^2]: [https://mccormickml.com/2015/06/12/minhash-tutorial-with-python-code/](https://mccormickml.com/2015/06/12/minhash-tutorial-with-python-code/)
[^3]: [stackoverflow](https://stackoverflow.com/questions/2758922/using-minhash-to-find-similarities-between-2-images)
[^4]: [geometric minhash](../Current%20Research/Primary/Geometric_min-Hashing_Finding_a_thick_needle_in_a_haystack.pdf)
[^5]: [https://gudok.xyz/minhash1/](https://gudok.xyz/minhash1/)
