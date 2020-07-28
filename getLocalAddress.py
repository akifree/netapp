# - Get Local Address ---

"""
他のやり方。こっちのほうがかんたん。
URL: https://qiita.com/KEINOS/items/ae5446a96fafb84cb127
>>> networksetup - GetInfo <networkservice>
                           <Wi-Fi, Ethernet>
"""

# def getLocalAddress():
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET=IPv4 SOCK_DGRAM=UDP
s.connect(("8.8.8.8", 80)) # 接続先の指定と接続
print(s.getsockname()) # アドレスの取得
s.close() # 接続の解除


