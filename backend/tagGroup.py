import enum


class TagGroup(enum.Enum):
    DISEASE = "disease"
    WELCOME = "welcome"
    QUESTION = "question"
    GOODBYE = "goodbye"
    THANKS = "thanks"
    NOANSWER = "noanswer"
    NAME = "name"
    MOOD = "mood"
    SPECIFY = "specify"
    FEW_QUESTIONS = "few_questions"

    @staticmethod
    def fetch_names():
        return [c.value for c in TagGroup]
