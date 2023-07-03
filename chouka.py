import tkinter as tk
from PIL import ImageTk, Image
import math
import random
import cv2
from moviepy.editor import VideoFileClip
def open_new_window():
    # 关闭初始界面
    window.destroy()

    # 创建新界面
    new_window = tk.Tk()
    new_window.title("设置界面")
    # 创建组件集1
    label1 = tk.Label(new_window, text="三星奖励")
    label1.grid(row=0, column=0, padx=10, pady=10)

    entry1 = tk.Entry(new_window)
    entry1.grid(row=0, column=1, padx=10, pady=10)

    list1=["翡玉法球","飞天御剑","以理服人","鸦羽弓","讨龙英杰谭","黑缨枪"]
    list2=["祭礼剑","弓藏","西风长枪","西风大剑","瑶瑶","鹿野院平藏"]
    list3=["刻晴","迪卢克","艾尔海森"]
    list4=["翡玉法球","飞天御剑","以理服人","鸦羽弓","讨龙英杰谭","黑缨枪"]+["祭礼剑","弓藏","西风长枪","西风大剑","瑶瑶","鹿野院平藏"]+["刻晴","迪卢克","艾尔海森"]
    var = [tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(),
           tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(),tk.IntVar(), tk.IntVar()]  # 用于记录checkbutton是否选中


    #设置三星
    checkbox0 = tk.Checkbutton(new_window,text=list4[0],variable=var[0])
    checkbox0.grid(row=0//2+1, column=0%2, padx=10, pady=5, sticky="w")
    checkbox1 = tk.Checkbutton(new_window, text=list4[1],variable=var[1])
    checkbox1.grid(row=1 // 2 + 1, column=1 % 2, padx=10, pady=5, sticky="w")
    checkbox2 = tk.Checkbutton(new_window, text=list4[2],variable=var[2])
    checkbox2.grid(row=2 // 2 + 1, column=2 % 2, padx=10, pady=5, sticky="w")
    checkbox3 = tk.Checkbutton(new_window, text=list4[3],variable=var[3])
    checkbox3.grid(row=3 // 2 + 1, column=3 % 2, padx=10, pady=5, sticky="w")
    checkbox4 = tk.Checkbutton(new_window, text=list4[4],variable=var[4])
    checkbox4.grid(row=4 // 2 + 1, column=4 % 2, padx=10, pady=5, sticky="w")
    checkbox5 = tk.Checkbutton(new_window, text=list4[5],variable=var[5])
    checkbox5.grid(row=5 // 2 + 1, column=5 % 2, padx=10, pady=5, sticky="w")

    # 创建组件集2
    label2 = tk.Label(new_window, text="四星奖励")
    label2.grid(row=4, column=0, padx=10, pady=10)

    entry2 = tk.Entry(new_window)
    entry2.grid(row=4, column=1, padx=10, pady=10)
    #设置四星
    checkbox6 = tk.Checkbutton(new_window,text=list4[6],variable=var[6])
    checkbox6.grid(row=0//2+5, column=0%2, padx=10, pady=5, sticky="w")
    checkbox7 = tk.Checkbutton(new_window, text=list4[7],variable=var[7])
    checkbox7.grid(row=1 // 2 + 5, column=1 % 2, padx=10, pady=5, sticky="w")
    checkbox8 = tk.Checkbutton(new_window, text=list4[8],variable=var[8])
    checkbox8.grid(row=2 // 2 + 5, column=2 % 2, padx=10, pady=5, sticky="w")
    checkbox9 = tk.Checkbutton(new_window, text=list4[9],variable=var[9])
    checkbox9.grid(row=3 // 2 + 5, column=3 % 2, padx=10, pady=5, sticky="w")
    checkbox10 = tk.Checkbutton(new_window, text=list4[10],variable=var[10])
    checkbox10.grid(row=4 // 2 + 5, column=4 % 2, padx=10, pady=5, sticky="w")
    checkbox11 = tk.Checkbutton(new_window, text=list4[11],variable=var[11])
    checkbox11.grid(row=5 // 2 + 5, column=5 % 2, padx=10, pady=5, sticky="w")
    print(checkbox6)

    # 创建组件集3
    label3 = tk.Label(new_window, text="五星奖励")
    label3.grid(row=8, column=0, padx=10, pady=10)

    entry3 = tk.Entry(new_window)
    entry3.grid(row=8, column=1, padx=10, pady=10)
    def save():
        with open("config.txt", "w",encoding="utf-8") as file:
            file.truncate()
            card_num = [entry1.get(), entry2.get(), entry3.get()]
            for i in range(0,15):
                file.write(list4[i]+"："+str(var[i].get())+"\n")
                print(list4[i]+"："+str(var[i].get()))
            file.write("三星奖励数量：" + card_num[0] + "\n")
            file.write("四星奖励数量：" + card_num[1] + "\n")
            file.write("五星奖励数量：" + card_num[2])
            print(card_num[0])
            print(card_num[1])
            print(card_num[2])
            new_window.destroy()
        #设置五星
    checkbox12 = tk.Checkbutton(new_window, text=list4[12],variable=var[12])
    checkbox12.grid(row=0//2+9, column=0%2, padx=10, pady=5, sticky="w")
    checkbox13 = tk.Checkbutton(new_window, text=list4[13],variable=var[13])
    checkbox13.grid(row=1 // 2 + 9, column=1 % 2, padx=10, pady=5, sticky="w")
    checkbox14 = tk.Checkbutton(new_window, text=list4[14],variable=var[14])
    checkbox14.grid(row=2 // 2 + 9, column=2 % 2, padx=10, pady=5, sticky="w")
    baocun = tk.Button(new_window, text="保存", width=20, height=5,command=lambda:save())
    baocun.grid(row=12, column=1, padx=5, pady=5)
    center_window(new_window)
    new_window.mainloop()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def on_button_click():
    text = entry.get()
    print("Button clicked! Entered text: " + text)

def open_windows():
    # 创建窗口
    window = tk.Tk()
    window.title("快乐学习抽卡器")
    window.geometry("600x400")

    # 加载背景图片
    image = Image.open("background.jpg")
    background_image = ImageTk.PhotoImage(image)

    # 创建背景图片标签
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # 创建按钮和文本框
    button1 = tk.Button(window, text="设置",width=30,height=5, command=open_new_window)
    button1.pack(pady=30)

    button2 = tk.Button(window, text="开始抽",width=30,height=5)
    button2.pack(pady=30)

    entry = tk.Entry(window,width=30)
    entry.pack(pady=30)

    # 创建垂直布局
    window.grid_rowconfigure(0, weight=3)
    window.grid_rowconfigure(4, weight=3)

    # 窗口居中显示
    center_window(window)

    # 运行窗口的消息循环
    window.mainloop()

# 创建窗口
window = tk.Tk()
window.title("快乐学习抽卡器")
window.geometry("600x400")
def draw():
    #获得各项数据
    list1=["翡玉法球：","飞天御剑：","以理服人：","鸦羽弓：","讨龙英杰谭：","黑缨枪："]
    list1_1={}
    for i in list1:
        with open("config.txt", 'r',encoding="utf-8") as file:
            # 逐行读取文件内容
            for line in file:
                # 查找字符串在每一行中的位置
                index = line.find(i)
                if index != -1:
                    # 如果找到了字符串，获取字符串后面的数字部分
                    number_str = line[index + len(i):].strip()
                    try:
                        # 尝试将数字字符串转换为整数并返回
                        number = int(number_str)
                    except ValueError:
                        # 如果转换失败，则输出错误信息并返回 None
                        print("无法将字符串转换为整数。")
                        return None
        if(number==1):
            list1_1[i[0:-1]]=1
            print(i[0:-1]+":"+str(list1_1[i[0:-1]]))
    list2=["祭礼剑：","弓藏：","西风长枪：","西风大剑：","瑶瑶：","鹿野院平藏："]
    list2_1 = {}
    for i in list2:
        with open("config.txt", 'r', encoding="utf-8") as file:
            # 逐行读取文件内容
            for line in file:
                # 查找字符串在每一行中的位置
                index = line.find(i)
                if index != -1:
                    # 如果找到了字符串，获取字符串后面的数字部分
                    number_str = line[index + len(i):].strip()
                    try:
                        # 尝试将数字字符串转换为整数并返回
                        number = int(number_str)
                    except ValueError:
                        # 如果转换失败，则输出错误信息并返回 None
                        print("无法将字符串转换为整数。")
                        return None
        if (number == 1):
            list2_1[i[0:-1]] = 1
            print(i[0:-1] + ":" + str(list2_1[i[0:-1]]))
    list3=["刻晴：","迪卢克：","艾尔海森："]
    list3_1 = {}
    for i in list3:
        with open("config.txt", 'r', encoding="utf-8") as file:
            # 逐行读取文件内容
            for line in file:
                # 查找字符串在每一行中的位置
                index = line.find(i)
                if index != -1:
                    # 如果找到了字符串，获取字符串后面的数字部分
                    number_str = line[index + len(i):].strip()
                    try:
                        # 尝试将数字字符串转换为整数并返回
                        number = int(number_str)
                    except ValueError:
                        # 如果转换失败，则输出错误信息并返回 None
                        print("无法将字符串转换为整数。")
                        return None
        if (number == 1):
             list3_1[i[0:-1]] = 1
             print(i[0:-1] + ":" + str(list3_1[i[0:-1]]))
    list4 = ["三星奖励数量：","四星奖励数量：","五星奖励数量："]
    list4_1 = {}
    all=0
    for i in list4:
        with open("config.txt", 'r', encoding="utf-8") as file:
            # 逐行读取文件内容
            for line in file:
                # 查找字符串在每一行中的位置
                index = line.find(i)
                if index != -1:
                    # 如果找到了字符串，获取字符串后面的数字部分
                    number_str = line[index + len(i):].strip()
                    try:
                        # 尝试将数字字符串转换为整数并返回
                        number = int(number_str)
                        all=all+number
                    except ValueError:
                        # 如果转换失败，则输出错误信息并返回 None
                        print("无法将字符串转换为整数。")
                        entry.insert(0, "未输入奖励数量")
                        return None
        list4_1[i[0:-1]] = number
    all=all*(len(list1_1)+len(list2_1)+len(list3_1))*max(len(list1_1),len(list2_1),len(list3_1))#卡牌总数，len(list1_1)：三星奖励有几个
    list5={}    #用来记录所有卡牌，字典格式为25:"祭礼剑",表示祭礼剑这张牌有25张
    print(all)
    for i in list1_1.keys():
        list5[i]=all*list4_1["三星奖励数量"]/(list4_1["三星奖励数量"]+list4_1["四星奖励数量"]+list4_1["五星奖励数量"])/len(list1_1)
        print(i+":")
        print(list5[i])
    for i in list2_1.keys():
        list5[i]=all*list4_1["四星奖励数量"]/(list4_1["三星奖励数量"]+list4_1["四星奖励数量"]+list4_1["五星奖励数量"])/len(list2_1)
        print(i+":")
        print(list5[i])
    for i in list3_1.keys():
        list5[i]=all*list4_1["五星奖励数量"]/(list4_1["三星奖励数量"]+list4_1["四星奖励数量"]+list4_1["五星奖励数量"])/len(list3_1)
        print(i+":")
        print(list5[i])
    #进行随机数情况模拟
    intervals_dict = {}
    start = 0
    for name, value in list5.items():
        end = start + value
        intervals_dict[(start, end)] = name
        start = end + 1
    random_number = random.randint(0, start)

    # 判断随机整数所属区间，并输出区间名字
    def play_video_with_audio(file_path):
        # 加载视频文件
        video = VideoFileClip(file_path)

        # 获取视频的音频
        audio = video.audio

        # 播放视频
        video.preview(audio=audio)
    file_path={}
    for interval, name in intervals_dict.items():
        if interval[0] <= random_number <= interval[1]:
            # 打开视频文件
            video_path = name+".mp4"  # 替换为你自己的视频文件路径
            cap = cv2.VideoCapture(video_path)

            # 检查视频文件是否成功打开
            if not cap.isOpened():
                print("无法打开视频文件！")
                print(name)
                exit()

            # 获取视频帧的宽度和高度
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # 创建窗口
            cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

            # 获取屏幕的宽度和高度
            screen_width = cv2.getWindowImageRect('Video')[2]
            screen_height = cv2.getWindowImageRect('Video')[3]

            # 调整窗口大小以适应屏幕比例
            if width / height > screen_width / screen_height:
                new_width = screen_width
                new_height = int(height * screen_width / width)
            else:
                new_width = int(width * screen_height / height)
                new_height = screen_height

            cv2.resizeWindow('Video', new_width, new_height)

            # 循环读取和显示视频帧，直到视频结束或按下 'q' 键退出
            while True:
                # 读取视频帧
                ret, frame = cap.read()

                # 检查是否成功读取视频帧
                if not ret:
                    break

                # 调整视频帧大小以适应窗口
                resized_frame = cv2.resize(frame, (new_width, new_height))

                # 显示视频帧
                cv2.imshow('Video', resized_frame)

                # 检查是否按下 'q' 键
                if cv2.waitKey(1) & 0xFF == ord(' '):
                    break

            # 释放视频对象和关闭窗口
            cap.release()
            cv2.destroyAllWindows()
            print("随机整数", random_number, "属于区间", interval, "对应的名字是", name)
            entry_content = entry.get().strip()
            if entry_content:
                entry.delete(0, tk.END)
            entry.insert(0, "恭喜你，你抽到了"+name)
            break
# 加载背景图片
image = Image.open("background.jpg")
background_image = ImageTk.PhotoImage(image)

# 创建背景图片标签
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# 创建按钮和文本框
button1 = tk.Button(window, text="设置",width=30,height=5, command=open_new_window)
button1.pack(pady=30)

button2 = tk.Button(window, text="抽一发",width=30,height=5,command=lambda:draw())
button2.pack(pady=30)

entry = tk.Entry(window,width=30)
entry.pack(pady=30)

# 创建垂直布局
window.grid_rowconfigure(0, weight=3)
window.grid_rowconfigure(4, weight=3)

# 窗口居中显示
center_window(window)

#抽卡设置
def iscomplete():
    # 打开文本文件
    with open('config.txt', 'r',encoding="utf-8") as file:
        # 使用readlines()方法读取所有行，并将其存储在一个列表中
        lines = file.readlines()
    # 打印行数
    print("行数:", len(lines))
iscomplete()

# 运行窗口的消息循环
window.mainloop()

