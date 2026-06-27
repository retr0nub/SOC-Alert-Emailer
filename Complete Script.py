import re
import smtplib
from email.message import EmailMessage

# ---------------------------
# Email Configuration
# ---------------------------

EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_16_character_app_password"

# ---------------------------
# Analyze Log File
# ---------------------------

failed_ips = []
count = 0

with open("auth.log", "r") as file:

    for line in file:

        if "Failed" in line:

            count += 1

            ip = re.search(
                r"\d+\.\d+\.\d+\.\d+",
                line
            )

            if ip:
                failed_ips.append(ip.group())

# ---------------------------
# Send Alert if Failed Logins Exist
# ---------------------------

if count > 0:

    msg = EmailMessage()

    msg["Subject"] = "SOC Alert - Failed Login Attempts Detected"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    body = f"""
Total Failed Logins: {count}

Suspicious IP Addresses:

"""

    for ip in failed_ips:
        body += f"[+] {ip}\n"

    msg.set_content(body)

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            EMAIL,
            APP_PASSWORD
        )

        smtp.send_message(msg)

    print("Alert Email Sent")

else:
    print("No failed logins found")