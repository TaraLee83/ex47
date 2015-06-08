###Merchant functionality
from sys import exit
from bag import *
from format_incoming import format_text
from scenes import encounter, Merchant_Scenes

Merchant_Inp = {'yes': 1, 'coin': 1, 'buy': 1, 'thanks': 2, 'goodbye': 2, 'sell': 0}

def merchant_main(self):
    #Print intro, take input, parse input, take input until goodbye key triggered.
    key = 0
    val = 0
    times_through = 0
    scenes = encounter[15]
    print format_text('self', Merchant_Scenes[0][0])

    user_input = raw_input("> ")
    
    while key != 2:
        for keys in Merchant_Inp:
            if user_input in keys and times_through == 0:
                key = Merchant_Inp[user_input]
                times_through = 1
                val += 1
                print format_text('self', Merchant_Scenes[0][0])
                print format_text('self', Merchant_Scenes[0][key])
            elif user_input in keys and times_through != 0:
                key = Merchant_Inp[user_input]
                print format_text('self', Merchant_Scenes[0][key])    
            elif user_input not in keys and val == len(Merchant_Inp):
                print "    I don't understand what you're looking for."
    else:
        print format_text('self', Merchant_Scenes[0][2])

   
def merchant_main_1(self):
    #Print intro, take input, parse input, take input until goodbye key triggered.
    val = 0
    key = 0
    scenes = encounter[15]
    print format_text('self', Merchant_Scenes[0][0])
    
    while key != 2:
        user_input = raw_input("> ")
        for keys in Merchant_Inp:
            if user_input in keys:
                print 1
                key = Merchant_Inp[user_input]

                if key == 0:
                    print 2
                    sell('self')
                elif key != 0:
                    print 3
                    print format_text('self', Merchant_Scenes[0][key])  

            elif user_input not in keys:
                val += 1
                if val == len(Merchant_Inp):
                    print "    I don't understand what you're looking for."
                else:
                    continue    
    else:
        print format_text('self', Merchant_Scenes[0][2])
        exit(1)                


def sell(self):
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
        return "It looks like you don't have any of that to sell."
 
    bag_contents[2] = [i for i in bag_contents[2] if i != item]
    bag_contents[4] = [i for i in bag_contents[4] if i != item]
    bag_contents[3][1] = bag_contents[3][1] + (val * qt)
    return "Here is %r gold for your %s." % ((val * qt), item)

go = merchant_main_1('self')    
