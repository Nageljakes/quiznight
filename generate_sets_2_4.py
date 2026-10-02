# -*- coding: utf-8 -*-
import json

def get_set_2():
    return {
        "setId": 2,
        "setName": "Set 2: Braai, Bokke & Beer",
        "badge": "Set 2 • Bokke & Braai",
        "theme": "Springbok Rugby, Braai Lore, 80s/90s Cult Movies & Local Roads",
        "rounds": [
            {
                "roundId": 1,
                "title": "Round 1: Bar & Pub Warm-Up",
                "badge": "Round 1 • Easy",
                "theme": "Everyday Trivia, Pints & Ice Breakers",
                "difficultyText": "Level 1: Fast & Fun",
                "hostVibe": "Warm up the room! Crack open some cold ones and get every table scoring points.",
                "questions": [
                    {
                        "q": "In standard South African bar pouring measurements, how many milliliters is a single tot of spirits?",
                        "options": ["A) 20 ml", "B) 25 ml", "C) 30 ml", "D) 35 ml"],
                        "a": "B) 25 ml",
                        "notes": "A standard SA single tot is 25ml; a double tot is 50ml."
                    },
                    {
                        "q": "Which iconic South African beer has been brewed since 1895 and is known as 'The taste that stood the test of time'?",
                        "options": ["A) Black Label", "B) Windhoek Lager", "C) Castle Lager", "D) Hansa Pilsener"],
                        "a": "C) Castle Lager",
                        "notes": "Founded by Charles Glass during the Johannesburg gold rush in 1895."
                    },
                    {
                        "q": "In a standard game of pub darts, what is the highest score possible with a single dart?",
                        "options": ["A) 50 (Bullseye)", "B) 60 (Treble 20)", "C) 57 (Treble 19)", "D) 100"],
                        "a": "B) 60 (Treble 20)",
                        "notes": "Treble 20 equals 60 points, which is higher than a 50-point red bullseye."
                    },
                    {
                        "q": "What spicy, carbonated ginger soft drink beloved across South Africa comes with the famous tagline 'Kwenzekani'?",
                        "options": ["A) Schweppes Ginger Ale", "B) Stoney Ginger Beer", "C) Fanta Pineapple", "D) Sparletta Iron Brew"],
                        "a": "B) Stoney Ginger Beer",
                        "notes": "Famous for its punchy fiery ginger bite."
                    },
                    {
                        "q": "How many total players are on the field for one team during a rugby union match?",
                        "options": ["A) 11 players", "B) 13 players", "C) 15 players", "D) 16 players"],
                        "a": "C) 15 players",
                        "notes": "15 players on the pitch: 8 forwards and 7 backs."
                    },
                    {
                        "q": "What is the traditional name for the dried, spiced beef or game sausage cured in vinegar and coriander?",
                        "options": ["A) Boerewors", "B) Droëwors", "C) Cabanossi", "D) Brawn"],
                        "a": "B) Droëwors",
                        "notes": "Droëwors is literally dried sausage, made thin to dry quickly without spoiling."
                    },
                    {
                        "q": "In the hit comedy sitcom Friends, what is the name of the Greenwich Village coffee shop?",
                        "options": ["A) Daily Grind", "B) Central Perk", "C) Java Hut", "D) Monk's Diner"],
                        "a": "B) Central Perk",
                        "notes": "Managed by Gunther on the famous orange sofa."
                    },
                    {
                        "q": "Which letter on a standard computer QWERTY keyboard is the only vowel not located on the top row of letters?",
                        "options": ["A) E", "B) I", "C) A", "D) U"],
                        "a": "C) A",
                        "notes": "The top letter row has Q-W-E-R-T-Y-U-I-O-P. The letter A is on the home row."
                    },
                    {
                        "q": "What number does the Roman numeral 'L' stand for?",
                        "options": ["A) 50", "B) 100", "C) 500", "D) 1000"],
                        "a": "A) 50",
                        "notes": "L = 50, C = 100, D = 500, M = 1000."
                    },
                    {
                        "q": "What animal is depicted on the front of the South African 2-Rand coin in the old circulation series?",
                        "options": ["A) Kudu", "B) Wildebeest", "C) Springbok", "D) Rhino"],
                        "a": "A) Kudu",
                        "notes": "The R2 coin featured the Kudu bull with majestic spiral horns."
                    }
                ]
            },
            {
                "roundId": 2,
                "title": "Round 2: Green & Gold Rugby & Proteas Icons",
                "badge": "Round 2 • Sports",
                "theme": "World Cups, Test Matches & Legendary Feats",
                "difficultyText": "Level 2: Sports Mastermind",
                "hostVibe": "Get the banter flying between the rugby boffins and cricket enthusiasts.",
                "questions": [
                    {
                        "q": "Who was the captain who led the Springboks to Rugby World Cup victories in both 2019 and 2023?",
                        "options": ["A) Duane Vermeulen", "B) Eben Etzebeth", "C) Siya Kolisi", "D) Handre Pollard"],
                        "a": "C) Siya Kolisi",
                        "notes": "Siya Kolisi became only the second captain in rugby history to lift the Webb Ellis Cup twice (after Richie McCaw)."
                    },
                    {
                        "q": "What nickname is given to South Africa's national men's cricket team?",
                        "options": ["A) The Black Caps", "B) The Proteas", "C) The Baggy Greens", "D) The Lions"],
                        "a": "B) The Proteas",
                        "notes": "Named after the King Protea, South Africa's national flower."
                    },
                    {
                        "q": "At which historic Johannesburg stadium did Joel Stransky kick the winning drop goal in the 1995 Rugby World Cup final?",
                        "options": ["A) FNB Stadium", "B) Wanderers Stadium", "C) Ellis Park", "D) Loftus Versfeld"],
                        "a": "C) Ellis Park",
                        "notes": "Ellis Park on 24 June 1995: Springboks defeated the All Blacks 15-12 in extra time."
                    },
                    {
                        "q": "Which South African all-rounder holds the record for scoring over 13,000 Test runs and taking 292 Test wickets?",
                        "options": ["A) Shaun Pollock", "B) Jacques Kallis", "C) Lance Klusener", "D) Hansie Cronje"],
                        "a": "B) Jacques Kallis",
                        "notes": "Regarded by many as the greatest all-rounder in cricket history."
                    },
                    {
                        "q": "How many total Rugby World Cup titles have the Springboks won (up to 2023)?",
                        "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
                        "a": "C) 4",
                        "notes": "1995, 2007, 2019, and 2023 (the first nation to win 4 titles)."
                    },
                    {
                        "q": "Who was the first Springbok player to score a try in a Rugby World Cup final, doing so against England in 2019?",
                        "options": ["A) Cheslin Kolbe", "B) Makazole Mapimpi", "C) Lukhanyo Am", "D) Damian de Allende"],
                        "a": "B) Makazole Mapimpi",
                        "notes": "Mapimpi scored in the 66th minute after a chip and gather from Lukhanyo Am."
                    },
                    {
                        "q": "What is the name of the iconic home stadium of the Blue Bulls in Pretoria?",
                        "options": ["A) Kings Park", "B) Newlands", "C) Loftus Versfeld", "D) Free State Stadium"],
                        "a": "C) Loftus Versfeld",
                        "notes": "Named after Robert Owen Loftus Versfeld, the pioneer of organized sports in Pretoria."
                    },
                    {
                        "q": "In cricket, what term is used when a batter is dismissed without scoring on the very first ball they face?",
                        "options": ["A) Silver duck", "B) Golden duck", "C) Diamond duck", "D) Pair"],
                        "a": "B) Golden duck",
                        "notes": "A golden duck is out on the first ball. A diamond duck is out without facing a ball (e.g. run out)."
                    },
                    {
                        "q": "Which Springbok coach and Director of Rugby became legendary for using colored disco lights on the stadium roof for tactical communication?",
                        "options": ["A) Jake White", "B) Heyneke Meyer", "C) Peter de Villiers", "D) Rassie Erasmus"],
                        "a": "D) Rassie Erasmus",
                        "notes": "Rassie used green, amber, and red lights from the coaching box to signal strategic plays."
                    },
                    {
                        "q": "Which South African fast bowler was nicknamed the 'Phalaborwa Express' for his blistering pace?",
                        "options": ["A) Dale Steyn", "B) Makhaya Ntini", "C) Kagiso Rabada", "D) Morne Morkel"],
                        "a": "A) Dale Steyn",
                        "notes": "Dale Steyn hailed from Phalaborwa in Limpopo and was the world's number 1 Test bowler for years."
                    }
                ]
            },
            {
                "roundId": 3,
                "title": "Round 3: 80s, 90s & Cult Cinema Legends",
                "badge": "Round 3 • Movies & Pop",
                "theme": "Action Blockbusters, Hollywood Quotes & Cult Classics",
                "difficultyText": "Level 3: Silver Screen Fever",
                "hostVibe": "Movie buffs, time to shine! Encourage team members to shout out the famous movie lines.",
                "questions": [
                    {
                        "q": "In the 1988 action movie Die Hard, what is the name of the Los Angeles skyscraper seized by Hans Gruber?",
                        "options": ["A) Empire Tower", "B) Nakatomi Plaza", "C) Century City Center", "D) Omni Corp Plaza"],
                        "a": "B) Nakatomi Plaza",
                        "notes": "Filmed in the actual Fox Plaza building in Century City, Los Angeles."
                    },
                    {
                        "q": "In Pulp Fiction (1994), what does Vincent Vega tell Jules Winnfield the French call a Quarter Pounder with Cheese?",
                        "options": ["A) Le Big Mac", "B) Royale with Cheese", "C) Fromage Deluxe", "D) Le Double Burger"],
                        "a": "B) Royale with Cheese",
                        "notes": "'Because of the metric system!' Royale with Cheese."
                    },
                    {
                        "q": "In the Back to the Future films, what sports car was modified by Doc Brown into a time-travel machine?",
                        "options": ["A) Pontiac Firebird", "B) Chevrolet Corvette", "C) DeLorean DMC-12", "D) Ford Mustang"],
                        "a": "C) DeLorean DMC-12",
                        "notes": "'If you're gonna build a time machine into a car, why not do it with some style?'"
                    },
                    {
                        "q": "Who played the role of Maximus Decimus Meridius in the 2000 epic blockbuster Gladiator?",
                        "options": ["A) Mel Gibson", "B) Gerard Butler", "C) Russell Crowe", "D) Christian Bale"],
                        "a": "C) Russell Crowe",
                        "notes": "Crowe won the Academy Award for Best Actor for his role."
                    },
                    {
                        "q": "In The Matrix (1999), what color pill does Morpheus offer Neo if he wants to see how deep the rabbit hole goes?",
                        "options": ["A) Blue pill", "B) Red pill", "C) Green pill", "D) Yellow pill"],
                        "a": "B) Red pill",
                        "notes": "Red pill shows the truth of reality; the blue pill lets you wake up in bed believing whatever you want."
                    },
                    {
                        "q": "Which legendary rock band released the monster 1987 hit 'Sweet Child O' Mine' featuring Slash's opening guitar riff?",
                        "options": ["A) Bon Jovi", "B) Guns N' Roses", "C) Motley Crue", "D) Aerosmith"],
                        "a": "B) Guns N' Roses",
                        "notes": "From their diamond-certified debut album Appetite for Destruction."
                    },
                    {
                        "q": "In Jurassic Park (1993), what prehistoric insect trapped in fossilized tree sap provided dinosaur DNA?",
                        "options": ["A) Dragonfly", "B) Beetle", "C) Mosquito", "D) Wasp"],
                        "a": "C) Mosquito",
                        "notes": "A fossilized blood-sucking mosquito preserved in amber."
                    },
                    {
                        "q": "What was the highest-grossing film of the 1990s worldwide, directed by James Cameron?",
                        "options": ["A) Jurassic Park", "B) The Lion King", "C) Titanic", "D) Armageddon"],
                        "a": "C) Titanic",
                        "notes": "Released in 1997, Titanic earned over $2 billion globally and won 11 Oscars."
                    },
                    {
                        "q": "Which hit 1980 South African comedy film followed a Kalahari Bushman journeying to throw a Coca-Cola bottle off the end of the earth?",
                        "options": ["A) The Gods Must Be Crazy", "B) Lipstiek Dipstiek", "C) There's a Zulu On My Stoep", "D) Oh Schucks...! Here Comes UNTAG"],
                        "a": "A) The Gods Must Be Crazy",
                        "notes": "Starring N!xau Toma, it became an international cult sensation and box office phenomenon."
                    },
                    {
                        "q": "Who voiced the wise old mandrill shaman Rafiki in Disney's animated 1994 masterpiece The Lion King?",
                        "options": ["A) James Earl Jones", "B) John Kani", "C) Robert Guillaume", "D) Morgan Freeman"],
                        "a": "C) Robert Guillaume",
                        "notes": "Robert Guillaume voiced Rafiki in the original 1994 animation (John Kani voiced him in the 2019 remake)."
                    }
                ]
            },
            {
                "roundId": 4,
                "title": "Round 4: Braai Master, Biltong & Craft Brews",
                "badge": "Round 4 • Food & Drink",
                "theme": "Coals, Meats, Marinades & Cold Draughts",
                "difficultyText": "Level 4: Braai Boss",
                "hostVibe": "Stir up appetites! Talk cuts of meat, wood choices, and ice cold draughts.",
                "questions": [
                    {
                        "q": "Which whole seed spice is toasted and coarsely crushed as the indispensable core seasoning in traditional boerewors?",
                        "options": ["A) Cumin seed", "B) Coriander seed", "C) Fennel seed", "D) Mustard seed"],
                        "a": "B) Coriander seed",
                        "notes": "Toasted coriander seeds ground with salt, pepper, and nutmeg give boerewors its signature flavor."
                    },
                    {
                        "q": "Which prime beef cut from the hindquarter is most commonly sliced into large slabs for making traditional biltong?",
                        "options": ["A) Ribeye", "B) Silverside", "C) Brisket", "D) Chuck"],
                        "a": "B) Silverside",
                        "notes": "Silverside (and topside) is lean with a consistent grain, ideal for hang-drying."
                    },
                    {
                        "q": "What famous cream liqueur is made using the fruit of the African Marula tree, also loved by elephants?",
                        "options": ["A) Cape Velvet", "B) Amarula", "C) Kahlua", "D) Baileys"],
                        "a": "B) Amarula",
                        "notes": "Amarula Cream Liqueur has been produced in South Africa since 1989."
                    },
                    {
                        "q": "Which invasive Australian acacia wood is prized by Western Cape braai masters for producing blistering hot, long-burning coals?",
                        "options": ["A) Pine", "B) Rooikrans", "C) Bluegum", "D) Jacaranda"],
                        "a": "B) Rooikrans",
                        "notes": "Acacia cyclops (Rooikrans) burns clean and forms intense, long-lasting coals."
                    },
                    {
                        "q": "What essential ingredient in beer brewing imparts crisp bitterness and floral aroma to balance malt sweetness?",
                        "options": ["A) Barley", "B) Yeast", "C) Hops", "D) Wheat"],
                        "a": "C) Hops",
                        "notes": "Hop cones contain alpha acids for bitterness and essential oils for aroma."
                    },
                    {
                        "q": "What is the classic South African sandwich called that is toasted over open braai coals with cheddar cheese, tomato, and onion?",
                        "options": ["A) Roosterkoek", "B) Braaibroodjie", "C) Vetkoek", "D) Gatsby"],
                        "a": "B) Braaibroodjie",
                        "notes": "The holy grail of braai side dishes! Best with a swipe of chutney."
                    },
                    {
                        "q": "Which unique South African red wine cultivar was created in 1925 at Stellenbosch University by crossing Pinot Noir with Cinsault?",
                        "options": ["A) Shiraz", "B) Cabernet Sauvignon", "C) Pinotage", "D) Merlot"],
                        "a": "C) Pinotage",
                        "notes": "Developed by Professor Abraham Izak Perold in 1925."
                    },
                    {
                        "q": "What is widely regarded as the golden rule of cooking a traditional South African potjiekos?",
                        "options": ["A) Add extra water every 10 minutes", "B) Stir the pot vigorously every 15 minutes", "C) Never stir the layers once the lid is closed", "D) Cook on maximum roaring fire"],
                        "a": "C) Never stir the layers once the lid is closed",
                        "notes": "Layers of meat, root veggies, and soft greens steam together in their own juices without stirring."
                    },
                    {
                        "q": "What dark carbonated beverage is the universal, undisputed pairing for Klipdrift or Richelieu brandy in South Africa?",
                        "options": ["A) Pepsi", "B) Coca-Cola", "C) Cream Soda", "D) Tonic Water"],
                        "a": "B) Coca-Cola",
                        "notes": "Klippies & Coke: South Africa's unofficial national highball."
                    },
                    {
                        "q": "What spicy Portuguese-inspired sauce made from crushed African bird's eye chilies is a staple on grilled chicken and chops?",
                        "options": ["A) Chimichurri", "B) Peri-Peri", "C) Hollandaise", "D) Monkey Gland"],
                        "a": "B) Peri-Peri",
                        "notes": "Peri-peri (Pili pili in Swahili) derives from the African bird's eye chili."
                    }
                ]
            },
            {
                "roundId": 5,
                "title": "Round 5: Mzansi Places, Roads & Milestones",
                "badge": "Round 5 • Geography & History",
                "theme": "Highways, Mountain Passes, Borders & Golden Heritage",
                "difficultyText": "Level 5: The Decider Round",
                "hostVibe": "Final regulation round! Tension is high - points here make or break the podium.",
                "questions": [
                    {
                        "q": "Which famous mountain pass with steep gravel switchbacks and 4x4 climbs connects Underberg in KZN to the kingdom of Lesotho?",
                        "options": ["A) Swartberg Pass", "B) Sani Pass", "C) Outeniqua Pass", "D) Chapman's Peak"],
                        "a": "B) Sani Pass",
                        "notes": "Rises to 2,876m altitude; home to the famous Highest Pub in Africa at the top."
                    },
                    {
                        "q": "Which South African coastal city is historically nicknamed 'The Friendly City'?",
                        "options": ["A) East London", "B) Durban", "C) Gqeberha (Port Elizabeth)", "D) George"],
                        "a": "C) Gqeberha (Port Elizabeth)",
                        "notes": "Also known as the Windy City or Die Baai."
                    },
                    {
                        "q": "What is the longest river in South Africa, flowing over 2,200 km before emptying into the Atlantic Ocean at Alexander Bay?",
                        "options": ["A) Vaal River", "B) Limpopo River", "C) Orange River (Gariep)", "D) Tugela River"],
                        "a": "C) Orange River (Gariep)",
                        "notes": "Rises in the Drakensberg mountains and traverses the width of the country."
                    },
                    {
                        "q": "In which province would you find the picturesque trout fishing and whiskey-tasting town of Dullstroom?",
                        "options": ["A) Free State", "B) Mpumalanga", "C) Limpopo", "D) North West"],
                        "a": "B) Mpumalanga",
                        "notes": "Perched high on the Steenkampsberg plateau in Mpumalanga."
                    },
                    {
                        "q": "What is the designated route number of the major national highway connecting Johannesburg to Cape Town via the Karoo?",
                        "options": ["A) N2", "B) N3", "C) N1", "D) N4"],
                        "a": "C) N1",
                        "notes": "The N1 runs from Cape Town through Bloemfontein, Joburg, and Pretoria all the way to Beitbridge."
                    },
                    {
                        "q": "In what year did South Africa host the FIFA World Cup, kicking off with Siphiwe Tshabalala's thunderous opening goal?",
                        "options": ["A) 2006", "B) 2010", "C) 2014", "D) 2018"],
                        "a": "B) 2010",
                        "notes": "11 June 2010 at Soccer City (FNB Stadium)."
                    },
                    {
                        "q": "Which national park on the northern border of South Africa contains the ancient golden rhinoceros archaeological site?",
                        "options": ["A) Golden Gate Highlands", "B) Mapungubwe National Park", "C) Marakele National Park", "D) Addo Elephant Park"],
                        "a": "B) Mapungubwe National Park",
                        "notes": "Mapungubwe was a thriving southern African kingdom in the 13th century."
                    },
                    {
                        "q": "What is the official currency of neighboring Namibia, which is pegged 1:1 with the South African Rand?",
                        "options": ["A) Pula", "B) Namibian Dollar", "C) Lilangeni", "D) Metical"],
                        "a": "B) Namibian Dollar",
                        "notes": "The Namibian Dollar trades at parity (1:1) with the South African Rand."
                    },
                    {
                        "q": "What famous rocky promontory at the south-western tip of the Cape Peninsula is often mistakenly thought to be the southernmost point of Africa?",
                        "options": ["A) Cape Agulhas", "B) Cape of Good Hope", "C) Robben Island", "D) Doringbaai"],
                        "a": "B) Cape of Good Hope",
                        "notes": "Cape Agulhas is the true southernmost point; Cape of Good Hope is the south-westernmost point."
                    },
                    {
                        "q": "In which South African town would you find the world's largest man-made hole excavated by pick and shovel during the diamond rush?",
                        "options": ["A) Welkom", "B) Kimberley", "C) Jagersfontein", "D) Cullinan"],
                        "a": "B) Kimberley",
                        "notes": "The Big Hole (Groot Gat) in Kimberley yielded 2,720 kilograms of diamonds."
                    }
                ]
            },
            {
                "roundId": 6,
                "title": "Sudden-Death Tie-Breakers",
                "badge": "Overtime • Closest Number",
                "theme": "Closest to the Pin Estimations",
                "difficultyText": "Overtime: Closest Estimate Takes The Gold!",
                "hostVibe": "Tied teams: write your number on a slip of paper. Hand it in. Closest number wins!",
                "questions": [
                    {
                        "q": "What was the combined final score of both teams in the 1995 Rugby World Cup final between South Africa and New Zealand?",
                        "options": ["A) 24 points", "B) 27 points", "C) 30 points", "D) 33 points"],
                        "a": "B) 27 points",
                        "notes": "South Africa 15 - New Zealand 12. Total = 27 points."
                    },
                    {
                        "q": "Approximately how many kilometers long is the famous Garden Route coastal driving stretch from Mossel Bay to Storms River?",
                        "options": ["A) 200 km", "B) 300 km", "C) 420 km", "D) 550 km"],
                        "a": "B) 300 km",
                        "notes": "Approximately 300 km of scenic coastline."
                    },
                    {
                        "q": "In what calendar year did SAB open the original Castle Brewery in central Johannesburg?",
                        "options": ["A) 1886", "B) 1895", "C) 1902", "D) 1910"],
                        "a": "B) 1895",
                        "notes": "1895 by brewmaster Charles Glass."
                    }
                ]
            }
        ]
    }

def get_set_3():
    return {
        "setId": 3,
        "setName": "Set 3: Bushveld & Backroads",
        "badge": "Set 3 • Bushveld Masters",
        "theme": "Super Rugby, Rock Anthems, Big Five Wildlife & Safari Roads",
        "rounds": [
            {
                "roundId": 1,
                "title": "Round 1: Rapid-Fire Pub Trivia",
                "badge": "Round 1 • Easy",
                "theme": "Everyday Knowledge, Bar Customs & General Trivia",
                "difficultyText": "Level 1: Quick Warm-Up",
                "hostVibe": "Welcome teams, keep the tempo snappy, and warm up the pencils.",
                "questions": [
                    {
                        "q": "Which fruit is traditionally used to garnish a classic Gin & Tonic cocktail?",
                        "options": ["A) Lime or Lemon", "B) Apple slice", "C) Pineapple wedge", "D) Banana wheel"],
                        "a": "A) Lime or Lemon",
                        "notes": "Crisp lime wedge or slice of lemon is the standard garnish."
                    },
                    {
                        "q": "How many millimeters are there in a standard metric meter?",
                        "options": ["A) 100 mm", "B) 500 mm", "C) 1,000 mm", "D) 10,000 mm"],
                        "a": "C) 1,000 mm",
                        "notes": "1,000 millimeters per meter."
                    },
                    {
                        "q": "Which animal is featured on the famous label of Castle Milk Stout?",
                        "options": ["A) Lion", "B) Black Bull", "C) Rhino", "D) Eagle"],
                        "a": "B) Black Bull",
                        "notes": "The iconic black bull with horns symbolizing rich malt strength."
                    },
                    {
                        "q": "What board game involves buying streets like Mayfair, building green houses, and collecting 200 for passing GO?",
                        "options": ["A) Scrabble", "B) Cluedo", "C) Monopoly", "D) Risk"],
                        "a": "C) Monopoly",
                        "notes": "Monopoly, originally published in its modern form by Parker Brothers in 1935."
                    },
                    {
                        "q": "How many days are there in a leap year?",
                        "options": ["A) 364 days", "B) 365 days", "C) 366 days", "D) 367 days"],
                        "a": "C) 366 days",
                        "notes": "February 29 gives a leap year 366 days."
                    },
                    {
                        "q": "What is the capital city of Australia?",
                        "options": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],
                        "a": "C) Canberra",
                        "notes": "Canberra was selected in 1908 as a compromise between Sydney and Melbourne."
                    },
                    {
                        "q": "In South African slang, if someone says 'nou-nou', roughly when do they mean?",
                        "options": ["A) Never in their lifetime", "B) Sometime in the near or distant future", "C) Right this very millisecond", "D) Exactly at midnight"],
                        "a": "B) Sometime in the near or distant future",
                        "notes": "Nou-nou is generally later than 'nou' (now), but sooner than 'later'!"
                    },
                    {
                        "q": "How many strings does a standard acoustic or electric guitar typically have?",
                        "options": ["A) 4 strings", "B) 5 strings", "C) 6 strings", "D) 7 strings"],
                        "a": "C) 6 strings",
                        "notes": "Tuned E-A-D-G-B-E."
                    },
                    {
                        "q": "Which planet in our solar system is nicknamed 'The Red Planet'?",
                        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Mercury"],
                        "a": "B) Mars",
                        "notes": "Iron oxide (rust) on Mars's surface gives it a reddish hue."
                    },
                    {
                        "q": "What is the main spirit used to make a classic Margarita cocktail?",
                        "options": ["A) Vodka", "B) Gin", "C) Tequila", "D) White Rum"],
                        "a": "C) Tequila",
                        "notes": "Tequila, triple sec, and fresh lime juice, traditionally served with a salted rim."
                    }
                ]
            },
            {
                "roundId": 2,
                "title": "Round 2: World Cups, Derbies & Golf Legends",
                "badge": "Round 2 • Sports Icons",
                "theme": "Golf Majors, Currie Cup Battles & Historic Derbies",
                "difficultyText": "Level 2: Sporting Greats",
                "hostVibe": "Test their sporting memories across golf greens and rugby turf.",
                "questions": [
                    {
                        "q": "Which South African golfer is nicknamed 'The Big Easy' for his smooth, effortless swing?",
                        "options": ["A) Retief Goosen", "B) Ernie Els", "C) Louis Oosthuizen", "D) Charl Schwartzel"],
                        "a": "B) Ernie Els",
                        "notes": "Ernie Els won four Major championships: two US Opens and two Open Championships."
                    },
                    {
                        "q": "Which legendary South African golfer won nine Major championships and is one of only five players to win the career Grand Slam?",
                        "options": ["A) Bobby Locke", "B) Gary Player", "C) Ernie Els", "D) Trevor Immelman"],
                        "a": "B) Gary Player",
                        "notes": "Gary Player: 'The Black Knight', with 9 Major victories."
                    },
                    {
                        "q": "In Super Rugby history, which South African franchise won the championship three times (2007, 2009, 2010)?",
                        "options": ["A) The Sharks", "B) The Stormers", "C) The Bulls", "D) The Lions"],
                        "a": "C) The Bulls",
                        "notes": "The Bulls won thrilling finals under coach Frans Ludeke and captain Victor Matfield."
                    },
                    {
                        "q": "In football (soccer), which two Soweto giants contest the famous 'Soweto Derby'?",
                        "options": ["A) Mamelodi Sundowns & SuperSport United", "B) Kaizer Chiefs & Orlando Pirates", "C) Moroka Swallows & Jomo Cosmos", "D) Cape Town City & Stellenbosch FC"],
                        "a": "B) Kaizer Chiefs & Orlando Pirates",
                        "notes": "One of the most fiercely contested derby matches in world soccer, packing FNB Stadium."
                    },
                    {
                        "q": "Which Springbok flyhalf kicked 100% of his goal kicks across the 2023 Rugby World Cup knockout stage?",
                        "options": ["A) Manie Libbok", "B) Handre Pollard", "C) Elton Jantjies", "D) Damian Willemse"],
                        "a": "B) Handre Pollard",
                        "notes": "Pollard had ice in his veins, slotting winning penalties against France, England, and New Zealand."
                    },
                    {
                        "q": "In cricket, how many runs are awarded when a batsman hits the ball over the boundary rope on the full without bouncing?",
                        "options": ["A) 4 runs", "B) 5 runs", "C) 6 runs", "D) 8 runs"],
                        "a": "C) 6 runs",
                        "notes": "A maximum: 6 runs on the full."
                    },
                    {
                        "q": "Which famous stadium in Durban was renowned for rugby fans braaiing on 'The Shark Tank' outer fields?",
                        "options": ["A) Moses Mabhida Stadium", "B) Kings Park Stadium", "C) Chatsworth Stadium", "D) Sugar Ray Xulu Stadium"],
                        "a": "B) Kings Park Stadium",
                        "notes": "Home of the Sharks rugby team."
                    },
                    {
                        "q": "Which South African swimmer won the Olympic Gold medal in the 100m breaststroke at the 1996 Atlanta Olympics?",
                        "options": ["A) Penny Heyns", "B) Tatjana Smith (Schoenmaker)", "C) Ryk Neethling", "D) Roland Schoeman"],
                        "a": "A) Penny Heyns",
                        "notes": "Penny Heyns made history by winning both the 100m and 200m breaststroke golds in Atlanta."
                    },
                    {
                        "q": "What is the regulation number of holes played in a full round of golf?",
                        "options": ["A) 9 holes", "B) 14 holes", "C) 18 holes", "D) 21 holes"],
                        "a": "C) 18 holes",
                        "notes": "St Andrews in Scotland standardized the 18-hole golf course in 1764."
                    },
                    {
                        "q": "Which country won the inaugural Rugby World Cup in 1987?",
                        "options": ["A) Australia", "B) New Zealand", "C) France", "D) England"],
                        "a": "B) New Zealand",
                        "notes": "The All Blacks defeated France 29-9 at Eden Park, Auckland."
                    }
                ]
            },
            {
                "roundId": 3,
                "title": "Round 3: Rock Anthems & Legendary Cinema",
                "badge": "Round 3 • Music & Movies",
                "theme": "Classic Rockers, Blockbuster Quotes & Action Icons",
                "difficultyText": "Level 3: Anthems & Action",
                "hostVibe": "Sing-alongs encouraged! Play high-energy riffs in between questions.",
                "questions": [
                    {
                        "q": "Which legendary British rock band recorded the operatic masterpiece 'Bohemian Rhapsody' in 1975?",
                        "options": ["A) Led Zeppelin", "B) Queen", "C) The Rolling Stones", "D) The Who"],
                        "a": "B) Queen",
                        "notes": "Fronted by Freddie Mercury, on their album A Night at the Opera."
                    },
                    {
                        "q": "In the 1984 sci-fi action film The Terminator, what is Arnold Schwarzenegger's immortal five-word catchphrase?",
                        "options": ["A) I will find you", "B) I'll be back", "C) Hasta la vista baby", "D) Get to the chopper"],
                        "a": "B) I'll be back",
                        "notes": "'I'll be back' was spoken at the police precinct desk before he drives a car through the front doors."
                    },
                    {
                        "q": "Which South African rock band had huge hits in the late 90s and 2000s with songs like 'Bubblegum On My Sole' and 'Genie'?",
                        "options": ["A) Just Jinger", "B) Springbok Nude Girls", "C) Prime Circle", "D) Wonderboom"],
                        "a": "B) Springbok Nude Girls",
                        "notes": "Fronted by Arno Carstens, formed in Stellenbosch in 1994."
                    },
                    {
                        "q": "In the 1994 Disney animated film The Lion King, what Swahili phrase translates literally to 'No worries'?",
                        "options": ["A) Jambo Bwana", "B) Hakuna Matata", "C) Asante Sana", "D) Karibu Tena"],
                        "a": "B) Hakuna Matata",
                        "notes": "Sung by Timon and Pumbaa."
                    },
                    {
                        "q": "Which Australian hard rock band released the timeless 1980 rock anthem 'Back in Black'?",
                        "options": ["A) INXS", "B) Midnight Oil", "C) AC/DC", "D) Silverchair"],
                        "a": "C) AC/DC",
                        "notes": "Their first album featuring new singer Brian Johnson following Bon Scott's death."
                    },
                    {
                        "q": "In the Lord of the Rings trilogy, what creature continuously refers to the One Ring as 'My Precious'?",
                        "options": ["A) Sauron", "B) Saruman", "C) Gollum", "D) Bilbo Baggins"],
                        "a": "C) Gollum",
                        "notes": "Portrayed by Andy Serkis via groundbreaking motion capture."
                    },
                    {
                        "q": "What British spy's signature cocktail order is a vodka martini, 'shaken, not stirred'?",
                        "options": ["A) Jason Bourne", "B) Austin Powers", "C) James Bond", "D) George Smiley"],
                        "a": "C) James Bond",
                        "notes": "Agent 007 created by author Ian Fleming."
                    },
                    {
                        "q": "Which American singer-songwriter released the record-breaking 1982 album Thriller, featuring 'Beat It' and 'Billie Jean'?",
                        "options": ["A) Prince", "B) Lionel Richie", "C) Michael Jackson", "D) Stevie Wonder"],
                        "a": "C) Michael Jackson",
                        "notes": "Thriller remains the best-selling studio album of all time."
                    },
                    {
                        "q": "In the 1994 hit movie Forrest Gump, what did Forrest's mama always say life was like?",
                        "options": ["A) A bowl of cherries", "B) A box of chocolates", "C) A game of baseball", "D) A river running wild"],
                        "a": "B) A box of chocolates",
                        "notes": "'You never know what you're gonna get.'"
                    },
                    {
                        "q": "Which South African alt-rock band fronted by Francois van Coke created shockwaves in 2003 with their raw Afrikaans punk?",
                        "options": ["A) Van Coke Kartel", "B) Fokofpolisiekar", "C) Straatligkinders", "D) Die Heuwels Fantasties"],
                        "a": "B) Fokofpolisiekar",
                        "notes": "Formed in Bellville, Western Cape in 2003."
                    }
                ]
            },
            {
                "roundId": 4,
                "title": "Round 4: Steaks, Sauces & Cellar Masters",
                "badge": "Round 4 • Food & Drink",
                "theme": "Butcher Cuts, Pub Chow, South African Wine & Distilleries",
                "difficultyText": "Level 4: Culinary Connoisseur",
                "hostVibe": "Pub grub lovers unite. Time to talk steaks, sauces, and fine drinks.",
                "questions": [
                    {
                        "q": "What uniquely South African steakhouse condiment, made with chutney, tomato sauce, and Worcestershire sauce, was invented by Johannesburg chefs in the 1960s?",
                        "options": ["A) Chakalaka", "B) Monkey Gland Sauce", "C) Prego Sauce", "D) Tartar Sauce"],
                        "a": "B) Monkey Gland Sauce",
                        "notes": "Created by overseas hotel chefs at the Carlton Hotel in Johannesburg; contains zero actual monkeys!"
                    },
                    {
                        "q": "Which famous wine-producing town in the Western Cape is renowned for its Cape Dutch architecture and prestigious university?",
                        "options": ["A) Paarl", "B) Franschhoek", "C) Stellenbosch", "D) Robertson"],
                        "a": "C) Stellenbosch",
                        "notes": "Founded in 1679 by Simon van der Stel; South Africa's premier wine center."
                    },
                    {
                        "q": "What is the key difference between biltong and American beef jerky?",
                        "options": ["A) Biltong is cured in vinegar and air-dried; jerky is typically heat-smoked and dried", "B) Biltong is only made from pork", "C) Jerky is never salted", "D) Biltong is deep-fried"],
                        "a": "A) Biltong is cured in vinegar and air-dried; jerky is typically heat-smoked and dried",
                        "notes": "Biltong uses vinegar, salt, and spices, air-drying gently without smoke or artificial cooking."
                    },
                    {
                        "q": "What French term is used for sparkling wines produced in South Africa using the traditional Champagne method?",
                        "options": ["A) Prosecco", "B) Méthode Cap Classique (MCC)", "C) Cava", "D) Spumante"],
                        "a": "B) Méthode Cap Classique (MCC)",
                        "notes": "MCC refers to bottle-fermented sparkling wine made in South Africa."
                    },
                    {
                        "q": "Which cut of steak is famous for featuring a T-shaped bone separating a strip loin from a smaller tenderloin fillet?",
                        "options": ["A) Sirloin", "B) T-Bone Steak", "C) Rump Steak", "D) Tomahawk"],
                        "a": "B) T-Bone Steak",
                        "notes": "A T-bone contains both sirloin and tenderloin fillet on either side of the bone."
                    },
                    {
                        "q": "What sweet dessert, made of a rich spongy cake covered in warm butter-caramel sauce, is a Sunday braai staple in South Africa?",
                        "options": ["A) Melktert", "B) Koeksister", "C) Malva Pudding", "D) Jan Ellis Pudding"],
                        "a": "C) Malva Pudding",
                        "notes": "Contains apricot jam in the batter, soaked in warm sweet cream sauce."
                    },
                    {
                        "q": "In a bar, what spirit forms the alcoholic foundation of an Irish Coffee?",
                        "options": ["A) Irish Whiskey", "B) Scotch Whisky", "C) Bourbon", "D) Dark Rum"],
                        "a": "A) Irish Whiskey",
                        "notes": "Hot black coffee, Irish whiskey, sugar, and float of fresh cream."
                    },
                    {
                        "q": "What popular spicy South African vegetable relish consists of grated carrots, peppers, beans, and curry spices?",
                        "options": ["A) Atchar", "B) Chakalaka", "C) Sambal", "D) Sheba"],
                        "a": "B) Chakalaka",
                        "notes": "Originated in the townships of Johannesburg to accompany pap and braaivleis."
                    },
                    {
                        "q": "Which popular style of beer is characterized by the acronym 'IPA'?",
                        "options": ["A) Imperial Pale Ale", "B) India Pale Ale", "C) Irish Pilsner Ale", "D) International Porter Ale"],
                        "a": "B) India Pale Ale",
                        "notes": "Heavily hopped beer brewed originally in Britain for export to colonial troops in India."
                    },
                    {
                        "q": "What twisted, plaited South African pastry is deep-fried, dipped straight into ice-cold sugar syrup, and eaten cold?",
                        "options": ["A) Koeksister", "B) Vetkoek", "C) Hertzoggie", "D) Churro"],
                        "a": "A) Koeksister",
                        "notes": "Sticky, crunchy, sweet heaven! (The Cape Malay version is a spiced doughnut rolled in coconut)."
                    }
                ]
            },
            {
                "roundId": 5,
                "title": "Round 5: Safari, Wildlife & World Capitals",
                "badge": "Round 5 • Geography & Nature",
                "theme": "The Big Five, National Parks, World Wonders & Capitals",
                "difficultyText": "Level 5: Global Explorer",
                "hostVibe": "Final round before the scoreboard is revealed! Make every point count.",
                "questions": [
                    {
                        "q": "Which five animals traditionally make up Africa's famous 'Big Five'?",
                        "options": [
                            "A) Lion, Leopard, Elephant, Rhino, Buffalo",
                            "B) Lion, Cheetah, Giraffe, Hippo, Zebra",
                            "C) Leopard, Cheetah, Wild Dog, Elephant, Hippo",
                            "D) Lion, Elephant, Rhino, Giraffe, Crocodile"
                        ],
                        "a": "A) Lion, Leopard, Elephant, Rhino, Buffalo",
                        "notes": "Originally coined by big-game hunters as the five most dangerous animals to hunt on foot."
                    },
                    {
                        "q": "What is the capital city of Canada?",
                        "options": ["A) Toronto", "B) Montreal", "C) Ottawa", "D) Vancouver"],
                        "a": "C) Ottawa",
                        "notes": "Ottawa was chosen by Queen Victoria in 1857 as Canada's capital."
                    },
                    {
                        "q": "In which province is the world-renowned Kruger National Park primarily located?",
                        "options": ["A) Limpopo & Mpumalanga", "B) KwaZulu-Natal & Free State", "C) North West & Gauteng", "D) Eastern Cape & Western Cape"],
                        "a": "A) Limpopo & Mpumalanga",
                        "notes": "Stretches across both Limpopo and Mpumalanga along the Mozambique border."
                    },
                    {
                        "q": "What spectacular waterfall on the Zambezi River between Zambia and Zimbabwe is known locally as 'Mosi-oa-Tunya' (The Smoke That Thunders)?",
                        "options": ["A) Tugela Falls", "B) Niagara Falls", "C) Victoria Falls", "D) Iguazu Falls"],
                        "a": "C) Victoria Falls",
                        "notes": "One of the Seven Natural Wonders of the World."
                    },
                    {
                        "q": "What is the highest mountain peak in Africa, located in northeastern Tanzania?",
                        "options": ["A) Mount Kenya", "B) Mount Kilimanjaro", "C) Table Mountain", "D) Drakensberg Thabana Ntlenyana"],
                        "a": "B) Mount Kilimanjaro",
                        "notes": "Stands 5,895 meters above sea level."
                    },
                    {
                        "q": "What is the capital city of France?",
                        "options": ["A) Marseille", "B) Lyon", "C) Paris", "D) Nice"],
                        "a": "C) Paris",
                        "notes": "The City of Light, home to the Eiffel Tower and the Louvre."
                    },
                    {
                        "q": "Which mammal is known as the fastest land animal in the world, capable of sprinting over 100 km/h?",
                        "options": ["A) Springbok", "B) Cheetah", "C) Lion", "D) Blue Wildebeest"],
                        "a": "B) Cheetah",
                        "notes": "Cheetahs can accelerate from 0 to 95 km/h in under 3 seconds."
                    },
                    {
                        "q": "Which South African bay along the Garden Route is renowned globally as one of the best land-based whale-watching spots?",
                        "options": ["A) Plettenberg Bay", "B) Hermanus (Walker Bay)", "C) Saldanha Bay", "D) Jeffreys Bay"],
                        "a": "B) Hermanus (Walker Bay)",
                        "notes": "Southern Right Whales visit Walker Bay in Hermanus from June to November."
                    },
                    {
                        "q": "What is the largest hot desert in the world, stretching across northern Africa?",
                        "options": ["A) Kalahari Desert", "B) Sahara Desert", "C) Gobi Desert", "D) Atacama Desert"],
                        "a": "B) Sahara Desert",
                        "notes": "Spanning over 9 million square kilometers."
                    },
                    {
                        "q": "What famous road along the Atlantic seaboard of Cape Town is carved into the cliffs between Hout Bay and Noordhoek?",
                        "options": ["A) Marine Drive", "B) Chapman's Peak Drive", "C) Victoria Road", "D) Boyes Drive"],
                        "a": "B) Chapman's Peak Drive",
                        "notes": "Affectionately called 'Chappies', featuring 114 curves over 9 kilometers."
                    }
                ]
            },
            {
                "roundId": 6,
                "title": "Sudden-Death Tie-Breakers",
                "badge": "Overtime • Closest Number",
                "theme": "Closest to the Pin Estimations",
                "difficultyText": "Overtime: Closest Estimate Takes The Trophy!",
                "hostVibe": "Captains, write your number clearly on a slip of paper!",
                "questions": [
                    {
                        "q": "How many total kilometers of fence surround the perimeter of the Kruger National Park?",
                        "options": ["A) 650 km", "B) 850 km", "C) 1,000 km", "D) 1,400 km"],
                        "a": "C) 1,000 km",
                        "notes": "Approximately 1,000 km of boundary fencing."
                    },
                    {
                        "q": "In what calendar year did South Africa win its second Rugby World Cup in Paris under captain John Smit?",
                        "options": ["A) 2003", "B) 2007", "C) 2011", "D) 2015"],
                        "a": "B) 2007",
                        "notes": "20 October 2007: Springboks 15 - England 6."
                    },
                    {
                        "q": "How many total test runs did Jacques Kallis score in his international Test cricket career?",
                        "options": ["A) 11,953 runs", "B) 12,410 runs", "C) 13,289 runs", "D) 14,050 runs"],
                        "a": "C) 13,289 runs",
                        "notes": "Jacques Kallis scored 13,289 runs in 166 Test matches."
                    }
                ]
            }
        ]
    }

def get_set_4():
    return {
        "setId": 4,
        "setName": "Set 4: The Biltong & Brandy Classic",
        "badge": "Set 4 • Taproom Master",
        "theme": "Currie Cup, Classic Rock, Kitchen Secrets & World Wonders",
        "rounds": [
            {
                "roundId": 1,
                "title": "Round 1: Taproom Warm-Up & General Quizzing",
                "badge": "Round 1 • Easy",
                "theme": "Pop Culture, Everyday Facts & Bar Humour",
                "difficultyText": "Level 1: Fast Start",
                "hostVibe": "Set the table! Quick easy points to get the spirits high.",
                "questions": [
                    {
                        "q": "In the game of snooker or pool, what color is the cue ball?",
                        "options": ["A) Red", "B) Yellow", "C) White", "D) Black"],
                        "a": "C) White",
                        "notes": "The cue ball is white."
                    },
                    {
                        "q": "How many players are on the field for one team in a standard association football (soccer) match?",
                        "options": ["A) 9 players", "B) 10 players", "C) 11 players", "D) 12 players"],
                        "a": "C) 11 players",
                        "notes": "10 outfield players plus 1 goalkeeper."
                    },
                    {
                        "q": "What spirit is traditionally the base of a classic Mojito cocktail?",
                        "options": ["A) White Rum", "B) Gin", "C) Vodka", "D) Brandy"],
                        "a": "A) White Rum",
                        "notes": "White rum muddled with fresh mint, lime juice, sugar, and club soda."
                    },
                    {
                        "q": "How many degrees are there in a standard right angle?",
                        "options": ["A) 45 degrees", "B) 90 degrees", "C) 180 degrees", "D) 360 degrees"],
                        "a": "B) 90 degrees",
                        "notes": "A right angle is exactly 90 degrees."
                    },
                    {
                        "q": "Which fast food chain is famous for the catchphrase 'Finger Lickin' Good'?",
                        "options": ["A) McDonald's", "B) KFC", "C) Nando's", "D) Steers"],
                        "a": "B) KFC",
                        "notes": "Kentucky Fried Chicken, founded by Colonel Harland Sanders."
                    },
                    {
                        "q": "What is the hardest natural substance known on Earth?",
                        "options": ["A) Titanium", "B) Diamond", "C) Granite", "D) Quartz"],
                        "a": "B) Diamond",
                        "notes": "Diamond rates 10 on the Mohs scale of mineral hardness."
                    },
                    {
                        "q": "What is the term for a score of one under par on a golf hole?",
                        "options": ["A) Eagle", "B) Birdie", "C) Bogey", "D) Albatross"],
                        "a": "B) Birdie",
                        "notes": "One under par = Birdie. Two under par = Eagle."
                    },
                    {
                        "q": "What popular South African maize meal porridge is a mandatory staple at a braai?",
                        "options": ["A) Pap", "B) Samp", "C) Couscous", "D) Polenta"],
                        "a": "A) Pap",
                        "notes": "Mieliepap: crumbly stywepap or smooth slappap served with sheba tomato relish."
                    },
                    {
                        "q": "What is the capital city of Italy?",
                        "options": ["A) Milan", "B) Florence", "C) Rome", "D) Venice"],
                        "a": "C) Rome",
                        "notes": "Rome: The Eternal City."
                    },
                    {
                        "q": "In bowling, what term is used when you knock down all 10 pins with your first roll?",
                        "options": ["A) Spare", "B) Strike", "C) Split", "D) Turkey"],
                        "a": "B) Strike",
                        "notes": "Marked as an 'X' on the scoreboard."
                    }
                ]
            },
            {
                "roundId": 2,
                "title": "Round 2: Super Rugby, Currie Cup & Ashes Clashes",
                "badge": "Round 2 • Sports Battles",
                "theme": "Currie Cup Trophies, Cricket Hat-Tricks & Rugby Derbies",
                "difficultyText": "Level 2: Derby Fever",
                "hostVibe": "Stir up provincial rivalries between the Bulls, Sharks, WP, and Lions!",
                "questions": [
                    {
                        "q": "What prestigious gold trophy has been awarded to the champions of South African provincial rugby since 1892?",
                        "options": ["A) The Super 14 Trophy", "B) The Currie Cup", "C) The Webb Ellis Cup", "D) The Lion Cup"],
                        "a": "B) The Currie Cup",
                        "notes": "Donated by Sir Donald Currie in 1889 to the touring British Isles team."
                    },
                    {
                        "q": "Which cricket ground in Centurion, Pretoria is famous for its grass banks and Boxing Day test matches?",
                        "options": ["A) SuperSport Park", "B) Wanderers Stadium", "C) Kingsmead", "D) St George's Park"],
                        "a": "A) SuperSport Park",
                        "notes": "SuperSport Park Centurion, fortress of the Titans."
                    },
                    {
                        "q": "Which South African rugby legend was named IRB International Player of the Year in 2004?",
                        "options": ["A) Bryan Habana", "B) Schalk Burger", "C) Victor Matfield", "D) Percy Montgomery"],
                        "a": "B) Schalk Burger",
                        "notes": "Schalk Burger won IRB World Player of the Year in 2004 for his incredible loose forward play."
                    },
                    {
                        "q": "In cricket, how many wickets must a bowler take on consecutive deliveries to achieve a 'hat-trick'?",
                        "options": ["A) 2 wickets", "B) 3 wickets", "C) 4 wickets", "D) 5 wickets"],
                        "a": "B) 3 wickets",
                        "notes": "Three wickets on three consecutive balls."
                    },
                    {
                        "q": "Which South African flyhalf scored all of South Africa's 15 points in the 2007 Rugby World Cup final in Paris?",
                        "options": ["A) Percy Montgomery & Francois Steyn", "B) Butch James", "C) Morne Steyn", "D) Handre Pollard"],
                        "a": "A) Percy Montgomery & Francois Steyn",
                        "notes": "Percy Montgomery kicked 4 penalties (12 pts) and Francois Steyn slotted a 50m penalty (3 pts)."
                    },
                    {
                        "q": "What is the famous nickname of the South African national netball team?",
                        "options": ["A) The Proteas (Spar Proteas)", "B) The Banyana", "C) The Springbokkies", "D) The Gazelles"],
                        "a": "A) The Proteas (Spar Proteas)",
                        "notes": "The SPAR Proteas represent South Africa in international netball."
                    },
                    {
                        "q": "Which South African winger set the joint record for the most tries scored in Rugby World Cup history (15 tries, tied with Jonah Lomu)?",
                        "options": ["A) Cheslin Kolbe", "B) Breyton Paulse", "C) Bryan Habana", "D) JP Pietersen"],
                        "a": "C) Bryan Habana",
                        "notes": "Habana scored 8 tries in 2007, 2 in 2011, and 5 in 2015."
                    },
                    {
                        "q": "Which test cricket ground in Port Elizabeth (Gqeberha) is world-famous for its brass band playing in the stands?",
                        "options": ["A) St George's Park", "B) Kingsmead", "C) Newlands", "D) Mangaung Oval"],
                        "a": "A) St George's Park",
                        "notes": "The St George's Park Brass Band has entertained test crowds for decades."
                    },
                    {
                        "q": "What is the nickname of the national men's soccer team of South Africa?",
                        "options": ["A) Bafana Bafana", "B) Banyana Banyana", "C) AmaGlug-glug", "D) The Indomitable Lions"],
                        "a": "A) Bafana Bafana",
                        "notes": "'The Boys, The Boys' in Zulu."
                    },
                    {
                        "q": "Which Formula One team did South African driver Jody Scheckter drive for when he won the F1 World Championship in 1979?",
                        "options": ["A) McLaren", "B) Ferrari", "C) Williams", "D) Lotus"],
                        "a": "B) Ferrari",
                        "notes": "Scheckter won the 1979 Drivers' Championship driving the Ferrari 312T4."
                    }
                ]
            },
            {
                "roundId": 3,
                "title": "Round 3: Radio Hits, One-Hit Wonders & Golden Oldies",
                "badge": "Round 3 • Music Legends",
                "theme": "Chart Toppers, 80s Synthesizers & Sing-Along Anthems",
                "difficultyText": "Level 3: Golden Ears",
                "hostVibe": "Hum the tunes, get toes tapping, and test their radio memories.",
                "questions": [
                    {
                        "q": "Which American rock band had a massive global hit in 1982 with the song 'Africa'?",
                        "options": ["A) Foreigner", "B) Toto", "C) Journey", "D) Boston"],
                        "a": "B) Toto",
                        "notes": "'I bless the rains down in Africa...' released on the Toto IV album."
                    },
                    {
                        "q": "Who sang the iconic 1984 pop anthem 'Summer of '69'?",
                        "options": ["A) Bruce Springsteen", "B) Bryan Adams", "C) Tom Petty", "D) John Mellencamp"],
                        "a": "B) Bryan Adams",
                        "notes": "Canadian rocker Bryan Adams from his album Reckless."
                    },
                    {
                        "q": "What legendary British singer and songwriter was born Farrokh Bulsara in Zanzibar?",
                        "options": ["A) David Bowie", "B) Elton John", "C) Freddie Mercury", "D) George Michael"],
                        "a": "C) Freddie Mercury",
                        "notes": "Freddie Mercury of Queen, born in Stone Town, Zanzibar in 1946."
                    },
                    {
                        "q": "Which South African music legend was affectionately known as 'The White Zulu' and co-founded the bands Juluka and Savuka?",
                        "options": ["A) Johnny Clegg", "B) Sipho Mchunu", "C) David Kramer", "D) PJ Powers"],
                        "a": "A) Johnny Clegg",
                        "notes": "Johnny Clegg OBE, creator of 'Asimbonanga' and 'Scatterlings of Africa'."
                    },
                    {
                        "q": "Which Swedish pop group won the Eurovision Song Contest in 1974 with the song 'Waterloo'?",
                        "options": ["A) Roxette", "B) ABBA", "C) Ace of Base", "D) A-ha"],
                        "a": "B) ABBA",
                        "notes": "Agnetha, Björn, Benny, and Anni-Frid."
                    },
                    {
                        "q": "In the 1980 hit song 'Don't Stop Believin'', which American band tells the story of a small-town girl and a city boy?",
                        "options": ["A) REO Speedwagon", "B) Journey", "C) Kansas", "D) Chicago"],
                        "a": "B) Journey",
                        "notes": "Featuring Steve Perry's soaring lead vocals."
                    },
                    {
                        "q": "What was the title of South African singer Kurt Darren's mega-hit Afrikaans party anthem released in 2002 that had everyone doing the line-dance?",
                        "options": ["A) Kaptein", "B) Meisie Meisie", "C) Loslappie", "D) Hemel Op Tafelberg"],
                        "a": "B) Meisie Meisie",
                        "notes": "'Meisie Meisie' became an absolute countrywide craze at weddings and bars."
                    },
                    {
                        "q": "Which British band released the critically acclaimed 1997 album OK Computer featuring 'Karma Police'?",
                        "options": ["A) Oasis", "B) Blur", "C) Radiohead", "D) Pulp"],
                        "a": "C) Radiohead",
                        "notes": "Fronted by Thom Yorke."
                    },
                    {
                        "q": "Which American rock icon was known as 'The Boss' and released the 1984 smash hit album Born in the U.S.A.?",
                        "options": ["A) Bob Dylan", "B) Bruce Springsteen", "C) Neil Young", "D) Billy Joel"],
                        "a": "B) Bruce Springsteen",
                        "notes": "Bruce Springsteen and the E Street Band."
                    },
                    {
                        "q": "What hit 1991 Metallica song begins with James Hetfield whispering 'Say your prayers, little one'?",
                        "options": ["A) Nothing Else Matters", "B) Master of Puppets", "C) Enter Sandman", "D) The Unforgiven"],
                        "a": "C) Enter Sandman",
                        "notes": "Lead single from Metallica's legendary self-titled 'Black Album'."
                    }
                ]
            },
            {
                "roundId": 4,
                "title": "Round 4: Bar Snacks, Spirits & Kitchen Myths",
                "badge": "Round 4 • Drinks & Grub",
                "theme": "Distilled Spirits, Pub Snacks, Brewing & Kitchen Trivia",
                "difficultyText": "Level 4: Bar Science",
                "hostVibe": "Test their bar literacy and food wisdom.",
                "questions": [
                    {
                        "q": "What is the primary agricultural grain used to produce traditional single malt Scotch whisky?",
                        "options": ["A) Wheat", "B) Corn (Maize)", "C) Malted Barley", "D) Rye"],
                        "a": "C) Malted Barley",
                        "notes": "By law, single malt Scotch must be made exclusively from 100% malted barley."
                    },
                    {
                        "q": "Which famous South African brandy has an export gold medal label depicting a clock face set to 8:20?",
                        "options": ["A) Richelieu", "B) Klipdrift Export", "C) Oude Meester", "D) Viceroy"],
                        "a": "B) Klipdrift Export",
                        "notes": "Klipdrift Export: 'Met eish, ja!' The clock on the label is famously set at 8:20."
                    },
                    {
                        "q": "What plant does authentic Tequila have to be distilled from?",
                        "options": ["A) Blue Agave", "B) Cactus", "C) Sugar Cane", "D) Yucca"],
                        "a": "A) Blue Agave",
                        "notes": "Specifically Blue Weber Agave in the designated state of Jalisco, Mexico."
                    },
                    {
                        "q": "Which famous street-food loaf stuffed with hot slap chips, polony or steak, and sauce originated in Cape Town's Athlone area?",
                        "options": ["A) Bunny Chow", "B) Gatsby", "C) Vetkoek Burger", "D) Dagwood"],
                        "a": "B) Gatsby",
                        "notes": "The Gatsby: a giant foot-long crusty roll stuffed with chips and meat, built to share."
                    },
                    {
                        "q": "What Durban Indian street-food delicacy consists of a hollowed-out quarter loaf of white bread filled with spicy curry?",
                        "options": ["A) Roti Roll", "B) Samosa", "C) Bunny Chow", "D) Biryani"],
                        "a": "C) Bunny Chow",
                        "notes": "Originated in Durban in the 1940s among Indian migrant laborers."
                    },
                    {
                        "q": "In South Africa, what is the colloquial term for small, thin, dry strips of biltong often flavored with chili?",
                        "options": ["A) Cabanossi", "B) Snapsticks / Chilli Sticks", "C) Crackling", "D) Jerky"],
                        "a": "B) Snapsticks / Chilli Sticks",
                        "notes": "Snapsticks: thin dried strips that snap when bent."
                    },
                    {
                        "q": "What is the botanical herb that gives absinthe and ouzo their distinctive aniseed / licorice flavor?",
                        "options": ["A) Coriander", "B) Aniseed / Star Anise", "C) Rosemary", "D) Tarragon"],
                        "a": "B) Aniseed / Star Anise",
                        "notes": "Aniseed contains anethole, which turns cloudy (the louche effect) when water is added."
                    },
                    {
                        "q": "What type of pastry is used to create traditional South African baked custard melktert (milk tart)?",
                        "options": ["A) Puff pastry or sweet shortcrust", "B) Filo pastry", "C) Choux pastry", "D) Sourdough"],
                        "a": "A) Puff pastry or sweet shortcrust",
                        "notes": "Dusting ground cinnamon on top of the baked custard is non-negotiable!"
                    },
                    {
                        "q": "Which South African craft gin distillery in the Karoo town of Richmond is famous for distilling botanicals from indigenous fynbos and wild juniper?",
                        "options": ["A) Inverroche", "B) Musgrave", "C) KWV", "D) Wilderer"],
                        "a": "A) Inverroche",
                        "notes": "Inverroche pioneered the use of Cape fynbos in craft gin production."
                    },
                    {
                        "q": "What is the name of the German beer purity law dating back to 1516 that limited beer ingredients to water, barley, and hops?",
                        "options": ["A) Reinheitsgebot", "B) Oktoberfest Verordnung", "C) Biergesetz", "D) Braumeister Regel"],
                        "a": "A) Reinheitsgebot",
                        "notes": "The Bavarian Reinheitsgebot of 1516."
                    }
                ]
            },
            {
                "roundId": 5,
                "title": "Round 5: Famous Landmarks, Oceans & Road Trips",
                "badge": "Round 5 • Geography & Roads",
                "theme": "South African Escarpments, World Oceans & Scenic Highways",
                "difficultyText": "Level 5: Road Warrior",
                "hostVibe": "Final round before the winners are determined! Everything on the line.",
                "questions": [
                    {
                        "q": "What is the name of the colossal green canyon along Mpumalanga's Panorama Route, recognized as the third largest canyon on Earth?",
                        "options": ["A) Fish River Canyon", "B) Blyde River Canyon", "C) Oribi Gorge", "D) Sundays River Gorge"],
                        "a": "B) Blyde River Canyon",
                        "notes": "Famous for the Three Rondavels and God's Window."
                    },
                    {
                        "q": "What ocean lies directly to the east of South Africa, carrying the warm Agulhas Current down the coastline?",
                        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Pacific Ocean", "D) Southern Ocean"],
                        "a": "B) Indian Ocean",
                        "notes": "The warm Indian Ocean washes the KwaZulu-Natal and Eastern Cape shores."
                    },
                    {
                        "q": "Which massive meteorite impact crater, located near Parys in the Free State, is the oldest and largest verified impact crater on Earth?",
                        "options": ["A) Tswaing Crater", "B) Vredefort Dome", "C) Barringer Crater", "D) Chicxulub Crater"],
                        "a": "B) Vredefort Dome",
                        "notes": "A UNESCO World Heritage Site formed over 2 billion years ago."
                    },
                    {
                        "q": "What is the official judicial capital of South Africa, where the Supreme Court of Appeal is located?",
                        "options": ["A) Pretoria", "B) Cape Town", "C) Bloemfontein", "D) Johannesburg"],
                        "a": "C) Bloemfontein",
                        "notes": "Bloemfontein (Judicial), Pretoria (Administrative), Cape Town (Legislative)."
                    },
                    {
                        "q": "What is the largest island in the world that is not a continent?",
                        "options": ["A) Madagascar", "B) Greenland", "C) Borneo", "D) New Guinea"],
                        "a": "B) Greenland",
                        "notes": "Greenland covers over 2.1 million square kilometers."
                    },
                    {
                        "q": "Which mountain range forms the border between France and Spain?",
                        "options": ["A) The Alps", "B) The Pyrenees", "C) The Carpathians", "D) The Apennines"],
                        "a": "B) The Pyrenees",
                        "notes": "The Pyrenees stretch between the Bay of Biscay and the Mediterranean Sea."
                    },
                    {
                        "q": "What famous island in Table Bay was used as a maximum-security prison where Nelson Mandela spent 18 of his 27 years in captivity?",
                        "options": ["A) Seal Island", "B) Dassen Island", "C) Robben Island", "D) Marion Island"],
                        "a": "C) Robben Island",
                        "notes": "'Robben' means seals in Dutch. Now a UNESCO World Heritage site."
                    },
                    {
                        "q": "Which South African province is the largest in geographic land area?",
                        "options": ["A) Eastern Cape", "B) Northern Cape", "C) Western Cape", "D) Free State"],
                        "a": "B) Northern Cape",
                        "notes": "The Northern Cape accounts for nearly 31% of South Africa's total land area."
                    },
                    {
                        "q": "What is the capital city of Japan?",
                        "options": ["A) Kyoto", "B) Osaka", "C) Tokyo", "D) Hiroshima"],
                        "a": "C) Tokyo",
                        "notes": "Tokyo is the world's most populous metropolitan area."
                    },
                    {
                        "q": "What major dam on the Orange River is the largest reservoir dam in South Africa by water volume?",
                        "options": ["A) Vaal Dam", "B) Gariep Dam", "C) Vanderkloof Dam", "D) Hartbeespoort Dam"],
                        "a": "B) Gariep Dam",
                        "notes": "Formerly the Hendrik Verwoerd Dam, holding over 5.3 billion cubic meters of water."
                    }
                ]
            },
            {
                "roundId": 6,
                "title": "Sudden-Death Tie-Breakers",
                "badge": "Overtime • Closest Number",
                "theme": "Closest to the Pin Estimations",
                "difficultyText": "Overtime: Closest Number Wins!",
                "hostVibe": "Tied teams: write down your estimate!",
                "questions": [
                    {
                        "q": "In what calendar year did the Vredefort asteroid hit Earth?",
                        "options": ["A) 500 million years ago", "B) 1.2 billion years ago", "C) 2.02 billion years ago", "D) 3.5 billion years ago"],
                        "a": "C) 2.02 billion years ago",
                        "notes": "Estimated at 2.023 billion years ago."
                    },
                    {
                        "q": "How many total test matches did Percy Montgomery play for the Springboks?",
                        "options": ["A) 88 caps", "B) 102 caps", "C) 110 caps", "D) 124 caps"],
                        "a": "B) 102 caps",
                        "notes": "Montgomery was the first Springbok in history to reach 100 test caps."
                    },
                    {
                        "q": "What is the maximum water capacity of Gariep Dam in billions of cubic meters?",
                        "options": ["A) 2.5 billion m³", "B) 5.3 billion m³", "C) 8.1 billion m³", "D) 12.0 billion m³"],
                        "a": "B) 5.3 billion m³",
                        "notes": "Gariep Dam holds approximately 5.34 billion cubic meters."
                    }
                ]
            }
        ]
    }

if __name__ == '__main__':
    print("Testing Set 2, 3, 4 generation...")
    s2 = get_set_2()
    s3 = get_set_3()
    s4 = get_set_4()
    for s in [s2, s3, s4]:
        print(f"{s['setName']}: {len(s['rounds'])} rounds")
        for r in s['rounds']:
            print(f"  Round {r['roundId']}: {len(r['questions'])} questions")
