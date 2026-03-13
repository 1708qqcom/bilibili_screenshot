from playwright.sync_api import sync_playwright

def save_login_state():
    with sync_playwright() as p:
        # 启动 Edge 浏览器
        browser = p.chromium.launch(channel="msedge", headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # 1. 这里替换为你需要登录的网站的地址
        login_url = "https://www.bilibili.com/" 
        print(f"正在打开登录页面: {login_url}")
        page.goto(login_url)
        
        # 2. 暂停脚本，等待你手动在浏览器里完成登录、扫码或过验证码
        print("\n" + "="*50)
        print("请在弹出的浏览器中完成登录操作！")
        print("登录成功，且页面加载完全后，请回到这个黑框框里按【回车键】继续...")
        print("="*50 + "\n")
        
        input() # 脚本会在这里卡住，直到你按下回车
        
        # 3. 将包含 Cookie 和 LocalStorage 的登录状态保存到本地文件
        context.storage_state(path="login_state.json")
        print("太棒了！登录状态已成功保存到当前目录下的 login_state.json 文件中。")
        
        browser.close()

if __name__ == "__main__":
    save_login_state()