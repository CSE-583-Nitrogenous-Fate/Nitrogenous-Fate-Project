"""
This module...
"""

import numpy as np
import pandas as pd
import re
import sys

def process_csv(csv_file):
    try:
        # Read the CSV file into a pandas dataframe
        transition_list = pd.read_csv(csv_file)

        clean_areas = transition_list[['Replicate Name', 'Precursor Ion Name', 'Area']] \
            .rename(columns={'Replicate Name': 'filename', 'Precursor Ion Name': 'compound_name', 'Area': 'area'})

        clean_areas['cmpd_type'] = clean_areas['compound_name'].apply(lambda x: 'IS' if re.search('A', x) else 'Non-IS')
        clean_areas['area'] = pd.to_numeric(clean_areas['area'], errors='coerce')
        clean_areas['samp_type'] = clean_areas['filename'].apply(lambda x: re.search(r'Poo|Blk|Smp|Std', x).group() if re.search(r'Poo|Blk|Smp|Std', x) else None)
        clean_areas['day'] = clean_areas['filename'].apply(lambda x: int(re.search(r'T\d+', x).group()[1:]) if re.search(r'T\d+', x) else None)
        clean_areas['filename'] = clean_areas['filename'].astype('category')
        clean_areas = clean_areas.sort_values(by=['compound_name', 'filename'])

        IS_list = clean_areas[clean_areas['cmpd_type'] == "IS"]
        IS_list = IS_list.rename(columns={"compound_name": "compound_name_IS", "area": "area_IS"})
        IS_list = IS_list[['filename', 'compound_name_IS', 'area_IS']]

        # Filter clean_areas for cmpd_type=="Non-IS"
        filtered_areas = clean_areas[clean_areas['cmpd_type'] == "Non-IS"]

	# Select relevant columns
        filtered_areas = filtered_areas[['filename', 'compound_name', 'area']]

	# Perform left join with filtered areas again
        merged_areas = pd.merge(filtered_areas, IS_list[['filename', 'compound_name_IS', 'area_IS']], on=['filename'], how='left')

        merged_areas['bmis_area'] = merged_areas['area'] / merged_areas['area_IS']

        mean_area_IS_14_to_44 = merged_areas['area_IS'].iloc[14:45].mean()

        # Multiply the new column with the mean of 'area_IS' (rows 14 through 44)
        merged_areas['result_column'] = merged_areas['bmis_area'] * mean_area_IS_14_to_44

        # Save merged_areas as a CSV file
        merged_areas.to_csv('_bmised_areas.csv', index=False)

        return merged_areas

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py path_to_csv_file")
    else:
        csv_file_path = sys.argv[1]
        result = process_csv(csv_file_path)
        if result is not None:
            print(result)
