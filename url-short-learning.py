import requests
url=input('Enter URL: ')
r=requests.get('https://v.ht/api.php?url='+url)
print(f'''\n
long/old url : {url}\n
short/new url : {r.text}\n''')

#By @TweakPY - @vv1ck
