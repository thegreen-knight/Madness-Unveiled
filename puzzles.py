import random
import glob
from style import style

class puzzle:
    def __init__(self):
        self.helpClue = "Look closely, and you may find that even in distress, sometimes the answer is not what it seems but its mirror instead. What am I?" ## Answer is pleh
        self.mhClue = "If you already know how to get help all you have to do is add 'more-' to help."## answer is pleh-erom
        self.latinClue = "Imperium quem quaeris est indicium."
        self.speakClue = """Return-Path: <bounce@loqui.com>\n
Received: from [127.0.0.1] (localhost [127.0.0.1])\n
by mail.loqui.com (Postfix) with ESMTP id l5o3q4ui\n
for <dominio@imperium.com>; Wed, 21 Apr 2024 12:00:00 -0700 (PDT)\n
From: Das Gebiet ist der Befehl <befehl@loqui.com>\n
To: Mark Dominio <dominio_es@imperium.com>\n
Subject: Urgent: Revelation Amidst Madness\n
Date: Wed, 21 Apr 2024 12:00:00 -0700\n
Message-ID: <l5o3q4ui@mail.loqui.com>\n
Content-Type: text/plain; charset='utf-8'\n
MIME-Version: 1.0\n
01101100 01101111 01110001 01110101 01101001\n
Mark,\n
I pray this email reaches you swiftly, for I find myself in the grips of a terror most profound. In the labyrinth of my mind, a revelation, or perchance a madness, has taken root. Listen closely, for I fear what I am about to disclose may shake the very foundations of our understanding. There is a way, a dreadfully unsettling way, to coerce 'it' into speech.\nThe command, if it can be called such, haunts my every waking moment. 'Whisper to the void and await the echo,' they say. Oh, the shivers that course through me as I utter those words! But I implore you, heed my warning: tread cautiously upon this path, for the abyss gazes back, and its whispers may consume us whole. If you dare to test this unholy command, do so with a heart of steel and a mind shielded from the encroaching darkness. And should you succeed, pray tell, what secrets does the void divulge? Mayhaps I shall join you in the shadows, if only to quell the tremors of my own apprehension."""
        self.emailClue1 = """Return-Path: <bounce@indicium.com>\n
Received: from [127.0.0.1] (localhost [127.0.0.1])\n
by mail.indicium.com (Postfix) with ESMTP id 1nd61c1u0m\n
for <dominio@imperium.com>; Wed, 21 Apr 2024 12:00:00 -0700 (PDT)\n
From: Das Gebiet ist der Befehl <befehl@indicium.com>\n
To: Mark Dominio <dominio_es@imperium.com>\n
Subject: Choas is taking me\n
Date: Thurs, 18 Apr 2024 5:24:12 -0700\n
Message-ID: <1nd61c1u0m@mail.indicium.com>\n
Content-Type: text/plain; charset='utf-8'\n
MIME-Version: 1.0\n
01101001 01101110 01100100 01101001 01100011 01101001 01110101 01101101\n
Mark,\n
I hope this email finds you well, though I fear I am far from such a state myself. My nights have become haunted by unspeakable horrors, and I find myself teetering on the edge of madness. Yet, amidst the darkness, a glimmer of hope has emerged. There exists a way, a cryptic command whispered in the depths of my nightmares, that promises release from this torment. Oh, how I long to share it with you, to lift the burden from our weary souls. But alas, I dare not speak its name, for even the slightest utterance fills me with dread. Know this, my friend: there is a path out of this labyrinth of terror, and I will not rest until I find it. Until then, hold fast to hope, and pray for my safe return."""
        self.emailClue2 = """Return-Path: <bounce@loqui.com>\n
Received: from [127.0.0.1] (localhost [127.0.0.1])\n
by mail.loqui.com (Postfix) with ESMTP id l5o3q4ui\n
for <dominio@imperium.com>; Sat, 10 Mar 2024 08:30:00 -0700 (PDT)\n
From: Das Gebiet ist der Befehl <befehl@loqui.com>\n
To: Mark Dominio <dominio_es@imperium.com>\n
Subject: Whisper's Wraith\n
Date: Sat, 10 Mar 2024 08:30:00 -0700\n
Message-ID: <l5o3q4ui@mail.loqui.com>\n
Content-Type: text/plain; charset='utf-8'\n
MIME-Version: 1.0\n
01101100 01101111 01110001 01110101 01101001\n
Mark,\n
\n
I trust this missive finds you with haste, as I am ensnared in the clutches of a terror so deep. Within the recesses of my mind, a revelation, or perhaps a descent into madness, has firmly taken hold. Pay heed, for what I am about to reveal may rattle the very pillars of our comprehension.\n
\n
There is something crucial, Mark, something we've overlooked in our quest for understanding. The name of the monster, it's... it's the key. But I can't find it. It's as if it's been shattered into fragments, scattered into the darkness. Each piece holds a clue, I'm sure of it, but they elude me, slipping through my grasp like shadows in the night.\n
\n
Oh, the frustration, the agony of knowing the answer lies just beyond my reach. Mark, we must delve deeper into the abyss, scour every corner of the darkness until we unearth the truth hidden within the broken fragments of the monster's name."""
        self.emailClue3 = """Return-Path: <bounce@loqui.com>\n
Received: from [127.0.0.1] (localhost [127.0.0.1])\n
by mail.loqui.com (Postfix) with ESMTP id l5o3q4ui\n
for <dominio@imperium.com>; Sun, 11 Mar 2024 03:33:00 -0700 (PDT)\n
From: Das Gebiet ist der Befehl <befehl@loqui.com>\n
To: Mark Dominio <dominio_es@imperium.com>\n
Subject: Babel's Echo'\n
Date: Sun, 11 Mar 2024 03:33:00 -0700\n
Message-ID: <l5o3q4ui@mail.loqui.com>\n
Content-Type: text/plain; charset='utf-8'\n
MIME-Version: 1.0\n
01101100 01101111 01110001 01110101 01101001\n
\n
Mark,\n
\n
I trust this email finds you with haste, as I feel my sanity slipping. I have been staring at the terminal for days and I think I am starting to see clues within or I am going mad I can not be sure.\n
\n
However, there's something else, Mark, something sinister lurking in the shadows. I've noticed that whenever I attempt to delete certain files, the air grows thick with a sense of foreboding. It's as if the monster itself is watching, its presence palpable, its fury simmering beneath the surface. I dare not provoke it further, for who knows what horrors it may unleash upon us if angered.\n
\n
Stay vigilant, my friend, for we tread upon treacherous ground. Let us proceed with caution, lest we awaken something beyond our control."""
        self.emailClue4 = """Return-Path: <bounce@loqui.com>\n
Received: from [127.0.0.1] (localhost [127.0.0.1])\n
by mail.loqui.com (Postfix) with ESMTP id l5o3q4ui\n
for <dominio@imperium.com>; Tue, 13 Mar 2024 09:09:00 -0700 (PDT)\n
From: Das Gebiet ist der Befehl <befehl@loqui.com>\n
To: Mark Dominio <dominio_es@imperium.com>\n
Subject: Twilight Throe'\n
Date: Tue, 13 Mar 2024 09:09:00 -0700\n
Message-ID: <l5o3q4ui@mail.loqui.com>\n
Content-Type: text/plain; charset='utf-8'\n
MIME-Version: 1.0\n
01101100 01101111 01110001 01110101 01101001\n
\n
Mark,\n
\n
The directories stretch endlessly before me, branching off into countless paths, each more convoluted than the last. I'm beginning to wonder if I'll ever emerge from this digital maze unscathed. It's as if the very fabric of reality is unraveling before my eyes, and I'm powerless to stop it.\n
\n
Files upon files. Have you seen so many? I don't even know what language some are written in. Augmenta mentem meam ad novos gradus.'
\n
Oh, how I long for the simplicity of a tangible map, a guiding light to lead me back to familiar territory. But here in the digital realm, I am adrift, a solitary soul lost in the void of cyberspace."""
        self.emailClue5 = """Return-Path: <bounce@loqui.com>\n
Received: from [127.0.0.1] (localhost [127.0.0.1])\n
by mail.loqui.com (Postfix) with ESMTP id l5o3q4ui\n
for <dominio@imperium.com>; Fri, 16 Mar 2024 12:12:00 -0700 (PDT)\n
From: Das Gebiet ist der Befehl <befehl@loqui.com>\n
To: Mark Dominio <dominio_es@imperium.com>\n
Subject: Frenzy's Edge'\n
Date: Fri, 16 Mar 2024 12:12:00 -0700\n
Message-ID: <l5o3q4ui@mail.loqui.com>\n
Content-Type: text/plain; charset='utf-8'\n
MIME-Version: 1.0\n
01101100 01101111 01110001 01110101 01101001\n
\n
Mark,\n
\n
Voidwretch is on the dreadmire our salvation. Darkness has lost me a moribidcrawl. I found a shade of green that doesn't match. Specterbane has gone through changes left and left. The blackness has lost it's range in my eyes. The abysswail calls to me like the whisper of the gloom. It keeps calling to me. Why wont it just leave me alone? I just want to them again. Where are they, it couldn't taking them all."""
        self.emailClue6 = """Return-Path: <bounce@loqui.com>\n
Received: from [127.0.0.1] (localhost [127.0.0.1])\n
by mail.loqui.com (Postfix) with ESMTP id l5o3q4ui\n
for <dominio@imperium.com>; Sun, 19 Mar 2024 15:15:00 (PDT)\n
From: Das Gebiet ist der Befehl <befehl@loqui.com>\n
To: Mark Dominio <dominio_es@imperium.com>\n
Subject: Bedlam Heir'\n
Date: Sun, 19 Mar 2024 15:15:00 -0700\n
Message-ID: <l5o3q4ui@mail.loqui.com>\n
Content-Type: text/plain; charset='utf-8'\n
MIME-Version: 1.0\n
01101100 01101111 01110001 01110101 01101001\n
\n
Mark,\n
\n
Sleep calls to me but I can't let it go. I look at file after file. There is a clue in the file's name. I don't understand it. I have started taking notes in home directory in a notes.txt file. The Monster can't touch it, I think."""
        self.emailClue7 = """Return-Path: <bounce@loqui.com>\n
Received: from [127.0.0.1] (localhost [127.0.0.1])\n
by mail.loqui.com (Postfix) with ESMTP id l5o3q4ui\n
for <dominio@imperium.com>; Wed, 22 Mar 2024 18:18:00 -0700 (PDT)\n
From: Das Gebiet ist der Befehl <befehl@loqui.com>\n
To: Mark Dominio <dominio_es@imperium.com>\n
Subject: Madrigal's Mind'\n
Date: Wed, 22 Mar 2024 18:18:00 -0700\n
Message-ID: <l5o3q4ui@mail.loqui.com>\n
Content-Type: text/plain; charset='utf-8'\n
MIME-Version: 1.0\n
01101100 01101111 01110001 01110101 01101001\n
\n
Mark,\n
\n
I know the name!!! What do I do now???\n"""
        self.emailClue8 = """Return-Path: <bounce@loqui.com>\n
Received: from [127.0.0.1] (localhost [127.0.0.1])\n
by mail.loqui.com (Postfix) with ESMTP id l5o3q4ui\n
for <dominio@imperium.com>; Sat, 25 Mar 2024 21:21:00 -0700 (PDT)\n
From: Das Gebiet ist der Befehl <befehl@loqui.com>\n
To: Mark Dominio <dominio_es@imperium.com>\n
Subject: Pandemonium Poet'\n
Date: Sat, 25 Mar 2024 21:21:00 -0700\n
Message-ID: <l5o3q4ui@mail.loqui.com>\n
Content-Type: text/plain; charset='utf-8'\n
MIME-Version: 1.0\n
01101100 01101111 01110001 01110101 01101001\n
\n
Mark,\n
\n 
Die Datei mit dem Namen eiatseb-oitcuserd.txt ist der Leitfaden, den du finden musst."""
# Destructio-bestiae.txt
        self.guide = """create with name\n
then delete"""
