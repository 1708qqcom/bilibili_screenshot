import os
import re
import time
from playwright.sync_api import sync_playwright

URLS = []
# 从 urls.txt 读取视频链接
with open('./urls.txt','r',encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            URLS.append(line)

SAVE_FOLDER = r"./screenshots"

def sanitize_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

def run():
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=False)
        
        # ================= 核心修改在这里 =================
        # 加载你刚才保存的登录状态文件
        context = browser.new_context(storage_state="login_state.json")
        # ==================================================
        
        page = context.new_page()

        for index, url in enumerate(URLS, start=1):
            try:
                print(f"[{index}/{len(URLS)}] 正在加载: {url}")
                page.goto(url, wait_until="networkidle", timeout=30000)
                
                # 留出时间让视频页面的动态数据（包括已登录的用户信息）加载出来
                time.sleep(2) 

                raw_title = page.title()
                safe_title = sanitize_filename(raw_title)

                filename = f"{index}_{safe_title}.png"
                filepath = os.path.join(SAVE_FOLDER, filename)

                page.screenshot(path=filepath)
                print(f" ---> 截图已成功保存为: {filename}\n")

            except Exception as e:
                print(f" ---> 访问 {url} 时出现错误: {e}\n")

        print("所有网页均已处理完毕，请前往文件夹查看！")
        browser.close()

if __name__ == "__main__":
    run()