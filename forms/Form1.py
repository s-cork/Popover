from anvil import *
from .Form2 import Form2

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.form2 = Form2()
#     self.content_panel.add_component(self.form2)

    # Any code you write here will run when the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
#     js.call_js('popOver',self.primary_color_1)
    js.call_js('popOver',self.primary_color_1, self.form2)
    self.form2.popper = self.primary_color_1
    print(self.primary_color_1)



