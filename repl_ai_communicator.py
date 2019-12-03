import requests
import json

REGISTERATION_URL = 'https://api.repl-ai.jp/v1/registration'
DIALOGUE_URL      = 'https://api.repl-ai.jp/v1/dialogue'


class ReplAICommunicater:
    '''
    ReplAI (https://repl-ai.jp) とやりとりをするためのクラス

    # args # 
        api_key : Repl-AIのAPIキー    (開発者についてunique)
        bot_id :    //   のボットID   (ボットについてunique)
        topic_id:   //   のシナリオID (シナリオについてunique)
    '''
    
    def __init__(self, api_key, bot_id, topic_id):
        self.api_key = api_key
        self.bot_id  = bot_id

        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': self.api_key
        }
        register_data = { "botId": self.bot_id }

        register_resp = requests.post(REGISTERATION_URL, headers=self.headers, data=json.dumps(register_data))
        self.app_user_id = json.loads(register_resp.text)['appUserId']
        
        # __init__はreturnできないので、最初のmessageはiniit_textに苦し紛れに代入してる
        self.init_text = self.change_topic(topic_id)


    def change_topic(self, topic_id):
        '''
        topic_idを変更して、initのメッセージを送る
        '''
        self.topic_id = topic_id
        return self.__post_dialogue()


    def talk(self, message):
        return self.__post_dialogue(message)


### private ###

    def __post_dialogue(self, message=None):
        '''
        message = None の場合、initとして送信する
        '''
        data = {
            "appUserId": self.app_user_id,
            "botId": self.bot_id,
            "voiceText": message,
            "initTalkingFlag": True,
            "initTopicId": self.topic_id
        }
        data['initTalkingFlag'] = (message == None)

        if data['initTalkingFlag']:
            data['voiceText']   = 'init'
            data['initTopicId'] = self.topic_id

        resp = requests.post(DIALOGUE_URL, headers=self.headers, data=json.dumps(data))

        return json.loads(resp.text)['systemText']['expression']
        

        

if __name__ == "__main__":
    dial = ReplAICommunicater('ZUQZEcApTGtAZySTmTYw2PmMEFDG143eNW5v5ovv', "b4wto1xmcc9w0fr", "s4wto2460oo80ny")
    while True:
        dial.talk(input())