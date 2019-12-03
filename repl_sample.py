from repl_ai_communicator import ReplAICommunicater

API_KEY  = 'ZUQZEcApTGtAZySTmTYw2PmMEFDG143eNW5v5ovv'
BOT_ID   = 'b4wto1xmcc9w0fr'
TOPIC_ID = 's4wto2460oo80ny'


if __name__ == "__main__":
    dial = ReplAICommunicater(API_KEY, BOT_ID, TOPIC_ID)
    while True:
        dial.talk(input())