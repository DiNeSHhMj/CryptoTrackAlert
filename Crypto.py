import requests
import validators
from bs4 import BeautifulSoup
from twilio.rest import Client

SID = 'AC0ee0d0b0759260bcd7d4092f48c9fcb6'
Auth_Token = 'cf6159a13aa33cd50bcdf44b995eb7c9'
variable = Client(SID,Auth_Token)

crypto_name= input(" Enter the crypto coin name :bitcoin or ethereum-->> ") 
crypto_url="https://www.coindesk.com/price/"+crypto_name + "/"
url_check = validators.url(crypto_url)

if url_check:
    print(crypto_url)
    limit = int(input("Set your " + crypto_name.upper() + " trigger amount:-->> "))
    data=requests.get(crypto_url)
    html_extract=BeautifulSoup(data.text,'html.parser')  #text is imp
 
    all_values = html_extract.find('div',class_='containerstyles__StyledContainer-sc-292snj-0 KqMZq')
    for values in all_values:
        name = values.find('div',class_='Box-sc-1hpkeeg-0 iHOgZm').h1.text
        dollar = '$'
        price = values.find('span',class_='currency-pricestyles__Price-sc-1rux8hj-0 jIzQOt').text.split(',')
        final_price= float (price[0]+price[1])
        current_past_value = values.find('div',class_='Box-sc-1hpkeeg-0 bWliNl')
        for all_time in current_past_value:
            current_per= current_past_value.find('h6',class_='typography__StyledTypography-owin6q-0 hZxwDe').text
            low_value = current_past_value.find('span',class_='typography__StyledTypography-owin6q-0 fZpnIj').text
            high_value = current_past_value.find('span',class_='typography__StyledTypography-owin6q-0 fZpnIj').text
            break
        
        print(name,dollar,final_price,current_per,low_value,high_value)
        break
    
    if  final_price > limit:
        message= variable.messages.create(body=" Congrats its greater then your trigger value ", from_='+18059024120' , to='+91 9022055065')
    
    elif final_price < limit:
        print( crypto_name.upper() +" is undervalued. Be calm hope for the best...")

else:
    print(" Wrong URL")