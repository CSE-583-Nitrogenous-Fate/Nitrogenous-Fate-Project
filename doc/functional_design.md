### Functional Design for NF Software ###
The Nitrogenous Fate Software uses metabolite data of isotopically-labeled molecules (Nitrite, Ammonia, and Urea) through incubations from samples in the Equatorial Pacific to show pathways of nitrogen within communities through simple data visualization.
The following table shows the preliminary functional design crafted by the team:

| Functional Design  | Use Case               | Description            | Prompt                 |
|--------------------|------------------------|------------------------|------------------------|
| Run Program | Program Terms of Use | Show Instructions (Functional Description, Process Diagram), Disclosure,  and Terms of Use | Yes / No Prompt: 'Understood and Proceed'|
|| Input Data Set | Loads data file based on run command checks for data format | May raise exceptions when encountered  |
||| User provides _unacceptable_ data set | Display: 'File not accepted, please check file type'; exit program|
| Run program _as is_ | Choose Standard Operation | Use app without customization |  Selection to choose: 'Default Settings' |
| or _with customization_ | Choose Custom Operation | Use app with customization | Selection to choose: 'Use Custom Settings' |
||| Setting configuration for changing parameter type and other settings | Display 'settings options' |
||| Set custom settings for operation | Provide prompt to enter values for settings |
|| Data Set Processing | scripts runs using either customization or without customizations. ||
||| _Section I: Data Cleaning and Organization_ |  |
||| _Section II: Best Matched Internal Standard Normalization_ |  |
||| _Section III: Data Visualization_ |  |
||| Data analysis encounters an error | raise Exception or display Error, write error log |
||| Data analysis is successful | Display: 'Analysis completed' save output files.
| User Feedback | Monitoring & Evaluation | Provides feedback mechanism for errors and improvements to program | Display link to raise an issue on Github repository  |
| End Program | Terminate Program | Safely terminate program and show credits | Display thank you prompt with credits, then exit app.|

Version 0.1 of this software implements only the following functional design for nitrogenousfate.py:
| Functional Design  | Use Case               | Description            | Prompt                 |
|--------------------|------------------------|------------------------|------------------------|
| Run Program | Input Data Set | Loads data file based on run command checks for data format | May raise exceptions when encountered  |
|| Data Set Processing | scripts runs using either customization or without customizations. ||
||| _Section I: Data Cleaning and Organization_ |  |
||| _Section II: Best Matched Internal Standard Normalization_ |  |
||| Data analysis encounters an error | raise Exception or display Error, exit program |
||| Data analysis is successful | Display: 'Analysis completed' save output files. |
| End Program | Terminate Program | Safely terminate program and show credits | Display thank you prompt with credits, then exit app.|

Section III is handled by a Jupyter Notebook.

Document Information: CSE583 NF Project Documentation for Functional Design
