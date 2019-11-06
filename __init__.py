from mycroft import MycroftSkill, intent_file_handler


class TestDep(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dep.test.intent')
    def handle_dep_test(self, message):
        self.speak_dialog('dep.test')


def create_skill():
    return TestDep()

