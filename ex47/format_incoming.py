import textwrap
from library import *


incoming = Desert_Scholar_Scenes[3]


def format_text(self, incoming):
	string = (", ".join(incoming))
	ready_to_print = textwrap.dedent(string).strip()
	for width in [80]:
		print
    	print textwrap.fill(ready_to_print, initial_indent='     ', subsequent_indent='', width=width)
    

go = format_text('stuff', incoming)
	   