
# Min hash

In its most simplicity minhash boils down to these few steps:

1. create "shingles" & hash them
2. pick the lowest (min) shingles [FALSE]
3. collection of min is your set

So this would take a big data and make it smaller by using the things that stands out the most. Which is great when we wish to compare but even then we run into too many comparisments. To tacle this [^1] recommends using LSH (local sensitive hashing) which would put the hash into buckets and when we compare the data we check against the other data that has their hashes in same buckets which should omit alot of other data. I think that a document lets say exists in 10 buckets (out of lets say 100 in total), in each bucket 100 documents exists, so our documnet would compare itself against 1000 documents. But thats 1000 to 10.000 if LSH not applied. This not to talk bout we need to do perumation checks, AB and BA basically (my understandment so far).

Contracdiction, it seems that min-hash is not quite to select the lowest shingles. We want to pick the minimum, this is called the signature and it involves hashing and bucketing..

## Parameters of minhash

when we create the shingles, basically it HEAVILY depends on how we pick then. In the implementation of versiona (which btw is only for text based) we pick 3 words. But normally you would see k-shingles and then parameter would be to choose K, too small and we have overfitting, too big and we have underfitting..

MinHash will give us the estimated Jaccard Similarity which will cut down process time. [^2]

>*To approximate the Jaccard Similarity between two sets, we will take their MinHash signatures, and simply* **count the number of components which are equal**. If you divide this count by the signature length, you have a pretty good approximation to the Jaccard Similarity between those two sets. [^2]

where signature referes to the computed hash itself. [^2]

Computing the shingles is a considerable hard task for min-hash when it comes to images and its suggested to use it with conjuction with another feature extraction approach. [^3]

The problem lies in the picking of pixels are representors of shingles. So we are first going to focus on creating min-hash for words and lets see if that leads us anyplace..

for words its eaiser like `"I like bananas"` could be grouped to `"I like" "like banans"` *(i think)*.

```bash
h(x) = (ax + b) % c
```

>The coefficients a and b are randomly chosen integers less than the maximum value of x. c is a prime number slightly bigger than the maximum value of x. [^2]

**Jaccard Similarity**:
> *Lets say you and I are both subscribers to Netflix, and we’ve each watched roughly 100 movies on Netflix. The list of movies I’ve seen is a set, and the list of movies you’ve seen is another set. To measure the similarity between these two sets, you can use the Jaccard Similarity,* **which is given by the intersection of the sets divided by their union**. That is, count the number of movies we’ve both seen, and divide that by the total number of unique movies that we’ve both collectively seen. [^2]

[^1]: [chapter3 minhash.pdf](chapter3%20minhash.pdf)
[^2]: [https://mccormickml.com/2015/06/12/minhash-tutorial-with-python-code/](https://mccormickml.com/2015/06/12/minhash-tutorial-with-python-code/)
[^3]: [stackoverflow](https://stackoverflow.com/questions/2758922/using-minhash-to-find-similarities-between-2-images)
[^4]: [geometric minhash](../Current%20Research/Primary/Geometric_min-Hashing_Finding_a_thick_needle_in_a_haystack.pdf)
[^5]: [https://gudok.xyz/minhash1/](https://gudok.xyz/minhash1/)
