import pandas as pd
import os

df = pd.read_csv('data/selection_under_randomization_file.csv')
df['Name'] = df['File path'].str[-19:-4]

selected_columns = ['Site name', 'Month', 'Condition', 'Name']
record_df = df[selected_columns]

# check whether the WAV and txt folders contain the selected files using the file names
wav_folder_path = 'data/selected_WAV_files'
wav_file_names = os.listdir(wav_folder_path)
wav_file_names = [name[:-4] for name in wav_file_names]

txt_folder_path = 'data/label_txt_files'
txt_file_names = os.listdir(txt_folder_path)
txt_file_names = [name[:-4] for name in txt_file_names]

record_df['Has WAV file'] = record_df['Name'].isin(wav_file_names)
record_df['Has txt file'] = record_df['Name'].isin(txt_file_names)
record_df['Finish manual labeling?'] = False

record_df.to_csv('data/labeling_progress_record.csv', index=False)