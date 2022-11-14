emailAddress = input("Enter the email address: ")

if emailAddress.lower().startswith("a00") and emailAddress.lower().endswith("@student.ait.ie"):
    print("Valid AIT Student Email Address")
elif emailAddress.lower().endswith("@ait.ie"):
    print("Valid AIT Staff Email Address")
else:
    print("Not a valid AIT email address")
