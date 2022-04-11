# スクレイピングでファッションサイトのwearから画像を取得してみる
import base64
import shutil
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


def main():
    # 現在入っているwebdriverのversionが適切になるように入れてくれる便利なやつ
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # レディースのファッションランキングのリンク
    driver.get('https://wear.jp/women-ranking/')
    div_search = driver.find_element(By.ID, 'main_list')
    print(div_search)
    class_search = div_search.find_element(By.CLASS_NAME, 'img')
    print(class_search)
    href = class_search.find_element(By.TAG_NAME, 'img').get_attribute('src')
    print(href)
    save_image(href, 'sample1.jpg')
    # ５秒間休憩（これをしないと、一瞬で閉じてしまう）
    time.sleep(5)
    driver.quit()


def save_image(src, file_save_path):
    if "base64" in src:
        with open(file_save_path, 'wb') as f:
            f.write(base64.b64decode(src.split(",")[1]))
    else:
        res = requests.get(src, stream=True)
        with open(file_save_path, 'wb') as f:
            shutil.copyfileobj(res.raw, f)

    return


if __name__ == "__main__":
    main()
