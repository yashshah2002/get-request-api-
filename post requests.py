import requests
in_values = {'username':'yash','password':'yash'}
res = requests.post('https://httpbin.org/post',data = in_values)
print(res.text)
