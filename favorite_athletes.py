import requests
import json
token = '<自己到 graph api explorer 找，或是透過授權取得（吧）>'
res = requests.get('https://graph.facebook.com/v2.8/me?access_token=%s'%(token)+'&fields=favorite_athletes')
jsondata = json.loads(res.text)
for athletes in jsondata['favorite_athletes']:
	print(athletes['name'])