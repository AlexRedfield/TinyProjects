from twilio.rest import Client
import pandas as pd
import datetime
import time
import cv2
import numpy as np
import easygui
import threading

auth_token = pd.read_csv('D:/Documents/token/auth token.txt', header=None)[0][0]
account_sid = pd.read_csv('D:/Documents/token/account sid.txt', header=None)[0][0]
phone_number = pd.read_csv('D:/Documents/token/Sre phone number.txt', header=None)[0][0]
dst_number = pd.read_csv('D:/Documents/token/Dst phone number.txt', header=None)[0][0]


def send_message():
    client = Client(account_sid, auth_token)
    client.messages.create(
        dst_number,
        body="your house has been breached",
        from_=phone_number,
    )

def add_time(time1):
    time2=time.time()
    delta=time2-time1
    return delta
if __name__ == '__main__':
    countdown = 5
    cv2.namedWindow("camera", 1)
    # 开启ip摄像头
    video = "http://admin:admin@192.168.0.3:8081/"
    camera = cv2.VideoCapture(video)

    if not camera.isOpened():
        #easygui.msgbox("Please turn on your camera")
        camera = cv2.VideoCapture(0)
    # 取得摄像头图像大小
    size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    print('camera size:', str(size))
    es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 4))
    kernel = np.ones((5, 5), np.uint8)
    background = None
    time1=None
    flag = 1
    warn=0

    while True:
        text = 'Undetected'
        grabbed, frame_img = camera.read()

        # 灰度化
        gray_img = cv2.cvtColor(frame_img, cv2.COLOR_BGR2GRAY)
        # 高斯模糊化,第三个参数表示模糊的程度
        gray_img = cv2.GaussianBlur(gray_img, (25, 25), 3)

        if background is None:
            background = gray_img
            continue

        # 调用差分方法，取得与标准图像之间的不同
        diff = cv2.absdiff(background, gray_img)

        # 设定一个阈值(源图像，阈值，填充色，阈值类型)
        # 此阈值类型（0）小于阈值的像素点置0，大于阈值的像素点置填充色
        diff = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY)[1]

        # 膨胀图像
        diff = cv2.dilate(diff, es, iterations=2)
        # type(diff):<class 'numpy.ndarray'>
        # 捕捉ROI(白色区域) @image,mode,method
        # contours: 图像轮廓的集合
        image, contours, hierarchy = cv2.findContours(diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            # type(c) <class 'numpy.ndarray'>
            # 轮廓面积
            if cv2.contourArea(c) < 2500:
                continue
            # x,y是矩阵左上点的坐标 w,h是矩阵的宽和高
            ''' /
            (x, y, w, h) = cv2.boundingRect(c)
            # 圈出ROI @image,pt1,pt2,color,thickness
            cv2.rectangle(frame_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            '''
            # 用红色表示有旋转角度的矩形框架
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(frame_img, [box], 0, (0, 0, 255), 2)

            text = 'Detected'

        if text == 'Undetected' and not warn:
            cv2.putText(frame_img, "Motion:{}".format(text), (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame_img, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                        (10, frame_img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)
            time1=None

        if text == 'Detected' or warn:
            cv2.putText(frame_img, "Motion:{}".format(text), (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(frame_img, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                        (10, frame_img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

            if time1 is None:
                time1=time.time()

            time2=add_time(time1)
            time2=round(countdown-time2,2)

            if time2>0:
                cv2.putText(frame_img, str(time2),(10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                warning='Warning! Your house has been invaded'
                warn=1
                cv2.putText(frame_img, warning, (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if countdown<add_time(time1):
                print("warning")



            # 发送短信
            if flag and countdown<add_time(time1):
                # send_message()
                print("your house has been breached")
                flag = 0

        cv2.imshow("camera", frame_img)
        cv2.imshow("dis", diff)
        cv2.waitKey(10)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    # release the capture
    camera.release()
    cv2.destroyAllWindows()

''' 
    num = 0
    while True:
        success, img = camera.read()
        cv2.imshow("camera", img)

        # 按键处理，注意，焦点应当在摄像头窗口，不是在终端命令行窗口
        key = cv2.waitKey(10)

        if key == 27:
            # esc键退出
            print("esc break...")
            break
        if key == ord('a'):
            # 按指定的键保存一张图像
            num = num + 1
            filename = "frames_%s.jpg" % num
            cv2.imwrite(filename, img)

    camera.release()
    cv2.destroyWindow("camera")

'''
