import pandas as pd
import os

df = pd.read_csv('data/bd2_files_for_mila.csv', index_col=0)
df.rename(columns={'start_time': 'Begin Time (s)'}, inplace=True)
df.rename(columns={'end_time': 'End Time (s)'}, inplace=True)
df.rename(columns={'low_freq': 'Low Freq (Hz)'}, inplace=True)
df.rename(columns={'high_freq': 'High Freq (Hz)'}, inplace=True)

# create a directory to save the txt files
output_folder = 'data/label_txt_files'
os.makedirs(output_folder, exist_ok=True)

# Iterate over the input files in the 'input_file' column, sliced the data based on unique input_file,
# and create corresponding the txt files
for input_file in df['input_file'].unique():
    sliced_df = df[df['input_file'] == input_file]

    txt_filename = f'{input_file[-20:-4]}.txt'
    txt_file_path = output_folder + txt_filename

    sliced_df.to_csv(txt_file_path, sep='\t', index=False)
