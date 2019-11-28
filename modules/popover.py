from anvil import *
# This is a module.
# You can define variables and functions here, and use them from any form. For example:
#
#    import Module1
#
#    Module1.say_hello()
#




def popover(self, content, title='', 
            placement = 'right',
            container=False, 
            animation=True, 
            delay={ "show": 100, "hide": 100 },
            trigger = 'focus',
            offset = 0
           ):
  js.call_js('popOver', self, content, title, placement, container, animation, delay, trigger, offset )
  
  
Button.popover = popover
Link.popover = popover