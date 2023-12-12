"""
This module executes Section I and II of the nfex program
components to calculate BMISED areas ready for visualization.
Section I code does data cleaning and wrangling. Section II code
does calculations for BMISED areas.

The associated script accepts comma separated value files (.csv).
This module uses pandas to clean the data and organize them for
formatting and calculations to internal standard. This produces
BMIS (best-match internal standard) values which can be used for
data visualization.

Attributes
----------

transition_list
    these are the data read from the original csv file provided.
clean_areas : str or int
    these are data taken from the transition_list that is formatted for use.
filename
    this is data taken from the column 'category' in the transition_list.
    it is also extracted by matching any of four possibel values: Poo, Blk,
    Smp, or Std; and replacing with None if there is no match.
    this is used for the Internal Standard.
compound_name
    this is data from transition_list 'comound_name' that is formatted as
    an internal standard.
area_is
    this is data from transition_list 'area'converted to numeric type, any
    invalid values are also replace with NaN for consistent data analysis.
    this is used for the Internal Standard.
compound_name_is
    this is renamed from 'compound_name' for use in the Internal Standard.
area_is
    this is renamed from the 'area' for use in the Internal Standard

Methods
-------

filtered_areas
    using 'cleaned_areas', this makes a dataframe that removes Non-IS.

is_list
    using 'cleaned_areas', this is all the dataframe related to values
    that have been formatted to be matched with the Internal Standard.

merged_areas
    filtered_areas and is_list
"""

import re
import sys
import pandas as pd  # pylint: disable=E0401
from pandas.api.types import is_numeric_dtype  # pylint: disable=E0401

def process_csv(csv_file):
    """
    This function completes Section I of the normalization workflow.

    Parameters
    ----------
    transition_list
        these are the data read from the original csv file provided.
    clean_areas : str or int
        these are data taken from the transition_list that is
        formatted for use.
    filename
        this is data taken from the column 'category' in the transition_list.
        it is also extracted by matching any of four possible values: Poo, Blk,
        Smp, or Std; and replacing with None if there is no match.
        this is used for the Internal Standard.
    compound_name
        this is data from transition_list 'comound_name' that is formatted as
        an internal standard.
    area_is
        this is data from transition_list 'area'converted to numeric type, any
        invalid values are also replace with NaN for consistent data analysis.
        this is used for the Internal Standard.
    compound_name_is
        this is renamed from 'compound_name' for use in the Internal Standard.
    area_is
        this is renamed from the 'area' for use in the Internal Standard

    Returns
    -------
    return merged_areas
        this returned the values of BMIS, which are the normalized
        values for the best-matched internal standard which can be
        used for visualization. A comma separated value file is
        created with this BMIS information.

    Raises
    ------
    EmptyFileError
        when the csv file contains no data.
    FileNoteFoundError
        when the csv file cannot be found.
    ValueError
        when an exception is raised due to incorrect data type,
        'Retention Time', 'Area', 'Background', or 'Height' is
        not numeric.
    """

    try:
        # Read the CSV file into a pandas dataframe
        transition_list = pd.read_csv(csv_file)
    except pd.read_csv(csv_file).empty:
        raise EmptyFileError("The CSV file contains no data.")
    except FileNotFoundError:
        raise FileNotFoundError("The CSV file could not be found.")
    except Exception:
        raise ValueError("The data in the CSV file is incorrect.")

    if not is_numeric_dtype(transition_list['Retention Time']):
        raise ValueError(
              "Retention Time in transition list should be numeric.")

    if not is_numeric_dtype(transition_list['Area']):
        raise ValueError("Area in transition list should be numeric.")

    if not is_numeric_dtype(transition_list['Background']):
        raise ValueError(
              "Retention time in transition list should be numeric.")

    if not is_numeric_dtype(transition_list['Height']):
        raise ValueError("Height in transition list should be numeric.")

    clean_areas = transition_list[['Replicate Name',
                                   'Precursor Ion Name',
                                   'Area']] \
        .rename(columns={'Replicate Name': 'filename',
                         'Precursor Ion Name': 'compound_name',
                         'Area': 'area'})

    clean_areas['cmpd_type'] = clean_areas['compound_name'].apply(lambda x:
                                   'IS' if re.search('A', x) else 'Non-IS')

    clean_areas['area'] = pd.to_numeric(clean_areas['area'],
                                        errors='coerce')

    clean_areas['samp_type'] = clean_areas['filename'].apply(lambda x:
                               re.search(r'Poo|Blk|Smp|Std', x).group()
                                   if re.search(r'Poo|Blk|Smp|Std',
                                                x) else None)

    clean_areas['day'] = clean_areas['filename'].apply(lambda x:
                             int(re.search(r'T\d+', x).group()[1:])
                             if re.search(r'T\d+', x) else None)

    clean_areas['filename'] = clean_areas['filename'].astype('category')

    clean_areas = clean_areas.sort_values(by=['compound_name', 'filename'])

    is_list = clean_areas[clean_areas['cmpd_type'] == "IS"]

    is_list = is_list.rename(columns={"compound_name": "compound_name_IS",
                                      "area": "area_IS"})

    is_list = is_list[['filename', 'compound_name_IS', 'area_IS']]

    # Filter clean_areas for cmpd_type=="Non-IS"
    filtered_areas = clean_areas[clean_areas['cmpd_type'] == "Non-IS"]

    # Select relevant columns
    filtered_areas = filtered_areas[['filename', 'compound_name', 'area']]

    # Perform left join with filtered areas again
    merged_areas = pd.merge(filtered_areas,
                            is_list[['filename',
                                     'compound_name_IS',
                                     'area_IS']],
                            on=['filename'], how='left')

    merged_areas['bmis_area'] = merged_areas[
                                    'area'] / merged_areas['area_IS']

    mean_area_is_14_to_44 = merged_areas['area_IS'].iloc[14:45].mean()

    # Multiply the new column with the mean of 'area_IS' (rows 14-44)
    merged_areas['result_column'] = merged_areas[
                                        'bmis_area'] * mean_area_is_14_to_44

    # Save merged_areas as a CSV file
    merged_areas.to_csv('merged_areas.csv', index=False)

    return merged_areas

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py path_to_csv_file")
    else:
        csv_file_path = sys.argv[1]
        result = process_csv(csv_file_path)
        if result is not None:
            print(result)
