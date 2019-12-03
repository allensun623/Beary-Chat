from bearychat import incoming
from loguru import logger

#send infomation to bearychat
def send(markdown, title, text, channel, attachments):
    data = {
        "markdown": markdown,
        "title": title,
        "text": text,
        "notification": title,
        "channel": channel,
        "attachments": attachments,
    }
    #channal
    resp = incoming.send(
        "https://hook.bearychat.com/=bwH7H/incoming/fa39b2010f0e6bba1b79a9f5af550e29",
        data)

    if resp.status_code > 200:
        logger.error("failed to send bearychat")

def main():
    #test
    pass
       

if __name__ == "__main__":
    main()

