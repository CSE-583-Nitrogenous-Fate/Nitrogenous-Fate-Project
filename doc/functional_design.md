### Use Case Characterization ###
The Nitrogenous Fate Software uses metabolite data of isotopically-labeled molecules (Nitrite, Ammonia, etc.) through incubations from samples in the equatorial Pacific to show pathways of isotopically labeled nitrogen within communities through simple data visualization.
Identified Users included:
* Research Scientist (Marine Biologist)
* Research Scientist (Generic)
* Research Scientist (Administrator)
* Researcher

| Functional Design  | Use Case               | Description            | Prompt                 |
|--------------------|------------------------|------------------------|------------------------|
| Use Program | Start Program | Show Instructions (Functional Description, Process Diagram), Disclosure,  and Terms of Use | Display button: 'Understood and Proceed'|
| Run program _as is_ | Choose Standard Operation | Use app without customization |  Display button: 'Use Default Settings' |
| or _with customization_ | Choose Custom Operatoin | Use app with customization | Display button: 'Use Custom Settings' |
||| Settings configuration panel for changing parameter type and other settings | Display settings configuration panel |
||| Set custom settings for operation | Display button: 'Confirm custom settings' |
|| Input Data Set | User uploads data set file with prompt for accepted file types | Display button: 'Upload file' |
|| Input Data Set | User provides _acceptable_ data set | Display: 'File accepted' |
||| User provides _unacceptable_ data set | Display: 'File not accepted, please check file type'; return to Input Data Set 'Upload file'|
|| Data Set Processing | User adjusts parameter-based settings and other analysis configurations. Default options are set for basic users. | Display parameter-based settings configuration panel; Display button: 'Confirm settings and run analysis' |
||| Data analysis encounters an error | Display: 'Error occured. Please check log file.' |
||| Download Log File for error | Display button: 'Download log file'; display button: 'try new data set', return to 'Upload File'; display button: 'try new customization', return to _Run Program_ function; Display button: 'Send error log and provide feedback', send to _User Feedback_ function |
||| Data analysis is successful | Display: 'Analysis completed' and show summary of results; Display button: 'Download analysis'; Display button: 'Download Visualizations'; Display button: 'Download entire results package (compressed file)' |
| User Feedback | Monitoring & Evaluation | Provides feedback mechanism for errors and improvements to program | Display comment box: 'Provide feedback'; Display button: 'Upload error log file', automatically append log file as default action |
| End Program | Terminate Program | Safely terminate program and show credits | Display thank you prompt with credits, then exit app.|

Document Information: CSE583 NF Project Documentation for Functional Design
