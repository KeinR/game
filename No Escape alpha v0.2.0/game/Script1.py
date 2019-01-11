import pygame
import Game

class Script():
    def __init__(self):
        pygame.init()

    def script(self, inp, p, sc, sab):
        if inp == "start":
            return "s", ("\n###\nGame start...\n\n*\nA tall rugged looking man stands before you. His face is empty and emotionless, and his right hand rests lightly on a holstered gun.\nMan:\"...So, what will it be?\"\n>(a) \"Wait, what?\"\n>(b) Reach for his weapon\n>(c) Look around")

        # Route s
        if inp == "a" and p == "s":
            return "sa", ("\n\n*\nMan: \"You weren’t listening, punk? I’ll say it one more time: You have two options: Either you accept my challenge, or you hand over your wallet.\"\n>(a) Give him your wallet\n>(b) \"What’s this challenge about?\"\n>(c) \"I choose the challenge\"\n>(d) Run for it")

        if inp == "b" and p == "s":
            pygame.mixer.music.load("sfx/fight.ogg")
            pygame.mixer.music.play()
            return "sb", ("\n\n*\nYou reach for his weapon and manage to grab it. However, since you left yourself wide open during your lunge, the man was able to tackle and pin you down. He is much stronger than you, and is able to wrestle his gun back with ease.\nMan: \"A feisty one, eh? Tell you what: I’ll forget you tried to steal my gun and spare your life, if you complete my challenge… And no, this time you lose your wallet regardless\"\nHe takes your wallet from your pocket and gets up.\nMan: \"Now then, as for my challenge:\"\n\"What is greater than God, more evil than the devil, the poor have it, the rich need it, and if you eat it, you'll die?\"\n<[free response, no caps, one word]>")

        if inp == "c" and p == "s" and not sc:  # Minor
            return "<sc>", ("\n\n*\nYou take in your surroundings. You are in a corridor of sorts. It’s quite dark, but above you you can make out pipes and machinery that continues upwards as far as the eye can see. Below you, the floor feels hard and metallic through your shoes. Behind the man is a sort of motorcycle.\nMan: \"Oi, did I not make myself clear?\"\nThe man’s right hand stiffens around his holstered gun.\nMan: \"Answer me, now!\"\n>(a) \"Wait, so, what was your question, again?\"\n>(b) Reach for his weapon")

        # Phase sa (Route 1)
        if inp == "a" and p == "sa":
            return "saa", ("\n\n*\nYou give the man your wallet.\nMan: \"Aw, you’re no fun. Guess I can’t complain though.\"\nThe man smiles as he sifts through your wallet.\nMan: \"Now, get out of my sight.\"\n>(a) Turn around and walk away\n>(b) Stand there like an idiot")

        if inp == "b" and p == "sa" and not sab:
            return "<sab>", ("\n\n*\nMan: \"I'll ask you one more time: your wallet or my challenge?\"\n>(a) Give him your wallet\n>(c) \"I choose the challenge\"\n>(d) Run for it")

        if inp == "c" and p == "sa":
            return "sac", ("\n\n*\nThe man smiles.\nMan: \"Ah, good choice! Now, as for my challenge... Answer this:\"\n\"A murderer is condemned to death. He has to choose between three rooms. The first is full of raging fires, the second is full of assassins with loaded guns, and the third is full of lions that haven't eaten in 3 years. Which room is safest for him?\"\n>(a) Room 1\n>(b) Room 2\n>(c) Room 3")

        if inp == "d" and p == "sa":
            pygame.mixer.music.load("sfx/missrun.ogg")
            pygame.mixer.music.play()
            return "sad", ("\n\n*\nYou turn away and run as fast as you can away from the man.\nMan: \"Oh, don't think you can escape me!\"\nYou hear him fire his gun, and missed shots hit the ground around you.\nThe tunnel bends and you are taken out of the pistol's range.\n>(a) Keep moving...")

        # Route sb
        if inp == "nothing" and p == "sb":
            return "sbt", ("\n\n*\nThe man is quiet for a moment.\nMan: \"Hmm... I didn't expect you to get that one...\"\nHe waits a little longer, staring at the floor.\nMan: \"Well, I suppose you won fair and square. I suppose I will forget your assault, and since you impressed me su much, you can have your wallet back. Oh, and my name's Rick, by the way.\"\nThe man hands you your wallet back and waves as he gets on his motorbike and speeds away from you.\nYou can choose to follow the man or play it safe and turn around.\n>(a) Turn around\n>(b) Follow Rick")

        if inp != "nothing" and p == "sb":
            pygame.mixer.music.load("sfx/pistol.ogg")
            pygame.mixer.music.play()
            return "sbf", ("\n\n*\nHe frowns.\nMan: \"A pity. I didn't want to kill you, but...\"\nHe gives you a devilish grin.\n\"...I simply cannot forgive your little assault.\"\nHe takes out his gun and shoots you dead.\nGAME OVER.")

        # Chain saa (a) and sacaa (a)
        if inp == "a" and (p == "saa" or p == "sacaa"):
            return "saaa", ("\n\n*\nYou obey the man and you turn around and start walking.\nThe corridor is windy, and appears to have no end...\n>(a) Must keep going...")

        if inp == "a" and p == "saaa":
            return "saaaa", ("\n\n*\nAfter a while, you notice something has changed. You look around you to find that there is now a nice roof above you, hiding the machinery above from view.\n>(a) Now we're getting somewhere!")

        if inp == "a" and p == "saaaa":
            return "saaaaa", ("\n\n*\nSome time later, you come across a door with a keypad blocking your way.\n>(a) Uh oh...")

        if inp == "a" and p == "saaaaa":
            return "saaaaaa", ("\n\n*\nYou walk up to the keypad and examine it:\nIt is a letter-only keypad, with a paper taped to the wall next to it that reads:\n\"Those who deny _____ to others do not deserve it for themselves.\"\nWhat should you enter?\n<[one word, no caps]>")

        if inp != "freedom" and p == "saaaaaa":
            pygame.mixer.music.load("sfx/deepbeep.ogg")
            pygame.mixer.music.play()
            return "saaaaaa", ("\n\n*\nYou hear a deep beep and an electronic voice saying, \"Incorrect passphrase\"...")

        if inp == "freedom" and p == "saaaaaa":
            pygame.mixer.music.load("sfx/3beep.ogg")
            pygame.mixer.music.play()
            return "saaaaaat", ("\n\n*\nYou hear three short beeps and an electronic voice says:\n\"So said Abraham Lincoln. Death to the tyrants!\"\nAfter the voice finishes, the door slides open.\n>(a) Continue moving...")

        if inp == "a" and p == "saaaaaat":
            return "saaaaaata", ("\n\n*\nYou don't get far before you hear voices from behind you.\n>(a) Uh oh...")

        if inp == "a" and p == "saaaaaata":
            pygame.mixer.music.load("sfx/3runmetal.ogg")
            pygame.mixer.music.play()
            return "saaaaaataa", ("\n\n*\nYou quicken your pace to try escaping them, but it's no use. Three men in rugged clothing and armed with semi-automatic rifles approach you.\n\"Don't move or we'll shoot!\" says one of them.\n>(a)Sh**")

        if inp == "a" and p == "saaaaaataa":
            return "saaaaaataaa", ("\n\n*\nOne of them lowers their weapon and steps forward\nArmed man: \"We have received reports of a strange individual heading towards the exit after speaking with one of our members!\"\nHe takes out a small rectangular device\nArmed man: \"You're gonna' have to show us some ID or we'll have to shoot you on the spot for espionage!\"\n>(a) Search your pockets for something...")

        if inp == "a" and p == "saaaaaataaa":
            return "saaaaaataaaa", ("\n\n*\nYou search everywhere, but find nothing. The armed men in front of you notice this, and nod to each other.\nArmed man: \"Well, I think it's clear that you're not one of us. Open fire!\"\n>(a) \"Wait—\"")

        if inp == "a" and p == "saaaaaataaaa":
            pygame.mixer.music.load("sfx/rifle4shot.ogg")
            pygame.mixer.music.play()
            return "saaaaaataaaaa", ("\n\n*\nThe men didn't wait for you to finish. They opened fire, killing you.\nGAME OVER")

        # Chain saa (b) and sacaa (b)
        if inp == "b" and (p == "saa" or p == "sacaa"):
            pygame.mixer.music.load("sfx/pistol.ogg")
            pygame.mixer.music.play()
            return "saab", ("\n\n*\nThe man rolls his eyes and sighs.\nMan: \"Idiot\"\nHe pulls out his gun and fires. You have no time to react, and you are on the floor bleeding in seconds.\nThe man shakes his head as if regretting his crime, then speeds away on his motorbike.\n>(a) \"Wh... Wha...\" *cough*")

        if inp == "a" and p == "saab":
            return "saaba", ("\n\n*\nYou wait in silence as death takes you. Why didn't you leave when the man told you to? Moreover, was there something special in your wallet that he wanted aside from money?\nThese thoughts are pointless, you reason. It's not like this is a game that you could just restart...\n>(a) If only...")

        if inp == "a" and p == "saaba":
            return "saabaa", ("\n\n*\nYour body finally gives into the effects of blood loss, and you dive into a world of darkness.\n>(a) GAME OVER!?")

        if inp == "a" and p == "saabaa":
            return "saabaaa", ("\n\n*\nYes, that is correct. Congrats, you failed. Why on earth did you just stand there? I mean, what did you think was going to happen, eh? The option itself said it was idiotic!\nAnyways: Leave now. Restart the program, or just type 'start'.")

        if (inp == "no" or inp == "No" or inp == "nope" or inp == "Nope") and p == "saabaaa":
            return "saabaaat", ("\n\n*\n...\n...\nYou cheeky bastard.\n...\nFine, I'll give you a hint:\nDon't give Rick your wallet!\nOr do, I don't really care.\nThat's all I'll say.")

        if (inp == "no" or inp == "No" or inp == "nope" or inp == "Nope") and p == "saabaaat":
            return "saabaaatt", ("\n\n*\nFUUUUUUUU—\nYou know that old saying, 'give them and inch and they'll take a mile?'\nWell exactly, you cheeky bas***d. I can't make this thing go on forever, you know... That would be a little bit too much work.\nThat's why it ends here.")

        if (inp == "no" or inp == "No" or inp == "nope" or inp == "Nope") and p == "saabaaatt":
            pygame.mixer.music.load("sfx/congratulations.mp3")
            pygame.mixer.music.play()
            return "saabaaattt", ("\n\n*\nYou know what? Fine. You win the game! Satisfied now? CONGRATULATIONS! YOU BEAT THE GAME AND GOT THE \"NEEDLESSLY PERSISTENT\" ENDING!")

        # Route sac -> saab (including sacc)
        if (inp == "a" or inp == "b") and p == "sac":
            return "saca", ("\n\n*\nMan: \"WRONG. It's room 3, because lions can't live without food for 3 years. Really, how did you miss that?\"\nThe man shakes his head.\nMan: \"Well, that means that you have to give me your wallet\"\n>(a) Give him your wallet\n>(b) Refuse")

        if inp == "b" and p == "saca":
            pygame.mixer.music.load("sfx/pistol.ogg")
            pygame.mixer.music.play()
            return "sacaa", ("\n\n*\nMan: \"So be it, fool.\"\nHe unloads his pistol on you, killing you instantly.\nGAME OVER")

        if inp == "a" and p == "saca":
            return "sacaa", ("\n\n*\nYou hand him your wallet.\nMan: \"Very good.\"\nHe ruffles through it.\nMan: \"Now, be off with you.\"\n>(a) Turn around and walk away\n>(b) Stand there like an idiot")

        if inp == "c" and p == "sac":
            return "sacc", ("\n\n*\nThe man is quiet for a moment.\nMan: \"Hmm... I didn't expect you to get that one...\"\nHe waits a little longer, staring at the floor.\nMan: \"Well, I suppose you won fair and square. A word of advice: to leave this place, turn around and follow the tunnel. You should find some sort of exit. Oh, and my name's Rick, by the way.\"\nThe man waves as he gets on his motorbike and speeds away from you, the opposite way he told you to go.\nYou can choose to follow the man or take his advice and turn around and head towards the exit.\n>(a) Head to the exit\n>(b) Follow Rick")

        # Route sad -> END
        if inp == "a" and p == "sad":
            pygame.mixer.music.load("sfx/motorcycle.ogg")
            pygame.mixer.music.play()
            return "sada", ("\n\n*\nYou hear the sound of an engine start, then wheels on the ground.\nYou look behind you in time to see the man on his motorcycle, the barrel of his gun pointing directly at you.\n>(a) Oh, fu**...")

        if inp == "a" and p == "sada":
            pygame.mixer.music.load("sfx/nani4shot.ogg")
            pygame.mixer.music.play()
            return "sadaa", ("\n\n*\nThe man quickly lets loose 4 rounds into you, killing you instantly.\nGAME OVER.")

        # Chain sacc (a) and sbt (a)
        if inp == "a" and (p == "sacc" or p == "sbt"):
            return "sacca", ("\n\n*\nYou turn around and start walking.\n>(a) Let's go!")

        if inp == "a" and p == "sacca":
            return "saccaa", ("\n\n*\nAfter a while, you notice something has changed. You look around you to find that there is now a nice roof above you, hiding the machinery above from view.\n>(a) Now we're getting somewhere!")

        if inp == "a" and p == "saccaa":
            return "saccaaa", ("\n\n*\nSome time later, you come across a door with a keypad blocking your way.\n>(a) Uh oh...")

        if inp == "a" and p == "saccaaa":
            return "saccaaaa", ("\n\n*\nYou walk up to the keypad and examine it:\nIt is a letter-only keypad, with a paper taped to the wall next to it that reads:\n\"Those who deny _____ to others do not deserve it for themselves.\"\nWhat should you enter?\n<[one word, no caps]>")

        if inp != "freedom" and p == "saccaaaa":
            pygame.mixer.music.load("sfx/deepbeep.ogg")
            pygame.mixer.music.play()
            return "saccaaaa", ("\n\n*\nYou hear a deep beep and an electronic voice saying, \"Incorrect passphrase\"...")

        if inp == "freedom" and p == "saccaaaa":
            pygame.mixer.music.load("sfx/3beep.ogg")
            pygame.mixer.music.play()
            return "saccaaaat", ("\n\n*\nYou hear three short beeps and an electronic voice says:\n\"So said Abraham Lincoln. Death to the tyrants!\"\nAfter the voice finishes, the door slides open.\n>(a) Continue moving...")

        if inp == "a" and p == "saccaaaat":
            return "saccaaaata", ("\n\n*\nYou don't get far before you hear voices from behind you\n>(a) Uh oh...")

        if inp == "a" and p == "saccaaaata":
            pygame.mixer.music.load("sfx/3runmetal.ogg")
            pygame.mixer.music.play()
            return "saccaaaataa", ("\n\n*\nYou quicken your pace to try escaping them, but it's no use. Three men in rugged clothing and armed with semi-automatic rifles approach you.\n\"Don't move or we'll shoot!\" says one of them.\n>(a)Sh**")

        if inp == "a" and p == "saccaaaataa":
            return "saccaaaataaa", ("\n\n*\nOne of them lowers their weapon and steps forward\nArmed man: \"We have received reports of a strange individual heading towards the exit after speaking with one of our members!\"\nHe takes out a small rectangular device\nArmed man: \"You're gonna' have to show us some ID or we'll have to shoot you on the spot for espionage!\"\n>(a) Search your pockets for something...")

        if inp == "a" and p == "saccaaaataaa":
            return "saccaaaataaaa", ("\n\n*\nA through search of your pockets produced only your wallet. You open it up to reveal nothing but a green card. Trembling, you show them your card.\nThe man in front looks at it in astonishment before replying, \"Sir, it's good to have you back. We were worried about you after you got arrested wile you were out recruiting. We will act as your personal escorts for the rest of the journey.\"\n>(a) Perfect.")

        if inp == "a" and p == "saccaaaataaaa":
            pygame.mixer.music.load("sfx/enterancedoor.ogg")
            pygame.mixer.music.play()
            return "saccaaaataaaaa", ("\n\n*\nThe men escort you until you reach the exit, which is marked by a massive metal double-doors inside a wide open space off of which springs the corridor.\nYou order the sentries at the gate to open the doors. They were fiercely against it and protested, but after you flashed your green card, they reluctantly obeyed.\n>(a) To freedom!")

        if inp == "a" and p == "saccaaaataaaaa":
            pygame.mixer.music.load("sfx/ambush.ogg")
            pygame.mixer.music.play()
            return "saccaaaataaaaaa", ("\n\n*\nWhat you find on the outside, however, is not freedom.\nYour escorts immediately get shot and lie dead on the ground. The gate sentries call for you to hurry back inside the gate, but before you can move you feel a sharp pain in your chest.\n>(a) I'm so... Tired...")

        if inp == "a" and p == "saccaaaataaaaaa":
            pygame.mixer.music.load("sfx/gameover.mp3")
            pygame.mixer.music.play()
            print("NOW PLAYING: All Gone (No Escape) by Gustavo Santaolalla (The Last of Us OST)")
            return "saccaaaataaaaaaa", ("\n\n*\nYou fall asleep on the spot, and awaken later in a cell. For the rest of your life, you remain in your cell, eating what's pushed under the door, signing what they ask you to sign, saying what they want you to say, and sleeping on the floor.\nBecause of these living conditions, you die just 5 years later.\nGAME OVER")

        # sacc (b) sbt (b) and  to (inclusive) saccbaab
        if inp == "b" and (p == "sacc" or p == "sbt"):
            return "saccb", ("\n\n*\nYou decide to press your luck and follow Rick.\n As you advance further, the walls slowly become worn and in some places missing, revealing hidden machinery.\nIt doesn't take you long to reach your first obstacle, a man wearing a red bandanna guarding a closed gate.\n>(a) Let's hope he's friendly...")

        if inp == "a" and p == "saccb":
            return "saccba", ("\n\n*\nBandanna-man notices you, and waves his pistol.\nHe hails you, \"Hey there, got clearance?\"\n>(a) \"Clearance...?\"")

        if inp == "a" and p == "saccba":
            return "saccbaa", ("\n\n*\nHe chuckles, but quickly sobers.\"You do know that HQ center is reserved for only senior members or those of the high command, and that if you can't provide any valid clearance, I'll have to execute you on spot for not following orders, right?\"\n>(a) Comply and search your pockets for anything.\n>(b) Run while you still can!")

        if inp == "b" and p == "saccbaa":
            pygame.mixer.music.load("sfx/pistolshot.ogg")
            pygame.mixer.music.play()
            return "saccbaab", ("\n\n*\nYou turn around in a hurry and try to run, but bandanna-man is quicker and quickly lands a single accurate shot in you, causing you to fall to the ground, bleeding. Before you drift off, you hear him say:\n\"So you were up to no good after all, weren't you?\"\nGAME OVER")

        # saccbaa (a) to WAR (GOLDEN ROUTE)
        if inp == "a" and p == "saccbaa":
            return "saccbaaa", ("\n\n*\nA quick search of your pockets produces nothing but your wallet. You open it to find nothing but a green card with numbers and phrases written all over it\n>(a) Use it!")

        if inp == "a" and p == "saccbaaa":
            return "saccbaaaa", ("\n\n*\nTrembling, you take out the green card and hand it to bandanna-man. He looks it over for a while, frequently looking back up at you.\nFinally, this time his hands trembling, he hands the card back to you.\nHe looks up at you and speaks:\n\"Commander Vincent... You're back!\"\nTears well up in his eyes.\n\"It's been so long since those bloody fascists took you... We thought we'd never see you again!\"\n>(a) Wait, what are you talking about?")

        if inp == "a" and p == "saccbaaaa":
            return "saccbaaaaa", ("\n\n*\nBandanna-man looks up at you in surprise.\n\"What do you mean? Did they...\"\nHis eyes widen.\n\"...did they really wipe your memory?\"\nHe gives you no time to respond as he curses to himself and uses his radio.\nAfter a lot of yelling and intense chatter, bandanna-man turns to face you.\n\"Alright, so: You are Vincent, commander-in-chief of the Sons of Liberty, a guerrilla force dedicated to removing our evil tyrannical government and restoring to the citizens of this land their liberty. You were ambushed and captured during a recruitment mission in one of the small nearby towns... That's all I can say for now. Go on ahead and talk to Commander Julian, he'll fill you in on your duties.\"\nHe opens the gate and waves for you to pass through.\n>(a) Doesn't look like I have a choice...")

        if inp == "a" and p == "saccbaaaaa":
            return "saccbaaaaaa", ("\n\n*\nYou continue on down the corridor until you reach a large open space with multible individual rooms and corridors leading off of it. It's filled with rough looking men tending to weapons, drinking, eating, playing cards, and all manner of things.\nUpon entering the room, everyone is silent and staring at you. A comparatively well dressed man in a beret walks up to you from the crowd\n\"Vincent,\" he says, \"Mike told us you came back. It's good to have our best commander, despite how they wiped your memories...\"\nHe looks around himself\n\"Follow me\"\n>(a) Follow him")

        if inp == "a" and p == "saccbaaaaaa":
            return "saccbaaaaaaa", ("\n\n*\nHe leads you to one of the rooms leading off of the main room and closes the door.\n\"Listen, Vincent... I know you don't remember anything. But you must know that you swore allegiance to the Sons of Liberty. You MUST honor your word— Do you?\"\n>(a) \"Yes\"\n>(b) \"No\"")

        if inp == "b" and p == "saccbaaaaaaa":
            pygame.mixer.music.load("sfx/sadpistol.ogg")
            pygame.mixer.music.play()
            return "saccbaaaaaaab", ("\n\n*\nHe sheds a tear and looks down\n\"Vincent, you and I, we were best friends. I had hoped that you would stay with us, but...\" He looks up now, his face is covered in tears, \"...we made a pact that our friendship would never come into conflict with our allegance to the Sons of Liberty. Besides...\" he sniffs and looks you in the eye, \"...The Vincent I knew would never break his word, even if he forgot everything.\"\nHe takes out a pistol and looks away as he unloads it's entire clip into your torso. As you lay there, dying, you see him break down crying before death takes you.\nGAME OVER")

        if inp == "a" and p == "saccbaaaaaaa":
            return "saccbaaaaaaaa", ("\n\n*\nHe breaths a sigh of relief and smiles.\n\"That's a relief. I was worried you would refuse, as I would be forced to execute you... Not only because you would be breaking your word, but because you were, or rather are, our best general. Which reminds me...\" He walks over to a table in the back of the room with a map sprawled out on it.\n\"Since you've lost your memory, I'll give you a little bit of a refresher. Mike already told you some, so I'll be brief:\"\n>(a) Listen to him")

        if inp == "a" and p == "saccbaaaaaaaa":
            return "saccbaaaaaaaaa", ("\n\n*\n\"You are Commander in Chief of the Sons of Liberty, Vincent Fall. I am the second in command, Ian Card. You are a military genius, insomuch that the Fascists would stop at nothing to capture you, such is your genius even without your memories. Or so we hope...\"\nHe looks at the map on the table before continuing.\n\"...You will be put in complete charge of our forces, responsible for positioning, maneuvering, supplying, and replenishing our troops. Are you ready to take on such a task?\"\n>(a) \"I am ready\"")

        if inp == "a" and p == "saccbaaaaaaaaa":
            return "saccbaaaaaaaaaa", ("\n\n*\n\"Good. I will leave you now. The generals will meet with you once a day to plot our next move. We are counting on you, commander.\"\nWith that, he leaves you alone.")

        if inp == "a" and p == "saccbaaaaaaaaaa":
            return "transition", ("You have reached the end of game thus far.\nMore is planned beyond this point!\nBe sure to leave feedback on any features that should be added/removed and an bugs or even just formatting mistakes in the script that you find.")