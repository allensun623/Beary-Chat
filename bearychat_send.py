from bearychat import incoming
from loguru import logger
import gate_news


def send(markdown, title, text, channel, attachments):
    data = {
        "markdown": markdown,
        "title": title,
        "text": text,
        "notification": title,
        "channel": channel,
        "attachments": attachments,
    }

    resp = incoming.send(
        "https://hook.bearychat.com/=bwH7H/incoming/fa39b2010f0e6bba1b79a9f5af550e29",
        data)

    if resp.status_code > 200:
        logger.error("failed to send bearychat")

def main():
    #test
    # receive the latest news
    news_inform = gate_news.news()
    send(True, 
        "GATE NEWS", 
        "GATE NEWS", 
        "promotion",
        [{
            "title": list(news_inform.keys())[1],
            "url": list(news_inform.keys())[1],
            "text": list(news_inform.values())[1],
            "images": [
                {"url": "https://cosmos-images2.imgix.net/file/spina/photo/20565/191010_nature.jpg?ixlib=rails-2.1.4&auto=format&ch=Width%2CDPR&fit=max&w=1600"}
            ]
        }]
    )

        # receive the latest price
    news_inform = gate_news.news()
    send(True, 
        "GATE NEWS", 
        "GATE NEWS", 
        "promotion",
        [{
            "title": list(news_inform.keys())[1],
            "url": list(news_inform.keys())[1],
            "text": list(news_inform.values())[1],
            "images": [
                {"url": "https://cosmos-images2.imgix.net/file/spina/photo/20565/191010_nature.jpg?ixlib=rails-2.1.4&auto=format&ch=Width%2CDPR&fit=max&w=1600"}
            ]
        }]
    )

if __name__ == "__main__":
    main()


"""template"""
"""
#test    
    send(True, 
        "test", 
        "promotion discount", 
        "promotion", 
        [
        {
            "title": "title_1",
            "url": "https://bearychat.com",
            "text": "attachment_text",
            "color": "#ffa500",
            "images": [
                {"url": "http://img3.douban.com/icon/ul15067564-30.jpg"}
            ]
        }
    ])
"""