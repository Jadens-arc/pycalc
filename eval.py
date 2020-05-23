class Evaluator:
    def __init__(self):
        pass

    def isNum(self, suspectedInteger):
        '''Takes string; returns boolean; if string can be interpeted as integer''' 
        try:
            float(suspectedInteger)
            return True
        except:
            return False

    def interpret(self, userString):
        '''Takes string; returns mathmatical equation'''
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
        '''Takes string; returns double; interprets user string and solves it returns value'''
        if interpret:
            userEquation = self.interpret(userEquation)
        return eval(userEquation)
