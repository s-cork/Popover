from anvil import *

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.popper.foreground = 'red'

  def link_1_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.popper.visible = False

  def link_1_copy_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.popper.text = 'help'



