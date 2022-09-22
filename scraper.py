#! /usr/bin/env python3

import pyperclip
import re

# Create a regex for phone numbers.
phone_regex = re.compile(r'''
( # Put the entire expression in brackets to group everything as group 0. Works for findall.
((\d\d\d)|(\(\d\d\d\)))?     # area code (optional) without/with parens
(\s|-)                         # first separator (space or dash)
\d\d\d                         # first 3 digits
-                              # second separator (dash)
\d\d\d\d                       # last 4 digits
(((ext(\.)?\s)|x)              # extension word part (optional)
(\d{2,5}))?                    # extension number part (optional)
)
''', re.VERBOSE)

# Create a regex for email address.
email_regex = re.compile(r'''
[a-zA-Z0-9_.+]+                # name part
@                              # @ symbol part
[a-zA-Z0-0_.+]+                # domain name part
''', re.VERBOSE)

# Get text from the clipboard.
text = pyperclip.paste()

# Extract phone numbers and email addresses from the text.
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

# Create a new list. Loop through extracted_phone and pull out all COMPLETE ph nums.
all_phone_numbers = []
for phone_number in extracted_phone:
    # Get the first string [0] in each returned tuple.
    all_phone_numbers.append(phone_number[0])

# Copy extracted phone numbers and email addresses to the clipboard.
# Put a new line between each extracted phone number and email.
results = "\n".join(all_phone_numbers) + "\n" + "\n".join(extracted_email)
# Print results to terminal for troubleshooting.
print(results)
# Copy results back to the clipboard.
pyperclip.copy(results)