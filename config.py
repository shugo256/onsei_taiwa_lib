# APIキーとBOTのID
API_KEY = '1Juy5Gv8Zg6afEGArJNkiY4cMAUT36MrQ6jRTZyL'
BOT_ID  = 'sample'

# 各シナリオのID
NORMAL_TOPIC_ID = 's4wve5oisr6g0ny'
HAPPY_TOPIC_ID  = 's4wvgsrfqyi60ny'
ANGRY_TOPIC_ID  = 's4ww2xmwo8r20ny'

# それぞれのモードに移行するスコアの境界値
THRESH = 2 

LIMMIT = THRESH * 2    # scoreの絶対値はこの値を超えない（超えた分はノーカン）
ANGRY_TOP    = -THRESH # この値以下のとき、Angry モード
HAPPY_BOTTOM =  THRESH # この値以上のとき、Happy もーど

# ユーザデータを格納しておくpickleのパス
PICKLE_PATH = 'onsei_taiwa_lib/user_data.pkl'