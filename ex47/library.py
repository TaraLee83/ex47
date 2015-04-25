##########################################Actions##########################################
Actions = [["gather"],[1, "twiggins bane"], [5, "gold"], [7, "twiggins bane"], 
          [13, "twiggins bane"], [28, "a stone"]]

Dragon1 = {5: "You drink a minor potion of 'protect against Dragon.'"}
Dragon2 = {15: "You don the fireopal encased in glass."}
##########################################Bag##########################################

Bag = []

##########################################Charms##########################################

Charms = [["Dragons"], ["polearm"], ['Fairy', 2]]

##########################################Collectibles##########################################
###Pages, Intro to world, notes about things learned, ?map?
Book = []

##########################################Foes##########################################

Dragons_Scenes = [
      #Red Dragon
      [["red_dragon"],
      ["The rumbling began beneath your feet. Your eyes traced tremors to the " 
"base of the mountain where lesser rocks tumbled down to the river bed. "
"Your eyes climbed the mountain, the world quaked harder. Trees shook loose " 
"their branches. Just as the relief of the still and faithful sky came into " 
"filled your vision, smoke poured from the mouth of the volcano and a great red "
"flash darted forth. There was no way from the valley fast enough to save "
"your life. But wait, that is not death come to sunder and encase you by a "
"dead and unthinking catastrophe of nature, it was the other death. Winged, "
"with terrible fangs and claws and an enormous, barbed tale that this most "
"fiersome of all the Dragons snapped with elegant and evil precision to bring "
"death in an instant. The Red Dragon has awakened. "
      ], 
	  [-20, "The red beast was upon you in a flash. Its' claws bit into your skin. It "
"slashed high and low."
	  ], 
	  [-20, "The Red giant reared, for a moment only its thick haunches and scaled belly "
"were visible. Then it lurched, shoulders first then haunches. Suddenly the length of its "
"tail was rushing toward you. It knocked the air out of you and broke at least one rib."
      ], 
	  [-40, "The Red Dragon looked away from you. It pointed its muzzle at the sky and took "
"in a great breath. You leap for cover behind a rock as a sea of flames pour over you and the "
"rock. Your clothes are on fire. You drop to the ground and roll and beat the flames out of "
"your garments."
      ], 
	  [-50, "The Dragon leaped and beat its wings until it was well above the horizon. Its "
"circling seemed to stir the clouds. When it came around to the point in its' path farthest "
"from you it dipped its head directly at you and took great gusts of wind under its wings as "
"it rushed, flames escaping its maw, wide open in a fanged scream. It scooped you up in its "
"mouth. One tooth punched through your gut so that you were skewered there. When you reached "
"a great enough altitude to see the sun at the horizon one last time, the red dragon began to "
"shake its head side to side. Life left you mercifully fast."
      ]],
      #Green Dragon 
      [["green_dragon"],
      ["The spruce trees blanket the lowest part of the Eastern snow-capped "
"mountain range, their frequency becomes spotted closer to histears "
"river. The trees that dot the shoreline are thick and burled, the "
"waterfront side stripped of all branches and leaves and enough bark "
"to make the snaking river appear to have stripes of white and green "
"flanking. It is a disruption in this bone white and deep green striping "
"that first catches your eye. Soon after, grey smoke effluent of nostrils "
"and bone white just like the trees, eyes, amber afire, seeming to burn "
"from within and the bleached-bone teeth that shaped her mouth into "
"a wicked grin, you see now that Dragons can smile. Perhaps this will be "
"the last thing you ever learn. "
      ], 
	  [-16, "You saw her chest, like green tinted iron armor a moment before"
"her claws tore at you. Less like knives and more like blunt sticks as they"
"tore your skin."	  
      ], 
	  [-16, "She launched off of her powerful legs and spun mid air. Her feet"
"met the ground with a deep thud. You turned to watch helplessly as her tail"
"crashed into you, knocking the wind out of you and bruising you badly."	  
      ],
      [-32, "She backed up quickly, bending trees in her path. Her claws dug"
"at the ground to speed her retreat. When she reached the edge of the circular"
"clearing in which you stood she opened her maw and flames jetted out. They"
"ripped and tore through the air toward you as you threw yourself to the ground"
"and rolled toward her, and toward the narrow neck of the flame-path."
      ], 
      [-40, "The green dragon took flight. One circle around. It rushed toward"
"you and artfully clasped one giant claw over each arm, clamping your arms, useless,"
"to your chest. It pulled you up and up. You wondered why it carried you higher still."
"Then she released you and swooped beneath you, then over you. After two perfect"
"circles around you as you fell a torrent of flames engulfed you. This was no casual"
"shot. She had aimed her arc so that the widest of the flame-path seared your body."
"Her desire for showmanship meant you still breathed as you crashed into the trees" 
"below breaking nearly every bone in your body."    
      ]],
	  #Gold Dragon
	  [["gold_dragon"],
	  ["What could have been the sun itself, lain upon the mountainside, shifted. " 
"Diamond-like eyes opened in its head, this beast was no longer than the tallest tree. "
"As it sprang upward you realized at once that it had spotted you and that its size "
"afforded it great speed."
	  ], 
	  [-14, "A flash, you saw, as though sunlight had hardened before you, then your stomach, "
"chest and arm were slashed by the Dragon's claws."	  
      ],
	  [-14, "The Dragon wove a cyclone into the air before you. Spinning circles madly, stirring "
"soil from the forest floor. It moved closer, still flying in a mad circular dash. It whipped you "	
"with its tail, throwing you forward and before you could regain your footing its tail hit your "
"chest, knocking you down." 
      ],
      [-28, "When it opened its leathery lips, you stirred to see the white teeth and pink tongue "
"the mortal and mundane hidden inside the golden dragon. Yet as the flames fell forward, golden fire "
"from a golden beast, it looked beautiful. You ducked, your back burned. It was hard to believe that "
"such a creature could die just as any human could."          
      ],
      [-35, "As the Golden Dragon stalked around you the realization that you had been edged into "
"the middle of the clearing dawned. You crouched, one knee to the damp forest floor, ready to make a "
"move for the opening in the trees ahead. The Dragon sprang, batting your body into the air with his "
"stomach, then keeping you there by bouncing you off different parts of its body. Its game bruised and "
"broke you. It dropped you."        
      ]
	  ]]  

Memory_Nymphs_Scenes = [["From the mist rising up all around the crashing waterfall a phantasmagoria of "
"pastels, like a dream of the surrounding landscape danced, the shape closest to spheres now and "
"parabolic uni-colored rainbows the next, too bold of perriwinkle, or lemon drop, or lime to have "
"been imagined, yet unnatural. As you thought to look away the movements became more intentional "
"patterns formed, dots and arches pulled together and colors slowed their shifting. Before you "
"materialized a creature. Male perhaps, beautiful. His face never resting in one form, his body "
"obfuscated to appear only as form behind a thick mist veil. He reached a lean arm out toward you "
"the palm lowered to a rock beside the falls small pool. \"Come, sit with me.\" Even his voice "
"melted through range and tone. Every part of him was a tiny part of someone you had known at some "
"point, some you remembered; the corner of your husband's mouth, your friends unmistakably bright "
"green eyes, but then it would melt into someone else. So quickly did he change that it took no time "
"at all to arrive, unsettled, at the realization the phantom knew the parts of your life that you "
"did not. Certainly souls from before you had been forced to leave your memories behind in this world "
"but perhaps even moments from a life that you were to young to remember either way. How he could "
"know truly all about you unsettled you. \"You have many questions,\" your mother's smile, oh gods it "
"has been a lifetime, \"I have many answers. I know you very well Karia, daughter of Janya. Won't "
"you sit by me. Let us talk about the past.\""],
                [-5, "del_weapon", "Do you ever look at yourself, naked in the mirror? I can not see "
"the other world. But I imagine that your body, its map of scars, burns, markings that you have "
"forgotten all the meanings of make your own body as a strangers vessel. Does that not bother you "
"to wear this person that you left in the name of love. Do you ever really forget that she is about? "
"You are quite brave to choose to embrace her again so suddenly and by chance meeting. You came into "
"woman-hood in what the old folk now call the age of fires. Torrhin sought to rest the throne from "
"Goethe by alliance with The Gold. But politics bore me. As they did you. The slice on your outer "
"left thigh was given you by your meadow-dwelling friend. All of girlhood spent giggling and scheming "
"flashed before you eyes as you cut her down before you. You couldn't stop yourself from uttering, I'm "
"so sorry, I'm so sorry. One might have thought you'd been struck dumb. She wouldn't be the last of "
"your friends to die, not even by your own hand. You humans are so confused; too many alliances; blood "
"tribes, mates. The scar that runs the length of the opposite arm, that was from the burning time as "
"well, though it was no friend's blade that drew your blood that night. It was one of the eleven who had "
"first raised the call to overthrow the king. All your fury you threw at him. As you slashed you saw "
"the fields, that had fed your friends families, that you had spent your girlhood running in, that time "
"had frozen with your first kiss in, burning, their houses burning, their corpses burning. You forced "
"him into retreat. The hill behind you gave you height and you steered him toward the steady fire of "
"a shed. You brought him near enough to wear him out and then you took his life. That was the first "
"that had felt like victory. A funny thing when killing feels like victory. But you inhaled sweet air "
"and that hatred inside of you felt sated, just for that moment."],
                [-5, "del all strength bonuses", "The green season, that of your eleventh year. "
"You awoke in lands you'd never meant to set foot in. None had by choice. Your sweet mother "
"had tucked you ever so gently into a crevass oer A Meer, but I must remember that you forget your homeland. "
"The cold western waters; A Meer. Her teeth of of rock to slice and her pets the vicious and "
"plentiful eel, with teeth that shone in the sun. They lay beneath you. Above, lay a climb straight "
"to the sky. Your hands to marry only with rock, sharpened by irregular gusts and sea spray. "
"When the sun tore sweet sleep, like a dark blanket from you and left you to "
"discover your situation you took stock. Smart, not to hurry. Time could only dry the spray and dew from those treacherous "
"handholds anyway. You knew our land to be the regurgitation of A vumu. And that that angry "
"mother's stomach had brought forth black glass for the world to sit upon. Layered heavily to "
"sit strong but sharp and brittle where revealed to A Meer's salty fingers. You were quite "
"the billy goat but this was no mountain. A Meer watched you strip your human ornament and bind "
"it thickly over your hands. She watched you carefully ascend, thick boulder by slightest crag. "
"All the time she watched expecting you to join her. She had decided that she quite loved you "
"I beleive she would have made you a creature of forever just to watch you swim under the sun. "
"But up you went. Only drops of blood, that poured from your hands as the rock finally bit through "
"your bandaging, reached her and became hers. When you set foot upon the Meadow you were Woman, "
"more, to your people, you were Frelt. Woman of the world. None to make a fish-wife of you. It is "
"your mother, you of flesh, who decides your path. And you did not remember this? Do you see how "
"valuable memories are. They are more than ruby or sapphire, they are they fire that forged your "
"soul."]
    ]

Scorpian_Scenes = [["The sand shifts slightly, at first it seems a trick of the intense heat "
"then a mass arrises, sand like a shower falls from its form. That being revealed to "
"be the size of an obese house cat. Quickly though, legs like sharp sticks reveal "
"themselves. Last, it lifts its head. Its buldging eyes squint at you a moment before "
"its MOUTH FANGS come up from the sand, sharp and barb-tipped. It's mouth cracks open "
"and a tiny dry tongue flicks quickly side to side, tic, tic, tic. "],
            [-10, "The Scorpian backed away slowly. Then it lunged forward, throwing its tail "
"over its head. Suddenly its stinger jabbed your skin. A noxious feeling came over you. "
"The poison worked fast. You felt sick already."],
            [-10, "Somehow the sharp points of the Scorpians tiny feet didn't sink into "
"sand. It drew itself up to full height and raised its pincers, saliva dripping from "
"its open maw. Its pincers clanged open and shut. Suddenly it scuttled toward you, "
"It sank a pincer into one hip and into the opposite arm. It emitted a gurgeling sound "
"as it shook its head side to side to drive the pincer points deeper into your skin. "]
            ]

Spewer_Scenes = [["A sqwauk pierced the air, an unfortunate looking creature entered your "
"air space. It seemed to be in the midst of a belching fit. Each gassy eruption caused the "
"dirt-brown bird to spit up a toxic looking yellow wad that fell onto whatever happened to "
"be below it. Leaves and earth sizzled under the yellow spit. It looked to be flying in "
"your direction."],
         [-10, "The gurgeling and belching overhead is nerve-wracking. Someone needs to put this "
"animal out of its misery. Two yellow land on you, one burns into your shoulder, the other "
"burns a whole in the top of your shoe."],
         [-5, "The bird is almost quiet as it passes overhead. Then haaagch, it sends a toxic "
"yellow blob down, where it burns a hole in the shoulder of your shirt."]
         ]

The_Sorrow_Scenes = [["As the water soaked your clothing, the great stillness and peace of it seemed "
"to seep into your skin. You felt calm. But as worries left your mind so to did need, anger "
"all of it, every element of the fire within drowned. You wondered if you too were a fire "
"to be put out."],
             [-5, "A stillness swept inside of you as if all the world had frozen into a dim "
"shadow. You became overly aware of your arms moving awkwardly to keep you afloat. What an "
"awkward and unnatural thing your life was. If you were to stop moving your arms, if you were "
"to allow the peace of nature to silence you back into non-existence then the shame and pain "
"of your orchestrations would cease. You could create no new pain; if you became part of these "
"cool golden depths."],
	           [-10, "Perhaps its brightness, the awe inspiring luminosity of the submerged mountain "
"of fresh gold, brought all else into darkness. Perhaps it was a reaction to the mineral makeup "
"of the metal that taste could not be had nor could the bouquet of forest, volcano or the jasmine "
"kissing the Northern shore be detected. Indeed, only sight remained to you and could it be that "
"even your eyes were failing? Could this grey dusk be falling so quickly. Where were the firebugs "
"that had danced over the waters, making its glassy surface glitter? Where were the clouds that "
"parted around A Vumu, married with her sulfuric gasses then traveled out to the East to "
"provide potion to creatures of the dark sea. All the world had ceased its breath. Here, the golden "
"mountain beneath you shone brighter than the sun of any land. Its heat radiated into you skin. You "
"were the only thing of some small warmth in this world that had sputtered out but an eternal fire, "
"a guilded hearth lay beneath to warm you forever. "], 
	           [-20, "The cold reached through your skin and grabbed hold of your bones. The pain didn't "
"cut or even burn like other cold. It was a lullaby. It absorbed all that had been you. Your "
"responsibility for your daughter, the sour aching that had settled into your belly the moment you had "
"seen her laying motionless, the fear that you pretended not to feel with every step; as you ran through "
"this strange land that yet knew you and had an appetite for your blood, the weariness "
"that had grown with every mile trodden and the great misery that had made breathing scarce "
"a possibility and would suffocate you slowly with thoughts of all that you had not yet accomplished. "
"Perhaps the riches of man did contain some innately useful property. Your body was almost completely "
"numb. Wading had become difficult."]
	           ]

Tree_Disease_Scenes = [["The aching began in your feet. As if the bones were straining "
"to burst. No injury could account for the sudden and quickly increasing pain. You "
"looked behind you to see if perhaps you had unwittingly stepped on a trap or into "
"a crevice. There you saw across the path the root of an Eating Tree. You had crushed "
"it underfoot without even noticing. Yellow-green spores still danced in the sunlight "
"behind you. "],
               [-10, "The ache spread like wild-fire; up your legs and into your hips. "
"Fever lit your brow. You'd begun to sweat by the time the aching touched your chest. Each "
"breath wrung a weak cry from you. You could stand no longer. The wet tangle of leaves "
"and mud beneath you made a sickening sucking sound as your back hit the forest floor. "],
               [-15, "A cold sweat came on. You began to shiver. Ahead of you, leaning "
"with her shoulder against a redwood, is Arturia. She is smiling that in that way of hers "
"both condescending and loving. Her arms are folded in front of her. She uses one elbow to "
"push herself away from the tree and she turns her back on you. You ran to her but she was "
"not behind the tree. Your hands trembled. More phantoms appeared around you. Some saw you "
"some didn't. Your husband held your son close. They wept in front of two tiny coffins. The "
"nearer coffin shook as someone pounded the lid from inside, screaming at the top of her "
"lungs. "],
               [20, "Dizzyness overcame you. Fever caused water to drip from your brow "
"as you wretched onto the ground in front of you. Even when your body would give no more "
"tiny bits of blood came forth. Your thirst was great. But you were too weak to sit yourself "
"up let alone leave to find water."]               
               ]


Twiggins_Scenes = [
           ["A distinctive and offputting sound brought your "
"eyes to a creature best described as a thumb-sized twig come-alive. Four wings, "
"flat to the sky, offset from each other; top at the right, second lower-left, third "
"lower-right, lowest-left, sliced at the air fast enough to leave only the strong "
"bones on the back, which twitched with each wing beat, as a clue to the creatures "
"odd aerial architecture. The Twiggins' legs dangled below it, each foot comprised "
"of a single webbed V. It held itself close to the wide mouth of the trumpet flower "
"at which it feasted with three-fingered hands much more alike in appearance to the "
"pincers of a scorpian or beatle; both hard, with barbed tangs; than to the fleshy "
"digits of humans."
	         ],
	         [-5, "The Twiggin looked at you. It was obviously agitated. Its whole body was "
"shaking, perhaps in fear, perhaps in rage. It's mouth opened in a dark gash. It shrieked. "
"Your ears ached and seemed to fill with liquid, blood? You lost your balance. Your head "
"throbbed in complaint. "
           ], 
           [-10, "The little pest flew forward and spit purple gunk at you. The gummy "
"substance would not be wiped off but began to change in color as it filled with your "
"blood."      
           ],
           [-15, "It's head snapped toward you and you saw how ugly its face was. "
"Like a walnut shell with a slash in it, but it's eyes were disarmingly . . . human. "
"\"Vvrumb\" It said. You quickly calculate that Vvrumb is Twiggin for yum. It flies "
"at you, pincers forward, hungry mouth leaking a gummy purple liquid. Pincers slashed "
"your flesh. Sharp feet stabbed your arms, neck and face."
	        ]], [["twiggin_swarm"], ["""Swarm before"""], ["""Swarm after"""], ["swarm three"]
	        ]

Twiggin_Swarm_Scenes = [["You have stumbled into an active twiggin nest. An upright cylinder, about "
"three feet tall. It is made up mostly of brush; sticks, leaves and long grasses. The hollow "
"structure is striped horizontally by a white gummy substance. The whole thing smells like "
"a mixture of the most acrid of lemons and diesel exhaust. The pungeant fumes forced bile to "
"rise in your throat. One shrill, kreeeep! was answered by several more, then a cacaphony of "
"shrieks erupted from the nest. An army of Twiggins poured forth; pincers cut the air: "
"ksh, ksh. Their mouths opened wide to hold an oozing purple goop that spilled over onto their "
"brown cracked lips. They form a wall between you and the nest."],
           [-14, "The dissonant noise of slashing pincers from the suspended, pulsating wall of "
"Twiggins, falls into synch, ksh, ksh, ksh. They open and slice in unison. Your skin goes cold. "
"Every fine hair on your body stands on end. As one, the murderous curtain comes at you, they "
"slashed every inch of your body as they landed. Some two hundred sharp feet found purchase, "
"then they set at you even more viciously. You threw yourself to the ground and again, "
"breaking them beneath you. When your hands were free you pulled the Twiggins from your scalp "
"as your own blood flowed into your eyes, stinging and blinding you."
           ],
           [-14, "The suspended wall of Twiggins breaks right. Retaining form; they rise and "
"join ends to create a living cylinder above you. They circle above. A gutteral hum breaks  "
"through the scissoring clamor of their flight. All at once hundreds of mouths open, rust-red "
"tongues dart forward and purple goop comes pouring down over your head. The goop melds to your "
"body, it spreads until it covers every inch of you. You find the goop on your bare hands turns "
"red first. As blood is drawn from your body, into the goop, you become faint. "
           ],
           [-10, "All at once a the swarm of Twiggins emitted a shrill and grating shriek. You "
"covered your ears but the pain overwhelmed you. You ran. They pursued you all the way to the "
"tiny marshy lake nearby. They flew at you, their shriek drew blood from your ears. You dove "
"into the water. The massive carp didn't mind your presence but took the opportunity to leap "
"up out of the water to catch several Twiggins for their lunch. "           
           ]]


##########################################Friends##########################################

Blacksmith_Scenes = [
          ["Intro dialogue containing clue about polearm"],
          ["Blacksmith gives hero polearm"],
          ["Blacksmith tell hero how to use it, page is added to book."]
          ]

Herbalist_Scenes = [
            ["The distinct smell and orange brown glow of cypress welcomed you as you "
"stepped inside the fragrant shop. The wood had needed harvesting from the southern gulf, "
"those oft-swamped marshes that prevented a southernmost trail between Garzhed forest and "
"the broken desert. Most of the herbs you smelled seemed local though, lilac and rosemary "
"most pungeant among them, though beneath those you caught smells more foul, something " 
"acrid. Jars of thick grey pultice line the shelves of the wall to the right, the case "
"on the table before you holds thumb-sized bottles, jewel colored; saphire, ruby, amethyst "
"darkened within by syrups. From the left hang bulk dried herbs and small animals, their "
"furs intact but well waxed. The man behind the counter, fiery red hair atop his head, a "
"trim beard and small hands going quickly about his work of sewing two dark, furry, mostly "
"indescribable pieces together, spoke to you without looking up from his work. \"Welcome. "
"My council is free with purchase of my goods. If nothing ails you today, look ahead. No "
"soul walks free of needing for long."],
            ["Here is my price list, please tell me what you would like"
             "Item                    Quantity   Price"
             "Health Augment                 3      15"
             "Minor Healing Draught          3      10 "],
            ["Thank you for your business. Go with good health. "],
            ["It depends on what type of weapon you're looking for. If you're in need of "
"something for personal protection the Desert Scholar may be your best bet. If you intend "
"to slay a beast much greater in size than yourself then you should see the blacksmith in "
"town here. Though it isn't cheap. A lot of metal goes into larger weapons and theres not "
"an easy job to be had about here. "],
            ["The Soul Shards are in the North, in the Dragonlands. If you go looking for "
"them you're unlikely to return."],
            ["I'm afraid I'm not a good source for information of the worldly sort as my "
"work sets me indoors, laboring well into the evening and there's not much talk that "
"happens in this shop. "] 
             ]
Desert_Scholar_Scenes = [
             ["Are you lost? You may drink as much water as you like. Then "
"you should be getting on your way. I have much to do. "],
             ["That which I have crafted has taken much time as I am a studious man. "
              "Item                    Quantity   Price" 
              "Catchers hat                   1      30"
              "Dagger                         2      15"],
             ["Farewell. May you choose the path of peace, for the sake of "
"all. "]
             ["Dragons did not ask for the terrible task of gaurding the souls. "
"They knew that ungaurded, those souls and the riches they created, both in "
"crude gold and in their combined ability to separate and protect a realm from "
"the rest of existence, would soon attract dark forces. Greed and the lust for "
"realms to press beneath ones thumb would draw the simple minded and many a "
"creature of tyrannical nature, even some of their own. It was the weakest, the "
"alliance of gold dragons who brought the need to the Green dragons, who in the "
"7th century of the current age ruled proudly. It is undoubtedly because of this "
"pride that they called for immediate relocation, they themselves moved from the "
"caverns of the forest, to the cold and unwelcoming territory now called "
"Dragonlands. When, in the next century, the alliance of The Red rose to "
"overwhelm the the alliance of The Green; in the bloody and savage manner that "
"Dragons have; they took the protectors mantle as their own. This ensured that no "
"human would oppose the new powers and that they longstanding peace between would "
"remain, as their own interests were still kept. It allowed The Green, having more "
"pride than sense, to succede before their numbers had dwindled to the post coup "
"numbers of the fallen of the old age. Peace among their own was of great interest "
"to The Red, they did afterall seek to rule all. And more was a much more "
"attractive all than less."],
             ["For one who knows nothing of them, they all seem alike enough. "
"there are three races that war, The Red, The Green and The Gold. The White do "
"no such thing. They seem unfettered by the bloody habits of every other living "
"creature. Except to eat, and they drink the birds of the sky at that, you'll see "
"no harm done in their presence. "],
             ["A friend helped me forge the defenses you saw 'round the hut. It "
"easy enough for me to make passage into my home impossible. That suits more than "
"just me, you understand? My work is of great importance to a great many souls in "
"our time and forward. It wouldn't do to have me killed off by some simple thug "
"or spiteful creature."],
             ["To some, I am the Dragonkinds historian. Giving detailed accounts "
"of thier culture and ways of life, so they remain undisturbed and understood. "
"To others, I am a chronicler of the story that unfolds between Human and Dragon "
"within our lands so that mistakes need not be repeated. I am called upon for "
"council to grievances from both sides and well I quell both usually. Never to the "
"knowledge of our seers, who see so many worlds that they can little comprehend a "
"single one, has a world with two intelligent and powerful creatures supported both. "
"Compassion was born into the heart of both these great species and that is my true "
"job. In the service of compassion, I do what is required of me to retain balance. "]
             ]
Meadow_Mystic_Scenes = [
                ["Hello Traveler. Please, come in. What can I do for you? "],
                ["Come take a look at my inventory. You should find what "
                "you're looking for here."
                "Item                    Quantity   Price"
                "Elixer of Minor Healing       2       10"
                "Elixer of Major Healing       2       20"
                "Elixer of Minor Protection    2       10"
                "Elixer of Major Protection    2       20"
                "Oil of Retrieve Memories      1       35"
                "Oil of Foresight              1       35"],
                ["I thank you for making your way to me. To thank you for your "
                "purchase I'd like to send you on your way with this gift. It "
                "is a token of protection, though a fragile one. To use your "
                "item simply type its name. Goodbye. "],
                ["I am sorry that none of my wares took your interest."],
                ["Is it knowledge you're after? I see. How unusual. Take a seat. "
                 "What do you wish to know?"],
                ["There are only two paths to free a soul from The Sorrow. One is "
                 "wet with blood and what is dark and slippery is treacherous of course "
                 "the other will require more than brute strength. You weild the sword "
                 "or try your hand at diplomacy, those are the roads that lead to the "
                 "sorrow. The first takes bravery, the second cunning; both will require "
                 "you to be prepared if you wish to be successful. "],
                ["I know who you are, though I will not speak with you about it. You did "
                 "no wrongs to me or mine, tis not your way. But I know why you've come "
                 "and I won't distract you from your path. "],
                ["Yes, your family survives. It is hard to remain hidden when one you love "
                 "is so close, you have no idea how hard. But they will not seek you out "
                 "nor let you find them. "],
                ["You are asking many questions. Do not let yourself beleive that any "
                 "curiousity is without reciprocity. You remember naught of the child-times "
                 "but you remember leaving, yes? Yes, I can see it in your eyes. Even without "
                 "your memories you know that you would not have undergone such an exit "
                 "ceremony in a frivolous nature. All those that watched you cut the skin "
                 "from over your own heart as you sang in the common tongue, the last words "
                 "as such you'd ever speak, that your heart had left this place, that it belonged "
                 "to another. Of course you have many questions, the answers will not satisfy "
                 "you. And they do not belong to you. You forsook knowledge of this place. I "
                 "wish you well but that is the truth at the end of it. "],
                 ["I do not have knowledge of that sort. You'll find that most practices of "
                  "any worth require much study. Focus in one thing leaves other areas "
                  "undiscovered. You will find your answers elsewhere. "],
                 ["I wish you luck in your quest. Goodbye. "]   
                 ]
#Peacekeeper Dragon
White_Dragon_Scenes = [
               ["Before you appeared, or came upon you from the convergence of the lightening-white "
"clouds and the mist hanging over the lake, a Dragon, the likes of which had never before been "
"seen. Almost as long as the mountain was tall and a third as wide. The whole of the land, the deep "
"green spruces, the ashen grey dead woods, the brown and grey dirt of the mountains foot, the "
"cerulean depths of sorrow even the uplifting powder-blue sky and the rainbowed prism of the soul "
"chards reflected from her white scales, so glossy as to look laquered or of molten china. "
"Everything was softened on her skins armor. You saw yourself. Ragged, tired. Blood left behind from "
"so many foes as was becoming hard to count. Yet in that instant that you allowed yourself to take "
"her in, the creature who responded to your prayer you saw in your reflection your love for Arturia. "
"It made your wounds minor nuisance, it made your fear for your own life a thought you may live to "
"consider when she was safe and breathing once more, when she was back in your world. No, in her "
"world. Gods let my love be enough. "],
               ["The White Dragon did not startle. She stared, without blinking, at you. there was no "
"weapon or sorcery so black that it could stain this white thing red. It seemed an eternity had passed "
"before she dipped her muzzle and spoke, \"I am greatly dissapointed in you youngling. Your actions "
"bring sorrow down upon you. I have watched you rage against the whole of existence as if the shaping "
"of your fortune were the work of any other soul. The Mother and her Babe. You will not be again be "
"mother until you see with the eyes of every mother. When one weeps for her loss, you too must wreath "
"in agony for the unbearable pain that shadows love. Of Love. If that human construct best speeds you "
"on your path whilst you're kept true then I will entertain it. Yet see how you justify violence, conquest "
"in the name of this thing love? Nothing of worth is born else from necessity.\" She crouched down "
"ever so slightly and then was aloft. Her body seemed to melt into the sky. A flash of sunlight off of her "
"tail then she was gone."],
               ["The White Dragons smile was deep set and satisfying to behold. You guessed that only a "
"handful of souls had shared this experience. \"I have taken note of the weight of your quest. You will "
"be with her again soon. You showed enough strength and wisdom to stay the true path. For this I send "
"you forth with truths; the first born of gratitude and the second born of promise. Others have watched this great "
"warrior, cutting down all who blocked her way, with one hunger; with one pain, humble herself here, now. "
"In that you manifest the Mother and all will be reminded that none deserves dominion and all are in " 
"service to another, thus we share the weight of existence. Next. Do not shield her from the lessons by which "
"you have survived. Never has an Everless risen that had not been forged in the fires of the wilds.\" "
"Your daughter, young Everless."               ]
               ]
##########################################Encounter Dictionary##########################################
encounter = {1: Twiggins_Scenes,
             2: Twiggins_Scenes,
             4: Dragons_Scenes,
             5: The_Sorrow_Scenes,
             6: Dragons_Scenes,
             7: Twiggins_Scenes,
             8: Meadow_Mystic_Scenes,
             10: Dragons_Scenes,
             11: The_Sorrow_Scenes,
             12: Dragons_Scenes,
             13: Twiggins_Scenes,
             14: Twiggins_Scenes,
             16: Dragons_Scenes,
             17: Dragons_Scenes,
             18: Dragons_Scenes,
             19: Scorpian_Scenes,
             20: Spewer_Scenes,
             21: Spewer_Scenes,
             22: Memory_Nymphs_Scenes,
             23: Memory_Nymphs_Scenes,
             24: Memory_Nymphs_Scenes,
             25: Desert_Scholar_Scenes,
             26: Spewer_Scenes,
             27: Spewer_Scenes,
             28: Tree_Disease_Scenes,
             29: Herbalist_Scenes,
             30: Blacksmith_Scenes,
             31: Scorpian_Scenes,
             32: Scorpian_Scenes,
             33: Scorpian_Scenes,
             34: Tree_Disease_Scenes,
             35: Tree_Disease_Scenes,
             36: Tree_Disease_Scenes
             }               
##########################################Hero_Attacks##########################################
Hero = {-5: 'punch'}               
##########################################Hitpoints##########################################
Hit_Points = {"Hero": 65, "Dragons":{"red_dragon":80, "green_dragon":70, "gold_dragon":65}, "Scorpian": 15}
Fairy = [30]
Histears = [65] 
Twiggin = [10]

##########################################Encounters Input Dictionaries########################################## 
Blacksmith_Inp = {'stuff': 1, 'stuff': 2, 'stuff': 3, 'stuff': 4}  
Desert_Scholar_Inp = {'hello': 0, 'buy': 1, 'weapons': 1, 'goods': 1,
'goodbye': 2, 'thanks': 2, 'soul shards':3, 'souls': 3, 'Dragons': 3,
'history': 3, 'white dragons': 4, 'White Dragons': 4, 'peace': 4,
'shards': 5, 'outside': 5, 'safe': 5, 'you': 6}
Herbalist_Inp = {'buy': 1, 'goods': 1, 'healing': 1, 'goodbye': 2, 'thanks': 2, 'weapon': 3,
'protection': 3, 'blacksmith': 3, 'weapons': 3, 'sould shards': 4, 'daughter': 4} 
Meadow_Mystic_Inp = {'hello': 0, 'buy': 1, 'oils': 1, 'healing': 1, 'trade': 1, 'poison': 1,
'goodbye': 2, 'thanks': 2, 'information': 4, 'soul shard': 4, 'where': 4, 'how': 4, 'the sorrow': 5,
'daughter': 5, 'Arturia': 5, 'dragons': 5, 'Dragons': 5, 'I': 6, 'me': 6,
'family': 7, 'mother': 7, 'father': 7}
White_Dragon_Inp = {'stuff': 1, 'stuff': 2, 'stuff': 3, 'stuff': 4}

encounter_directory = {
                       8: Meadow_Mystic_Inp,
                      25: Desert_Scholar_Inp,
                      29: Herbalist_Inp,
                      30: Blacksmith_Inp
                      }      

          
##########################################Action Input Dictionaries##########################################
direction = {'north': -6, 'east': 1,
            'south': 6, 'west': -1
            }       
action = {'sleep': +3, 'open bag': 0, 
       'sing': +1
       }
main_directory = {0: direction, 1: action, 2:Blacksmith_Inp, 3: Desert_Scholar_Inp, 4: Herbalist_Inp,
5: Meadow_Mystic_Inp, 6: White_Dragon_Inp}       
