# -*- coding: utf-8 -*-
import json

def get_set_8():
    return {
        "setId": 8,
        "setName": "Set 8: Karoo Nights & Cold Pints",
        "badge": "Set 8 • Karoo Legends",
        "theme": "Cricket Icons, Classic Sitcoms, Smoked Meats & Historic Battles",
        "rounds": [
            {
                "roundId": 1,
                "title": "Round 1: Clever Pints Trivia",
                "badge": "Round 1 • Easy",
                "theme": "Fast Answers, Bar Savvy & Everyday Trivia",
                "difficultyText": "Level 1: Table Warm-Up",
                "hostVibe": "Welcome everyone, top up the drinks, and let's get rolling!",
                "questions": [
                    {
                        "q": "What is the standard metric boiling point of water at sea level?",
                        "options": ["A) 90°C", "B) 95°C", "C) 100°C", "D) 105°C"],
                        "a": "C) 100°C",
                        "notes": "100°C (212°F) at standard atmospheric pressure."
                    },
                    {
                        "q": "In a deck of cards, how many Queens are there in total?",
                        "options": ["A) 2", "B) 4", "C) 6", "D) 8"],
                        "a": "B) 4",
                        "notes": "One Queen in each of Hearts, Diamonds, Clubs, and Spades."
                    },
                    {
                        "q": "What color jersey is awarded to the overall leader of the Tour de France cycling race?",
                        "options": ["A) Green Jersey", "B) Polka Dot Jersey", "C) Yellow Jersey (Maillot Jaune)", "D) White Jersey"],
                        "a": "C) Yellow Jersey (Maillot Jaune)",
                        "notes": "The iconic yellow jersey worn by the general classification leader."
                    },
                    {
                        "q": "What popular South African non-alcoholic malt beverage is brewed with barley and hops and marketed as an energy restorer?",
                        "options": ["A) Malta Guiness", "B) Castle Free", "C) Hansa", "D) Supermalt"],
                        "a": "B) Castle Free",
                        "notes": "South Africa's first homegrown 0.0% alcohol beer."
                    },
                    {
                        "q": "What is the capital city of the Netherlands, famous for its canals and bicycles?",
                        "options": ["A) Rotterdam", "B) The Hague", "C) Amsterdam", "D) Utrecht"],
                        "a": "C) Amsterdam",
                        "notes": "Amsterdam is the constitutional capital, while The Hague houses government."
                    },
                    {
                        "q": "How many players are on the ice for one team at full strength in an ice hockey game?",
                        "options": ["A) 5 players", "B) 6 players", "C) 7 players", "D) 8 players"],
                        "a": "B) 6 players",
                        "notes": "5 skaters plus 1 goaltender."
                    },
                    {
                        "q": "Which gas do plants absorb from the air to perform photosynthesis?",
                        "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
                        "a": "B) Carbon Dioxide",
                        "notes": "Plants take in CO2 and release O2."
                    },
                    {
                        "q": "What is the name of the green-skinned, pear-shaped fruit whose flesh is the main ingredient in guacamole?",
                        "options": ["A) Kiwi", "B) Papaya", "C) Avocado", "D) Fig"],
                        "a": "C) Avocado",
                        "notes": "Avocados (avocado pear)."
                    },
                    {
                        "q": "In a standard game of chess, which piece can only move diagonally across the board?",
                        "options": ["A) Rook", "B) Knight", "C) Bishop", "D) Pawn"],
                        "a": "C) Bishop",
                        "notes": "Bishops move any number of squares diagonally on their starting color."
                    },
                    {
                        "q": "Which popular South African fast-food chain, founded in 1967, is famous for its Mega Rib Burger, thick milkshakes, and breakfast plates?",
                        "options": ["A) Wimpy", "B) Spur", "C) Steers", "D) Chicken Licken"],
                        "a": "A) Wimpy",
                        "notes": "Wimpy opened its first South African restaurant in Durban in 1967."
                    }
                ]
            },
            {
                "roundId": 2,
                "title": "Round 2: Proteas Cricket & Global Cricket Icons",
                "badge": "Round 2 • Cricket Mastermind",
                "theme": "Flying Run-Outs, 300+ Scores & Fast Bowling Kings",
                "difficultyText": "Level 2: The Sound of Leather on Willow",
                "hostVibe": "Cricket tragics, your moment has arrived.",
                "questions": [
                    {
                        "q": "In the 1992 Cricket World Cup in Australia, which South African fielder produced the most iconic flying run-out in history by diving headfirst into the stumps to dismiss Inzamam-ul-Haq?",
                        "options": ["A) Hansie Cronje", "B) Jonty Rhodes", "C) Kepler Wessels", "D) Andrew Hudson"],
                        "a": "B) Jonty Rhodes",
                        "notes": "8 March 1992 in Brisbane: Jonty was airborne horizontally when he shattered the stumps."
                    },
                    {
                        "q": "Who was the first South African batsman to score a triple century (311 not out) in Test cricket, achieving the feat at The Oval against England in 2012?",
                        "options": ["A) Jacques Kallis", "B) Graeme Smith", "C) Hashim Amla", "D) Gary Kirsten"],
                        "a": "C) Hashim Amla",
                        "notes": "Hashim Amla batted for over 13 hours to score 311*."
                    },
                    {
                        "q": "Which South African fast bowler was nicknamed 'White Lightning' for his terrifying 150 km/h bouncers in the 1990s?",
                        "options": ["A) Fanie de Villiers", "B) Allan Donald", "C) Brett Schultz", "D) Shaun Pollock"],
                        "a": "B) Allan Donald",
                        "notes": "Allan Donald took 330 Test wickets for South Africa."
                    },
                    {
                        "q": "In cricket, how many runs is a 'century'?",
                        "options": ["A) 50 runs", "B) 75 runs", "C) 100 runs", "D) 150 runs"],
                        "a": "C) 100 runs",
                        "notes": "A century is 100 runs."
                    },
                    {
                        "q": "Which legendary Australian leg-spinner took 708 Test wickets and bowled the 'Ball of the Century' to Mike Gatting in 1993?",
                        "options": ["A) Glenn McGrath", "B) Shane Warne", "C) Stuart MacGill", "D) Brett Lee"],
                        "a": "B) Shane Warne",
                        "notes": "Shane Warne: 'The King of Spin'."
                    },
                    {
                        "q": "Which cricket ground in Cape Town is famed for its lush grass embankments, oaks, and stunning backdrop of Devil's Peak and Table Mountain?",
                        "options": ["A) Newlands Cricket Ground", "B) Wanderers Stadium", "C) Kingsmead", "D) Willowmoore Park"],
                        "a": "A) Newlands Cricket Ground",
                        "notes": "Widely regarded as one of the most picturesque cricket venues in the world."
                    },
                    {
                        "q": "What is the maximum number of fielders permitted outside the 30-yard fielding circle during the first 10 overs of a men's ODI powerplay?",
                        "options": ["A) 2 fielders", "B) 3 fielders", "C) 4 fielders", "D) 5 fielders"],
                        "a": "A) 2 fielders",
                        "notes": "Only 2 fielders outside the circle during Powerplay 1 (overs 1-10)."
                    },
                    {
                        "q": "Which South African wicketkeeper-batsman captained the Mumbai Indians and held the record for most dismissals by a keeper in Test history (555 dismissals)?",
                        "options": ["A) Dave Richardson", "B) Mark Boucher", "C) Quinton de Kock", "D) AB de Villiers"],
                        "a": "B) Mark Boucher",
                        "notes": "Mark Boucher took 532 catches and 23 stumpings in 147 Tests."
                    },
                    {
                        "q": "What is the international biennial Test cricket series played between England and Australia called?",
                        "options": ["A) The Border-Gavaskar Trophy", "B) The Ashes", "C) The Wisden Trophy", "D) The Chappell-Hadlee Trophy"],
                        "a": "B) The Ashes",
                        "notes": "Contested for a tiny terracotta urn supposedly containing the ashes of a cricket bail."
                    },
                    {
                        "q": "Which South African left-handed opener batted through all five days of a test match and later coached India to the 2011 World Cup title?",
                        "options": ["A) Daryll Cullinan", "B) Gary Kirsten", "C) Herschelle Gibbs", "D) Boeta Dippenaar"],
                        "a": "B) Gary Kirsten",
                        "notes": "Gary Kirsten played 101 Tests and coached India to World Cup triumph."
                    }
                ]
            },
            {
                "roundId": 3,
                "title": "Round 3: Comedy Classics & Sitcoms",
                "badge": "Round 3 • Comedy Gold",
                "theme": "Fawlty Towers, The Office, Monty Python & Laugh Out Loud TV",
                "difficultyText": "Level 3: Comic Relief",
                "hostVibe": "Keep the humor flowing! Don't mention the war!",
                "questions": [
                    {
                        "q": "In the legendary British comedy Fawlty Towers, what was Basil Fawlty's strict instruction to staff regarding his visiting German guests?",
                        "options": ["A) Don't charge them for wine", "B) Don't mention the war!", "C) Always speak German", "D) Put towels on their chairs"],
                        "a": "B) Don't mention the war!",
                        "notes": "'Don't mention the war! I mentioned it once, but I think I got away with it!'"
                    },
                    {
                        "q": "In the American version of The Office, who is the eccentric, beet-farming Assistant to the Regional Manager?",
                        "options": ["A) Jim Halpert", "B) Dwight Schrute", "C) Andy Bernard", "D) Stanley Hudson"],
                        "a": "B) Dwight Schrute",
                        "notes": "Dwight Kurt Schrute III, owner of Schrute Farms B&B."
                    },
                    {
                        "q": "Which British comedy troupe created Monty Python and the Holy Grail and Life of Brian?",
                        "options": ["A) The Goons", "B) Monty Python", "C) The League of Gentlemen", "D) Beyond the Fringe"],
                        "a": "B) Monty Python",
                        "notes": "John Cleese, Michael Palin, Terry Jones, Eric Idle, Graham Chapman, and Terry Gilliam."
                    },
                    {
                        "q": "In the classic comedy sitcom Blackadder, what was Baldrick always famous for having?",
                        "options": ["A) A bag of gold", "B) A cunning plan", "C) A bottle of wine", "D) A lucky turnip"],
                        "a": "B) A cunning plan",
                        "notes": "'I have a cunning plan, my Lord!'"
                    },
                    {
                        "q": "What is the name of Homer Simpson's long-suffering wife with the towering blue beehive hair?",
                        "options": ["A) Lisa", "B) Marge", "C) Selma", "D) Patty"],
                        "a": "B) Marge",
                        "notes": "Marjorie 'Marge' Simpson (née Bouvier)."
                    },
                    {
                        "q": "Which British sitcom set in Peckham followed market trader Derek 'Del Boy' Trotter trying to become millionaires?",
                        "options": ["A) Porridge", "B) Steptoe and Son", "C) Only Fools and Horses", "D) Dad's Army"],
                        "a": "C) Only Fools and Horses",
                        "notes": "'This time next year, Rodney, we'll be millionaires!'"
                    },
                    {
                        "q": "In the 2004 comedy Anchorman, what musical instrument does Ron Burgundy play during his jazz club solo?",
                        "options": ["A) Saxophone", "B) Jazz Flute", "C) Trumpet", "D) Trombone"],
                        "a": "B) Jazz Flute",
                        "notes": "Ron Burgundy's fiery jazz flute solo."
                    },
                    {
                        "q": "Which South African stand-up comedian became the global host of The Daily Show in New York from 2015 to 2022?",
                        "options": ["A) Barry Hilton", "B) Casper de Vries", "C) Trevor Noah", "D) Marc Lottering"],
                        "a": "C) Trevor Noah",
                        "notes": "Trevor Noah hosted the acclaimed satirical news show on Comedy Central."
                    },
                    {
                        "q": "In the sitcom Friends, which character was notoriously married and divorced three times (Carol, Emily, Rachel)?",
                        "options": ["A) Joey Tribbiani", "B) Chandler Bing", "C) Ross Geller", "D) Gunther"],
                        "a": "C) Ross Geller",
                        "notes": "Ross Geller: 'The Divorce Force'."
                    },
                    {
                        "q": "Which South African comedian is affectionately known as 'The Cousin' with his famous stand-up routines about Nou Gaan Ons Braai?",
                        "options": ["A) Casper de Vries", "B) Barry Hilton", "C) Tolla van der Merwe", "D) Dowwe Dolla"],
                        "a": "B) Barry Hilton",
                        "notes": "Barry Hilton: iconic face of South African comedy for over 30 years."
                    }
                ]
            },
            {
                "roundId": 4,
                "title": "Round 4: Smoked Meats, Spices & Beers",
                "badge": "Round 4 • Pub Cask",
                "theme": "Stout, Cask Ales, Spices, Meat Curing & Cellar Secrets",
                "difficultyText": "Level 4: Master Taster",
                "hostVibe": "Rich aromas, dark beers, and braai smoke.",
                "questions": [
                    {
                        "q": "What inert gas is used alongside carbon dioxide to give draught Guinness stout its creamy head and smooth texture?",
                        "options": ["A) Helium", "B) Nitrogen", "C) Hydrogen", "D) Argon"],
                        "a": "B) Nitrogen",
                        "notes": "Nitrogen creates smaller, tighter bubbles for the famous cascading surge."
                    },
                    {
                        "q": "What type of vinegar is traditionally preferred when curing traditional South African biltong?",
                        "options": ["A) Brown spirit vinegar or malt vinegar", "B) Distilled white vinegar only", "C) Balsamic vinegar", "D) Rice wine vinegar"],
                        "a": "A) Brown spirit vinegar or malt vinegar",
                        "notes": "Brown vinegar or malt vinegar imparts mellow acidity without bleaching the meat."
                    },
                    {
                        "q": "What cut of lamb from the loin or rib is cut with the bone in and braaied hot and fast for tender perfection?",
                        "options": ["A) Lamb Shank", "B) Lamb Chops (Loin or Rib Chops)", "C) Lamb Neck", "D) Lamb Breast"],
                        "a": "B) Lamb Chops (Loin or Rib Chops)",
                        "notes": "Tjops on the braai: crisp up the fat strip first, then sear the meat."
                    },
                    {
                        "q": "What is the main aromatic flavoring component in classic London Dry Gin?",
                        "options": ["A) Juniper Berries", "B) Coriander", "C) Cardamom", "D) Nutmeg"],
                        "a": "A) Juniper Berries",
                        "notes": "By legal definition, gin must have a predominant flavor of juniper."
                    },
                    {
                        "q": "What spicy North African paste made from red chili peppers, garlic, and caraway is popular as a braai marinade?",
                        "options": ["A) Harissa", "B) Chimichurri", "C) Pesto", "D) Salsa verde"],
                        "a": "A) Harissa",
                        "notes": "Harissa originated in Tunisia."
                    },
                    {
                        "q": "What is the traditional name for the large clay beer pots used in Zulu culture to serve traditional umqombothi sorghum beer?",
                        "options": ["A) Potjie", "B) Ukhamba", "C) Assegai", "D) Calabash"],
                        "a": "B) Ukhamba",
                        "notes": "Ukhamba: spherical earthenware beer vessel shared among guests."
                    },
                    {
                        "q": "What classic South African dessert consists of small, fluffy dumplings poached in spiced cinnamon syrup?",
                        "options": ["A) Souskluitjies", "B) Malva Pudding", "C) Hertzoggies", "D) Koeksisters"],
                        "a": "A) Souskluitjies",
                        "notes": "Souskluitjies: warm cinnamon sugar dumpling comfort food."
                    },
                    {
                        "q": "What is the German term used for bottom-fermented beers that are stored and conditioned at cold temperatures for weeks?",
                        "options": ["A) Ale", "B) Lager", "C) Stout", "D) Lambic"],
                        "a": "B) Lager",
                        "notes": "'Lagern' means 'to store' in German."
                    },
                    {
                        "q": "Which South African wine estate in Constantia, founded by Simon van der Stel in 1685, produced sweet wines favored by Napoleon Bonaparte on St Helena?",
                        "options": ["A) Groot Constantia", "B) Klein Constantia", "C) Buitenverwachting", "D) Constantia Glen"],
                        "a": "A) Groot Constantia",
                        "notes": "Groot Constantia is South Africa's oldest wine-producing estate."
                    },
                    {
                        "q": "What South African biscuit is shaped like a small tartlet, filled with apricot jam, and topped with a baked coconut meringue cap?",
                        "options": ["A) Jan Smuts Koekie", "B) Hertzoggie", "C) Melktert", "D) Soetkoekie"],
                        "a": "B) Hertzoggie",
                        "notes": "Named in honor of Prime Minister J.B.M. Hertzog."
                    }
                ]
            },
            {
                "roundId": 5,
                "title": "Round 5: History & World Capitals",
                "badge": "Round 5 • Battlefields",
                "theme": "Historic Battles, Famous Forts & World Capitals",
                "difficultyText": "Level 5: Master Strategist",
                "hostVibe": "Final round before the decisive overtime or trophy reveal!",
                "questions": [
                    {
                        "q": "In which province was the historic 1879 Battle of Isandlwana and the defense of Rorke's Drift fought between the British Army and the Zulu Kingdom?",
                        "options": ["A) Free State", "B) KwaZulu-Natal", "C) Eastern Cape", "D) Mpumalanga"],
                        "a": "B) KwaZulu-Natal",
                        "notes": "In the rolling hills of Zululand, KwaZulu-Natal."
                    },
                    {
                        "q": "What is the capital city of Greece, considered the cradle of Western civilization and democracy?",
                        "options": ["A) Thessaloniki", "B) Sparta", "C) Athens", "D) Corinth"],
                        "a": "C) Athens",
                        "notes": "Athens, home of the Acropolis and Parthenon."
                    },
                    {
                        "q": "What is the oldest surviving colonial building in South Africa, constructed by the Dutch East India Company between 1666 and 1679 in Cape Town?",
                        "options": ["A) The Tuynhuys", "B) Castle of Good Hope", "C) Slave Lodge", "D) Groote Kerk"],
                        "a": "B) Castle of Good Hope",
                        "notes": "A five-pointed star fortress in the heart of Cape Town."
                    },
                    {
                        "q": "What is the capital city of Scotland?",
                        "options": ["A) Glasgow", "B) Edinburgh", "C) Aberdeen", "D) Dundee"],
                        "a": "B) Edinburgh",
                        "notes": "Edinburgh, dominated by Edinburgh Castle."
                    },
                    {
                        "q": "Which South African general and statesman served as Prime Minister, helped draft the UN Charter, and was a member of the British Imperial War Cabinet?",
                        "options": ["A) Louis Botha", "B) Jan Smuts", "C) J.B.M. Hertzog", "D) D.F. Malan"],
                        "a": "B) Jan Smuts",
                        "notes": "Jan Christian Smuts: philosopher, botanist, and military commander."
                    },
                    {
                        "q": "What is the longest artificial structure ever built by human civilization, stretching thousands of kilometers across northern China?",
                        "options": ["A) The Grand Canal", "B) The Great Wall of China", "C) The Silk Wall", "D) The Yellow River Dyke"],
                        "a": "B) The Great Wall of China",
                        "notes": "Over 21,000 km in total length including all branches."
                    },
                    {
                        "q": "What is the capital city of Switzerland?",
                        "options": ["A) Zurich", "B) Geneva", "C) Bern", "D) Basel"],
                        "a": "C) Bern",
                        "notes": "Bern acts as the de facto federal city (capital) of Switzerland."
                    },
                    {
                        "q": "Which famous French military leader was defeated at the Battle of Waterloo in 1815?",
                        "options": ["A) Louis XIV", "B) Napoleon Bonaparte", "C) Charles de Gaulle", "D) Cardinal Richelieu"],
                        "a": "B) Napoleon Bonaparte",
                        "notes": "Defeated by the Duke of Wellington and Field Marshal Blücher."
                    },
                    {
                        "q": "What river flows directly through the city of Paris, France?",
                        "options": ["A) Danube", "B) Rhine", "C) Seine", "D) Thames"],
                        "a": "C) Seine",
                        "notes": "The Seine River divides Paris into the Left Bank and Right Bank."
                    },
                    {
                        "q": "In which Free State town was the National Museum founded, famous for its Florisbad skull archaeological discovery?",
                        "options": ["A) Welkom", "B) Kroonstad", "C) Bloemfontein", "D) Bethlehem"],
                        "a": "C) Bloemfontein",
                        "notes": "The Florisbad skull was discovered in 1932 near Bloemfontein."
                    }
                ]
            },
            {
                "roundId": 6,
                "title": "Sudden-Death Tie-Breakers",
                "badge": "Overtime • Closest Number",
                "theme": "Closest to the Pin Estimations",
                "difficultyText": "Overtime: Closest Number Wins!",
                "hostVibe": "Captains, write down your estimate on paper!",
                "questions": [
                    {
                        "q": "In what calendar year did the historic Battle of Blood River take place in KwaZulu-Natal?",
                        "options": ["A) 1824", "B) 1838", "C) 1852", "D) 1879"],
                        "a": "B) 1838",
                        "notes": "16 December 1838."
                    },
                    {
                        "q": "How many total balls did Hashim Amla face when he scored his historic 311 not out at The Oval in 2012?",
                        "options": ["A) 412 balls", "B) 478 balls", "C) 529 balls", "D) 610 balls"],
                        "a": "C) 529 balls",
                        "notes": "Amla faced 529 balls across 790 minutes of batting."
                    },
                    {
                        "q": "In what calendar year did construction of the Castle of Good Hope in Cape Town begin?",
                        "options": ["A) 1652", "B) 1666", "C) 1679", "D) 1685"],
                        "a": "B) 1666",
                        "notes": "Started in 1666 and completed in 1679."
                    }
                ]
            }
        ]
    }

def get_set_9():
    return {
        "setId": 9,
        "setName": "Set 9: Vaal River Vibes",
        "badge": "Set 9 • Vaal Cruisers",
        "theme": "Marathons, Superhero Sagas, Shooters & Mighty Rivers",
        "rounds": [
            {
                "roundId": 1,
                "title": "Round 1: Taproom Trivia",
                "badge": "Round 1 • Easy",
                "theme": "Bar Counters, Board Games & Common Knowledge",
                "difficultyText": "Level 1: Fast Start",
                "hostVibe": "Get the pencils sharpened! Easy openers for all.",
                "questions": [
                    {
                        "q": "In South Africa, what is a 750ml glass bottle of beer commonly called in bar slang?",
                        "options": ["A) A dumpy", "B) A quart", "C) A pint", "D) A growler"],
                        "a": "B) A quart",
                        "notes": "A 750ml bottle is traditionally known as a 'quart' (or 'large')."
                    },
                    {
                        "q": "How many seconds are in five full minutes?",
                        "options": ["A) 250 seconds", "B) 300 seconds", "C) 350 seconds", "D) 400 seconds"],
                        "a": "B) 300 seconds",
                        "notes": "5 x 60 = 300 seconds."
                    },
                    {
                        "q": "What is the primary spirit used to make a classic Cuba Libre cocktail?",
                        "options": ["A) Vodka", "B) Rum", "C) Gin", "D) Bourbon"],
                        "a": "B) Rum",
                        "notes": "Rum, cola, and fresh lime juice."
                    },
                    {
                        "q": "Which bird is the national bird of South Africa?",
                        "options": ["A) Ostrich", "B) Blue Crane", "C) Secretary Bird", "D) Fish Eagle"],
                        "a": "B) Blue Crane",
                        "notes": "The elegant Blue Crane (Anthropoides paradiseus)."
                    },
                    {
                        "q": "How many players are on a standard basketball court for one team during play?",
                        "options": ["A) 4 players", "B) 5 players", "C) 6 players", "D) 7 players"],
                        "a": "B) 5 players",
                        "notes": "5 players per team on the court."
                    },
                    {
                        "q": "What is the capital city of Ireland?",
                        "options": ["A) Belfast", "B) Cork", "C) Dublin", "D) Galway"],
                        "a": "C) Dublin",
                        "notes": "Dublin: home of St. James's Gate Brewery (Guinness)."
                    },
                    {
                        "q": "What is the common name for the dry meat snack made by stuffing sheep or beef casing with seasoned ground meat and drying it?",
                        "options": ["A) Boerewors", "B) Droëwors", "C) Salami", "D) Chorizo"],
                        "a": "B) Droëwors",
                        "notes": "Droëwors."
                    },
                    {
                        "q": "What color is the middle stripe on the national flag of Germany?",
                        "options": ["A) Black", "B) Red", "C) Gold (Yellow)", "D) White"],
                        "a": "B) Red",
                        "notes": "Black, Red, Gold from top to bottom."
                    },
                    {
                        "q": "In pool or billiards, what ball is traditionally solid black with the number 8?",
                        "options": ["A) The 1-ball", "B) The 8-ball", "C) The cue ball", "D) The 9-ball"],
                        "a": "B) The 8-ball",
                        "notes": "The 8-ball is the black ball potted last to win."
                    },
                    {
                        "q": "What is the traditional name for the morning alcoholic beverage made with tomato juice, vodka, Worcestershire sauce, and Tabasco?",
                        "options": ["A) Screwdriver", "B) Bloody Mary", "C) Mimosa", "D) Tequila Sunrise"],
                        "a": "B) Bloody Mary",
                        "notes": "Classic hangover remedy cocktail."
                    }
                ]
            },
            {
                "roundId": 2,
                "title": "Round 2: Athletics, Marathons & Water Sports",
                "badge": "Round 2 • Endurance",
                "theme": "The Comrades Marathon, World Records & Swimming Greats",
                "difficultyText": "Level 2: Grit & Heart",
                "hostVibe": "Test endurance knowledge from Durban to Pietermaritzburg.",
                "questions": [
                    {
                        "q": "Between which two KwaZulu-Natal cities is the world-famous Comrades Marathon run annually over approximately 89 kilometers?",
                        "options": ["A) Durban & Pietermaritzburg", "B) Durban & Richards Bay", "C) Newcastle & Ladysmith", "D) Margate & Durban"],
                        "a": "A) Durban & Pietermaritzburg",
                        "notes": "The world's largest and oldest ultramarathon, alternating between Up Run and Down Run."
                    },
                    {
                        "q": "Which South African running legend won the Comrades Marathon a record nine times between 1981 and 1992?",
                        "options": ["A) Shaun Meiklejohn", "B) Bruce Fordyce", "C) Nick Bester", "D) Ludwick Mamabolo"],
                        "a": "B) Bruce Fordyce",
                        "notes": "Bruce Fordyce: the undisputed king of the Comrades Marathon."
                    },
                    {
                        "q": "Which South African sprinter shattered Michael Johnson's 17-year-old world record to win 400m Olympic Gold in Rio 2016 in 43.03 seconds from lane 8?",
                        "options": ["A) Akani Simbine", "B) Wayde van Niekerk", "C) Anaso Jobodwana", "D) Clarence Munyai"],
                        "a": "B) Wayde van Niekerk",
                        "notes": "Wayde van Niekerk's mind-blowing 43.03 run from the outside lane in Rio."
                    },
                    {
                        "q": "What is the standard official length of a full marathon race in kilometers?",
                        "options": ["A) 40.0 km", "B) 41.5 km", "C) 42.195 km", "D) 45.0 km"],
                        "a": "C) 42.195 km",
                        "notes": "42.195 km (26 miles 385 yards), standardized at the 1908 London Olympics."
                    },
                    {
                        "q": "Which South African marathon race held in Cape Town every Easter weekend is famed as 'The World's Most Beautiful Marathon'?",
                        "options": ["A) Cape Peninsula Marathon", "B) Two Oceans Marathon", "C) Sanlam Cape Town Marathon", "D) Gun Run"],
                        "a": "B) Two Oceans Marathon",
                        "notes": "56 km ultramarathon over Chapman's Peak and Constantia Nek."
                    },
                    {
                        "q": "Which South African male swimmer won Olympic Gold in the 100m breaststroke at the 2012 London Olympics in world record time?",
                        "options": ["A) Cameron van der Burgh", "B) Chad le Clos", "C) Ryk Neethling", "D) Darian Townsend"],
                        "a": "A) Cameron van der Burgh",
                        "notes": "Cameron van der Burgh touched the wall in 58.46 seconds."
                    },
                    {
                        "q": "In rugby union, which position on the pitch wears the number 9 jersey?",
                        "options": ["A) Flyhalf", "B) Scrumhalf", "C) Fullback", "D) Inside Centre"],
                        "a": "B) Scrumhalf",
                        "notes": "Scrumhalf wears number 9; flyhalf wears number 10."
                    },
                    {
                        "q": "Which famous canoe marathon is held annually on the Msunduzi and Mngeni Rivers in KwaZulu-Natal over three gruelling days?",
                        "options": ["A) Fish River Canoe Marathon", "B) Dusi Canoe Marathon", "C) Berg River Marathon", "D) Breede River Marathon"],
                        "a": "B) Dusi Canoe Marathon",
                        "notes": "Founded in 1951 by Ian Player, paddling and portaging between Pietermaritzburg and Durban."
                    },
                    {
                        "q": "Which country won the FIFA Men's World Cup in Qatar in December 2022, captained by Lionel Messi?",
                        "options": ["A) France", "B) Brazil", "C) Argentina", "D) Croatia"],
                        "a": "C) Argentina",
                        "notes": "Argentina defeated France in a thrilling penalty shootout."
                    },
                    {
                        "q": "In cricket, how many runs are scored if a batter hits the ball and runs between the wickets three times without the ball crossing the boundary?",
                        "options": ["A) 2 runs", "B) 3 runs", "C) 4 runs", "D) 6 runs"],
                        "a": "B) 3 runs",
                        "notes": "Each completed run across the pitch equals 1 run."
                    }
                ]
            },
            {
                "roundId": 3,
                "title": "Round 3: Sci-Fi, Superheroes & Hollywood",
                "badge": "Round 3 • Blockbusters",
                "theme": "Marvel, Star Wars, Time Travel & Pop Culture Icons",
                "difficultyText": "Level 3: Comic Con",
                "hostVibe": "Hollywood fan favorites! Have fun with the quotes.",
                "questions": [
                    {
                        "q": "In the Marvel Cinematic Universe, what is the real identity of Iron Man?",
                        "options": ["A) Bruce Banner", "B) Steve Rogers", "C) Tony Stark", "D) Peter Parker"],
                        "a": "C) Tony Stark",
                        "notes": "Played by Robert Downey Jr."
                    },
                    {
                        "q": "In Star Wars, who is revealed to be Luke Skywalker's father in The Empire Strikes Back?",
                        "options": ["A) Obi-Wan Kenobi", "B) Darth Vader (Anakin Skywalker)", "C) Emperor Palpatine", "D) Grand Moff Tarkin"],
                        "a": "B) Darth Vader (Anakin Skywalker)",
                        "notes": "'No, I am your father.'"
                    },
                    {
                        "q": "Which 1985 adventure film starred Michael J. Fox as high school student Marty McFly travelling back to 1955?",
                        "options": ["A) The Goonies", "B) Back to the Future", "C) Ferris Bueller's Day Off", "D) Ghostbusters"],
                        "a": "B) Back to the Future",
                        "notes": "Directed by Robert Zemeckis."
                    },
                    {
                        "q": "What fictional African country is ruled by King T'Challa in Marvel's Black Panther?",
                        "options": ["A) Zamunda", "B) Wakanda", "C) Genovia", "D) Latveria"],
                        "a": "B) Wakanda",
                        "notes": "'Wakanda Forever!' Rich in the alien metal vibranium."
                    },
                    {
                        "q": "Who directed the 1994 cult masterpiece Pulp Fiction?",
                        "options": ["A) Quentin Tarantino", "B) David Fincher", "C) Guy Ritchie", "D) Stanley Kubrick"],
                        "a": "A) Quentin Tarantino",
                        "notes": "Won the Palme d'Or at Cannes in 1994."
                    },
                    {
                        "q": "In the Batman universe, what is the name of the fictional city protected by the Caped Crusader?",
                        "options": ["A) Metropolis", "B) Star City", "C) Gotham City", "D) Central City"],
                        "a": "C) Gotham City",
                        "notes": "Metropolis is Superman's home; Gotham belongs to Batman."
                    },
                    {
                        "q": "Which actor played Indiana Jones in Raiders of the Lost Ark (1981)?",
                        "options": ["A) Sean Connery", "B) Harrison Ford", "C) Tom Selleck", "D) Kurt Russell"],
                        "a": "B) Harrison Ford",
                        "notes": "Harrison Ford wielded the fedora and whip."
                    },
                    {
                        "q": "In the Harry Potter series, what platform at King's Cross station does the Hogwarts Express depart from?",
                        "options": ["A) Platform 7½", "B) Platform 9¾", "C) Platform 10½", "D) Platform 12"],
                        "a": "B) Platform 9¾",
                        "notes": "Hidden behind the barrier between platforms 9 and 10."
                    },
                    {
                        "q": "What British rock band wrote and performed the iconic soundtrack to the 1986 film Highlander, including 'Princes of the Universe' and 'Who Wants to Live Forever'?",
                        "options": ["A) Queen", "B) Def Leppard", "C) Iron Maiden", "D) Pink Floyd"],
                        "a": "A) Queen",
                        "notes": "Included on Queen's 1986 album A Kind of Magic."
                    },
                    {
                        "q": "What is the name of the green ogre who lives in a swamp alongside a talking Donkey in DreamWorks' hit animated film?",
                        "options": ["A) Sulley", "B) Shrek", "C) Fiona", "D) Gru"],
                        "a": "B) Shrek",
                        "notes": "Voiced by Mike Myers (with Eddie Murphy as Donkey)."
                    }
                ]
            },
            {
                "roundId": 4,
                "title": "Round 4: Cocktails, Shooters & Snacks",
                "badge": "Round 4 • Shooters & Sips",
                "theme": "Bar Shooters, Finger Food, Draught Beer & Snack Trays",
                "difficultyText": "Level 4: Nightclub & Taproom",
                "hostVibe": "Test their bar shelf memory! Shooters and snacks.",
                "questions": [
                    {
                        "q": "What South African shooter is served as a double shot of Klipdrift brandy accompanied by a chaser can of Passion Fruit soda?",
                        "options": ["A) Springbokkie", "B) Suitcase", "C) Soweto Toilet", "D) Ferrari"],
                        "a": "B) Suitcase",
                        "notes": "A 'Suitcase': shot of Klipdrift followed by Passion Fruit soda."
                    },
                    {
                        "q": "What shooter is made by layering peppermint green liqueur with cream liqueur (Amarula)?",
                        "options": ["A) Springbokkie", "B) B-52", "C) Slippery Nipple", "D) Jelly Baby"],
                        "a": "A) Springbokkie",
                        "notes": "The national shot of South Africa: green and gold in a glass."
                    },
                    {
                        "q": "What triangular pastry snack filled with curried potatoes, peas, or spicy mince is beloved at South African parties?",
                        "options": ["A) Spring roll", "B) Samosa", "C) Empanada", "D) Pastry puff"],
                        "a": "B) Samosa",
                        "notes": "Crispy golden fried samosas."
                    },
                    {
                        "q": "What cocktail is made with white rum, coconut cream, and pineapple juice, garnished with a pineapple wedge?",
                        "options": ["A) Mai Tai", "B) Piña Colada", "C) Daiquiri", "D) Bahama Mama"],
                        "a": "B) Piña Colada",
                        "notes": "National drink of Puerto Rico since 1978."
                    },
                    {
                        "q": "Which brand of South African cider was launched in 1996 with a famous dry taste and lemon wedge in the neck?",
                        "options": ["A) Hunter's Dry", "B) Savanna Dry", "C) Strongbow", "D) Bernini"],
                        "a": "B) Savanna Dry",
                        "notes": "Savanna Dry: 'It's dry, but you can drink it.'"
                    },
                    {
                        "q": "What popular bar snack consists of seasoned pork skin deep-fried until crisp and crackling?",
                        "options": ["A) Pork Crackling / Scratchings", "B) Droëwors", "C) Cabanossi", "D) Brawn"],
                        "a": "A) Pork Crackling / Scratchings",
                        "notes": "Crispy salted pork scratchings."
                    },
                    {
                        "q": "What Italian bitter liqueur, vibrant red in color, is the key ingredient in a Negroni cocktail alongside gin and sweet vermouth?",
                        "options": ["A) Aperol", "B) Campari", "C) Cynar", "D) Fernet-Branca"],
                        "a": "B) Campari",
                        "notes": "Equal parts Campari, sweet red vermouth, and gin."
                    },
                    {
                        "q": "What is the classic Cape Malay dish made of spiced minced meat baked with an egg custard topping and bay leaves?",
                        "options": ["A) Bobotie", "B) Bredie", "C) Denningvleis", "D) Gesmoor"],
                        "a": "A) Bobotie",
                        "notes": "South Africa's national dish, fragrant with curry spices and raisins."
                    },
                    {
                        "q": "In a bar, what term is used for draught beer served directly from the tap into a glass pitcher built for sharing at the table?",
                        "options": ["A) Growler", "B) Pitcher / Jug", "C) Yard of Ale", "D) Stein"],
                        "a": "B) Pitcher / Jug",
                        "notes": "A beer jug or pitcher, typically 1.5 to 2 liters."
                    },
                    {
                        "q": "What spicy tomato cocktail mix originated in Calgary, Canada, made with clam broth and tomato juice?",
                        "options": ["A) Bloody Mary", "B) Caesar (Bloody Caesar)", "C) Michelada", "D) Red Eye"],
                        "a": "B) Caesar (Bloody Caesar)",
                        "notes": "Made with Mott's Clamato juice."
                    }
                ]
            },
            {
                "roundId": 5,
                "title": "Round 5: World Rivers, Lakes & Mountains",
                "badge": "Round 5 • Earth & Waters",
                "theme": "Vaal River, Great Lakes, Alpine Peaks & World Geography",
                "difficultyText": "Level 5: Top of the World",
                "hostVibe": "Final round before the winners are determined! Every answer counts.",
                "questions": [
                    {
                        "q": "What major South African river forms the provincial boundary between Gauteng and the Free State, feeding the Vaal Dam?",
                        "options": ["A) Limpopo River", "B) Vaal River", "C) Orange River", "D) Tugela River"],
                        "a": "B) Vaal River",
                        "notes": "'Vaal' is Dutch for drab or pale, referring to the grayish silt color of the water."
                    },
                    {
                        "q": "What is the largest lake in Africa by surface area, shared by Uganda, Kenya, and Tanzania?",
                        "options": ["A) Lake Tanganyika", "B) Lake Victoria", "C) Lake Malawi", "D) Lake Kariba"],
                        "a": "B) Lake Victoria",
                        "notes": "Spanning over 68,000 square kilometers, it is the main source of the White Nile."
                    },
                    {
                        "q": "What is the highest mountain peak in the world above sea level, located on the border between Nepal and China?",
                        "options": ["A) K2", "B) Mount Everest (Sagarmatha)", "C) Kangchenjunga", "D) Lhotse"],
                        "a": "B) Mount Everest (Sagarmatha)",
                        "notes": "Stands 8,848.86 meters above sea level in the Himalayas."
                    },
                    {
                        "q": "Which major river flows through London before emptying into the North Sea?",
                        "options": ["A) River Severn", "B) River Thames", "C) River Mersey", "D) River Trent"],
                        "a": "B) River Thames",
                        "notes": "The River Thames flows past the Houses of Parliament and Tower Bridge."
                    },
                    {
                        "q": "What South African town in the Free State is located right on the banks of the Vaal River and is famous for art galleries, breweries, and antique shops?",
                        "options": ["A) Parys", "B) Sasolburg", "C) Kroonstad", "D) Frankfort"],
                        "a": "A) Parys",
                        "notes": "Parys on the Vaal: a bustling weekend getaway."
                    },
                    {
                        "q": "What is the capital city of Norway?",
                        "options": ["A) Stockholm", "B) Helsinki", "C) Oslo", "D) Copenhagen"],
                        "a": "C) Oslo",
                        "notes": "Oslo: situated at the head of the Oslofjord."
                    },
                    {
                        "q": "What is the largest ocean on Earth, covering more surface area than all of the world's landmasses combined?",
                        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Pacific Ocean", "D) Arctic Ocean"],
                        "a": "C) Pacific Ocean",
                        "notes": "Covering over 165 million square kilometers."
                    },
                    {
                        "q": "Which mountain range stretches through Switzerland, France, Italy, Austria, and Germany?",
                        "options": ["A) The Pyrenees", "B) The Alps", "C) The Urals", "D) The Andes"],
                        "a": "B) The Alps",
                        "notes": "Highest peak is Mont Blanc (4,808m)."
                    },
                    {
                        "q": "What South African town in the Western Cape is world-famous for its dramatic red rock cliffs and rock-climbing routes?",
                        "options": ["A) Montagu", "B) Clanwilliam", "C) Oudtshoorn", "D) Prince Albert"],
                        "a": "A) Montagu",
                        "notes": "Montagu on Route 62: a climbing and hot springs haven."
                    },
                    {
                        "q": "What is the capital city of New Zealand?",
                        "options": ["A) Auckland", "B) Christchurch", "C) Wellington", "D) Queenstown"],
                        "a": "C) Wellington",
                        "notes": "Wellington is the world's southernmost sovereign capital city."
                    }
                ]
            },
            {
                "roundId": 6,
                "title": "Sudden-Death Tie-Breakers",
                "badge": "Overtime • Closest Number",
                "theme": "Closest to the Pin Estimations",
                "difficultyText": "Overtime: Closest Number Takes 1st Place!",
                "hostVibe": "Tied teams: write your number down!",
                "questions": [
                    {
                        "q": "What is the official world record time set by Wayde van Niekerk in the 400m sprint in Rio 2016 in seconds?",
                        "options": ["A) 42.95 seconds", "B) 43.03 seconds", "C) 43.18 seconds", "D) 43.45 seconds"],
                        "a": "B) 43.03 seconds",
                        "notes": "43.03 seconds on 14 August 2016."
                    },
                    {
                        "q": "Approximately how many kilometers long is the full length of the Vaal River from its source near Breyten to its confluence with the Orange River?",
                        "options": ["A) 750 km", "B) 950 km", "C) 1,120 km", "D) 1,400 km"],
                        "a": "C) 1,120 km",
                        "notes": "Approximately 1,120 km in length."
                    },
                    {
                        "q": "In what calendar year was the first ever Comrades Marathon run between Pietermaritzburg and Durban?",
                        "options": ["A) 1910", "B) 1921", "C) 1932", "D) 1945"],
                        "a": "B) 1921",
                        "notes": "24 May 1921, founded by Vic Clapham."
                    }
                ]
            }
        ]
    }

def get_set_10():
    return {
        "setId": 10,
        "setName": "Set 10: The Masters Grand Finale",
        "badge": "Set 10 • Grand Finale",
        "theme": "Springbok Hall of Fame, Classic Rock Titans, Master Steaks & World Frontiers",
        "rounds": [
            {
                "roundId": 1,
                "title": "Round 1: Ultimate Bar Warm-Up",
                "badge": "Round 1 • Easy",
                "theme": "Brainteasers, Everyday Knowledge & Pub Trivia Classics",
                "difficultyText": "Level 1: The Grand Warm-Up",
                "hostVibe": "The final master set! High energy in the room, big points on offer.",
                "questions": [
                    {
                        "q": "How many hours are there in three full days?",
                        "options": ["A) 48 hours", "B) 60 hours", "C) 72 hours", "D) 84 hours"],
                        "a": "C) 72 hours",
                        "notes": "3 x 24 = 72 hours."
                    },
                    {
                        "q": "What is the common term in South African slang for a pickup truck?",
                        "options": ["A) Ute", "B) Bakkie", "C) Truckie", "D) Cruiser"],
                        "a": "B) Bakkie",
                        "notes": "A bakkie: South Africa's favorite vehicle."
                    },
                    {
                        "q": "What color is the center circle in the Japanese national flag?",
                        "options": ["A) Red", "B) White", "C) Gold", "D) Black"],
                        "a": "A) Red",
                        "notes": "A red disc representing the rising sun on a white field."
                    },
                    {
                        "q": "In golf, what is the term for a score of one over par on a single hole?",
                        "options": ["A) Birdie", "B) Bogey", "C) Eagle", "D) Albatross"],
                        "a": "B) Bogey",
                        "notes": "One over par is a bogey."
                    },
                    {
                        "q": "Which fruit is famous for having its seeds on the outside of its skin?",
                        "options": ["A) Raspberry", "B) Strawberry", "C) Blackberry", "D) Fig"],
                        "a": "B) Strawberry",
                        "notes": "Strawberries carry roughly 200 seed-like achenes on the outer skin."
                    },
                    {
                        "q": "What is the capital city of Greece?",
                        "options": ["A) Athens", "B) Sparta", "C) Rhodes", "D) Heraklion"],
                        "a": "A) Athens",
                        "notes": "Athens."
                    },
                    {
                        "q": "How many players are on the field for one team during an Australian Rules Football match?",
                        "options": ["A) 11", "B) 15", "C) 18", "D) 21"],
                        "a": "C) 18",
                        "notes": "18 players on the field per team in Aussie Rules (AFL)."
                    },
                    {
                        "q": "What popular South African tea is caffeine-free and made from the leaves of the indigenous Aspalathus linearis plant in the Cederberg?",
                        "options": ["A) Honeybush", "B) Rooibos", "C) Chamomile", "D) Buchu"],
                        "a": "B) Rooibos",
                        "notes": "Rooibos (red bush tea), indigenous to the Cederberg mountains."
                    },
                    {
                        "q": "What is the currency of Mexico?",
                        "options": ["A) Real", "B) Peso", "C) Sol", "D) Bolivar"],
                        "a": "B) Peso",
                        "notes": "Mexican Peso ($)."
                    },
                    {
                        "q": "In a game of pub darts, what is the value of the green outer bullseye ring?",
                        "options": ["A) 20 points", "B) 25 points", "C) 30 points", "D) 50 points"],
                        "a": "B) 25 points",
                        "notes": "Outer green bull = 25 points; inner red bull = 50 points."
                    }
                ]
            },
            {
                "roundId": 2,
                "title": "Round 2: Springbok Legends & Rugby Hall of Fame",
                "badge": "Round 2 • Rugby Immortals",
                "theme": "World Cup Double Champions, Iconic Tries & Legends",
                "difficultyText": "Level 2: The Green & Gold Vault",
                "hostVibe": "Celebrate the icons who made Springbok rugby the greatest team on earth.",
                "questions": [
                    {
                        "q": "Which beloved Springbok scrumhalf scored 38 test tries in 89 appearances, famously tackling Jonah Lomu in the 1995 final?",
                        "options": ["A) Fourie du Preez", "B) Joost van der Westhuizen", "C) Faf de Klerk", "D) Ricky Januarie"],
                        "a": "B) Joost van der Westhuizen",
                        "notes": "Joost van der Westhuizen: World Rugby Hall of Fame legend."
                    },
                    {
                        "q": "Who is the only Springbok prop forward to win two Rugby World Cups twelve years apart, winning in both 1995 and 2007?",
                        "options": ["A) Balie Swart", "B) Os du Randt", "C) Tendai Mtawarira", "D) Frans Malherbe"],
                        "a": "B) Os du Randt",
                        "notes": "Jacobus Petrus 'Os' du Randt: a giant of South African rugby."
                    },
                    {
                        "q": "Which Springbok flanker won the World Rugby Player of the Year award in 2019 after devastating performances in Japan?",
                        "options": ["A) Pieter-Steph du Toit", "B) Duane Vermeulen", "C) Kwagga Smith", "D) Francois Louw"],
                        "a": "A) Pieter-Steph du Toit",
                        "notes": "Pieter-Steph du Toit: 'The Malmesbury Missile'."
                    },
                    {
                        "q": "What South African scrumhalf became an internet sensation for his blond locks, South African flag speedo, and fearless confrontation with giant locks?",
                        "options": ["A) Cobus Reinach", "B) Jaden Hendrikse", "C) Faf de Klerk", "D) Grant Williams"],
                        "a": "C) Faf de Klerk",
                        "notes": "Faf de Klerk, celebrated double World Cup winning scrumhalf."
                    },
                    {
                        "q": "Who was the Springbok captain when South Africa won their second World Cup in Paris in 2007?",
                        "options": ["A) Victor Matfield", "B) John Smit", "C) Percy Montgomery", "D) Bobby Skinstad"],
                        "a": "B) John Smit",
                        "notes": "John Smit captained the Springboks in a record 83 test matches."
                    },
                    {
                        "q": "Which South African winger was named World Rugby Breakthrough Player of the Year in 2018, famous for his stepping and sidestep?",
                        "options": ["A) Makazole Mapimpi", "B) Cheslin Kolbe", "C) Aphiwe Dyantyi", "D) Kurt-Lee Arendse"],
                        "a": "C) Aphiwe Dyantyi",
                        "notes": "Aphiwe Dyantyi won the award in 2018 after scoring 6 tries in his debut season."
                    },
                    {
                        "q": "Which legendary Springbok flyhalf was known as 'The King' and scored all 27 points in a single match against the All Blacks in 1999?",
                        "options": ["A) Henry Honiball", "B) Jannie de Beer", "C) Naas Botha", "D) Braam van Straaten"],
                        "a": "B) Jannie de Beer",
                        "notes": "Jannie de Beer kicked a world record five drop goals against England in the 1999 World Cup quarter-final."
                    },
                    {
                        "q": "Which iconic lock forward from the Northern Transvaal was famous for kicking 50-meter penalties with a straight toe-poke style and also playing flank and lock?",
                        "options": ["A) Frik du Preez", "B) Moaner van Heerden", "C) Louis Moolman", "D) Burger Geldenhuys"],
                        "a": "A) Frik du Preez",
                        "notes": "Frik du Preez: named South Africa's rugby player of the 20th century."
                    },
                    {
                        "q": "In rugby union, what is the maximum number of substitutions allowed from the bench in a modern test match?",
                        "options": ["A) 5 replacements", "B) 7 replacements", "C) 8 replacements", "D) 10 replacements"],
                        "a": "C) 8 replacements",
                        "notes": "8 players on the bench (the famous Springbok 'Bomb Squad')."
                    },
                    {
                        "q": "At which stadium in Yokohama, Japan did the Springboks defeat England 32-12 to win the 2019 Rugby World Cup?",
                        "options": ["A) Tokyo Stadium", "B) International Stadium Yokohama (Nissan Stadium)", "C) Shizuoka Stadium", "D) Hanazono Stadium"],
                        "a": "B) International Stadium Yokohama (Nissan Stadium)",
                        "notes": "International Stadium Yokohama on 2 November 2019."
                    }
                ]
            },
            {
                "roundId": 3,
                "title": "Round 3: Classic Rock, Pop & Soundtrack Icons",
                "badge": "Round 3 • Music Legends",
                "theme": "Pink Floyd, Dire Straits, Queen & Vinyl Classics",
                "difficultyText": "Level 3: Master of Rock",
                "hostVibe": "Turn up the volume in your head and sing along to the rock anthems.",
                "questions": [
                    {
                        "q": "Which British rock band released the 1973 progressive rock masterpiece The Dark Side of the Moon?",
                        "options": ["A) The Who", "B) Led Zeppelin", "C) Pink Floyd", "D) Genesis"],
                        "a": "C) Pink Floyd",
                        "notes": "Spent over 950 weeks on the US Billboard 200 chart."
                    },
                    {
                        "q": "Which British rock band fronted by Mark Knopfler had massive 1985 hits with 'Money for Nothing' and 'Sultans of Swing'?",
                        "options": ["A) The Police", "B) Dire Straits", "C) Fleetwood Mac", "D) Supertramp"],
                        "a": "B) Dire Straits",
                        "notes": "Their album Brothers in Arms was one of the first CD releases to sell over a million copies."
                    },
                    {
                        "q": "Who released the hit 1971 folk-rock song 'American Pie' recounting 'the day the music died'?",
                        "options": ["A) Don McLean", "B) Bob Dylan", "C) James Taylor", "D) Neil Young"],
                        "a": "A) Don McLean",
                        "notes": "Refers to the 1959 plane crash that killed Buddy Holly, Ritchie Valens, and the Big Bopper."
                    },
                    {
                        "q": "Which Anglo-American rock band released the legendary 1977 album Rumours featuring 'Go Your Own Way' and 'Dreams'?",
                        "options": ["A) Fleetwood Mac", "B) Eagles", "C) Heart", "D) The Pretenders"],
                        "a": "A) Fleetwood Mac",
                        "notes": "Stevie Nicks, Lindsey Buckingham, Mick Fleetwood, Christine McVie, and John McVie."
                    },
                    {
                        "q": "Which British singer-songwriter composed the musical score and songs for Disney's 1994 animated movie The Lion King, including 'Can You Feel the Love Tonight'?",
                        "options": ["A) Phil Collins", "B) Elton John", "C) Paul McCartney", "D) Sting"],
                        "a": "B) Elton John",
                        "notes": "Elton John (music) with lyrics by Tim Rice."
                    },
                    {
                        "q": "In the hit song 'Hotel California' by the Eagles, what is the famous final line of the chorus?",
                        "options": ["A) You can never leave", "B) You can check out any time you like, but you can never leave", "C) Welcome to the Hotel California", "D) Such a lovely place"],
                        "a": "B) You can check out any time you like, but you can never leave",
                        "notes": "'You can check out any time you like, but you can never leave!'"
                    },
                    {
                        "q": "What British heavy metal band fronted by Bruce Dickinson is famous for mascot Eddie and anthems like 'The Trooper' and 'Run to the Hills'?",
                        "options": ["A) Judas Priest", "B) Iron Maiden", "C) Black Sabbath", "D) Motorhead"],
                        "a": "B) Iron Maiden",
                        "notes": "Iron Maiden, formed in East London in 1975 by Steve Harris."
                    },
                    {
                        "q": "Which South African female singer achieved international stardom in the 1980s with hits like 'Special Star' or collaborated with Sipho Mabuse on 'Burn Out'?",
                        "options": ["A) Brenda Fassie", "B) Miriam Makeba", "C) Yvonne Chaka Chaka", "D) PJ Powers"],
                        "a": "D) PJ Powers",
                        "notes": "PJ Powers ('Thandeka') fronted Hotline with hits like 'Jabulani'."
                    },
                    {
                        "q": "Which American band featured Kurt Cobain, Krist Novoselic, and Dave Grohl?",
                        "options": ["A) Pearl Jam", "B) Soundgarden", "C) Nirvana", "D) Alice in Chains"],
                        "a": "C) Nirvana",
                        "notes": "Pioneered the worldwide grunge explosion."
                    },
                    {
                        "q": "Which British rock icon released 'Space Oddity' in 1969 introducing the astronaut Major Tom?",
                        "options": ["A) David Bowie", "B) Marc Bolan", "C) Peter Gabriel", "D) Rod Stewart"],
                        "a": "A) David Bowie",
                        "notes": "David Bowie's breakthrough single released days before Apollo 11 moon landing."
                    }
                ]
            },
            {
                "roundId": 4,
                "title": "Round 4: The Ultimate Feast & Beverage Masterclass",
                "badge": "Round 4 • The Feast",
                "theme": "Dry-Aged Steaks, Cellar Reservers, Craft Distilling & Braai Mastery",
                "difficultyText": "Level 4: Master Chef & Sommelier",
                "hostVibe": "Culinary royalty! Separate the pros from the novices.",
                "questions": [
                    {
                        "q": "What is the culinary term for aging beef in a temperature- and humidity-controlled room for several weeks to intensify flavor and tenderize the meat?",
                        "options": ["A) Wet aging", "B) Dry aging", "C) Brining", "D) Curing"],
                        "a": "B) Dry aging",
                        "notes": "Dry aging allows natural enzymes to break down muscle fibers while moisture evaporates, concentrating beef flavor."
                    },
                    {
                        "q": "What is the famous South African dry white wine grape variety that is locally known as 'Steen'?",
                        "options": ["A) Sauvignon Blanc", "B) Chenin Blanc", "C) Chardonnay", "D) Viognier"],
                        "a": "B) Chenin Blanc",
                        "notes": "South Africa has more Chenin Blanc planted than any other country in the world."
                    },
                    {
                        "q": "What cut of steak is a thick cut of sirloin or ribeye served on a long, Frenched rib bone resembling a native axe?",
                        "options": ["A) T-bone", "B) Porterhouse", "C) Tomahawk", "D) Chateaubriand"],
                        "a": "C) Tomahawk",
                        "notes": "A bone-in ribeye with at least 12-15 cm of intact rib bone."
                    },
                    {
                        "q": "What famous brand of South African potstill brandy won the Worldwide Best Brandy trophy multiple times at the International Wine & Spirit Competition?",
                        "options": ["A) KWV 10 / 15 / 20 Year Old", "B) Klipdrift Export", "C) Wellington", "D) Commando"],
                        "a": "A) KWV 10 / 15 / 20 Year Old",
                        "notes": "KWV's potstill brandies from Paarl have consistently swept global awards."
                    },
                    {
                        "q": "What is the French culinary term for finely minced raw beef or game seasoned with capers, shallots, Worcestershire sauce, and topped with a raw egg yolk?",
                        "options": ["A) Carpaccio", "B) Steak Tartare", "C) Bresaola", "D) Ceviche"],
                        "a": "B) Steak Tartare",
                        "notes": "Steak Tartare: classic bistro fare."
                    },
                    {
                        "q": "Which South African coastal town is renowned for its annual Crayfish (West Coast Rock Lobster) Festival and open-air beach strandkombuis restaurants?",
                        "options": ["A) Paternoster", "B) Lamberts Bay", "C) Langebaan", "D) Elands Bay"],
                        "a": "B) Lamberts Bay",
                        "notes": "Lamberts Bay and Paternoster are the heartland of West Coast seafood."
                    },
                    {
                        "q": "What is the sweet fortified Portuguese wine from the Douro Valley that is traditionally aged in wooden casks and served as a digestif?",
                        "options": ["A) Sherry", "B) Port", "C) Madeira", "D) Marsala"],
                        "a": "B) Port",
                        "notes": "Tawny or Ruby Port, often paired with blue cheese."
                    },
                    {
                        "q": "What popular South African sweet confection consists of shredded coconut baked in caramelized brown sugar and rolled into patties?",
                        "options": ["A) Hertzoggie", "B) Klappertert / Coconut Ice", "C) Fudge", "D) Toffee"],
                        "a": "B) Klappertert / Coconut Ice",
                        "notes": "Traditional South African coconut ice or klapperys."
                    },
                    {
                        "q": "What is the main type of wood traditionally used in barrels to age fine whiskey and red wine?",
                        "options": ["A) Pine", "B) Oak", "C) Cedar", "D) Maple"],
                        "a": "B) Oak",
                        "notes": "French and American white oak impart vanilla, tannin, and spice notes."
                    },
                    {
                        "q": "In braai culture, what is the best way to test whether your coals are at the perfect medium-heat for chops and boerewors?",
                        "options": [
                            "A) If the grid turns glowing red",
                            "B) Hold your open palm about 10 cm above the grid: you can comfortably hold it for 5-7 seconds",
                            "C) Pour a cup of water over the coals",
                            "D) If white smoke stops completely"
                        ],
                        "a": "B) Hold your open palm about 10 cm above the grid: you can comfortably hold it for 5-7 seconds",
                        "notes": "The classic hand test: 5-7 seconds indicates medium heat; 3-4 seconds is high heat."
                    }
                ]
            },
            {
                "roundId": 5,
                "title": "Round 5: Global Frontiers & Epic Discoveries",
                "badge": "Round 5 • The Final Decider",
                "theme": "Space Frontiers, World Wonders, Deep Oceans & Human Triumph",
                "difficultyText": "Level 5: Mastermind Finale",
                "hostVibe": "The very last round! Give it everything you've got.",
                "questions": [
                    {
                        "q": "Which South African mountain pass connects Oudtshoorn in the Klein Karoo to Prince Albert in the Great Karoo, engineered by Thomas Bain in the 1880s?",
                        "options": ["A) Swartberg Pass", "B) Tradouw Pass", "C) Cogmanskloof", "D) Swartruggens Pass"],
                        "a": "A) Swartberg Pass",
                        "notes": "The Swartberg Pass: a national monument and masterpiece of 19th-century dry-stone walling."
                    },
                    {
                        "q": "What is the largest country in the world by total land area?",
                        "options": ["A) Canada", "B) China", "C) Russia", "D) United States"],
                        "a": "C) Russia",
                        "notes": "Covering over 17 million square kilometers across two continents."
                    },
                    {
                        "q": "In which city is the famous Sydney Opera House located?",
                        "options": ["A) Melbourne", "B) Sydney", "C) Brisbane", "D) Perth"],
                        "a": "B) Sydney",
                        "notes": "Designed by Danish architect Jørn Utzon on Bennelong Point in Sydney Harbour."
                    },
                    {
                        "q": "What massive astronomical radio telescope array located in the Karoo near Carnarvon is part of the international Square Kilometre Array (SKA)?",
                        "options": ["A) SALT (Southern African Large Telescope)", "B) MeerKAT", "C) Hartebeesthoek", "D) Boyden Observatory"],
                        "a": "B) MeerKAT",
                        "notes": "MeerKAT consists of 64 dish antennas peering deep into the early universe."
                    },
                    {
                        "q": "What is the highest mountain peak in North America, located in the Alaska Range?",
                        "options": ["A) Mount Logan", "B) Mount Denali (Mount McKinley)", "C) Mount Whitney", "D) Mount Rainier"],
                        "a": "B) Mount Denali (Mount McKinley)",
                        "notes": "Stands 6,190 meters above sea level."
                    },
                    {
                        "q": "Which canal connects the Atlantic Ocean and the Pacific Ocean across Central America, saving ships an 8,000-mile detour around Cape Horn?",
                        "options": ["A) Suez Canal", "B) Panama Canal", "C) Kiel Canal", "D) Erie Canal"],
                        "a": "B) Panama Canal",
                        "notes": "Opened in August 1914; features a series of gravity-fed water locks."
                    },
                    {
                        "q": "What is the capital city of Argentina?",
                        "options": ["A) Santiago", "B) Buenos Aires", "C) Montevideo", "D) Lima"],
                        "a": "B) Buenos Aires",
                        "notes": "Buenos Aires: situated on the western shore of the Río de la Plata."
                    },
                    {
                        "q": "What international laboratory near Geneva, Switzerland houses the 27-kilometer Large Hadron Collider particle accelerator?",
                        "options": ["A) NASA", "B) CERN", "C) ESA", "D) Fermilab"],
                        "a": "B) CERN",
                        "notes": "The European Organization for Nuclear Research (CERN), birthplace of the World Wide Web."
                    },
                    {
                        "q": "Which South African national park in the Eastern Cape was proclaimed in 1931 to save the remaining eleven Eastern Cape elephants from extinction?",
                        "options": ["A) Addo Elephant National Park", "B) Mountain Zebra National Park", "C) Karoo National Park", "D) Tsitsikamma"],
                        "a": "A) Addo Elephant National Park",
                        "notes": "Now home to over 600 elephants, lions, buffalo, and black rhino."
                    },
                    {
                        "q": "What is the official language of Brazil?",
                        "options": ["A) Spanish", "B) Portuguese", "C) French", "D) Italian"],
                        "a": "B) Portuguese",
                        "notes": "Brazil is the only Portuguese-speaking country in the Americas."
                    }
                ]
            },
            {
                "roundId": 6,
                "title": "Sudden-Death Tie-Breakers",
                "badge": "Overtime • Grand Decider",
                "theme": "Closest to the Pin Estimations",
                "difficultyText": "Overtime: Closest Number Takes The Grand Trophy!",
                "hostVibe": "Grand finale tie-breaker! Hand in your final numbers.",
                "questions": [
                    {
                        "q": "How many total dish antennas make up the MeerKAT radio telescope array in the Northern Cape?",
                        "options": ["A) 32 dishes", "B) 48 dishes", "C) 64 dishes", "D) 80 dishes"],
                        "a": "C) 64 dishes",
                        "notes": "64 interconnected dish antennas."
                    },
                    {
                        "q": "In what calendar year did the Swartberg Pass officially open to traffic?",
                        "options": ["A) 1865", "B) 1876", "C) 1888", "D) 1902"],
                        "a": "C) 1888",
                        "notes": "Opened on 10 January 1888."
                    },
                    {
                        "q": "How many test tries did Joost van der Westhuizen score in his international rugby career for the Springboks?",
                        "options": ["A) 32 tries", "B) 38 tries", "C) 44 tries", "D) 50 tries"],
                        "a": "B) 38 tries",
                        "notes": "38 tries in 89 test matches."
                    }
                ]
            }
        ]
    }

if __name__ == '__main__':
    print("Testing Set 8, 9, 10 generation...")
    s8 = get_set_8()
    s9 = get_set_9()
    s10 = get_set_10()
    for s in [s8, s9, s10]:
        print(f"{s['setName']}: {len(s['rounds'])} rounds")
        for r in s['rounds']:
            print(f"  Round {r['roundId']}: {len(r['questions'])} questions")
