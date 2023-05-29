# Anonymise Script

This script anonymises inputs in an attempt to mask the original sources from which the input originated.

## Set Up
Create a CSV file in the same directory as `main.py`:

```
touch words.csv
```

The CSV should contain word replacements in the format:

```csv
original word, replacement word
```
 
Each row should represent a unique replacement. Don't have blank spaces anywhere in the CSV file.

Install packages:

```
pip install -r requirements.txt
```

run the code:

```
python3 main.py
```

## Usage

### step 1
When you run the script a vim editor will appear where you will insert (i) your input and then save it (:wq)

Inputs can also be added by using the `--input' or '-i' arguments:

```
python3 main.py -i "hey this is my input!"
```

### step 2
Once that's done you will see the modified version, changes will be in yellow.

### step 3
The modified version will be in your clipboard now.

## Note

It is important to emphasise that the modified output generated by this script should not be solely relied upon to anonymise sensitive information. It is recommended to review the modified text carefully before pasting it into any generative AI or sharing it with others. The script aims to provide a convenient way to replace to anonymise data, but it does not guarantee the accuracy or completeness of the modifications. Therefore, it is crucial to exercise caution and ensure that the modified output aligns with the intended purpose and desired level of anonymisation.

Make sure to review and update the CSV file with appropriate word replacements before running the script.

**Disclaimer:** This script provides privacy and anonymisation features but does not guarantee complete security or confidentiality. Users are responsible for ensuring compliance with the organisation's privacy policies and legal requirements.