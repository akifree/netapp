# - Get Using DNS ---

import subprocess
import sys

# cp = subprocess.run(['networksetup', '-GetDNSServers', 'Wi-Fi'])
cp = subprocess.run(['networksetup', '-GetDNSServers', 'Ethernet'])
# cp = subprocess.run(['nslookup', 'google.com'])
if cp.returncode != 0:
    print('Get Using DNS failed', file=sys.stderr)
    sys.exit(1)
