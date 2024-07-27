"""
from forms.master_design import main_window

app = main_window()
app.mainloop()
"""

import tkinter as tk
from forms.views import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()