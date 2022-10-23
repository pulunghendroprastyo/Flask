import requests

mydata = {"nama":"andi"}

req =  requests.post("http://127.0.0.1:5001/cobarequest",data=mydata)

print (req.text)