print('''
--.   --..,_   _,.--.   --..,_   _,.--.   --..,_   _,.--.   --..,
o  `;__. `'.:'`__ o  `;__. `'.:'`__ o  `;__. `'.:'`__ o  `;__. `' .
---'`  `  .'.:`. '---'`  `  .'.:`. '---'`  `  .'.:`. '---'`  `  .'.
--....--'`.'  '.`'--....--'`.'  '.`'--....--'`.'  '.`'--....--'`.'
--....--'`      `'--....--'`      `'--....--'`      `'--....--'`
*******************************************************************
Treasure Island: A Tale of Fateful Choices

Welcome, brave traveler, to the cursed and hallowed grounds of Treasure Island.
Legends speak of an artifact hidden in the depths of this land—a relic of
boundless power and unspeakable beauty. You are destined to seek it,
but beware: the island is alive with trials meant to test the worthiest
of souls. Every choice matters. Let the journey begin.
''')


the_fork_in_the_road = input("""Before you stretch two paths, each veiled in mystery.
The air hums with anticipation as the voice of an unseen guide echoes:
“Choose, wanderer. Will you tread left, where shadows embrace the daring?
Or will you go right, where secrets lie in wait?”
 """).lower()

if the_fork_in_the_road == "left":
    print('''Left: The path is dark and treacherous. Roots twist like the claws of
the damned, and the ground beneath your feet crumbles.
Without warning, the earth gives way, and you plunge into an abyss.
Your story ends here, swallowed by the island’s merciless depths.''')
    exit()

elif the_fork_in_the_road == "right":
    print('''Right: This path opens into a clearing bathed in moonlight,
where a serene lake shimmers with unnatural light. You have passed the
first trial, but your journey is far from over.''')

    the_lake_of_time = input('''Standing before the lake, you sense its unnatural stillness.
The water’s surface reflects not the sky but a swirling void. A voice whispers:
“The lake demands a choice. Swim, and you may face the fury of its guardian.
Wait, and time may deliver a safer way.”
''').lower()

    if the_lake_of_time == "swim":
        print('''Swim: The moment you enter the water, it grows cold and viscous, pulling you
into its depths. From below emerges a monstrous trout, its eyes glowing red and its maw
lined with razor-sharp teeth. Your courage turns to folly as the guardian claims another soul.
Your tale ends here.''')
        exit()
    elif the_lake_of_time == "wait":
        print('''Wait: Patience rewards you as a spectral boat emerges from the mist.
A silent ferryman beckons you aboard. You glide across the lake without a word exchanged,
reaching the far shore unscathed. The second trial is complete.
''')
        the_doors_of_destiny = input('''Before you now stands an ancient structure,
its walls carved with runes that pulse faintly. Three doors, yellow, red and blue.Each marked by a
glowing sigil, block your way. The voice returns:
“Choose wisely. Each door leads to your fate—one to triumph, the others to doom. Will you dare
to enter or you will run away like the others?”
''')
        if the_doors_of_destiny == "red":
            print('''Red Door: You open the door, and flames burst forth,
engulfing you in a fiery inferno. Your screams echo in the emptiness as
the island claims another unworthy soul.''')
            exit()
        elif the_doors_of_destiny == "blue":
            print('''Blue Door: The door creaks open to reveal a chamber of ice. Frost creeps up your limbs,
freezing you in place. A howl of beasts pierces the air, and their glowing eyes appear in the dark.
They lunge, and the icy tomb becomes your grave.''')
            exit()
        elif the_doors_of_destiny == "yellow":
            print('''Yellow Door: The door reveals a golden glow that warms your very soul.
You step into the treasure room, where piles of gold and jewels surround the artifact.
A relic of ancient power lies atop a pedestal, untouched by time. You have succeeded where others have failed.
The treasure is yours, and your name will echo through the ages.''')
            print('''
**************************************************************************************
Epilogue

With the treasure in hand, you return to the world beyond the island, forever changed.
The trials of Treasure Island tested yoleftur courage, patience, and wisdom.
Few have walked these paths and lived to tell the tale, but you stand among the legends now.
What you do with your newfound power—that is a story for another time.
Go forth, adventurer, and let your deeds shape the world.
                  ''')
            exit()
        else:
            print('''Fear grips you, and you turn to flee the ominous doors.
As you sprint away, the air around you crackles with unseen power.
A malevolent force erupts from the runes, striking you down.
Your cowardice awakens the island’s wrath, and you perish in ignominy, forgotten by history.''')
            exit()