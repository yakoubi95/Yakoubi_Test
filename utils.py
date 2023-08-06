# reusable functions file
from datetime import datetime, timedelta

# Function to read and parse log file to extract data regularly   

def read_logs(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            song_id, user_id, country = line.strip().split(' | ')
            data.append((int(song_id), int(user_id), country))
    return data

read_logs('sample_listen-2021-12-01.txt')

# Function to filter data to include entries within the specified date window

def filter_data_by_date(data, target_date, days_window):
    start_date = target_date - timedelta(days=days_window - 1)
    filtered_data = [entry for entry in data if start_date <= entry[0] <= target_date]
    return filtered_data

# Function to compute the top 50 most listened songs _ iterative function to use later for each country filtering 

def compute_top_songs(data):
    songs_count = {}
    for entry in data:
        song_id, _, _ = entry
        songs_count[song_id] = songs_count.get(song_id, 0) + 1

    sorted_songs_count = sorted(songs_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_songs_count[:50]

# Funtion to generate output file with top songs for a specific country

def generate_output_file(file_path, country, top_songs):
    with open(file_path, 'a') as file:
        file.write(f"{country}|")
        for song_id, count in top_songs:
            file.write(f"{song_id}:{count},")
        file.write("\n")
