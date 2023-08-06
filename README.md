# Data Engineer Intern – Technical Test

## Data Engineering Exercise

### Context
In the context of a CRM campaign, the objective is to send each user the top 50 songs of their country as well as their own personal top 50 songs of the last 7 days. The data is received daily in a folder, and each day's data is stored in a text file named listen-YYYYMMDD.log. Each row in the log file represents a listening stream and is formatted as follows: sng_id|user_id|country.

### Objective
The purpose of this exercise is to develop a system that computes, on a daily basis, the top 50 songs most listened to in each country over the last 7 days. The system should generate one text file per day (country_top50_YYYYMMDD.txt), where each row contains the top 50 songs listened to in a specific country.

### Solution Implementation

#### File Structure
- `main.py`: The main script to compute and generate the top 50 songs for each country.
- `utils.py`: Contains utility functions for reading logs, filtering data by date, and computing top songs.
- `sample_listen-2021-12-01.txt`: Sample input file containing logs for December 1st, 2021 (provided for testing).
- `country_top50_20211201.txt`: Sample output file containing the top 50 songs for each country on December 1st, 2021 (generated during testing).

#### Test Phase
- Unit test for the 100 lines sample of data. 
- large test, as I don't have in my disposition a large quantity of data, I generated random large data using random_large_data.py file. Then I test my code and it's execution time is in around 1s (one second) for 1 million data lines.  

#### How to Run
1. Clone the project repository and navigate to the project directory.
2. Ensure you have Python 3 installed on your system.
3. Make sure the sample input file `sample_listen-2021-12-01.txt` is present in the project directory or provide the desired input file with the same format.
4. Open a terminal or command prompt in the project directory.
5. Run the main script using the following command: **python main.py**
6. The script will read the input file, compute the top 50 songs for each country, and generate the output file `country_top50_YYYYMMDD.txt` for the specified date (YYYYMMDD) in the file name.

#### Note
- The main script, `main.py`, uses the functions defined in `utils.py` to perform the data processing tasks.
- The script assumes the log files are present in the same format and structure as described in the exercise.
- The script is designed to handle large volumes of data efficiently, and intermediate information is saved on disk for reuse on the following day.

### Expected Delivery files
Please find enclosed a ZIP archive containing the following files:
- `main.py`
- `utils.py`
- `random_large_data.py`
- `sample_listen-2021-12-01.txt` (sample input file)
- `country_top50_20211201.txt` (sample output file)
- `sample_listen_large_2.txt` (large test input file)
- `large_test_2.txt` (large test output file)
- This `README.md` file

### System Requirements
- Python 3
- Operating System: Linux/Win

### Contact
If you have any questions or need further assistance, please don't hesitate to contact me at [yakabd95@hotmail.com].
