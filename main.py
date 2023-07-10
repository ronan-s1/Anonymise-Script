import argparse
import csv
import re
from urllib.parse import urlparse
from pathlib import Path
import pyperclip
import os
from editor import edit

CSV = "words.csv"

# ANSI escape codes for color formatting
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"
GREEN = "\033[32m"
PURPLE = "\033[35m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


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
            ip_count = len(ip_mapping) + 1
            generic_ip = f"<ip-address-{ip_count}>"
            ip_mapping[ip] = generic_ip
            return replacement_text_color(generic_ip)

    modified_text = re.sub(ip_pattern, replace_ip, input_text)
    return modified_text


def read_csv_file(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        replacement_dict = {f"{row[0].strip()}": row[1].strip() for row in reader}
    return replacement_dict


def main():
    clear_screen()
    parser = argparse.ArgumentParser(description="Process text with replacements")
    parser.add_argument("--input", "-i", help="Input text")
    parser.add_argument("--copy", "-c", action="store_true", help="If you want to add the output to your clipboard")
    parser.add_argument("--backtick", "-bt", action="store_true", help="Wrap output with backticks (`)")
    args = parser.parse_args()

    replacement_dict = read_csv_file(CSV)

    if args.input:
        user_input = args.input
    else:
        user_input = edit().decode("utf-8")

    modified_input = replace_words(user_input, replacement_dict)
    modified_input = replace_ip_address(modified_input)

    if args.backtick:
        modified_input = f"```\n{modified_input}\n```"

    print(f"{BOLD}{GREEN}Original:{RESET}\n{user_input}\n{BOLD}{GREEN}\nModified:{RESET}\n{modified_input}\n")

    if args.copy or input(f"{BOLD}{PURPLE}Add to clipboard? (y/n): {RESET}").lower() in ["yes", "y"]:
        pattern = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
        pyperclip.copy(pattern.sub("", modified_input))

if __name__ == "__main__":
    main()
