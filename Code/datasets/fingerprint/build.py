import json 
import os 

current_script_dir = os.path.dirname(os.path.abspath(__file__))

directory = os.path.normpath(os.path.join(current_script_dir, "../../Images/Finger_Prints/Altered/Altered-Easy"))
output_json = os.path.join(current_script_dir, "output.json")

image_paths = sorted(os.listdir(directory))
dataset = {
  'paths': [],
  'groups': [],
  'map': {}
}

index_map = {}
for entry in image_paths:
  image_path = os.path.join(directory, entry)

  group = "_".join(os.path.basename(image_path).split("_")[:5])
  if group not in index_map:
    index_map[group] = len(dataset['groups'])
    dataset['groups'].append([])
  
  index = index_map[group]
  dataset['groups'][index].append(image_path)
  dataset['map'][image_path] = index
  dataset['paths'].append(image_path)


with open(output_json, 'w') as file:
  json.dump(dataset, file)

