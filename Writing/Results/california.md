# Experiment Setup 

The layered framework provides a unique opportunity to conduct experiments with various configurations. As the layers allow for any algorithms to run together the important question has to be asked, which algorithms to choose and in which order? We can use permutations to give us great insight to overcome that problem. Here's a quick demonstration of how that works:

```python
def run(data, algorithms, size):
  configs = permutation(algorithms, size)

  for config in configs:
    layer = Layer(config)
    layer.run(data)
```

Where the algorithms variable is a pool of algorithms and their respective parameters already pre tuned. Pre tuning is a daunting process where the aim is to have the algorithm in target having low false positives, recall false positives would prevent later algorithms to have their chance to classify the images. The faster algorithms should be in the beginning to reak their fastness and we are okay to loose some of their accuracy as long as it cuts the false positives. The slower ones should be in the end and will run slower but are more accurate. 


# California Experiment

As mentioned before the California dataset is a collection of personal holiday photos with a size of 701 images. The algorithms chosen for this experiments are `phash, dhash, sift and vgg`, their initial tuning yielded us the following results. 

| algorithm | parameters |
| --------- | ---------- |
| dhash | threshold=0.9 |
| phash | threshold=11 |
| vgg | threshold=0.7 |
| sift | threshold=16, sigma=1.6, edge_threshold=10, n_octave_layers=3, contrast_threshold=0.04, image_ratio=0.1 |

## Results
Here is the results from the individual algorithms.

### Dhash
| Data size | TP  | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
| :-------: | :-: | :-: | :-: | :-------: | :----: | :------: | :------: | :--------------: |
|    100    | 50  |  0  | 50  |  1.0000   | 0.5000 |  0.6667  |  0.5000  |      1.2313      |
|    200    | 147 | 33  | 20  |  0.8167   | 0.8802 |  0.8473  |  0.7350  |      2.3574      |
|    400    | 197 | 146 | 57  |  0.5743   | 0.7756 |  0.6600  |  0.4925  |      4.6754      |
|    701    | 279 |  0  | 334 |  1.0000   | 0.4551 |  0.6256  |  0.4551  |      7.7574      |

### Phash
| Data size | TP  | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
| :-------: | :-: | :-: | :-: | :-------: | :----: | :------: | :------: | :--------------: |
|    100    | 69  |  0  | 41  |  1.0000   | 0.5900 |  0.7421  |  0.5900  |      1.8090      |
|    300    | 202 |  6  | 92  |  0.9712   | 0.6871 |  0.8048  |  0.6733  |      3.4085      |
|    701    | 319 |  0  | 294 |  1.0000   | 0.5204 |  0.6845  |  0.5204  |      7.8921      |

### VGG
| Data size | TP  | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
| :-------: | :-: | :-: | :-: | :-------: | :----: | :------: | :------: | :--------------: |
|    10     |  8  |  0  |  2  |  1.0000   | 0.8000 |  0.8889  |  0.8000  |      4.6451      |
|    100    | 78  |  0  | 22  |  1.0000   | 0.7800 |  0.8764  |  0.7800  |     49.6771      |
|    701    | 415 |  8  | 190 |  0.9811   | 0.6860 |  0.8074  |  0.6770  |     292.8172     |

### SIFT
| Data size | TP  | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
| :-------: | :-: | :-: | :-: | :-------: | :----: | :------: | :------: | :--------------: |
|    10     | 10  |  0  |  0  |  1.0000   | 1.0000 |  1.0000  |  1.0000  |      0.7154      |
|    80     | 76  |  0  |  4  |  1.0000   | 0.9500 |  0.9744  |  0.9500  |      1.0857      |
|    200    | 77  | 121 |  2  |  0.3889   | 0.9747 |  0.5560  |  0.3850  |     231.2505     |
|    400    | 338 |  0  | 62  |  1.0000   | 0.8450 |  0.9160  |  0.8450  |     22.7410      |
|    701    | 434 |  4  | 175 |  0.9909   | 0.7126 |  0.8290  |  0.7080  |     44.5817      |


### 3 size layer architecture
With the parameters in place we can now conduct the final experiment, the size of layer is set to 3. 

|     | filename         | Data size | TP  | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
| --- | ---------------- | --------- | --- | --- | --- | --------- | ------ | -------- | -------- | ---------------- |
| 1   | sift-dhash-vgg   | 613       | 512 | 10  | 91  | 0.9808    | 0.8491 | 0.9102   | 0.8352   | 170.5191         |
| 2   | dhash-sift-vgg   | 613       | 512 | 10  | 91  | 0.9808    | 0.8491 | 0.9102   | 0.8352   | 173.2788         |
| 3   | sift-vgg-phash   | 613       | 512 | 10  | 91  | 0.9808    | 0.8491 | 0.9102   | 0.8352   | 555.8749         |
| 4   | sift-vgg-dhash   | 613       | 512 | 10  | 91  | 0.9808    | 0.8491 | 0.9102   | 0.8352   | 804.7373         |
| 5   | phash-sift-vgg   | 613       | 511 | 9   | 93  | 0.9827    | 0.8460 | 0.9093   | 0.8336   | 151.2948         |
| 6   | vgg-dhash-sift   | 613       | 511 | 8   | 94  | 0.9846    | 0.8446 | 0.9093   | 0.8336   | 320.8972         |
| 7   | dhash-vgg-sift   | 613       | 510 | 8   | 95  | 0.9846    | 0.8430 | 0.9083   | 0.8320   | 206.3728         |
| 8   | vgg-sift-phash   | 613       | 510 | 8   | 95  | 0.9846    | 0.8430 | 0.9083   | 0.8320   | 269.8956         |
| 9   | sift-phash-vgg   | 613       | 510 | 11  | 92  | 0.9789    | 0.8472 | 0.9083   | 0.8320   | 558.8285         |
| 10  | vgg-phash-sift   | 613       | 509 | 11  | 93  | 0.9788    | 0.8455 | 0.9073   | 0.8303   | 278.4222         |
| 11  | phash-vgg-sift   | 613       | 507 | 11  | 95  | 0.9788    | 0.8422 | 0.9054   | 0.8271   | 201.7340         |
| 12  | vgg-sift-dhash   | 613       | 503 | 17  | 93  | 0.9673    | 0.8440 | 0.9014   | 0.8206   | 271.1108         |
| 13  | dhash-phash-sift | 613       | 477 | 0   | 136 | 1.0000    | 0.7781 | 0.8752   | 0.7781   | 38.0510          |
| 14  | sift-dhash-phash | 613       | 475 | 2   | 136 | 0.9958    | 0.7774 | 0.8732   | 0.7749   | 57.9484          |
| 15  | dhash-sift-phash | 613       | 474 | 1   | 138 | 0.9979    | 0.7745 | 0.8721   | 0.7732   | 41.9424          |
| 16  | phash-dhash-sift | 613       | 473 | 3   | 137 | 0.9937    | 0.7754 | 0.8711   | 0.7716   | 32.2344          |
| 17  | sift-phash-dhash | 613       | 473 | 1   | 139 | 0.9979    | 0.7729 | 0.8711   | 0.7716   | 56.5184          |
| 18  | phash-sift-dhash | 613       | 471 | 3   | 139 | 0.9937    | 0.7721 | 0.8690   | 0.7684   | 32.4826          |
| 19  | dhash-vgg-phash  | 613       | 421 | 8   | 184 | 0.9814    | 0.6959 | 0.8143   | 0.6868   | 231.5593         |
| 20  | vgg-phash-dhash  | 613       | 421 | 8   | 184 | 0.9814    | 0.6959 | 0.8143   | 0.6868   | 264.1087         |
| 21  | vgg-dhash-phash  | 613       | 421 | 8   | 184 | 0.9814    | 0.6959 | 0.8143   | 0.6868   | 297.9276         |
| 22  | dhash-phash-vgg  | 613       | 420 | 8   | 185 | 0.9813    | 0.6942 | 0.8132   | 0.6852   | 181.9143         |
| 23  | phash-vgg-dhash  | 613       | 420 | 8   | 185 | 0.9813    | 0.6942 | 0.8132   | 0.6852   | 228.7846         |
| 24  | phash-dhash-vgg  | 613       | 418 | 8   | 187 | 0.9812    | 0.6909 | 0.8109   | 0.6819   | 172.0623         |

The table has been sorted according to TP and elapsed time.


## Figures
![[cali_metrics_graph.png]]
![[cali-execution times.png]]
![[cali permutations graph.png]]