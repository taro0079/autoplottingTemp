from matplotlib import pyplot as plt
import csv 
import serial
import datetime
import os
import time
## 温度を計測してリアルタイムプロット

def main():
    # serial 接続設定
    serial.baudrate = 9600

    # ardiunoのポートを特定する（多分Mac専用）
    for file in os.listdir('/dev/'):
        if "tty.usbmodem" in file:
            serial.port = '/dev/' + file

    # データの初期化
    time_data = [] # 時間用に適当な大きさ配列を確保
    temp_data = [] # 温度データ用に適当な大きさ配列を確保
    starttime = time.time() # 時間の初期化
    # matplotlib設定
    fig = plt.figure()
    li, = plt.plot(time_data, temp_data)
    plt.xlabel ("Time (s)") # x軸ラベル
    plt.ylabel("Temperature") # y軸ラベル

    to = 6 # time out
    with serial.Serial(serial.port, serial.baudrate, timeout=to) as ser:
        while True:
            
            T = ser.readline().rstrip().decode(encoding='utf-8') # データを取得
            if T !="": # serialからのデータがなにもないときがある
                nowtime = time.time() # 時間計測
                temp = float(T) # String -> float

                Time = nowtime - starttime # 時間差分

                time_data.append(Time)
                temp_data.append(temp)

                li.set_data(time_data, temp_data)
                plt.xlim(min(time_data), max(time_data))
                plt.ylim(min(temp_data), max(temp_data))

                fig.canvas.mpl_connect('close_event', handle_close)
                plt.pause(.5)

def handle_close(evt):
    print("close!")
    exit()

if __name__ == "__main__":
    main()



