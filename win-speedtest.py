# - Speed Test ---

def speedTest():
    import subprocess
    import re
    import json

    import win_json_to_csv

    # speedtestコマンドの実行、結果を標準出力する。
    try:
        data = subprocess.check_output(['speedtest', '-f', 'json'], encoding='utf-8')
    except Exception:
        pass
    else:
        data = re.sub('\n', "", data)
        # print(data)

        data = json.loads(data)  # JSON文字列を辞書に変換

        json_data = open('win-output.json', mode='w')
        json.dump(data, json_data)  # 辞書をJSONファイルとして保存
        json_data.close()

        # Mbpsに変換
        download = int(data["download"]["bandwidth"]) * 8 / 1000 /1000
        upload = int(data["upload"]["bandwidth"]) * 8 / 1000 /1000
        download = round(download, 2)
        upload = round(upload, 2)
        print("    Download: {}Mbps, Upload: {}Mbps".format(download, upload))

        # CSVファイルへの出力
        win_json_to_csv.change()


if __name__ == '__main__':
    import time
    import datetime
    for i in range(1, 168, 1):
        time.sleep(60)
        print(datetime.datetime.now())
        speedTest()
