import re

class Calculadora():
    @staticmethod
    def operando(expresion):
        expresion = expresion.replace("^", "**") 
        if not re.match(r'^[\d+\-*/%().\s^]+$', expresion):
            return "No válida"
        
        try:
            resultado = Calculadora.evaluar(expresion)
            return f" = {resultado}"
        except Exception as error:
            return f" Error: {error}"

    @staticmethod
    def evaluar(expresion):
        return eval(compile(expresion, "<string>", "eval"), {"__builtins__": None}, {})

