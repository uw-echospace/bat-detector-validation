import csv
import os

# path to the randomized csv file
csv_file = 'randomization/selection_under_randomization_file.csv'
# alias + bucket name in format 'alias:/bucket_name'
bucket_name = 'something you need to change'
# path to the folder that you want to save
save_folder = 'something you need to change'

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # find the 'Sliced File Path' column in the randomized file
        # 'Sliced File Path' has the format: ubna_data_###/recover-###/UBNA_###/###_###.WAV
        path = row['Sliced File Path']

        # build and execute the rclone command
        rclone_command = f"rclone copy {bucket_name}/{path} {save_folder}"
        os.system(rclone_command)
