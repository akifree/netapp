import time


# 一定間隔で処理を実行する
# time.sleep()

for i in range(1, 11, 1):
    time.sleep(600)
    print(i*10, "分経過")
