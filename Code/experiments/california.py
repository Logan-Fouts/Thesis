import os
import permutation
import numpy as np
import re

correlation_matrix=np.load(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../datasets/california/gt_all.npy")))

dataset = permutation.get_dataset("california/output.json")
extracted_numbers = {}

def extract_number_path(path):
  if not path in extracted_numbers:
    match = re.search(r'(\d+)\.jpg$', path)

    if match:
      extracted_numbers[path] = int(match.group(1))
    else:
      print("COULD NOT DETERMINE NUMBER", path)

  return extracted_numbers[path]

def extract_number(group, index):
  path = group[index]

  return extract_number_path(path)

print("running california experiment")

# def accuracy_calculator(duplicate_groups, non_duplicate_list, lonely_imgs):
#   return permutation.accuracy_calculator(duplicate_groups, non_duplicate_list, lonely_imgs, dataset)

def accuracy_calculator(duplicate_groups, non_duplicate_list, lonely_imgs):
  tp=0
  tn=0
  fp=0
  fn=0
  
  # first we check the groups 
  for group in duplicate_groups:
    size=len(group)
    for i in range(size):
      row=extract_number(group, i)-1
      wholeset=True
      for j in range(i + 1, size):
        col=extract_number(group, j)-1
        
        score = correlation_matrix[row, col]
        # NOTE this results in higher number of results then it 
        # is as it checks each member of the group if they corresond to each other 
        if score == 0:
          wholeset=False 
          break

      if wholeset == True:
        tp += 1
      else:
        fp += 1

  # then we check the none groups and make sure they in fact are alone 
  for path in non_duplicate_list:
    row=extract_number_path(path)-1
    found = False 

    for i in range(701):
      if i != row: # making sure we dont check itself 
        if correlation_matrix[row, i] != 0:
          found = True 
          break
    
    # if we found a match means they are not alone 
    if found == True:
      fn += 1
    else:
      tn += 1

  print(f"tp:{tp},fp:{fp}")
  return tp, fp, tn, fn

def parameter_tuning_sift():
  """ 
  PARAMETERS
  - threshold=30,
  - sigma=1.6,
  - edge_threshold=10,
  - n_octave_layers=3,
  - contrast_threshold=0.04,
  - image_ratio=0.3,
  """
  permutation.experiment(
    dataset=dataset,
    dataset_size=701,
    config=[{'name': "sift", 'params': [16, 1.6, 10, 3, 0.04, 0.1]}],
    accuracy_calculator=accuracy_calculator,
    presets=permutation.presets['california'],
    foldername="california-sift-tuning"
  )

def parameter_tuning_dhash():
  permutation.experiment(
    dataset=dataset,
    dataset_size=701,
    config=[{'name': "dhash", 'params': [0.895]}],
    accuracy_calculator=accuracy_calculator,
    presets=permutation.presets['california'],
    foldername="california-dhash-tuning"
  )
  permutation.experiment(
    dataset=dataset,
    dataset_size=701,
    config=[{'name': "dhash", 'params': [0.899]}],
    accuracy_calculator=accuracy_calculator,
    presets=permutation.presets['california'],
    foldername="california-dhash-tuning"
  )

def parameter_tuning_phash():
  permutation.experiment(
    dataset=dataset,
    dataset_size=100,
    config=[{'name': "phash", 'params': [11]}],
    accuracy_calculator=accuracy_calculator,
    presets=permutation.presets['california'],
    foldername="california-phash-tuning"
  )
  # permutation.experiment(
  #   dataset=dataset,
  #   dataset_size=701,
  #   config=[{'name': "phash", 'params': [11]}],
  #   accuracy_calculator=accuracy_calculator,
  #   presets=permutation.presets['california'],
  #   foldername="california-phash-tuning"
  # )
  # permutation.experiment(
  #   dataset=dataset,
  #   dataset_size=300,
  #   config=[{'name': "phash", 'params': [14]}],
  #   accuracy_calculator=accuracy_calculator,
  #   presets=permutation.presets['california'],
  #   foldername="california-phash-tuning"
  # )

def parameter_tuning_vgg():
  permutation.experiment(
    dataset=dataset,
    dataset_size=701,
    config=[{'name': "vgg", 'params': [0.7]}],
    accuracy_calculator=accuracy_calculator,
    presets=permutation.presets['california'],
    foldername="california-vgg-tuning"
  )
  permutation.experiment(
    dataset=dataset,
    dataset_size=701,
    config=[{'name': "vgg", 'params': [0.8]}],
    accuracy_calculator=accuracy_calculator,
    presets=permutation.presets['california'],
    foldername="california-vgg-tuning"
  )
  # permutation.experiment(
  #   dataset=dataset,
  #   dataset_size=100,
  #   config=[{'name': "vgg", 'params': [0.5]}],
  #   accuracy_calculator=accuracy_calculator,
  #   presets=permutation.presets['california'],
  #   foldername="california-vgg-tuning"
  # )
  # permutation.experiment(
  #   dataset=dataset,
  #   dataset_size=100,
  #   config=[{'name': "vgg", 'params': [0.7]}],
  #   accuracy_calculator=accuracy_calculator,
  #   presets=permutation.presets['california'],
  #   foldername="california-vgg-tuning"
  # )


# controlled combined tests 
def phash_dhash_sift():
  permutation.experiment(
    dataset=dataset,
    dataset_size=701,
    config=[{'name': "phash", 'params': [11]}, {'name': "dhash", 'params': [0.9]}, {'name': "sift", 'params': [16, 1.6, 10, 3, 0.04, 0.1]}],
    accuracy_calculator=accuracy_calculator,
    presets=permutation.presets['california'],
    foldername="california-phash-dhash-sift"
  )

parameter_tuning_phash()

# permutation.experiment(
#   dataset=dataset,
#   dataset_size=701,
#   accuracy_calculator=accuracy_calculator,
#   presets=permutation.presets['california'],
#   foldername="california-experiment"
# )