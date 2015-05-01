import textwrap
#from library import *



def format_text(self, incoming):
	ready_to_print = textwrap.dedent(incoming).strip()
	for width in [80]:
		print textwrap.fill(ready_to_print, initial_indent='     ', subsequent_indent='', width=width)
    

#incoming = (", ".join(string))
#string = Memory_Nymphs_Scenes[1]
#print string
#go = format_text('stuff', string)   