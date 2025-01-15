import smtplib
import time
import socket

def connect_to_smtp(host):
    try:
        start_time = time.time()
        with smtplib.SMTP(host, 25, timeout=10) as server:
            server.ehlo()
            server.mail('sender@example.com')
            server.rcpt('recipient@example.com')
            print("SMTP request sent successfully!")
        print(f"Connection established in {time.time() - start_time:.2f} seconds.")
    except (smtplib.SMTPConnectError, socket.timeout, TimeoutError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    host = input("Enter the SMTP server hostname or IP address: ")
    connect_to_smtp(host)

if __name__ == "__main__":
    main()
