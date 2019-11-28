from anvil import *

class Form2(Form2Template):
  def __init__(self,popper=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.role = 'findme'
    self.popper = popper

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.text = 'Woop'
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.popper:
      print(self.popper)
      self.popper.text = 'hell yeah'


