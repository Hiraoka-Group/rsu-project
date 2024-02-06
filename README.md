# RSU Analyzer

RSU Analyzer is a Python project intended for chemical research, particularly focusing on analyzing RSU (Ring Strain per Unit). RSU serves as an indicator for estimating purely geometric strains in rings present in assemblies such as Pd6L4, Pd9L6, and Pd12L8. For more details, please consult the associated research paper.

This project offers:
- Tools for calculating RSU
- Analysis of RSU data
- Visualization of chains using matplotlib 3D plots

## About
This project is developed by the Hiraoka Laboratory at The University of Tokyo.

## Installation
To install the project, follow these steps:

1. Clone this repository:
```bash
git clone https://github.com/neji-craftsman/rsuanalyzer.git
```
2. Navigate to the project directory:
```bash
cd rsuanalyzer
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Execution
### Case 1: Reproducing Results from the Paper
Scripts for reproducing results from the paper are located in the analysis directory.

Each module within the analysis directory should be executed as follows:
```bash
python3 -m analysis.chain_visualization.src.alts_theta0
```
It's important to execute each module from the project's root directory. Running modules directly from their respective directories (such as the 'src' directory in this case) may lead to import errors.

### Case 2: Applying the Analysis to Your Original Assemblies
You can utilize the analysis by employing the `rsuanalyzer` and `chainvisualizer` packages. Please refer to the scripts in the `analysis` directory.

## Usage
[Add usage instructions here, including command-line tool usage or library interface.]

## License
This project is licensed under the MIT License. See the LICENSE file for details.
