import re
user_email = input("Enter your email address: ")

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
match = re.search(email_pattern, user_email)
if match:
    print("Email valid")
else:
    print("email not valid")