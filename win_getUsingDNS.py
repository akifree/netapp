# - Get Using DNS ---


import subprocess
import sys

cp = subprocess.Popen(['ipconfig', '/all'], encoding='utf-8')
if cp.returncode != 0:
    print("Get Using DNS faild!", file=sys.stderr)
    sys.exit(1)
