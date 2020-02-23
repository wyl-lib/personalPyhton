import werobot

robot = werobot.WeRoBot(token='tokenhere')
@robot.handler
def hello(message):
    return 'hello world!!'
