import asyncio 
import argparse
from src.mail import mail, create_message

async def send_notification(subject, body):
    from src.config import Config
    recipients = [Config.MAIL_FROM]
    
    message = create_message(recipients=recipients, subject=subject, body=body)
    await mail.send_message(message)

def main():
    parser = argparse.ArgumentParser(description='Send notification email')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--body', required=True, help='Email body')
    
    args = parser.parse_args()
    asyncio.run(send_notification(args.subject, args.body))

if __name__ == '__main__':
    main()