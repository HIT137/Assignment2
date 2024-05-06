import pandas as pd
import re

text_list = []
for file_path in [
    r'/Users/admin/Sami/Study CDU/HIT 137/Assignment 2/CSV1.csv',
    r'/Users/admin/Sami/Study CDU/HIT 137/Assignment 2/CSV2.csv',
    r'/Users/admin/Sami/Study CDU/HIT 137/Assignment 2/CSV3.csv',
    r'/Users/admin/Sami/Study CDU/HIT 137/Assignment 2/CSV4.csv'
]:
    df = pd.read_csv(file_path)
    
    if 'TEXT' in df.columns:
        text_list.extend([text.replace('\n', ' ') for text in df['TEXT'].tolist() if pd.notna(text)])
    else:
        print("Warning: 'TEXT' column not found in", file_path)
cleaned_text = ' '.join([re.sub(r'\b[a-zA-Z]{4,}\b', ' ', text) for text in text_list])

with open(r'/Users/admin/Sami/Study CDU/HIT 137/Assignment 2/CLEANED_TEXT.txt', 'w+') as f:
    f.write(cleaned_text)

print("DONE")
