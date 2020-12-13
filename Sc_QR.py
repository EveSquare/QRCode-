#       ::::::::::    :::     :::       ::::::::::       ::::::::       ::::::::      :::    :::           :::        :::::::::       ::::::::::
#      :+:           :+:     :+:       :+:             :+:    :+:     :+:    :+:     :+:    :+:         :+: :+:      :+:    :+:      :+:
#     +:+           +:+     +:+       +:+             +:+            +:+    +:+     +:+    +:+        +:+   +:+     +:+    +:+      +:+
#    +#++:++#      +#+     +:+       +#++:++#        +#++:++#++     +#+    +:+     +#+    +:+       +#++:++#++:    +#++:++#:       +#++:++#
#   +#+            +#+   +#+        +#+                    +#+     +#+    +#+     +#+    +#+       +#+     +#+    +#+    +#+      +#+
#  #+#             #+#+#+#         #+#             #+#    #+#     #+#    #+#     #+#    #+#       #+#     #+#    #+#    #+#      #+#
# ##########        ###           ##########       ########       ###########    ########        ###     ###    ###    ###      ##########
from pyzbar.pyzbar import decode
from PIL import Image
from os.path import expanduser
import os
import cv2
from PIL import ImageGrab
import urllib.request, urllib.error
from selenium import webdriver

file_path = "capture.png"

def QRreade(image):
  # image変数の指し示す画像からQRコードの検出をする
  readResult = decode(Image.open(image))
  if (readResult != []):
    return readResult
  else:
    print('QRコードを検出できませんでした')
    exit()
#
#スクリーンショット
def screen_shot():
  ImageGrab.grab().save(file_path)

# ファイル削除
def file_remove():
  os.remove(file_path)

def checkURL(url):
    try:
        f = urllib.request.urlopen(url)
        print ("OK:" + url )
        f.close()
        return True
    except:
        print ("NotFound:" + url)
        return False

screen_shot()

qrResult = QRreade(file_path)
url = qrResult[0][0].decode('utf-8', 'ignore')

print("Scanned success")
print(f"wite -> {url}")

checkURL(url)

file_remove()



# ブラウザを開く。
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("./chromedriver.exe",options=options)
# Googleの検索TOP画面を開く。
driver.get(url)