

# Sample dataset: a simple list of emails and labels
data = {
    "email": [
        "Congratulations! You've won a free lottery. Claim now.",
        "Hi, are we still meeting for lunch tomorrow?",
        "You have been selected for a prize. Call now!",
        "Dear friend, I hope you're doing well. Let's catch up soon.",
        "Exclusive offer! Buy one, get one free on all items."
    ],
    "label": [1, 0, 1, 0, 1]  # 1: Spam, 0: Not Spam
}

for i in range(len(data["email"])):
    email = data["email"][i]  # accessing the email content by index i
    label = data["label"][i]  # accessing the label by index i

    if label == 1:
        print(f"Spam Email: {email}")
    else:
        print(f"Not Spam Email: {email}")


# From this project, I have learned how to handle data (Data structure) in Python using lists and dictionaries.
# I have also learned how to iterate (Loops- for, while) through data and apply conditions (if elif else statement) to filter out spam emails.
