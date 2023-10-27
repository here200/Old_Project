from common import ky_requests, ky_etrees
import os
import time

# 发送请求，获取响应
res = ky_requests.decode_response(ky_requests.get("https://cn.bing.com/"))

# 获取标题和链接
ky_etrees.html_cache = ky_etrees.generate_html_by_string(res)
title = ky_etrees.get_one_data_by_xpath("//meta[@property=\"og:title\"]/@content")
imgURL = ky_etrees.get_one_data_by_xpath("//link[@id=\"preloadBg\"]/@href")

# 下载图片
if not os.path.exists("./data/"):
    os.mkdir("./data/")
save_path = "./data/" + time.strftime('%Y-%m-%d') + "_" + title + ".jpg"
if not os.path.exists(save_path):
    img_response = ky_requests.get(imgURL)
    with open(save_path, "wb") as f:
        f.write(img_response.content)

# 提示
print("程序执行结束")
