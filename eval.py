class Evaluator:
    def __init__(self):
        pass
    def isNum(self, suspectedInteger):
        try:
            float(suspectedInteger)
            return True
        except:
            return False

    def interpret(self, userString):
        userString = userString.split()
        equation = ''
        for word in userString:
            if isNum(word):
                equation += word
            if word in ['+', '-', '/', '*']:
                equation += word
            if word == '*':
                equation += '*'

        return equation
