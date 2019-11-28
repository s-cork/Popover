from anvil import *
# This is a module.
# You can define variables and functions here, and use them from any form. For example:
#
#    import Module1
#
#    Module1.say_hello()
#
print('running')

def popover(self, content, 
            title='', 
            placement = 'right',
            trigger = 'manual',
            animation=True, 
            delay={ "show": 100, "hide": 100 }
           ):
  """self - the element you wish to have the popover
  content - either text or an anvil component or Form
  placement -  right, left, top, bottom
  trigger - manual, focus, hover, click
  animation - boolean
  delay - {'show': 100, 'hide': 100}
  """
  if isinstance(content, str):
    html = False
  else:
    html = True
    content.popper = self

  js.call_js('popover', self, content, title, placement, trigger, animation, delay, html)

def pop(self,behaviour):
  js.call_js('pop', self, behaviour)
  
Button.popover = popover
Link.popover = popover
Button.pop = pop
Link.pop = pop


