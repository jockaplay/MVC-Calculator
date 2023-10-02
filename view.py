import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    
    
    PAD = 10
    MAX_BUTTONS_PER_ROW = 4
    button_captions = ['C', '+/-', '%', '/',
                       7, 8, 9, '*',
                       4, 5, 6, '-',
                       1, 2, 3, '+',
                       0, '.', '=', '¬']
    
    
    def __init__(self, controller):
        super().__init__()
        
        self.title('PyCulator 0.1')
        self.controller = controller
        self.value_var = tk.StringVar() #Like useState from React
        
        self._make_main_frame()
        self._make_entry()
        self._make_buttons()
        self._make_window()
    
    def main(self):
        self.mainloop()
        
    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
        
    def _make_entry(self):
        ent = ttk.Entry(self.main_frm, textvariable=self.value_var, justify='right', state='disabled', foreground='#212121')
        ent.pack(fill='x', ipady=self.PAD, pady=(0, self.PAD))
    
    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()
        
        frm = ttk.Frame(outer_frm)
        frm.pack()
        
        buttons_in_row = 0
        
        for caption in self.button_captions:
            
            if buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                frm = ttk.Frame(outer_frm)
                frm.pack(fill='x')
                buttons_in_row = 0
                
            btn = ttk.Button(frm, text=caption, command=(
                    lambda button=caption: self.controller.on_button_click(button)
                ))
            btn.pack(side='left', ipady=self.PAD) if caption != 0 else btn.pack(side='left', fill='x', expand=True, ipady=self.PAD)
            
            buttons_in_row += 1

    def _make_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = ((self.winfo_screenwidth() - width) // 2)
        y_offset = ((self.winfo_screenheight() - height) // 2)
        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')