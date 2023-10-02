from model import Model
from view import View


class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model()
    
    def main(self):
        self.view.main()
    
    def on_button_click(self, caption):
        self.view.value_var.set(self.model.calculate(caption))
        

if __name__ == "__main__":
    controler = Controller()
    controler.main()