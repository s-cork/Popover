from anvil import *

class Form2(Form2Template):
  def __init__(self,popper=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    
#     print('popper',self.popper)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.text = 'Woop'
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.popper:
      self.popper.parent.background = 'blue'
      print('popper',self.popper)
      print('same?', self.button == self.popper)
      print('parent',self.popper.parent)
      self.popper.text = 'hell yeah'
      self.popper.foreground = 'red'
#       self.button.text = 'hey'

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    self.popper = None



