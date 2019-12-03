from config import *
from repl_ai_communicator import ReplAICommunicater


NORMAL_MODE = 0
HAPPY_MODE  = 1
ANGRY_MODE  = 2


class AngrySiri(ReplAICommunicater):
    def __init__(self):
        super(AngrySiri, self).__init__(API_KEY, BOT_ID, NORMAL_TOPIC_ID)
        self.score = 0
        self.mode = NORMAL_MODE

    def update(self, happy_cnt=0, angry_cnt=0):
        self.score += happy_cnt - angry_cnt

        if self.mode != HAPPY_MODE and self.score >= HAPPY_BOTTOM:
            self.mode = HAPPY_MODE
            return self.change_topic(HAPPY_TOPIC_ID)
        
        elif self.mode != ANGRY_MODE and self.score <= ANGRY_TOP:
            self.mode = ANGRY_MODE
            return self.change_topic(ANGRY_TOPIC_ID)

        elif self.mode != NORMAL_MODE and ANGRY_TOP < self.score < HAPPY_BOTTOM:
            self.mode = NORMAL_MODE
            return self.change_topic(NORMAL_TOPIC_ID)
        
        return None

    '''
    親クラスの関数たち
    - change_topic(self, topic_id) # topic_idを変更してinit messageを送信
    - talk(self, message)          # messageを送信
    '''

if __name__ == "__main__":
    ansi = AngrySiri()
    print('[メッセージ] [加算スコア]\nという形式で入力してね', flush=True)
    while True:
        mes, score = input().split(' ')
        upd = ansi.update(int(score))
        if upd != None:
            print('==> ' + upd)
        print('>>> ' + ansi.talk(mes))
