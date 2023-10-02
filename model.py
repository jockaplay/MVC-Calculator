class Model():
    def __init__(self):
        self.previus_value = ''
        self.value = ''
        self.operator = ''
    
    def calculate(self, caption):
        match caption:
            case 'C':
                self.previus_value = ''
                self.value = ''
                self.operator = ''
            case '+/-':
                try:
                    self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
                except:
                    self.value = ''
            case '.':
                if not caption in self.value:
                    if self.value:
                        self.value += caption
                    else:
                        self.value += '0' + caption
            case '=':
                try:
                    self.value = str(self._evaluete())
                except:
                    self.value = ''
            case '%':
                try:
                    if self.operator:
                        self.percent(self.operator)
                        self.previus_value = ''
                        self.operator = ''
                    else:
                        self.previus_value = str(int(self.value) / 100)
                        self.operator = '*'
                        self.value = ''
                except:
                    self.value = ''
            case '¬':
                self.value = self.value[:-1]
            case _:
                if isinstance(caption, int):
                    self.value += str(caption)
                else:
                    if self.value:
                        self.operator = caption
                        self.previus_value = self.value
                        self.value = ''
                
        return self.value
    
    def _evaluete(self):
        return eval(self.previus_value + self.operator + self.value)

    def percent(self, caption):
        value = float(self.value) if '.' in self.value else int(self.value)
        porcentagem = (float(self.previus_value) * value) / 100
        temp = float(self.previus_value)
        if caption == '+':
            temp += float(porcentagem)
        elif caption == '-':
            temp -= float(porcentagem)
        elif caption == '*':
            temp = float(float(self.previus_value) * (value / 100))
        elif caption == '/':
            temp = float(float(self.previus_value) / (value / 100))
        self.value = str(temp)