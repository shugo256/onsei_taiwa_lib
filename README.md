# OnseiTaiwaLib

## 使い方
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

### MultiAngrySiri (複数人用)
```python3
# import
from onsei_taiwa_lib.angry_siri import MultiAngrySiri

# インスタンスの初期化、ユーザをAさん, Bさん, Cさんとする
siri = MultiAngrySiri(['Aさん', 'Bさん', 'Cさん'])

# ユーザーデータをロードせずに使う場合
siri = MultiAngrySiri(['Aさん', 'Bさん', 'Cさん'], load_pickle=False)

# 初期化メッセージの返答を表示
print(siri.init_talks()) # => ふつうです

# 発言者をAさんとしてカスというメッセージを送信し、angryポイントを1加算し、その返答を表示
print(siri.talk('Aさん', 'カス', angry_cnt=1)) # => ('せやな！', None)

# Bさんのモード、スコアを取得
print(siri.get_mode('Bさん')) # => normal
print(siri['Bさん'].score)    # => 10
# こういう感じでsiri[username]とすればuserに対応するAngrySiriオブジェクトにアクセスできるので、
# たとえば上のtalk関数は
siri['Aさん'].talk('カス', angry_cnt=1) # でもよい

# (今回は使わないとおもうが)ユーザの動的追加
siri.add_user('Dさん')

# 中断時の保存
try:
  ...
except KeyboardInterrupt:
    siri.save()
```

## 設定
`config.py`でAPIキーやボットID、モード切替のためのスコアの上限値、下限値などAngrySiriクラスで用いる定数を変更できる。
