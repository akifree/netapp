# - Ping ---

"""
Pingの結果次第でCloudflareとGoogleのDNSを切り替えます
"""


def Measurement():
    import subprocess
    import datetime


    ########################################################################
    # Cloudflare Zone
    ########################################################################

    # Get time
    c_timestamp = datetime.datetime.now()
    print(c_timestamp)

    c_dns = "Cloudflare"

    # Run ping process 
    cd = subprocess.check_output(['ping', '1.1.1.1'], encoding='shift_jis')

    # Store data
    buf = cd.splitlines()
    c_packet = buf[8]
    c_resultTime = buf[10]

    # Display result
    print("  Cloudflare")
    print(c_packet)
    print(c_resultTime)


    c_packetArray = c_packet.split('、')

    c_upload = c_packetArray[0].split()
    c_upload = c_upload[3]

    c_download = c_packetArray[1].split()
    c_download = c_download[2]

    c_packetloss = c_packetArray[2].split()
    c_packetloss = c_packetloss[2]


    c_resultTimeArray = c_resultTime.split('、')

    c_min = c_resultTimeArray[0].split()
    c_min = c_min[2]

    c_max = c_resultTimeArray[1].split()
    c_max = c_max[2]

    c_average = c_resultTimeArray[2].split()
    c_average = c_average[2]




    ########################################################################
    # Google Zone
    ########################################################################

    # Get time
    g_timestamp = datetime.datetime.now()
    # print(g_timestamp)

    g_dns = "Google"

    # Run ping process
    gd = subprocess.check_output(['ping', '8.8.8.8'], encoding='shift_jis')

    # Store data
    buf = gd.splitlines()
    g_packet = buf[8]
    g_resultTime = buf[10]

    # Display result
    print("  Google")
    print(g_packet)
    print(g_resultTime)


    g_packetArray = g_packet.split('、')

    g_upload = g_packetArray[0].split()
    g_upload = g_upload[3]

    g_download = g_packetArray[1].split()
    g_download = g_download[2]

    g_packetloss = g_packetArray[2].split()
    g_packetloss = g_packetloss[2]


    g_resultTimeArray = g_resultTime.split('、')

    g_min = g_resultTimeArray[0].split()
    g_min = g_min[2]

    g_max = g_resultTimeArray[1].split()
    g_max = g_max[2]

    g_average = g_resultTimeArray[2].split()
    g_average = g_average[2]


    ########################################################################
    # Store Zone
    ########################################################################

    c_results = []
    g_results = []

    c_results.append([c_timestamp, c_dns, c_upload, c_download,
                      c_packetloss, c_min, c_max, c_average])
    g_results.append([g_timestamp, g_dns, g_upload, g_download,
                      g_packetloss, g_min, g_max, g_average])


    # Check if the file is empty
    import os
    flag = os.stat('win_pingresult.csv').st_size != 0


    import csv
    if flag:
        raw_csv = open('win_pingresult.csv', 'a')
        csvwriter = csv.writer(raw_csv)
        for c_result in c_results:
            csvwriter.writerows(c_results)
        for g_result in g_results:
            csvwriter.writerows(g_results)
        raw_csv.close()
    else:
        raw_csv = open('win_pingresult.csv', 'r+')
        csvwriter = csv.writer(raw_csv)
        csvwriter.writerow(['timestamp', 'dns', 'upload', 'download', 'packketloss', 'min', 'max', 'average'])
        for c_result in c_results:
            csvwriter.writerows(c_results)
        for g_result in g_results:
            csvwriter.writerows(g_results)
        raw_csv.close()


if __name__ == '__main__':
    import time
    for i in range(1, 168, 1):
        time.sleep(3600)
        Measurement()
