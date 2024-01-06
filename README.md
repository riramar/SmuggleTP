# SmuggleTP

A simple tool to exploit SMTP Smuggling vulnerabilities (ref. https://sec-consult.com/blog/detail/smtp-smuggling-spoofing-e-mails-worldwide/).

# Usage

```
$ ./SmuggleTP.py -h
usage: SmuggleTP.py [-h] --smtp_server SMTP_SERVER --smtp_port SMTP_PORT [--smtp_username SMTP_USERNAME] [--smtp_password SMTP_PASSWORD] --sender_email SENDER_EMAIL --receiver_email
                    RECEIVER_EMAIL --spoofed_email SPOOFED_EMAIL [--enable_debug]

options:
  -h, --help            show this help message and exit
  --smtp_server SMTP_SERVER
                        SMTP server hostname
  --smtp_port SMTP_PORT
                        SMTP server port
  --smtp_username SMTP_USERNAME
                        SMTP username
  --smtp_password SMTP_PASSWORD
                        SMTP password
  --sender_email SENDER_EMAIL
                        Sender email address
  --receiver_email RECEIVER_EMAIL
                        Receiver email address
  --spoofed_email SPOOFED_EMAIL
                        Spoofed email address
  --enable_debug        Enable SMTP debug messages
```

If you have received an email from SPOOFED_EMAIL to RECEIVER_EMAIL, it's likely that the exploit worked.

# Contact

* https://twitter.com/ricardo_iramar
