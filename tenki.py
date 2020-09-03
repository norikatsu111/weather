# モジュールを取り込む
import json
import urllib.request

# 為替情報を得るクラス
class Kawase:
    ## 為替情報の取得元（筆者のWebサイト）
    #API = "https://api.aoikujira.com/kawase/json/usd"
    # サービス停止中の為、筆者のWebサイトのIPアドレス確認APIを取得
    API = "https://api.aoikujira.com/tenki/week.php?fmt=json&city=319"
    
    # 非公開のメソッド
    def __get_api(self):
        ''' APIから今日のレート情報を得る '''
        res = urllib.request.urlopen(Kawase.API)
        return res.read().decode("utf8")
    
    def __analize_result(self, json_str):
        ''' 結果を解析する '''
        return json.loads(json_str)
    
    # 公開メソッド
    def get_result(self):
        ''' APIから為替情報を取得する '''
        json_str = self.__get_api()
        return self.__analize_result(json_str)
    
    # 静的メソッド
    @staticmethod
    def get_usd_jpy():
        ''' USD/JPY の結果を得る '''
        kawase = Kawase()
        data = kawase.get_result()
        usd = data.get("319", -1)
        return usd
        #return data

## 本日の為替レート情報を表示
#print("USD:319 = 1 :", Kawase.get_usd_jpy())

# 
# IPアドレス情報を表示emurate
#for i, list in enumerate(Kawase.get_usd_jpy()): # リスト[]からインデックス付きのタプル
for list in (Kawase.get_usd_jpy()): # リスト[]からインデックス付きのタプル
	for info, value in list.items():

	    print(info, ":", value)

