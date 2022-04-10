# スクレイピングでファッションサイトのwearから画像を取得してみる
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


def main():
    # 現在入っているwebdriverのversionが適切になるように入れてくれる便利なやつ
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # レディースのファッションランキングのリンク
    driver.get('https://wear.jp/women-ranking/')
    # ５秒間休憩（これをしないと、一瞬で閉じてしまう）
    time.sleep(5)
    driver.quit()

    return


if __name__ == "__main__":
    main()
