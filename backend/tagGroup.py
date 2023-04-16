import enum


class TagGroup(enum.Enum):
    disease = "disease"
    welcome = "welcome"
    question = "question"
    goodbye = "goodbye"
    thanks = "thanks"
    noanswer = "noanswer"
    name = "name"
    mood = "mood"
    specify = "specify"
    few_questions = "few_questions"
    end_diagnosis = "end_diagnosis"

    @staticmethod
    def fetch_names():
        return [c.value for c in TagGroup]
