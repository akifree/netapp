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
    name = data['interface']['name']
    externalIp = data['interface']['externalIp']
    server_id = data['server']['id']
    server = data['server']['name']
    server = re.sub('"', "", server)
    location = data['server']['location']



    results.append([timestamp, ping, download, upload,
                    isp, internalIp, name, externalIp, server_id, server, location])
    flag = 0

    with open('win_speedtest.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                flag = 1
            else:
                flag = 0
    f.close()

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
                            'isp', 'internalIp', 'name', 'externalIp', 'server_id', 'server', 'location'])
        for result in results:
            csvwriter.writerows(results)
        raw_csv.close()
    


if __name__ == '__main__':
    change()
