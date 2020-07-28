# - Ping ---

"""
Pingの結果次第でCloudflareとGoogleのDNSを切り替えます
"""


import subprocess
import sys
import time


# 10分毎に24時間実行
for i in range(1, 145, 1):
    time.sleep(600)
    print(i*10, "分経過")


    # Cloudflare DNS への Ping
    cd = subprocess.Popen(['ping', '-c 5', '1.1.1.1'], encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    buf = []

    while True:
        line = cd.stdout.readline()
        buf.append(line)
        # sys.stdout.write(line) # ターミナルの標準出力

        if not line and cd.poll() is not None:
            break

    # print('----------------')
    # print(buf[9])

    c_s = buf[9]
    c_min = float(c_s[32:38])
    c_avg = float(c_s[39:45])
    c_max = float(c_s[46:52])
    c_stddev = float(c_s[53:59])

    print("Cloudflare")
    print("min    avg    max    stddev")
    print(c_min, c_avg, c_max, c_stddev)


    # Google DNS への Ping
    gd = subprocess.Popen(['ping', '-c 5', '8.8.8.8'], encoding='utf-8',
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    buf = []

    while True:
        line = gd.stdout.readline()
        buf.append(line)
        # sys.stdout.write(line)  # ターミナルの標準出力

        if not line and gd.poll() is not None:
            break

    # print('----------------')
    # print(buf[9])

    g_s = buf[9]
    g_min = float(g_s[32:38])
    g_avg = float(g_s[39:45])
    g_max = float(g_s[46:52])
    g_stddev = float(g_s[53:59])

    print("Google")
    print("min    avg    max    stddev")
    print(g_min, g_avg, g_max, g_stddev)



    # 2つ以上のフラグでDNSの切り替え。（Cloudflare優先）
    c_flag = 0
    g_flag = 0

    if c_min > g_min:
        g_flag += 1
    else:
        c_flag += 1

    if c_avg > g_avg:
        g_flag += 1
    else:
        c_flag += 1

    if c_max > g_max:
        g_flag += 1
    else:
        c_flag += 1

    if c_stddev > g_stddev:
        g_flag += 1
    else:
        c_flag += 1


    # DNSの切り替え
    if c_flag >= g_flag:
        cp = subprocess.run(['networksetup', '-setdnsservers',
                            'Ethernet', '2606:4700:4700::1111', '2606:4700:4700::1001', '1.1.1.1', '1.0.0.1'])
        if cp.returncode != 0:
            print('Change DNS failed', file=sys.stderr)
            sys.exit(1)
        print("--- Set Cloudflare DNS ---------")
    else:
        cp = subprocess.run(['networksetup', '-setdnsservers',
                            'Ethernet', '2001:4860:4860::8888', '2001:4860:4860::8844', '8.8.8.8', '8.8.4.4'])
        if cp.returncode != 0:
            print('Change DNS failed', file=sys.stderr)
            sys.exit(1)
        print("--- Set Google DNS ---------")




