import requests
from requests import status_codes

def slack_message(metin: str, slack_adresi: str) ->None:
    headers = {"Content-Type": "application/json"}
    response = requests.post(slack_adresi, json={"text": metin}, headers=headers)
    if response.status_code != 200:
        raise ValueError(
    f"Slack bilinmeyen bir hata döndürdü {response.status_code}",
    f"mesaj:\n{response.text}"
    )

if __name__ == "__main__":
    # slack_adresi webhook'u oluşturduğunuzda Slack tarafından sağlanan URL'ye ayarlayın.
    # https://my.slack.com/services/new/webhook/
    slack_message("<Göndermek istediğiniz mesajınız>", "<Slack kanalınızın url'i>")

    