###Merchant functionality
from bag import *


if __name__ == "__Merchant__":

    def merchant(self):
        global bag_contents
        print "Oh, you have brought me something. Wonderful! And what do you have to sell?"

        user_input = raw_input("> ")

        if "bluebells" in user_input and "bluebells" in bag_contents[2]:
            item = "bluebells"
            val = 5
            qt = bag_contents[2].count("bluebells")
        elif "cactus flower" in user_input and "cactus flower" in bag_contents[2]:
            item = "cactus flower"
            val = 5
            qt = bag_contents[2].count("cactus flower")    
        elif "honeysuckle" in user_input and "honeysuckle" in bag_contents[2]:
            item = "honeysuckle"
            val = 5
            qt = bag_contents[2].count("honeysuckle")     
        elif "obsidian" in user_input and "obsidian" in bag_contents[4]:
            item = "obsidian"
            val = 20
            qt = bag_contents[4].count("obsidian")
        elif "shells" in user_input and "shells" in bag_contents[4]:
            item = "shells"
            val = 20
            qt = bag_contents[4].count("shells")
        elif "spewer toxin" in user_input and "spewer toxin" in bag_contents[4]:
            item = "spewer toxin"
            val = 20
            qt = bag_contents[4].count("spewer toxin")
        else:
            print "It looks like you don't have any of that to sell."
 
        bag_contents[2] = [i for i in bag_contents[2] if i != item]
        bag_contents[4] = [i for i in bag_contents[4] if i != item]
        bag_contents[3][1] = bag_contents[3][1] + (val * qt)
        print "Here is %r gold for your %s." % ((val * qt), item)
