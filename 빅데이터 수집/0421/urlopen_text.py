from urllib.request import urlopen

f = urlopen('http://hanbit.co.kr')
# HTTPResponse 자료형 객체 반환

print("f.read() => ",f.read())

print("f.status => ",f.status)
# 상태코드 추출

print("f.getheader =>",f.getheader('Content-Type'))
# 헤더 추출