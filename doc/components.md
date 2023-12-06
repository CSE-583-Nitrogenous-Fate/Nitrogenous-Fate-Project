### Components ###
The Nitrogenous Fate Software uses metabolite data of isotopically-labeled molecules (Nitrite, Ammonia, and Urea) through incubations from samples in the equatorial Pacific to show pathways of nitrogen within communities through simple data visualization.
Based on the following use cases the following components are defined:
* Data Cleaning and Wrangling
* Data Processing 
* Data Visualization

These components are used together in separate scripts to be used for the two different datasets that can be analyzed in this software package - one for Dissolved (exo) and Particulate (endo) metabolite.

| Name  | Function               | Inputs            | Output                 | Interactions            |
|--------------------|------------------------|------------------------|------------------------|------------------------|
| Data Cleaning and Wrangling (Section I) | A `dataset` is loaded (either dissolved, exo or particulate, endo) and this component looks for relevant data (by column) from the data set. The script then calculates values for the following new columns which are appended to the `dataset` under a new file named `*_clean_areas.csv`: `filename`, `compound_name`, and `area`. It then computes an internal standard which is used to normalize data for use in section II, it creates two new columns for these values: `compoundname_IS` and `area_IS`, which are appended to the `dataset` under a new file names `*_IS_list.csv`.  | run nfex `Section I script` with correct data in `data_raw` folder | component will output two `new datasets`: `*_clean_areas.csv` for new columns with values for: `filename`, `compound_name`, and `area`; and `*_IS_list.csv` for new columnns with values for: `compoundname_IS` and `area_IS`. | User monitors for any errors |
| BMISED Computation (Section II) | The two `new dataset` which now contains values in the new columns: `filename`, `compound_name`, `area`, `compoundname_IS` and `area_IS` is used to calculate BMISED values.  These values are placed in a new column: `bmised_area` and is saved in a dataset named `*_bmisedareas.csv`. | run nfex `Section II script` with correct data in `intermediates` folder | component will output a `new dataset`: `*_bmisedareas.csv` for values in the new column: `bmised_area`  | User monitors for any errors |
| Data Visualization (Section III) | The `new dataset` which now contains values in the new column `bmised_area` is used to generate data visualization. The script generates two data visualization files. | run nfex `Section III script` with correct data in `intermediates` folder | component will output two image files: `*_1.png` and `*_2.png` to `intermediates` folder | User monitors for any errors |


In total there will be five Python scripts in this package. A Section I and Section II script each for Dissolved (exo) and Particulate (endo) metabolite data sets and one script for Section III Data Visualization. The figure below visualizes the components process flow.

![NFEX Project Components Relationships](https://www.websequencediagrams.com/cgi-bin/cdraw?lz=dGl0bGUgTkZFWCBQcm9qZWN0IENvbXBvbmVudCBSZWxhdGlvbnNoaXBzCgpVc2VyLT4qU29mdHdhcmU6IFVzZXIgcnVucwA8BQoKbm90ZSByaWdodCBvZiAAHgpDaGVja3MgYXJlIG1hZGUgdG8gZGF0YQoKAEMILT4qU2VjdGlvbiBJOiAAAgkgc2NyaXB0AF4FAFcHb3ZlcgAXCjogRGF0YSBpcyBjbGVhbmVkIGFuZCB3cmFuZ2xlZACBABEATwkKY29sdW1ucyBjcmVhdGVkOiAKZmlsZW5hbWUsIGNvbXBvdW5kXwAJBmFyZWEKbmV3IGNzdiBmaWxlIGlzAIFBBmZyb20gb3JpZ2luYWwAGgUKYW5kIGlzIGFwcGVuZGVkIHdpdGg6IF8AgRkFX2FyZWFzLmNzdgplbmQgbm90ZQB1LQCBEAhuYW1lX0lTAIEUBl9JUwBdQElTX2xpc3QAgQoPAIMHCS0-AINnCgCDCQcAgjAGcyAyIG5ldyBDU1YAghMFcyAAg3sGbGVmAIJhDgpvdXRwdXQAHwY6ICoAgX8QAIIxBioAchcAhG4IAIQYCEkAhGwMAAwKAIQlBwCEEhVJIAoKQk1JU0VEAINJBQCEKwVhbGN1bGF0ZWQKAINCBQCEagoAgSEMAIMHIkkAhEQHAIRBCQpibWlzZWQAg2gFAIN3QABFBgCEIxQAggQKAIMEGzEAgnkmSToAgWgMOiAqAGcRAIJyEgCCbhcAgmgeSQoAhyYIdmlzdWFsaXplZAp1c2luZwCDPAwAgmkXAHELLT5Vc2VyAIUFCWdlbmVyAIULBWRhdGEAUwkAiTUFAIFbGACBYhIxLnBuZwCIOgUqXzIucG5nCgo&s=default "NFEX Project Component Process Flow")

Document Information: CSE583 NF Project Documentation for Components
