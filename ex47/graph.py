#Provide tile access points.

graph = {1: [2, 7],
         2: [1, 3, 8],
	 3: [2, 4, 9],
         4: [3, 5, 10],
         5: [4, 6, 11],
         6: [5, 12],
         7: [8, 13],
         8: [7, 9, 14],
         9: [8, 10, 15],
         10: [9, 11, 16],
         11: [10, 12, 17],
         12: [11, 18],
         13: [7, 14, 19],
         14: [8, 13, 15, 20],
         15: [9, 14, 16, 21],
         16: [10, 15, 17, 22],
         17: [11, 16, 18, 23],
         18: [12, 17, 24],
         19: [13, 20],
         20: [14, 19, 21, 26],
         21: [14, 20, 22, 27],
         22: [16, 21, 23, 28],
         23: [17, 22, 24, 29],
         24: [18, 23],
         25: [19, 26, 31],
         26: [20, 25, 27, 32],
         27: [21, 26, 28, 33],
         28: [22, 27, 29, 34],
         29: [23, 28, 30, 35],
         30: [24, 29, 36],
         31: [32],
         32: [26, 31, 33],
         33: [27, 32, 34],
         34: [28, 33, 35],
         35: [29, 34, 36],
         36: [35]
         }

Meadow = {}

Desert = {
         }

Forest = {
	 }

charms = {'godswear': ['red', 'green', 'gold']
         }
Red = {0: }

attack = {'red': ['fire_breath', 'claws', 'tail_swipe', 'finisher'],
          'green': ['fire_breath', 'claws', 'tail_swipe', 'finisher'],
          'gold': ['fire_breath', 'claws', 'tail_swipe', 'finisher'],
          'his_tears': ['drown', 'sorrow']
          } 


his_tears = 0


encounter = {1: "temp",
             2: "temp",
	     3: "temp",
             4: "temp",
             5: "temp",
             6: "temp",
             7: "temp",
             8: "temp",
             9: "temp",
             10: 'Dragonlands',
             11: 'Dragonlands',
             12: 'Dragonlands',
             13: "temp",
             14: "temp",
             15: "temp",
             16: "temp",
             17: "temp",
             18: "temp",
             19: "temp",
             20: "temp",
             21: "temp",
             22: "temp",
             23: "temp",
             24: "temp",
             25: "temp",
             26: "temp",
             27: "temp",
             28: "temp",
             29: "temp",
             30: "temp",
             31: "temp",
             32: "temp",
             33: "temp",
             34: "temp",
             35: "temp",
             36: "temp"
           }

#tile_loc = {1: Meadow,
#            2: Meadow,
#	    3: Meadow,
#            4: Dragonlands,
#            5: Dragonlands,
#            6: Dragonlands,
#            7: Meadow,
#            8: Meadow,
#            9: Meadow,
#            10: Dragonlands,
#            11: Dragonlands,
#            12: Dragonlands,
#            13: Meadow,
#            14: Meadow,
#            15: Meadow,
#            16: Dragonlands,
#            17: Dragonlands,
#            18: Dragonlands,
#            19: Desert,
#            20: Desert,
#            21: Desert,
#            22: Forest,
#            23: Forest,
#            24: Forest,
#            25: Desert,
#            26: Desert,
#            27: Desert,
#            28: Forest,
#            29: Forest,
#            30: Forest,
#            31: Desert,
#            32: Desert,
#            33: Desert,
#            34: Forest,
#            35: Forest,
#            36: Forest
#           }
 
 
    
