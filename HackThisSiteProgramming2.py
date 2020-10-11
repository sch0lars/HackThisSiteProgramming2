# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                           #
#   Solution to Programming Mission 2 on Hack This Site.    #
#                                                           #
#   Author: Tyler Hooks                                     #
#                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from PIL import Image
from io import BytesIO
import requests

morse = {

        '.-':'a',
        '-...':'b',
        '-.-.':'c',
        '-..-':'d',
        '.':'e',
        '..-.':'f',
        '--.':'g',
        '....':'h',
        '..':'i',
        '.---':'j',
        '-.-':'k',
        '.-..':'l',
        '--':'m',
        '-.':'n',
        '---':'o',
        '.--.':'p',
        '--.-':'q',
        '.-.':'r',
        '...':'s',
        '-':'t',
        '..-':'u',
        '...-':'v',
        '.--':'w',
        '-..-':'x',
        '-.--':'y',
        '--..':'z',

        '.----':'1',
        '..---':'2',
        '...--':'3',
        '....-':'4',
        '.....':'5',
        '-....':'6',
        '--...':'7',
        '---..':'8',
        '----.':'9',
        '-----':'0'

    }

url = 'https://www.hackthissite.org/missions/prog/2/'
referer = 'https://www.hackthissite.org/missions/programming/'
# Change "YourCookieValue" to your own cookie value.
cookies = {'PHPSESSID':'YourCookieValue'}

# Start a session. 
session = requests.Session()
session.headers.update({'referer':referer})
site = session.post(url, cookies = cookies)

# Retrieve the image and convert differences in pixel values to ASCII characters. 
img = session.get('https://www.hackthissite.org/missions/prog/2/PNG/', cookies = cookies)
image = Image.open(BytesIO(img.content))
message = ""
answer = ""
index = 0
current = 0
for d in image.getdata():
    if d != 0:
        message += chr(index - current)
        current = index
    index += 1

# Convert the morse code.
for m in message.split():
    answer += morse[m]
        
url = 'https://www.hackthissite.org/missions/prog/2/'
payload = {'solution':answer}
site = session.post(url, cookies = cookies, data = payload)


