import requests
import json

data={
    "phone" : "18357117103",
}

r=requests.get("http://hb-api.newitd.com/get_user_task",data,timeout=30)
#print(r.text)
json_result = r.text[5:-1]
js_res = json.loads(json_result)
print(js_res)