# - Speed Test ---

import subprocess
import sys
import re
import json

import win_json_to_csv


cp = subprocess.run(['speedtest', '-f', 'json'], encoding='utf-8', stdout=subprocess.PIPE)
if cp.returncode != 0:
    print('speed test faild', file=sys.stderr)
    sys.exit(1)


data = cp.stdout
data = re.sub('\n', "", data)
# print(data)

data = json.loads(data)

json_data = open('win-output.json', mode='w')
json.dump(data, json_data)
json_data.close()


download = int(data["download"]["bandwidth"]) * 8 / 1000 /1000
upload = int(data["upload"]["bandwidth"]) * 8 / 1000 /1000
download = round(download, 2)
upload = round(upload, 2)
print("Download: {}Mbps, Upload: {}Mbps".format(download, upload))


win_json_to_csv.change()