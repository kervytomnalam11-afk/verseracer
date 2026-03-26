"""
VerseRacer - Verse Data
Made by KERVY NALAM
"""

import random
import time

VERSES = {
    "bible": [
        # ── Existing Bible verses ─────────────────────────────────────────────
        ("John 3:16",           "For God so loved the world that he gave his one and only Son"),
        ("Psalm 23:1",          "The Lord is my shepherd I shall not want"),
        ("Philippians 4:13",    "I can do all things through Christ who strengthens me"),
        ("Proverbs 3:5",        "Trust in the Lord with all your heart and lean not on your own understanding"),
        ("Joshua 1:9",          "Be strong and courageous do not be afraid for the Lord your God is with you"),
        ("Nehemiah 8:10",       "The joy of the Lord is your strength"),
        ("Hebrews 11:1",        "Faith is the substance of things hoped for the evidence of things not seen"),
        ("1 Corinthians 13:4",  "Love is patient love is kind it does not envy it does not boast"),
        ("Jeremiah 29:11",      "For I know the plans I have for you declares the Lord plans to prosper you"),
        ("Psalm 27:1",          "The Lord is my light and my salvation whom shall I fear"),
        ("Psalm 46:10",         "Be still and know that I am God"),
        ("Ecclesiastes 3:11",   "He has made everything beautiful in its time"),
        ("Matthew 11:28",       "Come to me all you who are weary and burdened and I will give you rest"),
        ("Philippians 4:6",     "Do not be anxious about anything but in every situation by prayer and petition present your requests to God"),
        ("Romans 8:28",         "And we know that in all things God works for the good of those who love him"),
        ("Isaiah 40:8",         "The grass withers and the flowers fall but the word of our God endures forever"),
        ("Isaiah 40:31",        "But those who hope in the Lord will renew their strength they will soar on wings like eagles"),
        ("Psalm 51:10",         "Create in me a pure heart O God and renew a steadfast spirit within me"),
        ("Matthew 5:9",         "Blessed are the peacemakers for they will be called children of God"),
        ("Psalm 119:105",       "Your word is a lamp for my feet a light on my path"),
        ("Matthew 6:21",        "For where your treasure is there your heart will be also"),
        ("Psalm 19:1",          "The heavens declare the glory of God the skies proclaim the work of his hands"),
        ("Psalm 147:3",         "He heals the brokenhearted and binds up their wounds"),
        ("Psalm 37:4",          "Delight yourself in the Lord and he will give you the desires of your heart"),
        ("Psalm 46:1",          "God is our refuge and strength an ever present help in trouble"),
        ("2 Timothy 4:7",       "I have fought the good fight I have finished the race I have kept the faith"),
        ("John 15:13",          "Greater love has no one than this to lay down ones life for ones friends"),
        ("Romans 8:31",         "If God is for us who can be against us"),
        ("Psalm 150:6",         "Let everything that has breath praise the Lord"),
        ("Proverbs 9:10",       "The fear of the Lord is the beginning of wisdom"),
        ("Proverbs 27:17",      "As iron sharpens iron so one person sharpens another"),
        ("Matthew 6:33",        "Seek first his kingdom and his righteousness and all these things will be given to you"),
        ("Ephesians 2:8",       "For it is by grace you have been saved through faith and this is not from yourselves it is the gift of God"),
        ("Luke 6:31",           "Do unto others as you would have them do unto you"),

        # ── Genesis ───────────────────────────────────────────────────────────
        # Chapter 1 — Creation
        ("Genesis 1:1",   "In the beginning God created the heavens and the earth"),
        ("Genesis 1:2",   "Now the earth was formless and empty darkness was over the surface of the deep and the Spirit of God was hovering over the waters"),
        ("Genesis 1:3",   "And God said let there be light and there was light"),
        ("Genesis 1:4",   "God saw that the light was good and he separated the light from the darkness"),
        ("Genesis 1:5",   "God called the light day and the darkness he called night and there was evening and there was morning the first day"),
        ("Genesis 1:10",  "God called the dry ground land and the gathered waters he called seas and God saw that it was good"),
        ("Genesis 1:11",  "Then God said let the land produce vegetation seed-bearing plants and trees on the land that bear fruit with seed in it"),
        ("Genesis 1:14",  "And God said let there be lights in the vault of the sky to separate the day from the night"),
        ("Genesis 1:21",  "So God created the great creatures of the sea and every living thing with which the water teems and every winged bird"),
        ("Genesis 1:26",  "Then God said let us make mankind in our image in our likeness so that they may rule over the fish in the sea and the birds in the sky"),
        ("Genesis 1:27",  "So God created mankind in his own image in the image of God he created them male and female he created them"),
        ("Genesis 1:28",  "God blessed them and said to them be fruitful and increase in number fill the earth and subdue it"),
        ("Genesis 1:31",  "God saw all that he had made and it was very good and there was evening and there was morning the sixth day"),

        # Chapter 2 — Garden of Eden
        ("Genesis 2:1",   "Thus the heavens and the earth were completed in all their vast array"),
        ("Genesis 2:2",   "By the seventh day God had finished the work he had been doing so on the seventh day he rested from all his work"),
        ("Genesis 2:3",   "Then God blessed the seventh day and made it holy because on it he rested from all the work of creating that he had done"),
        ("Genesis 2:7",   "Then the Lord God formed a man from the dust of the ground and breathed into his nostrils the breath of life and the man became a living being"),
        ("Genesis 2:9",   "The Lord God made all kinds of trees grow out of the ground trees that were pleasing to the eye and good for food"),
        ("Genesis 2:15",  "The Lord God took the man and put him in the Garden of Eden to work it and take care of it"),
        ("Genesis 2:18",  "The Lord God said it is not good for the man to be alone I will make a helper suitable for him"),
        ("Genesis 2:22",  "Then the Lord God made a woman from the rib he had taken out of the man and he brought her to the man"),
        ("Genesis 2:24",  "That is why a man leaves his father and mother and is united to his wife and they become one flesh"),

        # Chapter 3 — The Fall
        ("Genesis 3:5",   "For God knows that when you eat from it your eyes will be opened and you will be like God knowing good and evil"),
        ("Genesis 3:8",   "Then the man and his wife heard the sound of the Lord God as he was walking in the garden in the cool of the day"),
        ("Genesis 3:15",  "And I will put enmity between you and the woman and between your offspring and hers he will crush your head and you will strike his heel"),
        ("Genesis 3:19",  "By the sweat of your brow you will eat your food until you return to the ground since from it you were taken for dust you are and to dust you will return"),

        # Chapter 4 — Cain and Abel
        ("Genesis 4:7",   "If you do what is right will you not be accepted but if you do not do what is right sin is crouching at your door it desires to have you but you must rule over it"),
        ("Genesis 4:9",   "Then the Lord said to Cain where is your brother Abel I do not know he replied am I my brothers keeper"),

        # Chapter 5 — Genealogy
        ("Genesis 5:24",  "Enoch walked faithfully with God then he was no more because God took him away"),

        # Chapter 6 — Noah
        ("Genesis 6:5",   "The Lord saw how great the wickedness of the human race had become on the earth and that every inclination of the thoughts of the human heart was only evil all the time"),
        ("Genesis 6:8",   "But Noah found favor in the eyes of the Lord"),
        ("Genesis 6:9",   "Noah was a righteous man blameless among the people of his time and he walked faithfully with God"),
        ("Genesis 6:22",  "Noah did everything just as God commanded him"),

        # Chapter 7 — The Flood
        ("Genesis 7:1",   "The Lord then said to Noah go into the ark you and your whole family because I have found you righteous in this generation"),
        ("Genesis 7:5",   "And Noah did all that the Lord commanded him"),

        # Chapter 8 — After the Flood
        ("Genesis 8:1",   "But God remembered Noah and all the wild animals and the livestock that were with him in the ark and he sent a wind over the earth and the waters receded"),
        ("Genesis 8:20",  "Then Noah built an altar to the Lord and taking some of all the clean animals and clean birds he sacrificed burnt offerings on it"),
        ("Genesis 8:22",  "As long as the earth endures seedtime and harvest cold and heat summer and winter day and night will never cease"),

        # Chapter 9 — The Covenant with Noah
        ("Genesis 9:1",   "Then God blessed Noah and his sons saying to them be fruitful and increase in number and fill the earth"),
        ("Genesis 9:11",  "I establish my covenant with you never again will all life be destroyed by the waters of a flood"),
        ("Genesis 9:13",  "I have set my rainbow in the clouds and it will be the sign of the covenant between me and the earth"),
        ("Genesis 9:16",  "Whenever the rainbow appears in the clouds I will see it and remember the everlasting covenant between God and all living creatures of every kind on the earth"),

        # Chapter 10-11 — Tower of Babel
        ("Genesis 11:1",  "Now the whole world had one language and a common speech"),
        ("Genesis 11:4",  "Then they said come let us build ourselves a city with a tower that reaches to the heavens so that we may make a name for ourselves"),
        ("Genesis 11:7",  "Come let us go down and confuse their language so they will not understand each other"),
        ("Genesis 11:9",  "That is why it was called Babel because there the Lord confused the language of the whole world"),

        # Chapter 12 — The Call of Abram
        ("Genesis 12:1",  "The Lord had said to Abram go from your country your people and your fathers household to the land I will show you"),
        ("Genesis 12:2",  "I will make you into a great nation and I will bless you I will make your name great and you will be a blessing"),
        ("Genesis 12:3",  "I will bless those who bless you and whoever curses you I will curse and all peoples on earth will be blessed through you"),
        ("Genesis 12:4",  "So Abram went as the Lord had told him and Lot went with him Abram was seventy-five years old when he set out from Harran"),

        # Chapter 13
        ("Genesis 13:14", "The Lord said to Abram after Lot had parted from him look around from where you are to the north and south to the east and west"),
        ("Genesis 13:15", "All the land that you see I will give to you and your offspring forever"),

        # Chapter 14
        ("Genesis 14:20", "And praise be to God Most High who delivered your enemies into your hand and Abram gave him a tenth of everything"),

        # Chapter 15 — Covenant with Abram
        ("Genesis 15:1",  "After this the word of the Lord came to Abram in a vision do not be afraid Abram I am your shield your very great reward"),
        ("Genesis 15:5",  "He took him outside and said look up at the sky and count the stars if indeed you can count them then he said so shall your offspring be"),
        ("Genesis 15:6",  "Abram believed the Lord and he credited it to him as righteousness"),

        # Chapter 16
        ("Genesis 16:13", "She gave this name to the Lord who spoke to her you are the God who sees me for she said I have now seen the One who sees me"),

        # Chapter 17 — Covenant of Circumcision
        ("Genesis 17:1",  "When Abram was ninety-nine years old the Lord appeared to him and said I am God Almighty walk before me faithfully and be blameless"),
        ("Genesis 17:7",  "I will establish my covenant as an everlasting covenant between me and you and your descendants after you"),

        # Chapter 18
        ("Genesis 18:14", "Is anything too hard for the Lord I will return to you at the appointed time next year and Sarah will have a son"),

        # Chapter 21 — Isaac is Born
        ("Genesis 21:1",  "Now the Lord was gracious to Sarah as he had said and the Lord did for Sarah what he had promised"),
        ("Genesis 21:6",  "Sarah said God has brought me laughter and everyone who hears about this will laugh with me"),

        # Chapter 22 — The Binding of Isaac
        ("Genesis 22:1",  "Some time later God tested Abraham he said to him Abraham and Abraham replied here I am"),
        ("Genesis 22:8",  "Abraham answered God himself will provide the lamb for the burnt offering my son and the two of them went on together"),
        ("Genesis 22:12", "Do not lay a hand on the boy he said do not do anything to him now I know that you fear God because you have not withheld from me your son your only son"),
        ("Genesis 22:14", "So Abraham called that place The Lord Will Provide and to this day it is said on the mountain of the Lord it will be provided"),
        ("Genesis 22:18", "And through your offspring all nations on earth will be blessed because you have obeyed me"),

        # Chapter 24
        ("Genesis 24:7",  "The Lord the God of heaven who brought me out of my fathers household and my native land will send his angel before you"),

        # Chapter 25
        ("Genesis 25:23", "The Lord said to her two nations are in your womb and two peoples from within you will be separated one people will be stronger than the other and the older will serve the younger"),

        # Chapter 26
        ("Genesis 26:24", "That night the Lord appeared to him and said I am the God of your father Abraham do not be afraid for I am with you"),
        ("Genesis 26:28", "We saw clearly that the Lord was with you so we said there ought to be a sworn agreement between us"),

        # Chapter 28 — Jacobs Ladder
        ("Genesis 28:12", "He had a dream in which he saw a stairway resting on the earth with its top reaching to heaven and the angels of God were ascending and descending on it"),
        ("Genesis 28:15", "I am with you and will watch over you wherever you go and I will bring you back to this land I will not leave you until I have done what I have promised you"),
        ("Genesis 28:16", "When Jacob awoke from his sleep he thought surely the Lord is in this place and I was not aware of it"),
        ("Genesis 28:17", "He was afraid and said how awesome is this place this is none other than the house of God this is the gate of heaven"),

        # Chapter 29
        ("Genesis 29:20", "So Jacob served seven years to get Rachel but they seemed like only a few days to him because of his love for her"),

        # Chapter 32 — Jacob Wrestles with God
        ("Genesis 32:28", "Then the man said your name will no longer be Jacob but Israel because you have struggled with God and with humans and have overcome"),
        ("Genesis 32:30", "So Jacob called the place Peniel saying it is because I saw God face to face and yet my life was spared"),

        # Chapter 37 — Joseph
        ("Genesis 37:3",  "Now Israel loved Joseph more than any of his other sons because he had been born to him in his old age and he made an ornate robe for him"),
        ("Genesis 37:19", "Here comes that dreamer they said to each other come now lets kill him and throw him into one of these cisterns"),
        ("Genesis 37:28", "So when the Midianite merchants came by his brothers pulled Joseph up out of the cistern and sold him for twenty shekels of silver to the Ishmaelites who took him to Egypt"),

        # Chapter 39 — Joseph in Egypt
        ("Genesis 39:2",  "The Lord was with Joseph so that he prospered and he lived in the house of his Egyptian master"),
        ("Genesis 39:9",  "How then could I do such a wicked thing and sin against God"),
        ("Genesis 39:21", "But while Joseph was there in the prison the Lord was with him he showed him kindness and granted him favor in the eyes of the prison warden"),
        ("Genesis 39:23", "The warden paid no attention to anything under Josephs care because the Lord was with Joseph and gave him success in whatever he did"),

        # Chapter 40
        ("Genesis 40:8",  "Do not interpretations belong to God tell me your dreams"),

        # Chapter 41 — Pharaohs Dream
        ("Genesis 41:16", "I cannot do it Joseph replied to Pharaoh but God will give Pharaoh the answer he desires"),
        ("Genesis 41:38", "So Pharaoh asked them can we find anyone like this man one in whom is the spirit of God"),

        # Chapter 45 — Joseph Reveals Himself
        ("Genesis 45:5",  "And now do not be distressed and do not be angry with yourselves for selling me here because it was to save lives that God sent me ahead of you"),
        ("Genesis 45:7",  "But God sent me ahead of you to preserve for you a remnant on earth and to save your lives by a great deliverance"),
        ("Genesis 45:8",  "So then it was not you who sent me here but God he made me father to Pharaoh lord of his entire household and ruler of all Egypt"),

        # Chapter 46
        ("Genesis 46:3",  "I am God the God of your father he said do not be afraid to go down to Egypt for I will make you into a great nation there"),
        ("Genesis 46:4",  "I will go down to Egypt with you and I will surely bring you back again and Josephs own hand will close your eyes"),

        # Chapter 50 — Joseph Forgives His Brothers
        ("Genesis 50:20", "You intended to harm me but God intended it for good to accomplish what is now being done the saving of many lives"),
        ("Genesis 50:24", "Then Joseph said to his brothers I am about to die but God will surely come to your aid and take you up out of this land to the land he promised on oath to Abraham Isaac and Jacob"),
    ],
}

HARD_VERSES = [
    "Though I walk through the valley of the shadow of death I will fear no evil for you are with me your rod and your staff they comfort me",
    "We hold these truths to be self evident that all men are created equal that they are endowed by their Creator with certain unalienable Rights",
    "To be or not to be that is the question whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune",
    "In the beginning God created the heavens and the earth and the earth was without form and void and darkness was upon the face of the deep",
    "I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character",
    "Fourscore and seven years ago our fathers brought forth on this continent a new nation conceived in liberty and dedicated to the proposition that all men are created equal",
    "The Lord bless you and keep you the Lord make his face shine on you and be gracious to you the Lord turn his face toward you and give you peace",
    "And now do not be distressed and do not be angry with yourselves for selling me here because it was to save lives that God sent me ahead of you to preserve for you a remnant on earth",
    "By the seventh day God had finished the work he had been doing so on the seventh day he rested from all his work and he blessed the seventh day and made it holy",
    "He had a dream in which he saw a stairway resting on the earth with its top reaching to heaven and the angels of God were ascending and descending on it",
    "Then God blessed Noah and his sons saying to them be fruitful and increase in number and fill the earth and I will establish my covenant with you never again will all life be destroyed by the waters of a flood",
    "Now the Lord was gracious to Sarah as he had said and the Lord did for Sarah what he had promised so Sarah became pregnant and bore a son to Abraham in his old age",
    "Do not lay a hand on the boy he said do not do anything to him now I know that you fear God because you have not withheld from me your son your only son",
    "You intended to harm me but God intended it for good to accomplish what is now being done the saving of many lives and I will provide for you and your children",
    "The Lord said to Abram after Lot had parted from him look around from where you are to the north and south to the east and west all the land that you see I will give to you and your offspring forever",
]

# Seed with time to ensure different results each run
_rng = random.Random()

def _reseed():
    _rng.seed(time.time() * 1000 + id(_rng))

def _all_texts():
    """Return flat list of just the verse text strings (no references)."""
    return [text for ref, text in VERSES["bible"]]

# Reference lookup: text → reference string
_BIBLE_REF = {text: ref for ref, text in VERSES["bible"]}

def get_reference(verse_text):
    """Return the bible reference for a verse, or empty string if not found."""
    return _BIBLE_REF.get(verse_text, "")

def get_verses(mode="classic", count=5):
    _reseed()
    if mode == "hard":
        pool = list(HARD_VERSES)
        _rng.shuffle(pool)
        return pool[:min(count, len(pool))]
    pool = list(_all_texts())
    _rng.shuffle(pool)
    return pool[:min(count, len(pool))]

def get_random_verse():
    _reseed()
    return _rng.choice(_all_texts())

def get_hard_verse():
    _reseed()
    return _rng.choice(HARD_VERSES)
