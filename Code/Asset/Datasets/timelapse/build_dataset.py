import cv2
import sys
import os

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
def group_frames(relative_directory, threshold):
  frameindex = 0

  directory = os.path.normpath(os.path.join(current_script_dir, relative_directory))

  dataset = {
    paths: [],
    results: {}
  }

  firstgroupindex = 0

  for entry in os.listdir(directory):
      # Construct the full path to the entry
      full_path = os.path.join(directory, entry)

      if os.path.isfile(full_path):

          dataset.paths.append(full_path)
          dataset.results[full_path] = 
          frameindex += 1

def main():
  group_frames("multiple-timelapse/00", 1)  


main()