# - Speed Test ---
# def speedTest():
import subprocess
import sys
import json
import re

import json_to_csv


path_w = '/Users/aki/StudyProg/studyPython/output.json'

# speedtestコマンドの実行、結果を標準出力する。
# cp = subprocess.run(['speedtest', '--server-id=17838', '-f', 'json'], encoding='utf-8', stdout=subprocess.PIPE)
cp = subprocess.run(['speedtest', '--server-id=24774', '-f',
                    'json'], encoding='utf-8', stdout=subprocess.PIPE)
if cp.returncode != 0:
    print('speed test faild', file=sys.stderr)
    sys.exit(1)


data = cp.stdout
data = re.sub('\n', "", data)

# print(data)
# print("---------output")

data = json.loads(data)  # JSON文字列を辞書に変換
# print(type(data))

json_data = open(path_w, mode='w')
json.dump(data, json_data)  # 辞書をJSONファイルとして保存
json_data.close()
# print("--------dump")

# Mbpsに変換
download = int(data["download"]["bandwidth"]) * 8 / 1000 / 1000
upload = int(data["upload"]["bandwidth"]) * 8 / 1000 / 1000
download = round(download, 2)
upload = round(upload, 2)
print("Download: {}Mbps, Upload: {}Mbps".format(download, upload))

# CSVファイルへの出力
json_to_csv.change()


