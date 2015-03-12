

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
The_Sorrow = [[-5, """A stillness swept inside of you as if all the world had frozen
	     into a dim shadow. You became overly aware of your arms moving awkwardly
	     to keep you afloat. What an awkward and unnatural thing your life was. If
	     you were to stop moving your arms, if you were to allow the peace of nature
	     to silence you back into nonexistence then the shame and pain of your
	     orchestrations would cease. You could create no new pain. If you became
	     part of these cool golden depths."""],
	     [-7, """"""], 
	     [-9, """"""]
	     ]
	  
Twiggins = [
           ["""A distinctive and offputting sound brought your eyes to a creature best
	   described as a thumb-sized twig come-alive. Four wings, flat to the sky, 
	   offset from each other; top at the right, second lower-left, third lower-right, 
	   lowest-left, sliced at the air fast enough to leave only the strong bones on
	   the back, which twitched with each wing beat, as a clue to the creatures odd
	   aerial architecture. The Twiggins' legs dangled below it, each foot comprised
	   of a single webbed V. It held itself close to the wide mouth of the trumpet
	   flower at which it feasted with three-fingered hands much more alike in appearance
	   to the pincers of a scorpian or beatle; both hard, with barbed tangs; than
	   to the fleshy digits of humans.
	   """,
	   """It's head snaps toward you and you see how ugly its face is. Like a walnut
	   shell with a slash in it, but it's eyes are disarmingly . . . human. "Vvrumb"
	   It says. You quickly calculate that Vvrumb is Twiggin for yum. It flies at you,
	   pincers forward, hungry mouth leaking a gummy purple liquid.""",
	   """Single after"""], 
	   ["""Cluster Intro""", """Cluster before""", """Cluster after"""], 
	   ["""Swarm Intro""", """Swarm before""", """Swarm after"""]
	   ]	  

##########################################Friends##########################################

Blacksmith = [
             ["""Intro dialogue containing clue about polearm"""],
             ["""Blacksmith gives hero polearm"""],
             ["""Blacksmith tell hero how to use it, page is added to book."""]
             ]

Herbalist = [
            ["""intro herb shop with minor healing and protective elixers"""],
            ["""Shop inventory"""],
            ["""tells how to use items"""]
            ]
Glasssmith = [
             ["""Tests hero's mettle. """],
             ["""Tells true history of humans and dragons. Add page to book
	      Dragons did not ask for the terrible task of gaurding the souls.
	      They knew that ungaurded those souls and the riches the created
	      both in crude gold and in their combined ability to separate and
	      protect a realm from the rest of existence would soon attract dark
	      forces. Greed and the lust for realms to press beneath ones thumb
	      would draw the simple minded and many a creature of tyrannical 
	      nature, even some of their own. It was the weakest, the alliance
	      of gold dragons who brought the need to the Green dragons, who in
	      the 7th century of the current age ruled proudly. It is undoubtedly
	      because of this pride that they called for immediate relocation, they
	      themselves moved from the caverns of the forest, to the cold and
	      unwelcoming territory now called Dragonlands. When, in the next 
	      century, the alliance of The Red rose to overwhelm the the alliance
	      of The Green; in the bloody and savage manner that Dragons have;
	      they took the protectors mantle as their own. This ensured that 
	      no human would oppose the new powers and that they longstanding peace
	      between would remain, as their own interests were still kept. It
	      allowed The Green, having more pride than sense, to succede before
	      their numbers had dwindled to the post coup numbers of the fallen 
	      of the old age. Peace among their own was of great interest to The
	      Red, they did afterall seek to rule all. And more was a much more
	      attractive all than less.
	          The White are ever the workers of the shards. 
	      """],
             ["""3"""]
             ]
Healer = [
         ["""1"""],
         ["""2"""],
         ["""3"""]
         ]
#Peacekeeper Dragon
White_Dragon = [
               ["""1"""],
               ["""2"""],
               ["""3"""]
               ]
##########################################Hitpoints##########################################

Hero = [65]
Dragon = [70]
Fairy = [30]
Histears = [65] 

for group in Dragons:
    for subgroup in group[0:1]:
        print subgroup
