SOC Alert Emailer is a Python-based security automation tool designed to assist SOC analysts in detecting suspicious authentication activity. The tool parses log files, identifies failed login attempts, extracts source IP addresses using regular expressions, and automatically sends email alerts containing security findings.

Features:
- Parses authentication log files
- Detects failed login attempts
- Extracts suspicious IP addresses using Regex
- Counts failed authentication events
- Sends automated email alerts via Gmail SMTP
- Provides real-time security notifications

Technologies Used:
- Python
- Regular Expressions (re)
- smtplib
- EmailMessage
- File Handling
