# Experiment Setup 

The layered framework provides a unique oppertunity to conduct experiments with various configurations. As the layers allow for any algorithms to run together the important question has to be asked, which algorithms to choose and in which order? We can use permutations to give us great insight to overcome that problem. Here's a quick demostration of how that works:

```python
def run(data, algorithms, size):
  configs = permutation(algorithms, size)

  for config in configs:
    layer = Layer(config)
    layer.run(data)
```

Where the algorithms variable is a pool of algorithms and their respective parameters already pre tuned. Pre tuning is a daunting process where the aim is to have the algorithm in target having low false positives, recall false positives would prevent later algorithms to have their chance to classify the images. The faster algorithms should be in the beginning to reak their fastness and we are okay to loose some of their accuracy as long as it cuts the false positives. The slower ones should be in the end and will run slower but are more accurate. 


# California Experiment

As mentioned before the california is a collection of personal holiday photos with a size of 701 images. The algorithms choosen for this experiments are `phash, dhash, sift and vgg`, their pre-tunings yielded us the following results. 

| algorithm | parameters |
| --------- | ---------- |
| dhash | threshold=0.9 |
| phash | threshold=11 |
| vgg | threshold=0.7 |
| sift | threshold=16, sigma=1.6, edge_threshold=10, n_octave_layers=3, contrast_threshold=0.04, image_ratio=0.1 |

## Results
Here is the results from the individual algorithms.

### Dhash
| Data size | TP | FP | FN | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
|:---------:|:--:|:--:|:--:|:---------:|:------:|:--------:|:--------:|:----------------:|
| 100 | 50 | 0 | 50 | 1.0000 | 0.5000 | 0.6667 | 0.5000 | 1.2313 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 701 | 279 | 0 | 334 | 1.0000 | 0.4551 | 0.6256 | 0.4551 | 7.7574 |

### Phash
| Data size | TP | FP | FN | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
|:---------:|:--:|:--:|:--:|:---------:|:------:|:--------:|:--------:|:----------------:|
| 100 | 69 | 0 | 41 | 1.0000 | 0.5900 | 0.7421 | 0.5900 | 1.8090 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 701 | 319 | 0 | 294 | 1.0000 | 0.5204 | 0.6845 | 0.5204 | 7.8921 |

### VGG
| Data size | TP | FP | FN | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
|:---------:|:--:|:--:|:--:|:---------:|:------:|:--------:|:--------:|:----------------:|
| 100 | 78 | 0 | 22 | 1.0000 | 0.7800 | 0.8764 | 0.7800 | 49.6771 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 701 | 415 | 8 | 190 | 0.9811 | 0.6860 | 0.8074 | 0.6770 | 292.8172 |

### SIFT
| Data size | TP | FP | FN | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
|:---------:|:--:|:--:|:--:|:---------:|:------:|:--------:|:--------:|:----------------:|
| 80 | 76 | 0 | 4 | 1.0000 | 0.9500 | 0.9744 | 0.9500 | 1.0857 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 701 | 434 | 4 | 175 | 0.9909 | 0.7126 | 0.8290 | 0.7080 | 44.5817 |


We are experimenting with a 3-size layer architecture and the top 3 results (focus on TP and F1-score) we have the following.

### 3 size layer architecture
| Algorithms | Data size | TP | FP | FN | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s) |
|:---:|:---------:|:--:|:--:|:--:|:---------:|:------:|:--------:|:--------:|:----------------:|
| | 80 | 76 | 0 | 4 | 1.0000 | 0.9500 | 0.9744 | 0.9500 | 1.0857 |
| | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| | 701 | 434 | 4 | 175 | 0.9909 | 0.7126 | 0.8290 | 0.7080 | 44.5817 |