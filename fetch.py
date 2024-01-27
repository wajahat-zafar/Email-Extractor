import re

def extract_emails(file_path):
    # Regular expression for extracting email addresses
    # This version stops at common delimiters like |, space, or end of line
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}(?=[\|\s]|$)'

    with open("Data.txt", 'r') as file:
        text = file.read()

    # Find all email addresses using the regular expression
    emails = re.findall(email_regex, text)

    return emails

# Replace 'your_file.txt' with the path to your text file
file_path = 'your_file.txt'
emails = extract_emails(file_path)

# Print or process the extracted emails
for email in emails:
    print(email)
