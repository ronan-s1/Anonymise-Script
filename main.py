import argparse
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


def replacement_text_color(text):
    return f"{YELLOW}{text}{RESET}"


def replace_words(input_text, replacement_dict):
    for word, new_word in replacement_dict.items():
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        input_text = pattern.sub(replacement_text_color(new_word), input_text)
    return input_text


def replace_ip_address(input_text):
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    ip_mapping = {}

    def replace_ip(match):
        ip = match.group(0)
        if ip in ip_mapping:
            return replacement_text_color(ip_mapping[ip])
        else:
            generic_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
            ip_mapping[ip] = generic_ip
            return replacement_text_color(generic_ip)

    # Replace IP addresses with generic IPs or reuse existing generic IPs
    modified_text = re.sub(ip_pattern, replace_ip, input_text)
    return modified_text


def replace_timeseries(input_text):
    timeseries_pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z"
    replacement_text = replacement_text_color("2010-01-01T10:10:10.10101")
    modified_text = re.sub(timeseries_pattern, replacement_text, input_text)
    return modified_text


def replace_file_paths(input_text):
    file_paths = re.findall(r"\/[^,:]*\.\w+", input_text)
    for file_path in file_paths:
        # if it's not a URL (not perfect but works usually)
        if file_path[:2] != "//":
            _, file_name = os.path.split(file_path)
            file_extension = os.path.splitext(file_name)[1]
            # keeping file extension
            new_file_path = replacement_text_color(f"/path/to/file/my_file{file_extension}")
            input_text = input_text.replace(file_path, new_file_path)
    return input_text


def read_csv_file(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        replacement_dict = {f"{row[0].strip()}": row[1].strip() for row in reader}
    return replacement_dict


def main():
    parser = argparse.ArgumentParser(description="Process text with replacements")
    parser.add_argument("--input", "-i", help="Input text")
    args = parser.parse_args()

    replacement_dict = read_csv_file(CSV)

    if args.input:
        user_input = args.input
    else:
        user_input = edit().decode("utf-8")

    modified_input = replace_words(user_input, replacement_dict)
    modified_input = replace_ip_address(modified_input)
    modified_input = replace_timeseries(modified_input)
    modified_input = replace_file_paths(modified_input)
    pyperclip.copy(re.sub(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])", "", modified_input))

    print(f"\n{BOLD}{GREEN}Original:{RESET}\n{user_input}\n{BOLD}{GREEN}Modified:{RESET}\n{modified_input}")


if __name__ == "__main__":
    main()
