from anvil import *
"""for more information visit the w3 bootstrap popover page
https://www.w3schools.com/bootstrap4/bootstrap_ref_js_popover.asp

or the bootstrap popover page
https://getbootstrap.com/docs/4.0/components/popovers/
"""

def popover(self, content, 
            title='', 
            placement = 'right',
            trigger = 'click',
            animation=True, 
            delay={ "show": 100, "hide": 100 }
           ):
  """self - the element you wish to have the popover
  content - either text or an anvil component or Form
  placement -  right, left, top, bottom
  trigger - manual, focus, hover, click
  animation - True or False
  delay - {'show': 100, 'hide': 100}
  """
  if isinstance(content, str):
    html = False
  else:
    html = True
    content.popper = self

  js.call_js('popover', self, content, title, placement, trigger, animation, delay, html)

def pop(self,behaviour):
  """behavior can either be any of
  show, hide, toggle, dispose, enable, disable, toggleEnabled, update"""
  js.call_js('pop', self, behaviour)
  
Button.popover = popover
Link.popover = popover
Button.pop = pop
Link.pop = pop


