import cv2
import sys
import os
import math 
import json

current_script_dir = os.path.dirname(os.path.abspath(__file__))


def video_to_frames(video_file_path, output_dir):
    # Make sure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Capture video
    video = cv2.VideoCapture(video_file_path)
    success, image = video.read()
    count = 0
    
    while success:
        # Save frame as JPEG file
        cv2.imwrite(os.path.join(output_dir, f"frame{count}.jpg"), image)
        success, image = video.read()
        print(f'Read a new frame: {success}, count: {count}')
        count += 1


def run_video_to_frames():
  video_file_path = os.path.normpath(os.path.join(current_script_dir, 'multiple-timelapse-set', 'multiple-timelapse-240.mp4'))
  output_dir = os.path.normpath(os.path.join(current_script_dir, 'output'))

  # run the main function with params 
  video_to_frames(video_file_path, output_dir)


# this function would group frames into smaller groups based on threshold,
# this means, if set contains 100 images and threshold is 10%, we can expect 10 groups containing 10 frames each 
def group_frames(directory, threshold):
  frameindex = 0

  dataset = {
    'paths': [],
    'groups': {},
    'map': {}
  }

  entries = sorted(os.listdir(directory))
  size = len(entries)

  poolsize = max(1, math.floor(size * threshold))
  number_of_pools = math.ceil(size / poolsize)
  poolindex = 0

  for entry in entries:
    # Construct the full path to the entry
    full_path = os.path.join(directory, entry)

    if os.path.isfile(full_path):
      dataset['paths'].append(full_path)
      # poolindex = frameindex % number_of_pools

      if poolindex not in dataset['groups']:
        dataset['groups'][poolindex] = []

      dataset['groups'][poolindex].append(full_path)
      dataset['map'][full_path] = poolindex

      frameindex += 1

      if len(dataset['groups'][poolindex]) > number_of_pools:
        poolindex += 1

  return dataset

def build_multiple_timelapse_set(threshold = 0.1, name = "high"):
  directory = os.path.normpath(os.path.join(current_script_dir, "multiple-timelapse"))
  output_json = os.path.join(directory, f"{name}fit.dataset.json")

  sets = {}

  for entry in sorted(os.listdir(directory)):
    full_path = os.path.join(directory, entry)

    if os.path.isdir(full_path):
      sets[entry] = group_frames(full_path, threshold)

  with open(output_json, 'w') as file:
    json.dump(sets, file)


def main():
  # build high fit dataset 
  build_multiple_timelapse_set(0.06, "high")

  # build low fit dataset 
  build_multiple_timelapse_set(0.25, "low")

main()