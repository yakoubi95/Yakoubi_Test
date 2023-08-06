import random

# List of sample country codes
countries = ['BL', 'GN', 'BN', 'ST', 'PW', 'HK', 'NL', 'BN', 'HM', 'NR', 'GT', 'GU', 'PA', 'CW', 'GA', 'KG']

# Generate thousands of lines of data
num_lines = 1000000
data_lines = []

for _ in range(num_lines):
    song_id = random.randint(10000000, 99999999)
    user_id = random.randint(1000000, 9999999)
    country = random.choice(countries)
    data_lines.append(f"{song_id} | {user_id} | {country}\n")

# Write the data to a text file
with open("sample_listen_large_2.txt", "w") as file:
    file.writelines(data_lines)
