

Dragon1 = {5: "You drink a minor potion of 'protect against Dragon.'"}
Dragon2 = {15: "You don the fireopal encased in glass."}
##########################################Bag##########################################

Bag = []

##########################################Charms##########################################

Charms = {'Dragonlands': 1, 'Fairy': 2}

##########################################Collectibles##########################################

Book = []

##########################################Foes##########################################

Dragons = [
          #Red Dragon
          [["""The rumbling began beneath your feet. Your eyes traced tremors to the
	  base of the mountain where lesser rocks tumbled down to the river bed. 
	  Your eyes climbed the mountain, the world quaked harder. Trees shook loose 
	  their branches. Just as the relief of the still and faithful sky came into 
	  filled your vision, smoke poured from the mouth of the volcano and a great red
	  flash darted forth. There was no way from the valley fast enough to save
	  your life. But wait, that is not death come to sunder and encase you by a
	  dead and unthinking catastrophe of nature, it was the other death. Winged,
	  with terrible fangs and claws and an enormous, barbed tale that this most 
	  feirsome of all the Dragons snapped with elegant and evil precision to bring
	  death in an instant. The Red Dragon has awakened.
	  """], 
	  [-20, "Red claw attack before.", "Red claw attack after."], 
	  [-20, "Red tail_swipe before.", "Red tail_swipe after."], 
	  [-40, "Red fire_breath before.", "Red fire_breath after."], 
	  [-50, "Red finisher before.", "Red finisher after."]],
          #Green Dragon 
          [["""The spruce trees blanket the lowest part of the Eastern snow-capped
      	  mountain range, their frequency becomes spotted closer to histears
      	  river. The trees that dot the shoreline are thick and burled, the
      	  waterfront side stripped of all branches and leaves and enough bark
      	  to make the snaking river appear to have stripes of white and green
      	  flanking. It is a disruption in this bone white and deep green striping
      	  that first catches your eye. Soon after, grey smoke effluent of nostrils
      	  and bone white just like the trees, eyes, amber afire, seeming to burn
      	  from within and the bleached-bone teeth that shaped her mouth into 
      	  a wicked grin, you see now that Dragons can smile. Perhaps this will be
      	  the last thing you ever learn.
      	  """], 
	  [-16, "Green claw attack before.", "Green claw attack after."], 
	  [-16, "Green tail_swipe before.", "Green tail_swipe after."],
          [-32, "Green fire_breath before.", "Green fire_breath after."], 
          [-40, "Green finisher before.", "Green finisher after."]],
	  #Gold Dragon
	  [["""What could have been the sun itself, lain upon the mountainside, shifted. 
	  Diamond-like eyes opened in its' head, that larger than the mouth of the 
	  river.
	  """], 
	  [-14, "Gold tail_swipe before.", "Gold tail_swipe after."],
          [-28, "Gold fire_breath before.", "Gold fire_breath after."],
          [-35, "Gold finisher before.", "Gold finisher after."]]
	  ]
	  
Fairies = []	  
	  
##########################################Hitpoints##########################################

Hero = [65]
Dragon = [70]
Fairy = [30]
Histears = [65] 

for group in Dragons:
    for subgroup in group[0:1]:
        print subgroup
