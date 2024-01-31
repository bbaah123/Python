# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:01:48 2024

@author: USER
"""

import re

# Problem 1: Validate email addresses
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Problem 2: Match valid URLs
url_pattern = r"^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Problem 3: Extract phone numbers in "xxx-xxx-xxxx" format
phone_pattern = r"\b\d{3}-\d{3}-\d{4}\b"

# Problem 4: Extract words that start with a capital letter
capital_word_pattern = r"\b[A-Z][a-zA-Z]*\b"

# Problem 5: Match dates in "MM/DD/YYYY" format
date_pattern = r"\b\d{2}/\d{2}/\d{4}\b"

# Problem 6: Extract mentions in social media post
mention_pattern = r"@\w+"

# Problem 7: Extract words with exactly three letters
three_letter_word_pattern = r"\b[a-zA-Z]{3}\b"

# Problem 8: Match hexadecimal color codes in CSS
hex_color_pattern = r"#[0-9a-fA-F]{6}"

# Problem 9: Extract HTML tags with attributes
html_tag_pattern = r"<[^>]+>"

# Problem 10: Match valid IPv4 addresses
ipv4_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

# Sample text to test the regular expressions
sample_text = """
Emails: john@example.com, alice@example.net
URLs: https://example.com, http://sub.domain.org
Phone numbers: 123-456-7890, 555-5555
Capital Words: Apple, Banana, Orange
Dates: 12/25/2022, 01/15/2023
Social media post: @user123 mentioned @friend456
Three-letter words: dog, cat, fox
CSS colors: #FF0000, #00aabb, #1234567
HTML tags: <div class="content">, <a href="https://example.com">
IPv4 addresses: 192.168.1.1, 10.0.0.255, 255.255.255.255
"""

# Function to find and print matches using a given pattern
def find_and_print_matches(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        print("Matches found:", matches)
    else:
        print("No matches found")

# Test each regular expression pattern with the sample text
find_and_print_matches(email_pattern, sample_text)
find_and_print_matches(url_pattern, sample_text)
find_and_print_matches(phone_pattern, sample_text)
find_and_print_matches(capital_word_pattern, sample_text)
find_and_print_matches(date_pattern, sample_text)
find_and_print_matches(mention_pattern, sample_text)
find_and_print_matches(three_letter_word_pattern, sample_text)
find_and_print_matches(hex_color_pattern, sample_text)
find_and_print_matches(html_tag_pattern, sample_text)
find_and_print_matches(ipv4_pattern, sample_text)
