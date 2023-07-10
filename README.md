# Anonymise Script

This script anonymises inputs in an attempt to mask the original sources from which the input originated.

## Features

This script currently performs the following:

- Replaces specified words in words.csv.
- Replaces IP addresses with generic IPs.
- Wraps the modified output with backticks (```) if the --backtick flag is provided.

## Set Up
Create a CSV file in the same directory as `main.py`:

```
touch words.csv
```

The CSV should contain word replacements in the format:

```csv
original word, replacement word
```

For example:

```csv
company123, fake_company_name
john, firstname
smith, lastname
tenant123, fake_tenant_name
```
 
Each row should represent a unique replacement. Don"t have blank spaces anywhere in the CSV file.

<hr>

Install packages:

```
pip install -r requirements.txt
```
<hr>

run the code:

```
python3 main.py
```

## Usage

### The script accepts the following command-line arguments:

- `--input` or `-i`: 
Specifies the input text to be processed. If not provided, the script will open a vim text editor for you to enter the input interactively.

- `--copy` or `-c`: 
If provided, the modified output will be copied to the clipboard.

- `--backtick` or `-bt`: 
If provided, the modified output will be wrapped with backticks (```).

- `--test` or `-t`: 
If provided, the test.csv will be used instead of words.csv.

### example

This command will process the input text "This is my input text", wrap the modified output with backticks and copy it to the clipboard

```
python script.py --input "This is my input text" --copy --backtick
```
or
```
python script.py -i "This is my input text" -c -bt
```

### running script

When you run the script a vim editor will appear where you will insert (i) your input and then save it (:wq)

### reading output

Once that"s done you will see the modified version, changes will be in yellow.

## Example

Try this:
```
python main.py -bt -t -i "@john.smith there's an issue with tenant123 with ip 173.126.26.218. The problem should be coming from here https://bitbucket.company123.com/projects/bot. Next to 173.126.26.218, you should also inspect 173.111.261.218 and 113.126.66.182."
```

![image](https://github.com/ronan-s1/Anonymise-Script/assets/85257187/20474eee-f54e-4b63-b195-5a3eb02169d2)

## Note

It is important to emphasise that the modified output generated by this script should not be solely relied upon to anonymise sensitive information. It is recommended to review the modified text carefully before pasting it into any generative AI or sharing it with others. The script aims to provide a convenient way to replace to anonymise data, but it does not guarantee the accuracy or completeness of the modifications. Therefore, it is crucial to exercise caution and ensure that the modified output aligns with the intended purpose and desired level of anonymisation.

Make sure to review and update the CSV file with appropriate word replacements before running the script.

**DISCLAIMER:** This script provides privacy and anonymisation features but does not guarantee complete security or confidentiality. Users are responsible for ensuring compliance with the organisation"s privacy policies and legal requirements.
