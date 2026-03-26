"""
VerseRacer - Verse Data (100+ verses, always randomized)
Made by KERVY NALAM
"""

import random
import time

VERSES = {
    "bible": [
        "For God so loved the world that he gave his one and only Son",
        "The Lord is my shepherd I shall not want",
        "I can do all things through Christ who strengthens me",
        "Trust in the Lord with all your heart and lean not on your own understanding",
        "Be strong and courageous do not be afraid for the Lord your God is with you",
        "The joy of the Lord is your strength",
        "Faith is the substance of things hoped for the evidence of things not seen",
        "Love is patient love is kind it does not envy it does not boast",
        "In the beginning God created the heavens and the earth",
        "For I know the plans I have for you declares the Lord plans to prosper you",
        "The Lord is my light and my salvation whom shall I fear",
        "Be still and know that I am God",
        "He has made everything beautiful in its time",
        "Come to me all you who are weary and burdened and I will give you rest",
        "Do not be anxious about anything but in every situation by prayer and petition present your requests to God",
        "And we know that in all things God works for the good of those who love him",
        "The grass withers and the flowers fall but the word of our God endures forever",
        "But those who hope in the Lord will renew their strength they will soar on wings like eagles",
        "Create in me a pure heart O God and renew a steadfast spirit within me",
        "Blessed are the peacemakers for they will be called children of God",
        "Your word is a lamp for my feet a light on my path",
        "For where your treasure is there your heart will be also",
        "The heavens declare the glory of God the skies proclaim the work of his hands",
        "He heals the brokenhearted and binds up their wounds",
        "Delight yourself in the Lord and he will give you the desires of your heart",
        "God is our refuge and strength an ever present help in trouble",
        "I have fought the good fight I have finished the race I have kept the faith",
        "Greater love has no one than this to lay down ones life for ones friends",
        "If God is for us who can be against us",
        "Let everything that has breath praise the Lord",
        "The fear of the Lord is the beginning of wisdom",
        "As iron sharpens iron so one person sharpens another",
        "Seek first his kingdom and his righteousness and all these things will be given to you",
        "For it is by grace you have been saved through faith and this is not from yourselves it is the gift of God",
        "Do unto others as you would have them do unto you",
    ],
    "poems": [
        "Two roads diverged in a wood and I took the one less traveled by",
        "Shall I compare thee to a summers day thou art more lovely and more temperate",
        "I wandered lonely as a cloud that floats on high over vales and hills",
        "Do not go gentle into that good night rage rage against the dying of the light",
        "Hope is the thing with feathers that perches in the soul",
        "Because I could not stop for death he kindly stopped for me",
        "The fog comes on little cat feet it sits looking over harbor and city",
        "Out of the night that covers me black as the pit from pole to pole",
        "If you can keep your head when all about you are losing theirs",
        "Once upon a midnight dreary while I pondered weak and weary",
        "I am the master of my fate I am the captain of my soul",
        "To see a world in a grain of sand and a heaven in a wild flower",
        "How do I love thee let me count the ways I love thee to the depth and breadth",
        "In Xanadu did Kubla Khan a stately pleasure dome decree",
        "Tyger tyger burning bright in the forests of the night",
        "The road not taken has made all the difference in my life",
        "She walks in beauty like the night of cloudless climes and starry skies",
        "It matters not how strait the gate how charged with punishments the scroll",
        "Water water everywhere and all the boards did shrink water water everywhere nor any drop to drink",
        "I took the one less traveled by and that has made all the difference",
        "Tell me not in mournful numbers life is but an empty dream",
        "There is a pleasure in the pathless woods there is a rapture on the lonely shore",
        "And miles to go before I sleep and miles to go before I sleep",
        "Not all those who wander are lost the old that is strong does not wither",
        "I celebrate myself and sing myself and what I assume you shall assume",
        "Half a league half a league half a league onward into the valley of death",
        "The best things in life are free but you can give them to the birds and bees",
        "A thing of beauty is a joy forever its loveliness increases it will never pass into nothingness",
        "O Captain my Captain our fearful trip is done the ship has weathered every rack",
        "Alone alone all all alone alone on a wide wide sea",
    ],
    "songs": [
        "Is this the real life is this just fantasy caught in a landslide",
        "We will we will rock you singing we will we will rock you",
        "Just a small town girl living in a lonely world",
        "Hello from the other side I must have called a thousand times",
        "Imagine all the people living life in peace you may say Im a dreamer",
        "Every breath you take every move you make Ill be watching you",
        "We are the champions my friends and well keep on fighting till the end",
        "Let it be let it be let it be let it be whisper words of wisdom",
        "Here comes the sun and I say its all right",
        "What a wonderful world I see trees of green red roses too",
        "I will always love you I will always love you my darling",
        "Yesterday all my troubles seemed so far away now it looks as though they are here to stay",
        "Like a rolling stone how does it feel to be on your own",
        "Sweet child of mine she has got eyes of the bluest skies",
        "Stairway to heaven when she gets there she knows all that glitters is gold",
        "Hotel California such a lovely place such a lovely face",
        "Bohemian like you because you look so fine and I really want to make you mine",
        "Another one bites the dust and another one gone and another one gone",
        "Take me home country roads to the place I belong West Virginia",
        "I got a feeling that tonights gonna be a good night",
        "Dont stop believing hold on to that feeling streetlight people",
        "You may say Im a dreamer but Im not the only one",
        "Hey Jude dont make it bad take a sad song and make it better",
        "Living on a prayer woah were halfway there take my hand well make it I swear",
        "Under pressure pushing down on me pressing down on you no man ask for",
        "I see a red door and I want it painted black no colors anymore I want them to turn black",
        "Shake it off shake it off the haters gonna hate hate hate",
        "Somebody that I used to know but you didnt have to cut me off",
        "We found love in a hopeless place we found love in a hopeless place",
        "Cant help falling in love with you take my hand take my whole life too",
        "Dancing queen young and sweet only seventeen feeling the beat",
        "Thriller night cause this is thriller thriller night and no one is gonna save you",
        "Africa I bless the rains down in Africa gonna take some time to do the things we never had",
        "Piano man sing us a song tonight cause were all in the mood for a melody",
        "Smells like teen spirit here we are now entertain us",
    ],
}

HARD_VERSES = [
    "Though I walk through the valley of the shadow of death I will fear no evil for you are with me your rod and your staff they comfort me",
    "Shall I compare thee to a summers day thou art more lovely and more temperate rough winds do shake the darling buds of May and summers lease hath all too short a date",
    "It was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness it was the epoch of belief it was the epoch of incredulity",
    "We hold these truths to be self evident that all men are created equal that they are endowed by their Creator with certain unalienable Rights",
    "To be or not to be that is the question whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune",
    "In the beginning God created the heavens and the earth and the earth was without form and void and darkness was upon the face of the deep",
    "I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character",
    "All that is gold does not glitter not all those who wander are lost the old that is strong does not wither deep roots are not reached by the frost",
    "The only thing we have to fear is fear itself nameless unreasoning unjustified terror which paralyzes needed efforts to convert retreat into advance",
    "Ask not what your country can do for you ask what you can do for your country and together we shall build a brighter tomorrow for all",
    "It is not the critic who counts not the man who points out how the strong man stumbles or where the doer of deeds could have done them better",
    "Fourscore and seven years ago our fathers brought forth on this continent a new nation conceived in liberty and dedicated to the proposition that all men are created equal",
    "The Lord bless you and keep you the Lord make his face shine on you and be gracious to you the Lord turn his face toward you and give you peace",
    "Whether you think you can or you think you cannot you are right the mind is everything what you think you become so think wisely and act boldly",
    "Two things are infinite the universe and human stupidity and I am not sure about the universe but I am quite certain about the stupidity",
]

# Seed with time to ensure different results each run
_rng = random.Random()

def _reseed():
    _rng.seed(time.time() * 1000 + id(_rng))

def get_verses(mode="classic", count=5):
    _reseed()
    if mode == "hard":
        pool = list(HARD_VERSES)
        _rng.shuffle(pool)
        return pool[:min(count, len(pool))]
    all_verses = VERSES["bible"] + VERSES["poems"] + VERSES["songs"]
    pool = list(all_verses)
    _rng.shuffle(pool)
    return pool[:min(count, len(pool))]

def get_random_verse():
    _reseed()
    all_verses = VERSES["bible"] + VERSES["poems"] + VERSES["songs"]
    return _rng.choice(all_verses)

def get_hard_verse():
    _reseed()
    return _rng.choice(HARD_VERSES)
