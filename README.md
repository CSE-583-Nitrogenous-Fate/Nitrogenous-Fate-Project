# _**NitrogenousFate**_
---

The Nitrogenous Fate Software is a tool that `normalizes data` to minimize the effects of obscuring variation and `quantifies metabolite production` rates in the environment.  It uses metabolite data of isotopically-labeled molecules (`Nitrite, Ammonia, and Urea`) through incubations from samples in the equatorial Pacific to show pathways of nitrogen within communities through simple `data visualization`. The current version is 0.1.

### Historical background
---
In 2023, the Ingalls lab carried out incubations with added 15NH4+, 15NO3- and 15N13C urea in deck incubations in the equatorial Pacific. The team handling these experiments measured the rate of intracellular and dissolved metabolite production in these samples by tracking the isotope label through community metabolism over time. Obscuring variations are a common challenge when doing such experiments and data normalization is a method to reduce these effects.

Helpful academic papers to expand this background are the following:

_On the CX-SPE Method_
* [Sacks, J.S., _et al._(2022) Quantification of dissolved metabolites in environmental samples through cation-exchange solid-phase extraction paired with liquid chromatography–mass spectrometry, _Limnology and Oceanography: Methods_, 20(11), p683-700.](https://aslopubs.onlinelibrary.wiley.com/doi/full/10.1002/lom3.10513)

_On marine microbial metabolites_
* [Moran, A.M., _et al_ (2022) Microbial metabolites in the marine carbon cycle, _Nature Microbiology_, 7, p508-523.](https://www.nature.com/articles/s41564-022-01090-3)
 
_On BMIS (Best-Matched Internal Standard Normalization in Liquid Chromatography−Mass Spectrometry Metabolomics Applied to Environmental Samples_
* [Boysen, A.K., _et al_ (2018) Best-Matched Internal Standard Normalization in Liquid
Chromatography−Mass Spectrometry Metabolomics Applied to Environmental Samples, _Analytical Chemistry_, 90, p1363-1369.](https://pubmed.ncbi.nlm.nih.gov/29239170/)

### Mission
---
NitrogenousFate hopes to assist marine biology researchers who use normalized data to quantify metabolite production rates in the environment in a convenient, replicable, and transparent manner that provides beautiful visualizations that researchers can use to better disseminate their results to the public.

### Project Objective
---
This project's objective is to assist marine biology researchers in normalizing peak concentrations for Ammonia, Nitrate, and Urea from particulate and dissolved sample data and producing visualizations for the results.

### Current Version Status
---
The following is included in this version 0.1:
* basic functions for Marine Biologist Research Scientist which is the ability to run calculations for Best-Matched Internal Standard Normalization and provide visualizations)

Future versions of this tool may include the following:
* a user-friendly graphical user interface
* customizations to parameters
* expanded visualizations

### Repository Structure
 ```
.
├── data_raw
├── doc
├── nfex
│   ├── assets
│   ├── notebook
│   ├── visual
│   └── test
├── LICENSE
├── README.md
└── environment.yml
 ```

### Installation
---
NitrogenousFate is installed using the command line and is best used with a virtual environment due to its dependencies.
1. Open your choice of terminal 
2. Clone the repository using `git clone git@github.com:CSE-583-Nitrogenous-Fate/Nitrogenous-Fate-Project.git`
3. Change to the NitrogenousFate directory using `cd Nitrogenous-Fate-Project`
4. Set up a new virtual environment with all the necessary packages and their dependecies using `conda env create -f environment.yml`
5. Activate the NitrogenousFate virtual environment with `conda activate nfex`
6. Deactivate the NitrogenousFate virtual environment using `conda deactivate`

### Requirements
---
NitrgenousFate requires python 3.11 with the following packages installed:
1. OS
2. Pandas
3. Inquirer
4. Win32.com.client
2. Matplotlib
3. Seaborne
4. Vega-Altair

### Usage
---
#### Tool
The NitrogenousFate contains two specific modules that each contain a class of functions for data processing and data visualization.

#### Use Cases
Marine Biologists who conduct research on the science of metabolites in ocean waters have large data sets for nitrogenous pathways that require processing so that results can be shared amongst other scientists; these results can be expressed through data visualization that is friendly for the public. Read more about the [user stories here](https://github.com/CSE-583-Nitrogenous-Fate/Nitrogenous-Fate-Project/blob/main/doc/functional_design.md).

### Requests
---
If you ideas for features to extend the functionality of  future versions of NitrogenousFate please feel free to raise an [issue](https://github.com/CSE-583-Nitrogenous-Fate/Nitrogenous-Fate-Project/issue).

### Bug Report
---
The current version published has been tested to be stable. However, If you have encountered a bug or issue and would like to report a bug or issue, please submit detailed report [here](https://github.com/CSE-583-Nitrogenous-Fate/Nitrogenous-Fate-Project/issue/new). 

### Contributions
---
If you would like to expand on NitrogenousFate please fork the repository, add your contribution, and generate a pull request. A complete list of contributors can be found [here](https://github.com/CSE-583-Nitrogenous-Fate/Nitrogenous-Fate-Project/blob/main/doc/CONTRIBUTORS.md). This project oprates under the [Contributor Code of Conduct](https://www.contributor-covenant.org/version/1/0/0/code-of-conduct/) 

### Acknowledgements
---
The NitrogenousFate Team would like to thank Dr. David Beck and Evan Komp from the University of Washington for their support, guidance, and feedback in the development of this package.
