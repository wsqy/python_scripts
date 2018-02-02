import requests

from functools import lru_cache


@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with requests.get(resource) as s:
            return s.content()
    except Exception as e:
        return 'error:{}'.format(e)


for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
    pep = get_pep(n)
    print(n, len(pep))

print(dir(get_pep))
print(help(get_pep.cache_info))
print(get_pep.cache_info())

print(help(get_pep.cache_clear))
