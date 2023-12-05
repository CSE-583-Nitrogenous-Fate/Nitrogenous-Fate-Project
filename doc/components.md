### Components ###
The Nitrogenous Fate Software uses metabolite data of isotopically-labeled molecules (Nitrite, Ammonia, and Urea) through incubations from samples in the Equatorial Pacific to show pathways of nitrogen within communities through simple data visualization.
Based on the following use cases the following components are defined:
* Start Program
* Choose Operation Mode (Standard or Custom)
* Input Data Set
* Data Processing 
    * Section I: Data Cleaning and Organization
    * Section II: Parameter Setting
    * Section III: Best Matched Internal Standard Normalization
    * Section IV: Quantification
* Data Visualization
* Monitoring & Evaluation
* Terminate Program

| Name  | Function               | Inputs            | Output                 | Interactions            |
|--------------------|------------------------|------------------------|------------------------|------------------------|
| Start Program | This displays a welcome screen displaying the function of the software and prompting the user to accept a Terms of Use before proceeding. | Boolean: True or False | If False, _'Terminate Program'_; If True, _choose operation mode (standard or custom)_ | Write User Input into Log |
| Choose Operation Mode | This displays a screen for the user to select either standard operation or custom operation. | Boolean: Standard (True) or Custom (False) | If Standard (True), continue with _'Input Data Set'_; If Custom (False), continue with _'Input Data Set' with customization_ |||
| Input Data Set | This displays a short descrsiption of accepted file types and a button for the user to upload data and then validates the file format and content upon upload.  | File, types: *.csv | Boolean: If Validated (True), continue to ''  |  |
| Data Processing: Section I |  |  |  |  |  |
| Data Processing: Section II |  |  |  |  |
| Data Processing: Section III |  |  |  |  |
| Data Processing: Section IV |  |  |  |  |
| Data Visualization |  |  |  |  |
| Monitoring & Evaluation |  |  |  |  |
| Terminate Program |  |  |  |  |

Document Information: CSE583 NF Project Documentation for Components
