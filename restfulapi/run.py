from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
	return 'hello world3'

if __name__=="__main__":
	app.run(host='10.0.2.15',debug=True)

# 端口转发配置：TCP 192.168.56.1 5000 10.0.2.15 5000
# 以太网适配器 VirtualBox Host-Only Network:

#    连接特定的 DNS 后缀 . . . . . . . :
#    本地链接 IPv6 地址. . . . . . . . : fe80::e8a1:e016:714b:4181%18
#    IPv4 地址 . . . . . . . . . . . . : 192.168.56.1
# 主机浏览器访问：192.168.56.1:5000


# 或者端口转发配置：TCP 127.0.0.1 5000 10.0.2.15 5000
# 或者端口转发配置：TCP （空白） 5000 10.0.2.15 5000
# 或者端口转发配置：TCP （空白） 5000 (空白) 5000 
# 空白其实等同于0.0.0.0任一ip