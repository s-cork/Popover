from anvil import *
from .Form2 import Form2
from .popover import *

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.form2 = Form2()
    
    print(self.primary_color_1)
    
    self.primary_color_1.popover(self.form2)
#     self.content_panel.add_component(self.form2)

    # Any code you write here will run when the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
#     js.call_js('popOver',self.primary_color_1)
#     print(event_args['sender'])
    self.form2.popper = self.primary_color_1
#     print(self.primary_color_1)
    

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.primary_color_1.text = 'done'

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
#     js.call_js('popOver',self.primary_color_1, self.form2)
#     js.call_js('popOver',self.link_1, self.form2)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.form2.popper = self.link_1






