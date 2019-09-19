from http.client import HTTPConnection

host = 'www.example.com'
conn = HTTPConnection(host)
conn.request('GET', '/')
r1 = conn.getresponse()
print(r1.status, r1.reason) # 200 OK

data1 = r1.read()
# 일부만 읽는 경우는, 두 번째 요청 시 에러 남
# data1 = r1.read(100)

# 두 번째 요청에 대한 테스트
conn.request('GET', '/')
r2 = conn.getresponse()
print(r2.status, r2.reason) # 200 OK

data2 = r2.read()
print(data2.decode())

conn.close()
