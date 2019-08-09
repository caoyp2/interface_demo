
#添加cookie
import pytest

from interface_frame.ApiGet import ApiGet


@pytest.fixture()
def getCookie():
    cookie = ApiGet().set_url("http://httpbin.org/cookies"). \
        set_cookie("freeform", "123"). \
        run(). \
        extract("json().cookies")
    return cookie