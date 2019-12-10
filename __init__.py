from mycroft import MycroftSkill, intent_file_handler


class HolaAm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('am.hola.intent')
    def handle_am_hola(self, message):
        self.speak_dialog('am.hola')


def create_skill():
    return HolaAm()

