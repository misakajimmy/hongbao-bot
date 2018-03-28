#此处测试点数查询API
import requests
data = {
            "phone": "18357117103",
            "url": ""
        }
r =requests.get("http://hb-api.newitd.com/user_info",data,timeout=30)
print(r.text)

#if result.status_code == 200: