import numpy as np
import os
import json
from collections import defaultdict

script_dir = os.path.dirname(os.path.abspath(__file__))

def parse_groups(file_path):
    """ Parse the near-duplicate groups from a given file. """
    groups = []
    with open(file_path, 'r') as file:
        line_number = 0
        for line in file:
            line_number += 1
            try:
                group = set()
                items = line.strip().split(',')
                for item in items:
                    if '-' in item:
                        start, end = item.split('-')
                        group.update(range(int(start), int(end) + 1))
                    else:
                        group.add(int(item))
                groups.append(frozenset(group))  # Use frozenset for immutability
            except ValueError as e:
                print(f"Error parsing line {line_number} in file {file_path}: {line}")
                print(f"Error: {e}")
    return groups

def load_annotations(folder_path):
    """ Load all annotation files and return a list of sets. """
    all_groups = []
    for filename in os.listdir(os.path.join(script_dir, folder_path)):
        if filename.endswith('.txt'):
            file_path = os.path.join(script_dir, folder_path, filename)
            groups = parse_groups(file_path)
            all_groups.extend(groups)
    return all_groups

# Load annotations
folder_path = 'Individual annotations'
annotations = load_annotations(folder_path)

# Determine the most common grouping for each photo number
group_count = defaultdict(int)
for group in annotations:
    group_count[group] += 1

# Determine the groups that appear most frequently
median_groups = []
group_seen = set()

for group, count in sorted(group_count.items(), key=lambda x: -x[1]):
    if not group_seen.intersection(group):
        median_groups.append(group)
        group_seen.update(group)

# Convert sets to lists for JSON serialization and format numbers with leading zeros
median_groups_formatted = []
output = {
    'paths': [],
    'groups': [],
    'map': {}
}

groupindex = -1
for group in median_groups:
    groupindex += 1
    formatted_group = []
    for photo in group:
        formatted = f"datasets/california/californiaND/Photos/{photo:03}.jpg"
        output['paths'].append(formatted)
        output['map'][formatted] = groupindex
        formatted_group.append(formatted)
    
    output['groups'].append(formatted_group)

    # formatted_group = [f"{photo:03}" for photo in group]  # Format as three-digit numbers
    # median_groups_formatted.append(formatted_group)

# Save results
output_file_path = 'output.json'
with open(os.path.join(script_dir, output_file_path), 'w') as file:
    json.dump(output, file)

# print("Median groups saved to:", output_file_path)
