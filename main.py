import csv
import re
import random
import pyperclip
import os
from editor import edit

CSV = "words.csv"

# ANSI escape codes for color formatting
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"
GREEN = "\033[32m"

def replace_words(input_text, replacement_dict):
    for word, new_word in replacement_dict.items():
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        input_text = pattern.sub(f"{YELLOW}{new_word}{RESET}", input_text)
    return input_text


def replace_ip_address(input_text):
    # Regular expression pattern for matching IP addresses
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    # Dictionary to store the mapping of original IP addresses to generic IPs
    ip_mapping = {}
    def replace_ip(match):
        ip = match.group(0)
        if ip in ip_mapping:
            return f"{YELLOW}{ip_mapping[ip]}{RESET}"
        else:
            generic_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
            ip_mapping[ip] = generic_ip
            return f"{YELLOW}{generic_ip}{RESET}"
    # Replace IP addresses with generic IPs or reuse existing generic IPs
    modified_text = re.sub(ip_pattern, replace_ip, input_text)
    return modified_text


def replace_timeseries(input_text):
    # Regular expression pattern for matching timeseries format
    timeseries_pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z"
    # Text to replace the timeseries format
    replacement_text = f"{YELLOW}2010-01-01T10:10:10.10101{RESET}"
    # Replace timeseries format with the desired text
    modified_text = re.sub(timeseries_pattern, replacement_text, input_text)
    return modified_text


def replace_file_paths(input_text):
    file_paths = re.findall(r"\/[^,:]*\.\w+", input_text)
    for file_path in file_paths:
        if file_path[:2] != "//":
            directory_path, file_name = os.path.split(file_path)
            file_extension = os.path.splitext(file_name)[1]
            new_file_path = f"{YELLOW}{directory_path}/my_file{file_extension}{RESET}"
            input_text = input_text.replace(file_path, new_file_path)
    return input_text


def read_csv_file(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        replacement_dict = {f"{row[0].strip()}": row[1].strip() for row in reader}
    return replacement_dict


def main():
    replacement_dict = read_csv_file(CSV)
    user_input = edit().decode("utf-8")
    modified_input = replace_words(user_input, replacement_dict)
    modified_input = replace_ip_address(modified_input)
    modified_input = replace_timeseries(modified_input)
    modified_input = replace_file_paths(modified_input)
    pyperclip.copy(re.sub(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])", "", modified_input))

    print(f"\n{BOLD}{GREEN}Original:{RESET}\n{user_input}\n{BOLD}{GREEN}Modified:{RESET}\n{modified_input}")


if __name__ == "__main__":
    main()
