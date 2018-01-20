from slackclient import SlackClient
import os

def _format_text(details):
    title = details["title"]
    coin_name = details["coin_name"]
    desc = details["desc"]
    validation_votes = details["validation_votes"]
    added_date = details["added_date"]
    proof_url = details["proof_url"]
    source_url = details["source_url"]
    validation_percentage = details["validation_percentage"]
    date = details["date"]

    text = "タイトル:" + title
    text += "、コイン名:" + coin_name
    text += "、イベント日:" + date + "\n"
    text += "詳細:" + desc + "\n"
    text += "ソース（画像）" + proof_url + "\n"
    text += "ソース（リンク）" + source_url + "\n"
    text += "信憑性:" + validation_percentage + "(投票人数:" + validation_votes + ")、"
    text += "追加日:" + added_date
    return text


def send_alert(details):
    slack_token = "YOUR TOKEN"
    sc = SlackClient(slack_token)
    text = _format_text(details)
    sc.api_call(
        "chat.postMessage",
        channel="cripto_calendar_alert",
        text=text
    )

if __name__ == '__main__':
    details = {'desc': '"New projects to unveil, all building on ost."', 'validation_votes': '(17 votes)', 'added_date': '13 January 2018', 'coin_name': 'Simple Token (OST)', 'proof_url': 'http://coinmarketcal.com//images/proof/542992631541f7dd2d5e6d1ccba65fbf.png', 'source_url': 'https://twitter.com/betashop/status/951776366189563904', 'title': 'OST Startup Day', 'validation_percentage': '94.117647058824', 'date': '15 January 2018'}
    send_alert(details)
