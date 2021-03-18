import requests
from line_access_token import ACCESS_TOKEN

import datetime
time = datetime.datetime.now()
#見やすい形（〇〇年◯◯月〇〇日　00:00:00）に変換
time = time.strftime('%Y年%m月%d日 %H:%M:%S')

def main():
    line_notify_api_url = 'https://notify-api.line.me/api/notify'
    headers = {"Authorization": "Bearer {}".format(ACCESS_TOKEN)}
    data = {"message": ("\r\n" + "任意のメッセージ" + "\r\n" + str(time) + " 現在")}

    #第一引数にアクセスするwebAPIのURL、引数のheadersに認証情報、引数のdataに送りたい内容
    requests.post(line_notify_api_url, headers = headers, data = data)


if __name__ == "__main__":
    main()