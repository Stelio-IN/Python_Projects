import smtplib

sender = "batats@gmail.com"
receiver = "asdasdasad@gmail.com"
password = "sdasdasd"  # Use your app password here
subject = "EMail Test"
body = "Make a test"

message = f"""From:{sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!!!!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    server.quit()
