import requests
import time

socks5 = ['https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all']
socks4 = ['https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all']
http = ['https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all']
logo=f"""
_ (`-.  _  .-')              ) (`-.                                  ('-.  _  .-')   
  ( (OO  )( \( -O )              ( OO ).                              _(  OO)( \( -O )  
 _.`     \ ,------.  .-'),-----.(_/.  \_)-. ,-.-')    ,------.,-.-') (,------.,------.  
(__...--'' |   /`. '( OO'  .-.  '\  `.'  /  |  |OO)('-| _.---'|  |OO) |  .---'|   /`. ' 
 |  /  | | |  /  | |/   |  | |  | \     /\  |  |  \(OO|(_\    |  |  \ |  |    |  /  | | 
 |  |_.' | |  |_.' |\_) |  |\|  |  \   \ |  |  |(_//  |  '--. |  |(_/(|  '--. |  |_.' | 
 |  .___.' |  .  '.'  \ |  | |  | .'    \_),|  |_.'\_)|  .--',|  |_.' |  .--' |  .  '.' 
 |  |      |  |\  \    `'  '-'  '/  .'.  \(_|  |     \|  |_)(_|  |    |  `---.|  |\  \  
 `--'      `--' '--'     `-----''--'   '--' `--'      `--'    `--'    `------'`--' '--' """
####################################################################################################

print(logo)
main = int(input('[1] Scrape Proxies\n\n\n>'))
if main ==1:
    type = int(input('[1] HTTP\n[2] SOCKS4\n[3] SOCKS5\n\n\n>'))
    if type ==1:
        s = requests.get(http[0])
        http1 = open('http.txt', 'a')
        http1.write(s.text)
        http1.close()
        print('finished , exitting now')
        time.sleep(2)
    elif type ==2:
        e = requests.get(socks4[0])
        socks = open('socks4.txt', 'a')
        socks.write(e.text)
        socks.close()
        print('finished , exitting now')
        time.sleep(2)
    elif type ==3:
        x = requests.get(socks5[0])
        socks = open('socks5.txt', 'a')
        socks.write(x.text)
        socks.close()
        print('finished , exitting now')
        time.sleep(2)
else:
    print('invalid option , exitting')
    time.sleep(2)
    
    







