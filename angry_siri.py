import sys
sys.path.append('onsei_taiwa_lib')
from config import *
from repl_ai_communicator import ReplAICommunicater


NORMAL_MODE = 0
HAPPY_MODE  = 1
ANGRY_MODE  = 2


class AngrySiri(ReplAICommunicater):
    '''
    ReplAICommmunicaterにスコア機能を追加し、APIキーなどはconfig.pyから勝手に取得するようにしたクラス
    '''
    def __init__(self):
        super(AngrySiri, self).__init__(API_KEY, BOT_ID)
        self.score = 0
        self.mode = NORMAL_MODE

    def init_talk(self, topic_id=NORMAL_TOPIC_ID):
        return super(AngrySiri, self).init_talk(topic_id)


    def talk(self, message, happy_cnt=0, angry_cnt=0):
        '''
        messageを送信しつつ、スコアを更新し、必要に応じてモードを変える
        返答文章のリストを返す
        '''
        dia_resp = super(AngrySiri, self).talk(message)
        upd_resp = self.__update(happy_cnt, angry_cnt)

        return dia_resp, upd_resp
        

    def __update(self, happy_cnt, angry_cnt):
        '''
        スコアを更新し、必要に応じてモードを変える
        '''
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

if __name__ == "__main__":
    ansi = AngrySiri()
    print(ansi.init_talk())
    print('[メッセージ] [加算スコア]\nという形式で入力してね', flush=True)
    while True:
        mes, score = input().split(' ')
        print(ansi.talk(mes, int(score)))
