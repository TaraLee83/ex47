###help function (as I am behind on my desired time for completing this project, the help functionality is what I can make off the top of my head)
from format_incoming import format_text
buy = "You can make purchases in the town of Garzhed, close to the landing rock."
fight = "You can only strike characters who are attempting violence against you. To use a weapon: type that weapons attack. For example: if you have found the dagger, type \"stab\"."
move = "To move, type the direction you wish to go. For example: west. If the way is blocked try another direction."
sell = "To sell an item you must find the merchant, who is always in the same location."
win = "To win the game you must figure out how to free your daughters soul from the shard."
help_d = {"move": move, "sell": sell, "buy": buy, "purchase": buy, "fight": fight, "win": win}

def help(self):
    print "    Tell me what you need help with. When you are done, type \"done\"."
    val = 0
    u_i = 0

    while u_i != "done":
    	u_i = raw_input("> ")
    	for key in help_d:
    	    if key in u_i:
    	    	print format_text('self', help_d[key])
    	    elif key not in u_i:
    	    	val += 1
    	        if val != len(help_d):
    	        	continue
    	        elif val == len(help_d):
    	        	print "    Please try to explain your problem again."
    else:
    	print "    I hope we've solved your issue."
    
go = help('self')