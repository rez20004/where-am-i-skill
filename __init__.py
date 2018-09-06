from mycroft import MycroftSkill, intent_file_handler


class WhereAmI(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('i.am.where.intent')
    def handle_i_am_where(self, message):
        self.speak_dialog('i.am.where')


def create_skill():
    return WhereAmI()

