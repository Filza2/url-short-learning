import requests

url=input(
    
'Enter URL: '

)
r=requests.get(
    'https://v.ht/api.php?url='+url)

print('\n')
print('long/old url : {}'.format(url))
print('short/new url : {}'.format(r.text))

#another way to print 
#print(f'''
      
#\n
#long/old url : {url}
#short/new url : {r.text}

#''')