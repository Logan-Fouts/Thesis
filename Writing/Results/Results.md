> [!NOTE] Should be in [[Research Project Implementation]]
> ## Experiment Setup 
> 
> The layered framework provides a unique opportunity to conduct experiments with various configurations. As the layers allow for any algorithms to run together the important question has to be asked, which algorithms to choose and in which order? We can use permutations to give us great insight to overcome that problem. Here's a quick demonstration of how that works:
> 
> ```python
> def run(data, algorithms, size):
>   configs = permutation(algorithms, size)
> 
>   for config in configs:
>     layer = Layer(config)
>     layer.run(data)
> ```
> 
> Where the algorithms variable is a pool of algorithms and their respective parameters already pre-tuned. Pre-tuning is a daunting process where the aim is to have the algorithm in target having low false positives, recall false positives would prevent later algorithms to have their chance to classify the images. The faster algorithms should be in the beginning to reap their fastness and we are okay to loose some of their accuracy as long as it cuts the false positives. The slower ones should be in the end and will run slower but are more accurate. 


## SOCOFing Data Set
### Permutations (Random Subset of size 90)

| Algorithms Combination                            | Time Elapsed (s) | Accuracy (%) | Groups of Duplicate Images |
| ------------------------------------------------- | ---------------- | ------------ | -------------------------- |
| Phash[4], SIFT[17, 1.8, 10000, 3, 0.01], VGG[0.6] | 4.67             | 90.41        | 30                         |
| Phash[4], SIFT[17, 1.8, 10000, 3, 0.01], Dhash[3] | 3.19             | 100.00       | 28                         |
| Phash[4], Dhash[3], VGG[0.6]                      | 8.53             | 48.89        | 17                         |
| Phash[4], Dhash[3], SIFT[17, 1.8, 10000, 3, 0.01] | 3.18             | 100.00       | 28                         |
| Dhash[3], VGG[0.6], SIFT[17, 1.8, 10000, 3, 0.01] | 9.00             | 35.71        | 13                         |
| Dhash[3], VGG[0.6], Phash[4]                      | 9.11             | 35.71        | 13                         |
| Dhash[3], SIFT[17, 1.8, 10000, 3, 0.01], VGG[0.6] | 4.90             | 87.84        | 29                         |
| Dhash[3], SIFT[17, 1.8, 10000, 3, 0.01], Phash[4] | 3.25             | 100.00       | 28                         |
| Dhash[3], Phash[4], VGG[0.6]                      | 8.21             | 48.53        | 17                         |
| Dhash[3], Phash[4], SIFT[17, 1.8, 10000, 3, 0.01] | 3.22             | 100.00       | 28                         |
| Phash[4], VGG[0.6], Dhash[3]                      | 8.90             | 39.36        | 13                         |
| Phash[4], VGG[0.6], SIFT[17, 1.8, 10000, 3, 0.01] | 8.98             | 39.36        | 13                         |
| SIFT[17, 1.8, 10000, 3, 0.01], Dhash[3], Phash[4] | 3.26             | 100.00       | 28                         |
| SIFT[17, 1.8, 10000, 3, 0.01], Dhash[3], VGG[0.6] | 4.35             | 96.34        | 30                         |
| SIFT[17, 1.8, 10000, 3, 0.01], Phash[4], Dhash[3] | 3.26             | 100.00       | 28                         |
| SIFT[17, 1.8, 10000, 3, 0.01], Phash[4], VGG[0.6] | 4.18             | 98.72        | 31                         |
| SIFT[17, 1.8, 10000, 3, 0.01], VGG[0.6], Dhash[3] | 4.34             | 96.34        | 30                         |
| SIFT[17, 1.8, 10000, 3, 0.01], VGG[0.6], Phash[4] | 4.30             | 96.34        | 30                         |
| VGG[0.6], Dhash[3], Phash[4]                      | 8.62             | 23.99        | 6                          |
| VGG[0.6], Dhash[3], SIFT[17, 1.8, 10000, 3, 0.01] | 8.88             | 23.99        | 6                          |
| VGG[0.6], Phash[4], Dhash[3]                      | 8.79             | 23.99        | 6                          |
| VGG[0.6], Phash[4], SIFT[17, 1.8, 10000, 3, 0.01] | 8.64             | 23.99        | 6                          |
| VGG[0.6], SIFT[17, 1.8, 10000, 3, 0.01], Dhash[3] | 8.78             | 23.99        | 6                          |
| VGG[0.6], SIFT[17, 1.8, 10000, 3, 0.01], Phash[4] | 8.68             | 23.99        | 6                          |
*Figure i.i SOCOFing permutation testing results*

### Individual and Combined Results

#### 1. Dhash Results

| Data Size | TP   | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
|-----------|------|-----|-----|-----------|--------|----------|----------|------------------|
| 300       | 297  | 3   | 3   | 0.9900    | 0.9900 | 0.9900   | 0.9900   | 6.2310           |
| 600       | 593  | 7   | 7   | 0.9883    | 0.9883 | 0.9883   | 0.9883   | 18.3165          |
| 900       | 887  | 13  | 13  | 0.9855    | 0.9855 | 0.9855   | 0.9855   | 40.6721          |
| 1200      | 1186 | 14  | 14  | 0.9882    | 0.9882 | 0.9882   | 0.9882   | 72.0654          |
| 1500      | 1484 | 16  | 16  | 0.9893    | 0.9893 | 0.9893   | 0.9893   | 112.9932         |
*Figure i.i SOCOFing Dhash testing results*
#### 2. Phash Results

| Data Size | TP  | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
| --------- | --- | --- | --- | --------- | ------ | -------- | -------- | ---------------- |
| 300       | 136 | 0   | 164 | 1.0000    | 0.4533 | 0.6239   | 0.4533   | 0.5607           |
| 600       | 264 | 4   | 336 | 0.9851    | 0.4430 | 0.6111   | 0.4400   | 1.6792           |
| 900       | 398 | 6   | 502 | 0.9851    | 0.4430 | 0.6111   | 0.4400   | 3.5723           |
| 1200      | 529 | 9   | 671 | 0.9832    | 0.4408 | 0.6094   | 0.4408   | 6.4721           |
| 1500      | 665 | 15  | 835 | 0.9779    | 0.4433 | 0.6109   | 0.4433   | 10.3482          |
*Figure i.i SOCOFing Phash testing results*
#### 3. SIFT Results

| Data Size | TP   | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
|-----------|------|-----|-----|-----------|--------|----------|----------|------------------|
| 300       | 300  | 0   | 0   | 1.0000    | 1.0000 | 1.0000   | 1.0000   | 8.9167           |
| 600       | 600  | 0   | 0   | 1.0000    | 1.0000 | 1.0000   | 1.0000   | 35.1776          |
| 900       | 900  | 0   | 0   | 1.0000    | 1.0000 | 1.0000   | 1.0000   | 79.6654          |
| 1200      | 1200 | 0   | 0   | 1.0000    | 1.0000 | 1.0000   | 1.0000   | 142.9932         |
| 1500      | 1500 | 0   | 0   | 1.0000    | 1.0000 | 1.0000   | 1.0000   | 221.4671         |
*Figure i.i SOCOFing SIFT testing results*
#### 4. Combined Results (Phash, Dhash, SIFT)

| Data Size | TP   | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
|-----------|------|-----|-----|-----------|--------|----------|----------|------------------|
| 300       | 300  | 0   | 0   | 1.0000    | 1.0000 | 1.0000   | 1.0000   | 2.5530           |
| 600       | 598  | 0   | 2   | 1.0000    | 0.9967 | 0.9983   | 0.9967   | 9.1599           |
| 900       | 883  | 7   | 10  | 0.9921    | 0.9888 | 0.9905   | 0.9811   | 19.7361          |
| 1200      | 1162 | 23  | 15  | 0.9806    | 0.9873 | 0.9839   | 0.9683   | 33.8846          |
| 1500      | 1433 | 47  | 20  | 0.9682    | 0.9862 | 0.9772   | 0.9553   | 51.8370          |
*Figure i.i SOCOFing combined suite testing results*

![[Metrics_Graph.png]]
*Figure i.i SOCOFing resulting metrics graph*

![[Time_Graph.png]]
*Figure i.i SOCOFing resulting elapsed time graph*

## California-ND Data Set

As mentioned before the California dataset is a collection of personal holiday photos with a size of 701 images. The algorithms chosen for this experiments are `phash, dhash, sift and vgg`, their initial tuning yielded us the following results. 

| algorithm | parameters |
| --------- | ---------- |
| dhash | threshold=0.9 |
| phash | threshold=11 |
| vgg | threshold=0.7 |
| sift | threshold=16, sigma=1.6, edge_threshold=10, n_octave_layers=3, contrast_threshold=0.04, image_ratio=0.1 |

### Individual and Combined Results
Here is the results from the individual algorithms.

#### 1. Dhash

| Data size | TP  | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
| :-------: | :-: | :-: | :-: | :-------: | :----: | :------: | :------: | :--------------: |
|    100    | 50  |  0  | 50  |  1.0000   | 0.5000 |  0.6667  |  0.5000  |      1.2313      |
|    200    | 147 | 33  | 20  |  0.8167   | 0.8802 |  0.8473  |  0.7350  |      2.3574      |
|    400    | 197 | 146 | 57  |  0.5743   | 0.7756 |  0.6600  |  0.4925  |      4.6754      |
|    701    | 279 |  0  | 334 |  1.0000   | 0.4551 |  0.6256  |  0.4551  |      7.7574      |

#### 2. Phash
| Data size | TP  | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
| :-------: | :-: | :-: | :-: | :-------: | :----: | :------: | :------: | :--------------: |
|    100    | 69  |  0  | 41  |  1.0000   | 0.5900 |  0.7421  |  0.5900  |      1.8090      |
|    300    | 202 |  6  | 92  |  0.9712   | 0.6871 |  0.8048  |  0.6733  |      3.4085      |
|    701    | 319 |  0  | 294 |  1.0000   | 0.5204 |  0.6845  |  0.5204  |      7.8921      |

#### 3. VGG
| Data size | TP  | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
| :-------: | :-: | :-: | :-: | :-------: | :----: | :------: | :------: | :--------------: |
|    10     |  8  |  0  |  2  |  1.0000   | 0.8000 |  0.8889  |  0.8000  |      4.6451      |
|    100    | 78  |  0  | 22  |  1.0000   | 0.7800 |  0.8764  |  0.7800  |     49.6771      |
|    701    | 415 |  8  | 190 |  0.9811   | 0.6860 |  0.8074  |  0.6770  |     292.8172     |

#### 4. SIFT
| Data size | TP  | FP  | FN  | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
| :-------: | :-: | :-: | :-: | :-------: | :----: | :------: | :------: | :--------------: |
|    10     | 10  |  0  |  0  |  1.0000   | 1.0000 |  1.0000  |  1.0000  |      0.7154      |
|    80     | 76  |  0  |  4  |  1.0000   | 0.9500 |  0.9744  |  0.9500  |      1.0857      |
|    200    | 77  | 121 |  2  |  0.3889   | 0.9747 |  0.5560  |  0.3850  |     231.2505     |
|    400    | 338 |  0  | 62  |  1.0000   | 0.8450 |  0.9160  |  0.8450  |     22.7410      |
|    701    | 434 |  4  | 175 |  0.9909   | 0.7126 |  0.8290  |  0.7080  |     44.5817      |


### Permutations
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