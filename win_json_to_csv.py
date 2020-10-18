import json
import csv
import re

def change():
    raw_data = open('win-output.json', 'r')
    data = json.load(raw_data)
    raw_data.close()


    results = []

    timestamp = data['timestamp']
    ping = data['ping']['latency']
    download = data['download']['bandwidth']
    upload = data['upload']['bandwidth']
    isp = data['isp']
    internalIp = data['interface']['internalIp']
    # name = data['interface']['name']
    externalIp = data['interface']['externalIp']
    server_id = data['server']['id']
    server = data['server']['name']
    server = re.sub('"', "", server)
    location = data['server']['location']

    # results.append([timestamp, ping, download, upload,
    #                 isp, internalIp, name, externalIp, server_id, server, location])
    results.append([timestamp, ping, download, upload,
                    isp, internalIp, externalIp, server_id, server, location])

        
    # ファイルが空か調べる
    # https://www.it-swarm-ja.tech/ja/python/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%8C%E7%A9%BA%E3%81%8B%E3%81%A9%E3%81%86%E3%81%8B%E8%AA%BF%E3%81%B9%E3%82%8B%E6%96%B9%E6%B3%95%E3%81%AF%EF%BC%9F/968141004/
   
    import os
    flag = os.stat('win_speedtest.csv').st_size != 0 
   

    if flag: # データがあるので、一番下に追加
        raw_csv = open('win_speedtest.csv', 'a')
        csvwriter = csv.writer(raw_csv)
        for result in results:
            csvwriter.writerows(results)
        raw_csv.close()
        
    else: # データがなければ新規作成
        raw_csv = open('win_speedtest.csv', 'r+')
        csvwriter = csv.writer(raw_csv)
        # csvwriter.writerow(['timestamp', 'ping', 'download', 'upload', 'packetLoss', 'isp', 'internalIp', 'name', 'externalIp', 'server_id', 'server', 'location'])
        csvwriter.writerow(['timestamp', 'ping', 'download', 'upload',
                            'isp', 'internalIp', 'externalIp', 'server_id', 'server', 'location'])
        for result in results:
            csvwriter.writerows(results)
        raw_csv.close()
    


if __name__ == '__main__':
    change()
