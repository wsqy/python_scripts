import urllib.request

def print_list(L):
    for i in L:
        print(i)

def demo_21_6_22_1():
    f = urllib.request.urlopen('http://www.pythn.org')
    print(f.read())
    
def demo_21_6_22_2(): 
    req = urllib.request.Request(url='https://localhost/cgi-bin/test.cgi',data=b'This data is passed to stdin of the CGI')
    f = urllib.request.urlopen(req)
    print(f.read().decode('utf-8')) 

    
if __name__ == '__main__':
    demo_21_6_22_2()