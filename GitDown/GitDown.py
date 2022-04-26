import time
import wget
import requests
import ast

#获取项目Github项目源地址
print("例如：https://github.com/Cyril0563/Github_tools")
url_pull = input("请输入要下载的github项目根目录地址：")
if url_pull =="":
    print("接口不能为空！")
    url_pull = input("请输入要下载的github项目根目录地址：")
print("解析中！请稍后……")
resp = requests.get("https://cdn.jsdelivr.net/gh/Cyril0563/Github_tools@main/GitDown/Api/url.txt")#获取镜像网站列表
str_url = resp.text
list_url = ast.literal_eval(str_url)
for i in range(10):
    #print(i)
    url_down = list_url[i] + "/" + url_pull + "/archive/refs/heads/" + "master.zip"
    resp2 = requests.get(url_down)
    if resp2.status_code == 200:
        wget.download(url_down)
        print("Github地址获取成功！解析请成功！")
        time.sleep(1)
        print("下载成功！请检查根目录内的zip文件")
        break
    else:
        i = i+1
        print("解析失败！正在自动切换第%d个接口"%(i))
        time.sleep(0.5)
        if i >= 5:
            print("\n请检查网络连接是否正常或Github地址是否正确！")
            print("若长时间无法使用！请联系作者反馈！")
            print("WeChat:Cyril0563")
            break





















































# print(url_down)
#wget.download(url_down)
    # resp = requests.get(url_down)
    # if resp.status_code == 404:
