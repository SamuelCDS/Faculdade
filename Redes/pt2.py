import http.client
conn = http.client.HTTPConnection(HOST, PORT)
conn.request("GET" "/pages/index2.html")
r1 = conn.getresponse()
print(r1.status, r1.reason)
headers = r1.getheader()
print(headers[0][0], ":", headers[0][1])
