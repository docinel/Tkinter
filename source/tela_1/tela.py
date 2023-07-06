from typing import Optional, Tuple, Union
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

       

app = App(ctk.CTk)
app.title("teste")
app.mainloop()        