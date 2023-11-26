import pandas as pd
import os

df = pd.read_csv('../data/bd2_files_for_mila.csv')

# create a directory to save the txt files
output_folder = '../data/label_txt_files'
os.makedirs(output_folder, exist_ok=True)

# Iterate over the input files in the 'input_file' column, sliced the data based on unique input_file,
# and create corresponding the duplicated txt files
for input_file in df['input_file'].unique():
    sliced_df = df[df['input_file'] == input_file]

    duplicated_df = sliced_df.loc[sliced_df.index.repeat(2)].reset_index(drop=True)

    txt_filename = f'{input_file[-20:-4]}.txt'
    txt_file_path = output_folder + txt_filename

    duplicated_df.to_csv(txt_file_path, sep='\t', index=False)
