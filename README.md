# NBA Player Season Stats Downloader

This script allows you to download NBA player season stats for a specified season using the NBA API.

## Prerequisites
- Python 3.x
- `nba_api` library
- `pandas` library

# Setting Up Virtual Environment
# It's recommended to use a virtual environment to manage dependencies for this project.
# Follow these steps to create and activate a virtual environment:

# 3. Create a virtual environment. If you're using `venv`:
python -m venv venv

# 4. Activate the virtual environment. On Windows:
source venv/bin/activate

## Installation
Ensure you have Python installed on your system. Then, install the required libraries using pip:

```bash
pip install nba_api pandas
```

## Usage
1. Clone or download the script.
2. Make sure you have the necessary libraries installed.
3. Run the script using Python.

```python
python nba_player_stats_downloader.py
```

By default, the script downloads player stats for the 2023-24 NBA season. You can change the season by modifying the `season` parameter in the function call.

## Parameters
- `season`: The NBA season for which you want to download player stats. Format: `'YYYY-YY'`. Default is `'2023-24'`.
- `max_retries`: Maximum number of retries in case of network errors. Default is `5`.

## Output
The script generates a CSV file containing player stats for the specified season. The file is saved in the directory specified by `file_path` with a filename containing the current date and time of execution.

## Note
- This script may take some time to execute, depending on the number of active NBA players and network conditions.
- Ensure that you have proper network connectivity to access the NBA API.
- Modify the `file_path` variable to specify the directory where you want to save the output CSV file.
