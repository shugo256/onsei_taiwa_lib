# OnseiTaiwaLib

## 使い方
```python3
# import
from onsei_taiwa_lib.angry_siri.py import AngrySiri

# インスタンスの初期化
siri = AngrySiri()

# 初期化メッセージを送信し、その返答を表示
print(siri.init_talk()) # => ふつうです

# カスというメッセージを送信し、angryポイントを1加算し、その返答を表示
print(siri.talk('カス', angry_cnt=1)) # => ('せやな！', None)