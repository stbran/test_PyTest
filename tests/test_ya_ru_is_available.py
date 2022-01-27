# This test checks the availability of the site https://ya.ru/. 
# if the site is available, the value 200 is returned and test is considered passed.
# Otherwise the site is not available

import urllib.request

def test_ya_ru_is_on():
    str = urllib.request.urlopen("https://ya.ru/").getcode()
    assert str == 200, "Site ya.ru is not available"