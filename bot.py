from settings import URL,API_KEY
import requests
from time import sleep
from randommer.finance import Finance
from randommer.card import Card
from randommer.misc import Misc
from randommer.text import Text
from randommer.name import Name
from randommer.phone import Phone
from randommer.socialnumber import SocialNumber


message = '''
<b>Hello and welcome to Randommer Bot!</b>

🎉 Get ready for a diverse range of randomness with our exciting features. Here's a quick guide on how to use this bot:

1. /start: Use this command to receive a warm welcome message and get instructions on how to interact with the bot.

2. /card: Feeling lucky? Use this command to draw a random card and see what fortune it holds for you.

3. /finance: Looking for some crypto randomness? Type this command to get a random crypto address.

4. /misc: Explore the richness of various cultures! Use this command to receive information on 5 randomly selected cultures.

5. /name: Need a name on the spot? Type this command for a completely random full name.

6. /phone: If you're in need of phone numbers, use this command to get 5 randomly generated Uzbekistan phone numbers.

7. /social_number: Curious about social numbers? Use this command to get a randomly generated social number.

8. /text: Want some Lorem Ipsum text? Type this command to receive 20 words of normal Lorem Ipsum text.

''' 

def get_last_update(url: str) -> dict:
    endpoint = '/getUpdates'
    url += endpoint
    
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()["result"]

        if len(result) !=0:
            return result[-1]
        else:
            return 404 
    
    return response.status_code

def send_message(url: str, chat_id: int, text: str):
    endpoint = '/sendMessage'
    url = url +  endpoint

    payload = {
        'chat_id': chat_id,
        'text': text,
        "parse_mode" :"HTML"
    }
    requests.get(url, params=payload)

def main(url: str):
    last_update_id = -1
    card = Card()
    finance = Finance()
    misc = Misc()
    name = Name()
    phone = Phone()
    socialnumber = SocialNumber()
    t = Text()
    while True:
        curr_update = get_last_update(url)

        if curr_update['update_id'] != last_update_id:
            user = curr_update['message']['from']
            text = curr_update['message'].get('text')

            if text is None:
                send_message(url, user['id'],"Iltimos keltrilganlardan birini tanlang!")
            elif text == "/start":
                send_message(url,user["id"],message)
            elif text =="/card":
                a = f"Card number : {card.get_card(API_KEY)['cardNumber']}\n Name: {card.get_card(API_KEY)['fullName']}"
                send_message(url,user["id"], str(a))
            elif text == "/finance":
                crypto_type = set(finance.get_crypto_address_types(API_KEY))
                a = f"<b>Crypto Adress</b>: {finance.get_crypto_address(crypto_type,API_KEY)['address']}\n Type: {finance.get_crypto_address(crypto_type,API_KEY)['type']}"
                send_message(url,user["id"],a)
            elif text == "/misc":
                number = 5
                culture = misc.get_cultures(API_KEY)
                a = misc.get_random_address(api_key =API_KEY,number=number,culture=culture)
                send_message(url,user["id"],a)
            elif text == "/name":
                quantity = 1
                n = "fullname"
                a = name.get_name(api_key=API_KEY,nameType=n,quantity=quantity)
                send_message(url,user["id"],a)
            elif text == "/phone":
                quan = 5
                country = "UZ"
                a = phone.generate(api_key=API_KEY,CountryCode=country,Quantity=quan)
                send_message(url,user["id"],a)
            elif text == "/social_number" :
                a = socialnumber.get_SocialNumber(API_KEY)
                send_message(url,user["id"],a)
            elif text == "/text":
                lorem = "normal"
                ty = "words"
                a = t.generate_LoremIpsum(api_key=API_KEY,loremType =lorem,type =ty,number=20)
                send_message(url,user["id"],a)
            last_update_id = curr_update['update_id']

        sleep(0.5)
main(URL)