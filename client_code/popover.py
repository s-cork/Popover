from anvil import Button, Link, js, Label
"""for more information visit the w3 bootstrap popover page
https://www.w3schools.com/bootstrap4/bootstrap_ref_js_popover.asp

or the bootstrap popover page for v 3.3.7
https://bootstrapdocs.com/v3.3.6/docs/javascript/#popovers
"""

def popover(self, content, 
            title='', 
            placement = 'right',
            trigger = 'click',
            animation=True, 
            delay={ "show": 100, "hide": 100 }
           ):
  """should be called by a button or link
  content - either text or an anvil component or Form
  placement -  right, left, top, bottom (for left/right best to have links and buttons inside flow panels)
  trigger - manual, focus, hover, click (can be a combination of two e.g. 'hover focus')
  animation - True or False
  delay - {'show': 100, 'hide': 100}
  
  if the content is a form then the form will have an attribute self.popper added
  """
  if isinstance(content, str):
    html = False
  else:
    html = True
    # add the popper to the content form
    content.popper = self

  js.call_js('popover', self, content, title, placement, trigger, animation, delay, html)

def pop(self,behaviour):
  """behaviour can be any of
  show, hide, toggle, destroy (included with bootstrap 3.3.7)
  features added not in bootstrap 3.3.7 docs:
  update  - updates position of popover - useful for dynamic content that changes the size of the popover
  is_visible: returns True or False if the popover is visible - note a popover will only be visible after it has animated onto screen so may need to sleep(.15) before calling """
  return js.call_js('pop', self, behaviour)
  
Button.popover = popover
Link.popover = popover
Button.pop = pop
Link.pop = pop
Label.popover = popover
Label.pop = pop

