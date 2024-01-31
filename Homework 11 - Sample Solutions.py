# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 07:46:54 2024

@author: USER
"""

#Problem 1: Phone Number Extraction


import re

def extract_phone_numbers(text):
    pattern = r"\d{3}-\d{3}-\d{4}"
    return re.findall(pattern, text)

text = "Call me at 123-456-7890 or 987-654-3210 for more information."
phone_numbers = extract_phone_numbers(text)
print("Phone numbers found:", phone_numbers)

#Problem 2: Email Address Validation

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

email_addresses = [
    "user@example.com",
    "invalid-email",
    "name@domain.co",
    "another.email@subdomain.example.org",
]

valid_emails = [email for email in email_addresses if validate_email(email)]
print("Valid email addresses:", valid_emails)
#Problem 3: Password Strength Checker

def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
    return bool(re.match(pattern, password))

passwords = ["Password123", "p@ssW0rd", "12345678", "Short1"]
strengths = [validate_password(password) for password in passwords]

for i, password in enumerate(passwords):
    if strengths[i]:
        print(f"'{password}' is a strong password.")
    else:
        print(f"'{password}' is not a strong password.")
#Problem 4: HTML Tag Extraction

def extract_html_tags(html):
    pattern = r"<[^>]+>"
    return re.findall(pattern, html)

html_text = "<p>This is <b>bold</b> text.</p> <a href='https://example.com'>Visit Example</a>"
tags = extract_html_tags(html_text)
print("HTML tags found:", tags)
#Problem 5: Date Format Conversion

def convert_date_formats(text):
    # Convert MM/DD/YYYY to YYYY-MM-DD format
    text = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2", text)
    # Convert YYYY-MM-DD to MM/DD/YYYY format
    text = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", text)
    return text

input_text = "Date: 12/25/2022, Time: 15:30 | Date: 2023-01-15, Time: 09:45"
converted_text = convert_date_formats(input_text)
print("Converted text:", converted_text)
#Problem 6: URL Extraction

def extract_urls(text):
    pattern = r"https?://[^\s]+"
    return re.findall(pattern, text)

text = "Visit my website at https://example.com. You can also check https://sub.domain.org/page?q=query"
urls = extract_urls(text)
print("URLs found:", urls)

#Problem 7: IP Address Validation

def validate_ip(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.([25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.([25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.([25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip))

ip_addresses = ["192.168.1.1", "256.0.0.1", "10.0.0.255", "abc.def.ghi.jkl"]
valid_ips = [ip for ip in ip_addresses if validate_ip(ip)]
print("Valid IP addresses:", valid_ips)