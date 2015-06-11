###Merchant functionality

from bag import bag_contents, bag_items
from format_incoming import format_text
from maps import bag_map
from scenes import encounter, Merchant_Scenes

Merchant_Inp = {'yes': 1, 'coin': 1, 'buy': 1, 'thanks': 2, 'goodbye': 2, 'sell': 0, 'done': 3}
   
def merchant_func(self):
    #Print intro, take input, parse input, take input until goodbye key triggered.
    val = 0
    key = 0
    scenes = encounter[15]
    print format_text('self', Merchant_Scenes[0][0])
    
    while key != 2:
        u_i = raw_input("> ")
        for keys in Merchant_Inp:
            if keys in u_i:
                key = Merchant_Inp[keys]
                if key == 0:
                    print sell('self')
                    key = 2
                elif key != 0:
                    print format_text('self', Merchant_Scenes[0][key])  
            elif u_i not in keys:
                val += 1
                if val == len(Merchant_Inp):
                    print "    I don't understand what you're looking for."
                else:
                    continue    
    else:
        return "    Goodbye" 
        
def sell(self):
    #Check whether or not input matches item dictionary. Count qt of item possessed, get item value.
    #Add gold to bag, delete item stock.
    val = 0
    print "    Do you have something to sell? What is it?"

    u_i = raw_input("> ")

    if "no" in u_i or "done" in u_i:
            return "    Nothing? Alright." 

    for i in bag_items:
        if i in u_i:
            sec = bag_map[i][0]
            if i in bag_contents[sec]:
                qt = bag_contents[sec].count(i)
                vl = bag_map[i][1]
                bag_contents[3][1] = (bag_contents[3][1]) + (vl * qt)
                while i in bag_contents[sec]:
                    bag_contents[sec].remove(i)
                else:
                    return "    Thank you for the %s. Here is %r gold for your troubles." % (i, (vl * qt))
            else:
                print "    It looks like you don't have that item."
                sell('self') 
        elif i not in u_i:
            val += 1
            if val != len(bag_items):
                continue
            elif val == len(bag_items):
                return "    I am not interested in purchasing that item." 
