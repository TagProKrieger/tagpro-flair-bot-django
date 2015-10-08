# -*- coding: utf-8 -*-
FLAIR_DATA = [
    ("Developer", "TagPro Developer", "-32px -16px"),
    ("Contributor", "Community Contributor", "0px -16px"),
    ("Moderator", "Moderator", "-96px 0px"),
    ("Donor", "Level 1 Donor ($10)", "-16px -16px"),
    ("Donor2", "Level 2 Donor ($40)", "-48px -16px"),
    ("Donor3", "Level 3 Donor ($100)", "-64px -16px"),
    ("Donor4", "Level 4 Donor ($200)", "-112px -16px"),
    ("Bitcoin", "Bitcoin Donor (Any Amount)", "-128px -16px"),
    ("Contest", "Community Contest Winner", "-80px -16px"),
    ("Monthly", "Monthly Leader Board Winner", "-32px 0px"),
    ("Weekly", "Weekly Leader Board Winner", "-16px 0px"),
    ("Daily", "Daily Leader Board Winner", "0px 0px"),
    ("75WinRate", "75% Public Game Win Rate", "-80px 0px"),
    ("65WinRate", "65% Public Game Win Rate", "-64px 0px"),
    ("55WinRate", "55% Public Game Win Rate", "-48px 0px"),
    ("Birthday", "Happy Birthday TagPro", "0px -32px"),
    ("Lucky", "Lucky You", "-16px -32px"),
    ("Fools", "How Foolish", "-32px -32px"),
    ("Easter", "Hare Today, Goon Tomorrow", "-48px -32px"),
    ("Unfortunate", "UnfortunateSniper Hacks TagPro", "-64px -32px"),
    ("Halloween", "So Very Scary", "-80px -32px"),
    ("Axe", "Daryl Would Be Proud", "-96px -32px"),
    ("Birthday2", "Happy 2nd Birthday TagPro", "-112px -32px"),
    ("Mario", "Tower 1-1 Complete", "-128px -32px"),
    ("Lucky2", "Good and Lucky", "-144px -32px"),
    ("Fools2", "Clowning Around Gravity", "-160px -32px"),
    ("Easter2", "Racing for Eggs", "0px -48px"),
    ("Easter3", "Racing For Carrots", "-16px -48px"),
    ("Lgbt", "All balls are created equal!", "-32px -48px"),
    ("Halloween2", "Easy as Pumpkin Pie", "-48px -48px"),
    ("Witch", "Lighter Than a Duck", "-64px -48px"),
    ("Bacon", "Bacon (6&#176;)", "0px -80px"),
    ("Moon", "Moon (11&#176;)", "-16px -80px"),
    ("Penguin", "Penguin (17&#176;)", "-112px -96px"),
    ("Freezing", "Freezing (32&#176;)", "-32px -80px"),
    ("Dolphin", "Dolphin (42&#176;)", "-48px -80px"),
    ("Alien", "Alien (51&#176;)", "-64px -80px"),
    ("Route", "Road Sign (66&#176;)", "-80px -80px"),
    ("Peace", "Peace (69&#176;)", "-96px -80px"),
    ("Magma", "Magma (79&#176;)", "-128px -96px"),
    ("Flux", "Flux Capacitor (88&#176;)", "-112px -80px"),
    ("Microphone", "Microphone (98&#176;)", "-128px -80px"),
    ("Boiling", "Boiling (100&#176;)", "-144px -80px"),
    ("Dalmatians", "Dalmatians (101&#176;)", "0px -96px"),
    ("ABC", "ABC (123&#176;)", "-16px -96px"),
    ("Plane", "Plane (130&#176;)", "-144px -96px"),
    ("Love", "Love (143&#176;)", "-32px -96px"),
    ("Pokemon", "Pokemon (151&#176;)", "-48px -96px"),
    ("Phi", "Phi (162&#176;)", "-64px -96px"),
    ("UTurn", "U Turn (180&#176;)", "-80px -96px"),
    ("World", "World (196&#176;)", "-96px -96px"),
    ("Boiling2", "Boiling 2 (212&#176;)", "-160px -80px"),
    ("Uranium", "Uranium (238&#176;)", "-160px -96px"),
    ("Boxing", "Boxing (276&#176;)", "-32px -112px"),
    ("Bowling", "Bowling (300&#176;)", "0px -112px"),
    ("Pi", "Pi (314&#176;)", "-16px -112px"),
]

FLAIR = dict((k, {'position': p, 'title': t}) for k, t, p in FLAIR_DATA)
FLAIR_BY_POSITION = dict((p, {'id': k, 'title': t}) for k, t, p in FLAIR_DATA)
