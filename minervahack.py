import json
import requests

webhook_url = 'https://hooks.slack.com/services/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'# enter your own web hook url
slack_data = {'text': "Fight, Get the location here", "attachments": [
        {
            "text":"https://www.google.com/maps/place/GitHub/@37.782347,-122.3911146,16z/data=!4m5!3m4!1s0x8085807f619a62df:0x491ce2f73977af35!8m2!3d37.7822671!4d-122.3912479",
            "fallback": "Internet problem, can't get location sorry!!",
            "callback_id": "ConCVe",
            "color": "#3AA3E3",
            "attachment_type": "default",
        }
    ]}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
