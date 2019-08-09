import requests

from interface_frame.ApiGet import ApiGet
from interface_frame.ApiPost import ApiPost


def test_version():
    from interface_frame import __version__
    assert __version__ == "0.1.0"

def test_get():
    ApiGet().run().validate("status_code",200)

def test_get_withparams():
    ApiGet().set_url("http://httpbin.org/get").set_params(abc=123).run(). \
        validate("status_code",200).\
        validate("headers.server","nginx").\
        validate("json().url","https://httpbin.org/get?abc=123")

def test_post():
    ApiPost().set_url("http://httpbin.org/post").set_json({"abc":123}).run().\
        validate("status_code",200). \
        validate("json().url", "https://httpbin.org/post")

def test_extract():
    cookies = ApiGet().set_url("http://httpbin.org/cookies").\
            set_cookie("freeform", "123").\
            run().\
            extract("json().cookies")
    print("============",cookies)

def test_request_withcookie(getCookie):
    cookies = ApiGet().set_url("http://httpbin.org/cookies"). \
        set_cookies(getCookie). \
        run(). \
        extract("json().cookies")
    print("============", cookies)

def test_yongdian():
    cookie = ApiPost().set_url("https://starry.chinawyny.com/login").\
        set_json({"username":"18380462343","password":"ad07fb25aa2d3a9f96ee12f25e0be902"}).\
        run().extract("headers.Set-Cookie")
    print(cookie)


