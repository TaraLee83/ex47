###Merchant functionality
qt = 0

def merchant(self):
    print "Oh, you have brought me something. Wonderful! And what do you have to sell?"
    user_input = raw_input("> ")
    if "bluebells" in user_input:
    	item = "bluebells"
    	val = 5
    	for m in bag_contents[2]:
    		if m == item:
    			qt += 1
    elif "cactus flower" in user_input:
    	item = "cactus flower"
    	val = 5
    	for m in bag_contents[2]:
    		if m == item:
    			qt += 1
    elif "honeysuckle" in user_input:
        item = "honeysuckle"
        val = 5
        for m in bag_contents[2]:
            if m == item:
                qt += 1		
    elif "obsidian" in user_input:
    	item = "obsidian"
    	val = 20
    	for n_t in bag_contents[4]:
    		if n_t == item:
    			qt += 1
    elif "shells" in user_input:
    	item = "shells"
    	val = 20
    	for n_t in bag_contents[4]:
    		if n_t == item:
    			qt += 1
    elif "spewer toxin" in user_input:
    	item = "spewer toxin"
    	val = 20
    	for n_t in bag_contents[4]:
    		if n_t == item:
    			qt += 1
      