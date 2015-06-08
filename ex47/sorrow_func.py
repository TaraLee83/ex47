import random
from format_incoming import format_text
from hp import Hit_Points
from scenes import encounter, The_Sorrow_Lake_Scenes, The_Sorrow_Island_Scenes


def the_sorrow(self, current_space):
	scene_group = encounter[current_space]
	scene = random.randrange(1, len(scene_group))
	Hit_Points["Hero"] = (Hit_Points["Hero"] + scene_group[scene][0])
	return format_text('self', scene_group[0][0]), format_text('self', scene_group[scene][1]), "    Your health is now %r." % Hit_Points["Hero"]
