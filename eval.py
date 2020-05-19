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
            if self.isNum(word):
                equation += word
            
            if word in ['+', '-', '/', '*', '**', '(', ')']:
                equation += word
            
            if word in ['x', 'multiplied', 'times']:
                equation += '*'
            
            if word == 'divided':
                equation += '/'
            
            if word in ['subtracted', 'minus']:
                equation += '-'
            
            if word == 'plus':
                equation += '+'
            
            if word == 'power':
                equation += '**'   
        return equation

    def solve(self, userEquation, interpret=True):
        if interpret:
            userEquation = self.interpret(userEquation)
        return eval(userEquation)
