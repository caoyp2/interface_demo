import  requests
class BaseApi(object):

    method="GET"
    url = "http://httpbin.org/get"
    headers={"Accept": "application/json"}
    params=""
    cookies={}
    json={}

    def run(self):
        self.response = requests.request(
                self.method,
                self.url,
                headers = self.headers,
                params = self.params,
                json = self.json,
                cookies = self.cookies,
                verify = False
                )
        return self

    def set_cookie(self,key,value):
        self.cookies.update({key:value})
        return self

    def set_cookies(self, cookies):
        self.cookies = cookies
        return self

    def set_url(self,url):
        self.url = url
        self.headers = {"Accept": "application/json"}
        self.params = ""
        self.json = {}
        return self

    def set_headers(self,**kwargs):
        self.headers = kwargs
        return self

    def set_params(self,**params):
        self.params = params
        return self

    def set_json(self,json_data):
        self.json = json_data
        return self

    #提取值
    def extract(self,key):
        value = self.response
        for _key in key.split("."):
            if isinstance(value, requests.Response):
                if _key == "json()":
                    value = value.json()
                else:
                    value = getattr(value, _key)
            elif isinstance(value, (dict, requests.structures.CaseInsensitiveDict)):
                value = value[_key]
        return value

    #校验
    def validate(self,keys,expect_value):
        value = self.extract(keys)
        assert value == expect_value
        return self



