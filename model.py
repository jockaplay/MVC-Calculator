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
                self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
            case '.':
                if not caption in self.value:
                    self.value += caption
            case '=':
                self.value = str(self._evaluete())
            case '%':
                pass
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