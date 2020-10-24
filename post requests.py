import requests
in_values = {'username':'Jack','password':'Hello'}
res = requests.post('https://httpbin.org/post',data = in_values)
print(res.text)