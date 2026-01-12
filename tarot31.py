cardList = ["fool", "magician", "high priestess", "empress", "emprror", "hierophant", "lovers", "chariot", "strength", "hermit", "wheel of fortune", "justice", "hanged man", "death", "temperance", "devil", "tower", "star", "moon", "sun", "judgement", "world"]

cardDict = {
    "fool" : "being inexperienced, being carefree",
    "magician" : "ability to communicate clearly and to be innovative",
    "high priestess" : "secrets, mystery, intuition, wisdom, and magic",
    "empress" : "family oriented person, love of the home and family",
    "emperor" : "masculin energy, head of community, solid foundstion to build",
    "hierophant" : "group religion, ceremony, tradition, giving spiritual guidance",
    "lovers" : "love and relationship, being with soulmates",
    "chariot" : "will power and determination, victory, take control in area of attention",
    "strength" : "courage, strength, self-confidence, build self-worth",
    "hermit" : "spending time alone, soul-searching",
    "wheel of fortune" : "what is meant to be is meant to be",
    "justice" : "cause and effect, to be fair to achieve the best redult",
    "hanged man" : "temporarily suspended, life is on hold but serves a purpose",
    "death" : "transformation, things will not be the same wgain",
    "temperance" : "great balance and strength between different areas",
    "devil" : "form of our desires and earthly needs",
    "tower" : "disaster, anger issues. sudden change",
    "star" : "hope, a bright future, joy, optimism, get answer of question",
    "moon" : "illusions, fantasies  fears, and anxiety",
    "sun" : "life is simple rather than complicated",
    "judgement" : "seeing the truth and knowing what you want",
    "world" : "your life lessons have mare you smart and accomplished"
}

import random

cardindex = random.randrange(1,len(cardList)) - 1

openedcard = cardList[cardindex]

print(openedcard)

print(cardDict[openedcard])