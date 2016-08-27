import urllib.request
import http.cookiejar

filename = 'cookie.txt'
#声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

response = opener.open('http://www.baidu.com')
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)

#########################################################
#                                                              错误处理                                                            #
#########################################################
#request = urllib.request.Request("http://k3k4k5k9.com")
#try:
#	response = urllib.request.urlopen(request)
#	print (response.read())	
#except urllib.error.HTTPError as e:
#	print (e.code)
#except urllib.error.URLError as e:
#	print (e.reason)

