from translate import Translator
import requests
from bs4 import BeautifulSoup


def translate_text(text, target_lang):
    # 翻訳元の言語を自動検出し、翻訳先の言語を指定してTranslatorをインスタンス化
    translator = Translator(from_lang='autodetect', to_lang=target_lang)
    # 翻訳メソッドを呼び出して結果を取得
    translation = translator.translate(text)
    return translation

def pull_text(url):
    # HTTPリクエストを送信してページのHTMLを取得
    response = requests.get(url)
    # ステータスコードが200以外の場合、エラーを出力して終了
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        exit()
    # 取得したHTMLをBeautifulSoupで解析
    soup = BeautifulSoup(response.text, 'html.parser')

    # ここからはBeautifulSoupを使用して必要な情報を取得する
    # 例: タイトルを取得
    title = soup.title.text
    print(f"Title: {title}")


# スクレイピング対象のURL
pull_text('https://ncode.syosetu.com/n1784ga/1/')



print(translate_text("おっぱい", target_lang='en'))