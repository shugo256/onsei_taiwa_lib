import sys
sys.path.append('onsei_taiwa_lib')
import os
import pickle
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
        self.init_messages = [None, None, None]

    def init_talk(self, topic_id=NORMAL_TOPIC_ID):
        if self.init_messages[self.mode] == None:
            self.init_messages[self.mode] = super(AngrySiri, self).init_talk(topic_id)
        return self.init_messages[self.mode]


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

        # でかくなりすぎない & 小さくなりすぎないようにする
        self.score = min(self.score,  LIMMIT)
        self.score = max(self.score, -LIMMIT)

        if self.mode != HAPPY_MODE and self.score >= HAPPY_BOTTOM:
            self.mode = HAPPY_MODE
            return self.init_talk(HAPPY_TOPIC_ID)
        
        elif self.mode != ANGRY_MODE and self.score <= ANGRY_TOP:
            self.mode = ANGRY_MODE
            return self.init_talk(ANGRY_TOPIC_ID)

        elif self.mode != NORMAL_MODE and ANGRY_TOP < self.score < HAPPY_BOTTOM:
            self.mode = NORMAL_MODE
            return self.init_talk(NORMAL_TOPIC_ID)
        
        return None


class MultiAngrySiri(dict):
    '''
    AngrySiriを複数人分保持するクラス
    saveで保存したデータは、次回インスタンス生成時に復元される
    '''
    def __init__(self, user_list=[], load_pickle=True):
        if load_pickle and os.path.exists(PICKLE_PATH):
            with open(PICKLE_PATH, 'rb') as f:
                loaded_siri = pickle.load(f)
            self.__dict__.update(loaded_siri.__dict__)
            self.update(loaded_siri)
        else:
            self.init_normal_resp = None
        for user in user_list:
            self.add_user(user)
    
    def init_talks(self):
        return self.init_normal_resp
    
    def talk(self, target, message, happy_cnt, angry_cnt):
        return self[target].talk(message, happy_cnt, angry_cnt)

    def get_mode(self, target):
        ans = ['normal', 'happy', 'angry']
        return ans[self[target].mode]
    
    def add_user(self, username):
        if not username in self:
            self[username] = AngrySiri()
        self.init_normal_resp = self[username].init_talk()

    def save(self):
        with open(PICKLE_PATH, 'wb') as f:
            pickle.dump(self, f)

if __name__ == "__main__":
    # ansi = AngrySiri()
    # print(ansi.init_talk())
    # print('[メッセージ] [加算スコア]\nという形式で入力してね', flush=True)
    # while True:
    #     mes, score = input().split(' ')
    #     print(ansi.talk(mes, int(score)))

    os.chdir('..')
    masi = MultiAngrySiri(['Taro', 'Unko'], load_pickle=True)
    masi.save()
    masi2 = MultiAngrySiri()
    masi2.talk('Unko', 'カス', happy_cnt=30, angry_cnt=0)
    masi2.talk('Taro', 'カス', happy_cnt=0, angry_cnt=30)
    print(masi2['Unko'].score, masi2['Taro'].score)
    print(masi2.get_mode('Unko'), masi2.get_mode('Taro'))
