# 前言
主要用于需要批量上传一键三联的视频截图

# 安装第三方软件
pip install playwright
playwright install chromium

# 使用方法
1、首先需要自己登录账号，把需要进行上传的一键三联的视频进行一键三联，方便后面自动截图。
2、在电脑运行 python get_login.py 登录自己的账号，登录之后，就会在当前文件目录下生成一个 json文件
3、添加需要截图的b站链接，填写urls.txt
4、运行python auto_screenshot.py 文件，就会开始自动截图，

# 实现效果
<img width="1260" height="665" alt="image" src="https://github.com/user-attachments/assets/6a0ca4ac-b0dc-41a9-b957-c02bc78d0425" />
