# OnseiTaiwaLib

## 使い方
### MultiAngrySiri
```python3
# import
from onsei_taiwa_lib.angry_siri import MultiAngrySiri

# インスタンスの初期化、ユーザをAさん, Bさん, Cさんとする
siri = MultiAngrySiri(['Aさん', 'Bさん', 'Cさん'])

# 初期化メッセージの返答を表示
print(siri.init_talks()) # => ふつうです

# 発言者をAさんとしてカスというメッセージを送信し、angryポイントを1加算し、その返答を表示
print(siri.talk('Aさん', 'カス', angry_cnt=1)) # => ('せやな！', None)

# Bさんのモードを取得
print(siri.get_mode('Bさん')) # => normal

# (今回は使わないとおもうが)ユーザの動的追加
siri.add_user('Dさん')
```

### AngrySiri
```python3
# import
from onsei_taiwa_lib.angry_siri import AngrySiri

# インスタンスの初期化
siri = AngrySiri()

# 初期化メッセージを送信し、その返答を表示
print(siri.init_talk()) # => ふつうです

# カスというメッセージを送信し、angryポイントを1加算し、その返答を表示
print(siri.talk('カス', angry_cnt=1)) # => ('せやな！', None)
```

## 設定
`config.py`でAPIキーやボットID、モード切替のためのスコアの上限値、下限値などAngrySiriクラスで用いる定数を変更できる。
