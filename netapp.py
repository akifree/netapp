# - Change DNS ---
"""
使用法: networksetup -setdnsservers < networkservice > <dns1 > [dns2][...]
<networkservice > DNSサーバを < dns1 > [dns2][...]に設定します。任意の数のDNSサーバを
を指定します。< dns1 > に"Empty"を指定すると、すべてのDNSエントリがクリアされます。

Cloudflare 1.1.1.1 1.0.0.1 2606:4700:4700::1111 2606:4700:4700::1001
google 8.8.8.8 8.8.4.4 2001:4860:4860::8888 2001:4860:4860::8844
"""

import subprocess
import sys


cloudflare
if cloudflare:
    cp = subprocess.run(['networksetup', '-setdnsservers',
                        'Ethernet', '2606:4700:4700::1111', '2606:4700:4700::1001', '1.1.1.1', '1.0.0.1'])
    if cp.returncode != 0:
        print('Change DNS failed', file=sys.stderr)
        sys.exit(1)
else:
    cp = subprocess.run(['networksetup', '-setdnsservers',
                         'Ethernet', '2606:4700:4700::1111', '2606:4700:4700::1001', '1.1.1.1', '1.0.0.1'])
    if cp.returncode != 0:
        print('Change DNS failed', file=sys.stderr)
        sys.exit(1)
