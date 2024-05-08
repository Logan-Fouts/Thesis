import permutation

dataset = permutation.get_dataset("california/output.json")

def accuracy_calculator(duplicate_groups, non_duplicate_list, lonely_imgs):
  tp = 0
  fp = 0
  tn = 0
  fn = 0

  for list in duplicate_groups:
    groups = {}

    # keep track of the most common 
    maxmap = {
      value: 0,
      index: -1
    }
    for path in list:
      index = dataset['map'][path]

      if index not in groups:
        groups[index] = 0

      groups[index] += 1

      if groups[index] > maxmap['value']:
        maxmap['value'] = groups[index]
        maxmap['index'] = index

    # treat most common group as the main group 
    tp += maxmap['value']

    # put the remaining into false positives 
    for group_index, count in groups.items():
      if group_index != maxmap['index']:
        fp += count 

  # now lets check the tn & fn by checking non_duplicate_list
  for path in non_duplicate_list:
    grouplength = len(dataset['groups'][dataset['map'][path]])
    if grouplength == 1:
      tn += 1
    else:
      fn += 1

  return tp, fp, tn, fn
    

print("running california experiment")

permutation.experiment(
  dataset=dataset,
  dataset_size=701, 
  accuracy_calculator=accuracy_calculator,
  presets=permutation.presets['california'],
  foldername="california-701"
)