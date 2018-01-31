"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
domain_name("www.xakep.ru") == "xakep"
"""
import re
from urllib.parse import urlparse

# def domain_name(url):
#     return (urlparse(url).netloc or urlparse(url).path).split('.')[-2]
#
#
def domain_name(url):
    return url.split("//")[-1].split('.')[-2]
#
#
# def domain_name(url):
#     return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


print(domain_name("http://www.test.zombie-bites.com/dsfgfg/.43854.oerui"))
