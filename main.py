# Main function to compute top 50 songs for each country and generate the output file

from datetime import datetime, timedelta
from utils import read_logs, filter_data_by_date, compute_top_songs, generate_output_file

if __name__ == "__main__":
    input_file = "sample_listen-2021-12-01.txt"
    # input_file = "sample_listen_large_2.txt"
    output_file = "country_top50_20211201.txt"
    # output_file = "large_test_2.txt"

    days_window = 7

    # Read the data from the input file
    data = read_logs(input_file)

    # Get unique countries from the data
    countries = set(entry[2] for entry in data)

    # Compute and generate top 50 songs for each country
    for country in countries:
        country_data = [entry for entry in data if entry[2] == country]
        top_songs = compute_top_songs(country_data)
        generate_output_file(output_file, country, top_songs)
