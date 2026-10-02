# -*- coding: utf-8 -*-
import json

def get_set_5():
    return {
        "setId": 5,
        "setName": "Set 5: Champions & Chommies",
        "badge": "Set 5 • Gold & Glory",
        "theme": "Olympic Gold, Motorsport, Iconic Inventions & Braai Customs",
        "rounds": [
            {
                "roundId": 1,
                "title": "Round 1: Easy Pints & Everyday Smarts",
                "badge": "Round 1 • Easy",
                "theme": "Everyday Trivia, Currencies & Pub Culture",
                "difficultyText": "Level 1: Fast Points",
                "hostVibe": "Welcome teams, pass the snacks, and start the scoreboard ticking.",
                "questions": [
                    {
                        "q": "What is the standard unit of currency used in the United Kingdom?",
                        "options": ["A) Euro", "B) British Pound Sterling", "C) Franc", "D) Dollar"],
                        "a": "B) British Pound Sterling",
                        "notes": "Pound Sterling (£)."
                    },
                    {
                        "q": "How many centimeters are there in a standard meter?",
                        "options": ["A) 10 cm", "B) 100 cm", "C) 1,000 cm", "D) 10,000 cm"],
                        "a": "B) 100 cm",
                        "notes": "100 centimeters = 1 meter."
                    },
                    {
                        "q": "What is the traditional ingredient that gives beer its natural fizz and alcohol during fermentation?",
                        "options": ["A) Yeast", "B) Hops", "C) Sugar syrup", "D) Barley malt"],
                        "a": "A) Yeast",
                        "notes": "Yeast consumes sugars and converts them into ethanol and carbon dioxide."
                    },
                    {
                        "q": "Which popular South African draught beer is famous for the advertising slogan 'Champion Men Deserve Champion Beer'?",
                        "options": ["A) Castle Lager", "B) Carling Black Label", "C) Hansa Pilsener", "D) Amstel Lager"],
                        "a": "B) Carling Black Label",
                        "notes": "Carling Black Label: 'Zamalek' or 'The Black Bull'."
                    },
                    {
                        "q": "How many sides does a standard stop sign have on South African roads?",
                        "options": ["A) 6 sides (Hexagon)", "B) 8 sides (Octagon)", "C) 10 sides (Decagon)", "D) 12 sides"],
                        "a": "B) 8 sides (Octagon)",
                        "notes": "An eight-sided octagon."
                    },
                    {
                        "q": "In golf, what is the term used for when a player finishes a hole two strokes over par?",
                        "options": ["A) Bogey", "B) Double Bogey", "C) Birdie", "D) Eagle"],
                        "a": "B) Double Bogey",
                        "notes": "One over = Bogey; two over = Double Bogey."
                    },
                    {
                        "q": "What is the common English name for the constellation called the 'Suiderkruis' in Afrikaans?",
                        "options": ["A) Orion's Belt", "B) The Southern Cross", "C) The Big Dipper", "D) Ursa Major"],
                        "a": "B) The Southern Cross",
                        "notes": "Crux, depicted on flags of Australia, New Zealand, Brazil, and Samoa."
                    },
                    {
                        "q": "Which popular board game challenges players to solve a murder in Tudor Mansion involving Colonel Mustard and Mrs White?",
                        "options": ["A) Cluedo", "B) Battleship", "C) Risk", "D) Stratego"],
                        "a": "A) Cluedo",
                        "notes": "Created in Birmingham, England by Anthony E. Pratt in 1944."
                    },
                    {
                        "q": "What gas makes up approximately 78% of the Earth's atmosphere?",
                        "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Argon"],
                        "a": "B) Nitrogen",
                        "notes": "Nitrogen ~78%, Oxygen ~21%, Argon ~0.9%."
                    },
                    {
                        "q": "Which fruit is dried in the sun to become a raisin?",
                        "options": ["A) Plum", "B) Grape", "C) Fig", "D) Apricot"],
                        "a": "B) Grape",
                        "notes": "Sun-dried grapes become raisins (or sultanas)."
                    }
                ]
            },
            {
                "roundId": 2,
                "title": "Round 2: Olympic Gold, Motorsport & Gridiron",
                "badge": "Round 2 • Champions",
                "theme": "Speed, Wheels, Rings & Grand Prix Champions",
                "difficultyText": "Level 2: High Octane",
                "hostVibe": "Rev up the engines! Sports fanatics will love this one.",
                "questions": [
                    {
                        "q": "Which South African motorcycle racer won the Moto3 World Championship in 2016 and now competes for Red Bull KTM Factory Racing in MotoGP?",
                        "options": ["A) Brad Binder", "B) Darryn Binder", "C) Greg Albertyn", "D) Giniel de Villiers"],
                        "a": "A) Brad Binder",
                        "notes": "Brad Binder from Krugersdorp: known for his fearless braking and MotoGP race wins."
                    },
                    {
                        "q": "Which South African swimmer stunned the world by defeating Michael Phelps to win Olympic Gold in the 200m butterfly at the 2012 London Olympics?",
                        "options": ["A) Cameron van der Burgh", "B) Chad le Clos", "C) Ryk Neethling", "D) Roland Schoeman"],
                        "a": "B) Chad le Clos",
                        "notes": "Chad le Clos won by 0.05 seconds in a dramatic finish."
                    },
                    {
                        "q": "At which iconic South African motorsport circuit outside Johannesburg was the South African Formula One Grand Prix historically held?",
                        "options": ["A) Killarney Raceway", "B) Kyalami Grand Prix Circuit", "C) Zwartkops Raceway", "D) Phakisa Freeway"],
                        "a": "B) Kyalami Grand Prix Circuit",
                        "notes": "Kyalami hosted the South African Grand Prix from 1967 to 1993."
                    },
                    {
                        "q": "Which South African off-road rally driver won the prestigious Dakar Rally in 2009 driving for Volkswagen?",
                        "options": ["A) Giniel de Villiers", "B) Alfie Cox", "C) Sarel van der Merwe", "D) Brian Capper"],
                        "a": "A) Giniel de Villiers",
                        "notes": "Giniel de Villiers won the 2009 Dakar Rally alongside co-driver Dirk von Zitzewitz."
                    },
                    {
                        "q": "How many gold medals did South African swimming legend Tatjana Smith (Schoenmaker) win across the Tokyo 2020 and Paris 2024 Olympic Games?",
                        "options": ["A) 1 Gold", "B) 2 Golds", "C) 3 Golds", "D) 4 Golds"],
                        "a": "B) 2 Golds",
                        "notes": "Gold in 200m breaststroke (Tokyo) and Gold in 100m breaststroke (Paris)."
                    },
                    {
                        "q": "In rugby union, what penalty is awarded against a team when a forward intentionally collapses a scrum?",
                        "options": ["A) Free kick", "B) Full Penalty Kick", "C) Scrum reset", "D) Yellow card only"],
                        "a": "B) Full Penalty Kick",
                        "notes": "Collapsing a scrum is dangerous play resulting in a full penalty kick."
                    },
                    {
                        "q": "Which legendary rally and circuit driver, known affectionately as 'SuperVan', won 11 South African National Rally Championships?",
                        "options": ["A) Giniel de Villiers", "B) Sarel van der Merwe", "C) Serge Damseaux", "D) Jan Hettema"],
                        "a": "B) Sarel van der Merwe",
                        "notes": "Sarel van der Merwe: an icon of South African motorsport."
                    },
                    {
                        "q": "In cricket, what is the maximum number of overs a single bowler can bowl in an official 50-over One Day International?",
                        "options": ["A) 8 overs", "B) 10 overs", "C) 12 overs", "D) 15 overs"],
                        "a": "B) 10 overs",
                        "notes": "10 overs per bowler in a 50-over match."
                    },
                    {
                        "q": "Which South African middle-distance runner won Olympic Gold in the women's 800m at both London 2012 and Rio 2016?",
                        "options": ["A) Caster Semenya", "B) Zola Budd", "C) Elana Meyer", "D) Sunette Viljoen"],
                        "a": "A) Caster Semenya",
                        "notes": "Caster Semenya dominated the 800m world stage."
                    },
                    {
                        "q": "What are the five colors of the Olympic rings?",
                        "options": [
                            "A) Blue, Yellow, Black, Green, Red",
                            "B) Blue, Red, White, Green, Gold",
                            "C) Purple, Yellow, Black, Orange, Green",
                            "D) Red, Blue, White, Yellow, Black"
                        ],
                        "a": "A) Blue, Yellow, Black, Green, Red",
                        "notes": "Blue, Yellow, Black, Green, and Red on a white background."
                    }
                ]
            },
            {
                "roundId": 3,
                "title": "Round 3: Action Heroes, Sci-Fi & TV Sitcoms",
                "badge": "Round 3 • TV & Cinema",
                "theme": "Hollywood Blockbusters, Cult Series & Classic Sitcoms",
                "difficultyText": "Level 3: Prime Time",
                "hostVibe": "Quote along! Everyone remembers these iconic TV and film moments.",
                "questions": [
                    {
                        "q": "In the hit 80s TV series The A-Team, what was B.A. Baracus's greatest fear that required Hannibal to drug him before flights?",
                        "options": ["A) Spiders", "B) Flying in airplanes", "C) Swimming in deep water", "D) Heights"],
                        "a": "B) Flying in airplanes",
                        "notes": "'I ain't gettin' on no plane, Hannibal!'"
                    },
                    {
                        "q": "Which 1999 sci-fi movie starring Keanu Reeves introduced the iconic slow-motion visual effect known as 'bullet time'?",
                        "options": ["A) Speed", "B) The Matrix", "C) Point Break", "D) Constantine"],
                        "a": "B) The Matrix",
                        "notes": "Directed by the Wachowskis, winning 4 Academy Awards."
                    },
                    {
                        "q": "In the sitcom Seinfeld, what holiday was invented by George Costanza's father Frank as an alternative to Christmas?",
                        "options": ["A) Festivus", "B) Costanzamas", "C) Serenity Now", "D) Winterpalooza"],
                        "a": "A) Festivus",
                        "notes": "'Festivus for the rest of us!' Featuring the airing of grievances and feats of strength."
                    },
                    {
                        "q": "Which action star played John Rambo in the First Blood movie series?",
                        "options": ["A) Arnold Schwarzenegger", "B) Sylvester Stallone", "C) Jean-Claude Van Damme", "D) Bruce Willis"],
                        "a": "B) Sylvester Stallone",
                        "notes": "Sylvester Stallone also co-wrote the screenplay."
                    },
                    {
                        "q": "In Star Wars, what is the name of Han Solo's modified Corellian smuggling spaceship?",
                        "options": ["A) Star Destroyer", "B) Millennium Falcon", "C) X-Wing", "D) Slave I"],
                        "a": "B) Millennium Falcon",
                        "notes": "'She made the Kessel Run in less than twelve parsecs.'"
                    },
                    {
                        "q": "Which television secret agent was famous for disarming bombs using a Swiss Army knife, paperclips, and duct tape?",
                        "options": ["A) James Bond", "B) Angus MacGyver", "C) Ethan Hunt", "D) Maxwell Smart"],
                        "a": "B) Angus MacGyver",
                        "notes": "Played by Richard Dean Anderson in the 1985 series."
                    },
                    {
                        "q": "In the animated sitcom The Simpsons, what is Homer Simpson's favorite brand of beer?",
                        "options": ["A) Duff Beer", "B) Buzz Cola", "C) Red Tick Ale", "D) Fud Beer"],
                        "a": "A) Duff Beer",
                        "notes": "Served on tap by Moe Szyslak at Moe's Tavern."
                    },
                    {
                        "q": "Who directed the 1993 epic World War II drama Schindler's List?",
                        "options": ["A) James Cameron", "B) Steven Spielberg", "C) Martin Scorsese", "D) Ridley Scott"],
                        "a": "B) Steven Spielberg",
                        "notes": "Won seven Academy Awards including Best Director and Best Picture."
                    },
                    {
                        "q": "In the film Braveheart (1995), what famous word does Mel Gibson's character shout before his execution?",
                        "options": ["A) Victory!", "B) Scotland!", "C) Freedom!", "D) Never!"],
                        "a": "C) Freedom!",
                        "notes": "William Wallace shouting 'Freedom!' with his final breath."
                    },
                    {
                        "q": "What British television comedy featured Rowan Atkinson as a bumbling, silent character driving a green Mini Cooper?",
                        "options": ["A) Blackadder", "B) Fawlty Towers", "C) Mr. Bean", "D) Only Fools and Horses"],
                        "a": "C) Mr. Bean",
                        "notes": "First broadcast on ITV in January 1990."
                    }
                ]
            },
            {
                "roundId": 4,
                "title": "Round 4: Meat on the Coals, Sauces & Breweries",
                "badge": "Round 4 • Braai Lore",
                "theme": "Braai Etiquette, Skewers, Craft Ales & Sweet Treats",
                "difficultyText": "Level 4: Fire & Spice",
                "hostVibe": "Passionate debates on braai methods! Keep it friendly.",
                "questions": [
                    {
                        "q": "What traditional South African bread dough is shaped into round balls and baked directly over the braai grid?",
                        "options": ["A) Vetkoek", "B) Roosterkoek", "C) Mosbolletjie", "D) Potbrood"],
                        "a": "B) Roosterkoek",
                        "notes": "Roosterkoek is baked on the braai grid until golden and hollow-sounding when tapped."
                    },
                    {
                        "q": "What are skewers of marinated lamb or beef cubes interleaved with dried apricots and onions called in South Africa?",
                        "options": ["A) Kebab", "B) Sosaties", "C) Satay", "D) Yakitori"],
                        "a": "B) Sosaties",
                        "notes": "From Cape Malay tradition: seasoned with curry, tamarind, and turmeric."
                    },
                    {
                        "q": "Which Namibian beer, brewed under the German Purity Law with only malted barley, hops, and water, is famous across South Africa?",
                        "options": ["A) Windhoek Lager", "B) Tafel Lager", "C) Castle Draught", "D) Hansa Pilsener"],
                        "a": "A) Windhoek Lager",
                        "notes": "Brewed by Namibia Breweries Limited in Windhoek since 1920."
                    },
                    {
                        "q": "What is the traditional South African sweet confection made of a tart pastry crust filled with baked custard and dusted with cinnamon?",
                        "options": ["A) Koeksister", "B) Hertzoggie", "C) Melktert (Milk Tart)", "D) Malva Pudding"],
                        "a": "C) Melktert (Milk Tart)",
                        "notes": "Melktert: smooth, cinnamon-dusted custard perfection."
                    },
                    {
                        "q": "What is the term used in wine tasting for the aroma profile of an aged wine as opposed to a young wine?",
                        "options": ["A) Nose", "B) Bouquet", "C) Body", "D) Tannin"],
                        "a": "B) Bouquet",
                        "notes": "Aroma relates to the grape variety; bouquet develops with bottle aging."
                    },
                    {
                        "q": "Which cut of pork spare ribs is characterized by meat attached to the lower breastbone, trimmed into a neat rectangular rack?",
                        "options": ["A) Baby Back Ribs", "B) St. Louis Cut / Belly Ribs", "C) Pork Chops", "D) Pork Loin"],
                        "a": "B) St. Louis Cut / Belly Ribs",
                        "notes": "St. Louis cut ribs are meatier and flatter than baby backs."
                    },
                    {
                        "q": "What popular South African lager, introduced in 1994, is marketed as low-carb and extra cold?",
                        "options": ["A) Castle Lite", "B) Amstel Lite", "C) Windhoek Light", "D) Flying Fish"],
                        "a": "A) Castle Lite",
                        "notes": "'Extra Cold' lager with ice-cold thermochromatic packaging."
                    },
                    {
                        "q": "What sweet jam is traditionally spread inside a braaibroodjie to give it a hint of sweetness against the cheese and onion?",
                        "options": ["A) Strawberry jam", "B) Mrs Ball's Chutney or Apricot jam", "C) Marmalade", "D) Fig preserve"],
                        "a": "B) Mrs Ball's Chutney or Apricot jam",
                        "notes": "Mrs Ball's Chutney or a touch of smooth apricot jam elevates the braaibroodjie."
                    },
                    {
                        "q": "What dark beer style originated in London in the early 18th century as a hearty drink favored by street and river porters?",
                        "options": ["A) Stout", "B) Porter", "C) Bock", "D) Amber Ale"],
                        "a": "B) Porter",
                        "notes": "Named after the street and river porters who loaded cargo along the Thames."
                    },
                    {
                        "q": "What spice gives South African Cape Malay curries, bobotie, and yellow rice their distinctive vibrant yellow color?",
                        "options": ["A) Saffron", "B) Turmeric (Borrie)", "C) Paprika", "D) Cardamom"],
                        "a": "B) Turmeric (Borrie)",
                        "notes": "Turmeric (known locally as borrie) imparts warm earthy flavor and rich golden color."
                    }
                ]
            },
            {
                "roundId": 5,
                "title": "Round 5: World History, Inventions & Discoveries",
                "badge": "Round 5 • History & Inventions",
                "theme": "South African Breakthroughs, Space Races & World Wonders",
                "difficultyText": "Level 5: Brain Buster",
                "hostVibe": "Final round of the set! Determine the champions.",
                "questions": [
                    {
                        "q": "At which Cape Town hospital did Professor Christiaan Barnard perform the world's first successful human-to-human heart transplant in 1967?",
                        "options": ["A) Tygerberg Hospital", "B) Groote Schuur Hospital", "C) Somerset Hospital", "D) Red Cross Children's Hospital"],
                        "a": "B) Groote Schuur Hospital",
                        "notes": "3 December 1967: recipient Louis Washkansky lived for 18 days with the new heart."
                    },
                    {
                        "q": "Which South African coastal engineering invention, a distinctive geometric 20-ton concrete block, is used worldwide to protect breakwaters from ocean waves?",
                        "options": ["A) Dolos", "B) Tetrapod", "C) Accropode", "D) Hexaleg"],
                        "a": "A) Dolos",
                        "notes": "Invented in East London in 1963 by Eric Merrifield and Aubrey Kruger."
                    },
                    {
                        "q": "Which South African-born physicist shared the 1979 Nobel Prize in Physiology or Medicine for the development of computer-assisted tomography (CAT scan)?",
                        "options": ["A) Max Theiler", "B) Allan Cormack", "C) Aaron Klug", "D) Sydney Brenner"],
                        "a": "B) Allan Cormack",
                        "notes": "Allan Cormack attended the University of Cape Town before conducting research at Tufts University."
                    },
                    {
                        "q": "In what calendar year did Apollo 11 astronaut Neil Armstrong become the first human to step onto the surface of the Moon?",
                        "options": ["A) 1965", "B) 1967", "C) 1969", "D) 1971"],
                        "a": "C) 1969",
                        "notes": "20 July 1969: 'That's one small step for man, one giant leap for mankind.'"
                    },
                    {
                        "q": "What ancient trade network linked China and the Mediterranean world for overland silk, spice, and horse trade?",
                        "options": ["A) The Amber Road", "B) The Silk Road", "C) The Spice Route", "D) The King's Highway"],
                        "a": "B) The Silk Road",
                        "notes": "Spanned over 6,400 km across Eurasia."
                    },
                    {
                        "q": "Which British passenger ocean liner sank in the North Atlantic in April 1912 after striking an iceberg?",
                        "options": ["A) RMS Lusitania", "B) RMS Titanic", "C) SS Britannic", "D) Queen Mary"],
                        "a": "B) RMS Titanic",
                        "notes": "Sank on its maiden voyage from Southampton to New York City."
                    },
                    {
                        "q": "Which Portuguese explorer became the first European to sail around the southernmost tip of Africa (Cape of Good Hope) in 1488?",
                        "options": ["A) Vasco da Gama", "B) Bartolomeu Dias", "C) Ferdinand Magellan", "D) Christopher Columbus"],
                        "a": "B) Bartolomeu Dias",
                        "notes": "Dias named it Cabo das Tormentas (Cape of Storms), later renamed Cape of Good Hope by King John II."
                    },
                    {
                        "q": "In which city is the famous Leaning Tower located?",
                        "options": ["A) Florence", "B) Pisa", "C) Venice", "D) Genoa"],
                        "a": "B) Pisa",
                        "notes": "The freestanding bell tower of Pisa Cathedral in Italy."
                    },
                    {
                        "q": "What international wall dividing an iconic European city fell on 9 November 1989, marking the end of the Cold War era?",
                        "options": ["A) The Warsaw Wall", "B) The Berlin Wall", "C) The Iron Curtain Wall", "D) The Danube Wall"],
                        "a": "B) The Berlin Wall",
                        "notes": "The fall of the Berlin Wall reunited East and West Germany."
                    },
                    {
                        "q": "Which ancient civilization built the colossal stone monument known as the Great Sphinx at Giza?",
                        "options": ["A) Ancient Romans", "B) Ancient Egyptians", "C) Ancient Greeks", "D) Babylonians"],
                        "a": "B) Ancient Egyptians",
                        "notes": "Carved out of limestone during the reign of Pharaoh Khafre (~2500 BC)."
                    }
                ]
            },
            {
                "roundId": 6,
                "title": "Sudden-Death Tie-Breakers",
                "badge": "Overtime • Closest Number",
                "theme": "Closest to the Pin Estimations",
                "difficultyText": "Overtime: Closest Number Takes Gold!",
                "hostVibe": "Highest stakes! One number on paper.",
                "questions": [
                    {
                        "q": "How many total days did Nelson Mandela spend imprisoned before his release on 11 February 1990?",
                        "options": ["A) 7,500 days", "B) 9,000 days", "C) 10,052 days", "D) 12,000 days"],
                        "a": "C) 10,052 days",
                        "notes": "Mandela spent 27 years, 6 months, and 6 days (10,052 days) in prison."
                    },
                    {
                        "q": "What is the official weight in metric tons of a standard full-size concrete dolos used on harbor breakwaters?",
                        "options": ["A) 5 tons", "B) 10 tons", "C) 20 tons", "D) 40 tons"],
                        "a": "C) 20 tons",
                        "notes": "Standard breakwater dolosse weigh approximately 20 tons each."
                    },
                    {
                        "q": "In what calendar year did the historic Apollo 11 moon landing take place?",
                        "options": ["A) 1967", "B) 1968", "C) 1969", "D) 1970"],
                        "a": "C) 1969",
                        "notes": "July 1969."
                    }
                ]
            }
        ]
    }

def get_set_6():
    return {
        "setId": 6,
        "setName": "Set 6: Highveld Hustle",
        "badge": "Set 6 • Highveld Legends",
        "theme": "Cricket Centuries, 90s Grunge, Fast Food Empires & Ancient Wonders",
        "rounds": [
            {
                "roundId": 1,
                "title": "Round 1: Counter Chat & Fun Trivia",
                "badge": "Round 1 • Easy",
                "theme": "Pop Trivia, Word Play & Bar Counter Wit",
                "difficultyText": "Level 1: Counter Fun",
                "hostVibe": "Get teams laughing and chatting over the opening questions.",
                "questions": [
                    {
                        "q": "How many cards are in a standard deck of playing cards (excluding jokers)?",
                        "options": ["A) 48 cards", "B) 50 cards", "C) 52 cards", "D) 54 cards"],
                        "a": "C) 52 cards",
                        "notes": "4 suits of 13 cards each = 52 cards."
                    },
                    {
                        "q": "What color is the gemstone known as an emerald?",
                        "options": ["A) Red", "B) Blue", "C) Green", "D) Yellow"],
                        "a": "C) Green",
                        "notes": "Emeralds are a green variety of beryl."
                    },
                    {
                        "q": "In bowling, what term describes scoring three consecutive strikes in a row?",
                        "options": ["A) Hat-trick", "B) Turkey", "C) Triple", "D) Clover"],
                        "a": "B) Turkey",
                        "notes": "A turkey: three strikes in a row."
                    },
                    {
                        "q": "What South African fast-food brand is famous for the flame-grilled 'King Steer Burger' and seasoned hand-cut slap chips?",
                        "options": ["A) Wimpy", "B) Steers", "C) Spur", "D) RocoMamas"],
                        "a": "B) Steers",
                        "notes": "Founded in 1960 by George Halamandaris."
                    },
                    {
                        "q": "Which mammal is the only one capable of true, sustained flight?",
                        "options": ["A) Flying Squirrel", "B) Bat", "C) Sugar Glider", "D) Lemur"],
                        "a": "B) Bat",
                        "notes": "Bats possess webbed wings for true powered flight."
                    },
                    {
                        "q": "What is the capital city of Spain?",
                        "options": ["A) Barcelona", "B) Seville", "C) Madrid", "D) Valencia"],
                        "a": "C) Madrid",
                        "notes": "Madrid, located in the geographical center of Spain."
                    },
                    {
                        "q": "How many meters is a standard Olympic swimming pool in length?",
                        "options": ["A) 25 meters", "B) 50 meters", "C) 100 meters", "D) 200 meters"],
                        "a": "B) 50 meters",
                        "notes": "50 meters in length (long course)."
                    },
                    {
                        "q": "What popular breakfast egg dish, baked over a tomato and onion spicy sauce in a pan, is known as 'Shakshuka'?",
                        "options": ["A) Poached eggs in spicy tomato relish", "B) Omelette filled with mushrooms", "C) Fried eggs on toast", "D) Scrambled eggs with cheese"],
                        "a": "A) Poached eggs in spicy tomato relish",
                        "notes": "Middle Eastern and North African dish of eggs gently poached in spiced tomato sauce."
                    },
                    {
                        "q": "What is the common name for the voice box in the human neck containing the vocal cords?",
                        "options": ["A) Pharynx", "B) Larynx", "C) Trachea", "D) Esophagus"],
                        "a": "B) Larynx",
                        "notes": "The larynx houses the vocal folds."
                    },
                    {
                        "q": "Which South African television soap opera set around the mining town of The Deep aired for over two decades on SABC3?",
                        "options": ["A) Generations", "B) Isidingo", "C) Egoli: Plek van Goud", "D) 7de Laan"],
                        "a": "B) Isidingo",
                        "notes": "Isidingo: The Need (1998-2020), set at the Horizon Deep mine."
                    }
                ]
            },
            {
                "roundId": 2,
                "title": "Round 2: Cricket Centuries & Rugby Hat-Tricks",
                "badge": "Round 2 • Sporting Legends",
                "theme": "The 438 Game, World Records & Stadium Miracles",
                "difficultyText": "Level 2: The Greatest Games",
                "hostVibe": "Relive the legendary 438 game at the Wanderers and famous rugby feats.",
                "questions": [
                    {
                        "q": "In the famous '438 Game' at the Wanderers in 2006, South Africa chased down Australia's 434. Who hit the winning boundary four over mid-off?",
                        "options": ["A) Herschelle Gibbs", "B) Mark Boucher", "C) Jacques Kallis", "D) Justin Ontong"],
                        "a": "B) Mark Boucher",
                        "notes": "Mark Boucher lofted Brett Lee for four to seal the highest successful ODI run chase in history (438/9)."
                    },
                    {
                        "q": "Who scored an astonishing 175 off 111 balls for South Africa in that exact same 438 game?",
                        "options": ["A) Graeme Smith", "B) Herschelle Gibbs", "C) AB de Villiers", "D) Shaun Pollock"],
                        "a": "B) Herschelle Gibbs",
                        "notes": "Herschelle Gibbs played one of the most explosive one-day innings ever witnessed."
                    },
                    {
                        "q": "Which South African cricket superstar holds the world record for the fastest ever ODI century, reaching 100 off just 31 balls against the West Indies?",
                        "options": ["A) Jacques Kallis", "B) AB de Villiers", "C) David Miller", "D) Quinton de Kock"],
                        "a": "B) AB de Villiers",
                        "notes": "AB de Villiers: 149 off 44 balls at the Wanderers on 18 January 2015."
                    },
                    {
                        "q": "Which Springbok lock forward, famous for dominating the lineouts, was named Man of the Match in the 2007 Rugby World Cup Final?",
                        "options": ["A) Bakkies Botha", "B) Victor Matfield", "C) Johann Muller", "D) Albert van den Berg"],
                        "a": "B) Victor Matfield",
                        "notes": "Victor Matfield's mastery of the lineout choked England's possession throughout the final."
                    },
                    {
                        "q": "Who was the legendary South African cricket captain who famously batted with a broken hand at the SCG against Australia in 2009?",
                        "options": ["A) Hansie Cronje", "B) Graeme Smith", "C) Shaun Pollock", "D) Faf du Plessis"],
                        "a": "B) Graeme Smith",
                        "notes": "Graeme Smith walked out to bat at number 11 with a broken left hand and damaged elbow to try and save the Test."
                    },
                    {
                        "q": "In tennis, what Grand Slam tournament is played on traditional grass courts in London every July?",
                        "options": ["A) Roland Garros", "B) Wimbledon", "C) The US Open", "D) The Australian Open"],
                        "a": "B) Wimbledon",
                        "notes": "The Championships, Wimbledon: the oldest tennis tournament in the world."
                    },
                    {
                        "q": "Which South African rugby prop was nicknamed 'The Beast' by roaring crowds at Kings Park and around the world?",
                        "options": ["A) Tendai Mtawarira", "B) Os du Randt", "C) Trevor Nyakane", "D) Frans Malherbe"],
                        "a": "A) Tendai Mtawarira",
                        "notes": "'BEEEEAAAST!' 117 caps and 2019 World Cup champion."
                    },
                    {
                        "q": "What is the maximum break of points possible in a standard frame of snooker without fouls?",
                        "options": ["A) 120", "B) 147", "C) 155", "D) 160"],
                        "a": "B) 147",
                        "notes": "15 reds with 15 blacks (120 points) plus the 6 colors (27 points) = 147."
                    },
                    {
                        "q": "Which South African long jumper won the Olympic silver medal in Beijing 2008 and world gold in Berlin 2009?",
                        "options": ["A) Luvo Manyonga", "B) Khotso Mokoena", "C) Ruswahl Samaai", "D) Akani Simbine"],
                        "a": "B) Khotso Mokoena",
                        "notes": "Khotso Mokoena won South Africa's only medal at the 2008 Beijing Olympics."
                    },
                    {
                        "q": "In rugby league or union, how many points are awarded for an unconverted try in modern rugby union?",
                        "options": ["A) 3 points", "B) 4 points", "C) 5 points", "D) 6 points"],
                        "a": "C) 5 points",
                        "notes": "Raised from 4 points to 5 points in 1992."
                    }
                ]
            },
            {
                "roundId": 3,
                "title": "Round 3: 90s Nostalgia, Vinyl & Billboard Hits",
                "badge": "Round 3 • 90s Grooves",
                "theme": "Grunge, Pop Royalty, Big 90s Radios & Iconic Riffs",
                "difficultyText": "Level 3: Tape Deck Rewind",
                "hostVibe": "Sing along to 90s classics that every bar patron knows by heart.",
                "questions": [
                    {
                        "q": "Which Seattle grunge band released the genre-defining 1991 album Nevermind, featuring 'Smells Like Teen Spirit'?",
                        "options": ["A) Pearl Jam", "B) Soundgarden", "C) Nirvana", "D) Alice in Chains"],
                        "a": "C) Nirvana",
                        "notes": "Fronted by Kurt Cobain, with Krist Novoselic and Dave Grohl."
                    },
                    {
                        "q": "Which multi-racial South African band fronted by Claire Johnston had massive 1989/1990 hits with 'Special Star' and 'Dance Some More'?",
                        "options": ["A) Juluka", "B) Mango Groove", "C) Clout", "D) Bright Blue"],
                        "a": "B) Mango Groove",
                        "notes": "Mango Groove blended big band swing, marabi, and kwela pop."
                    },
                    {
                        "q": "What British rock band brothers Liam and Noel Gallagher led during the Britpop era with hits like 'Wonderwall' and 'Don't Look Back in Anger'?",
                        "options": ["A) Blur", "B) Oasis", "C) The Verve", "D) Pulp"],
                        "a": "B) Oasis",
                        "notes": "Their 1995 album (What's the Story) Morning Glory? sold over 22 million copies."
                    },
                    {
                        "q": "Which pop diva sang the mega-selling theme song 'My Heart Will Go On' for the movie Titanic?",
                        "options": ["A) Whitney Houston", "B) Mariah Carey", "C) Celine Dion", "D) Barbra Streisand"],
                        "a": "C) Celine Dion",
                        "notes": "Composed by James Horner, winning the Oscar for Best Original Song."
                    },
                    {
                        "q": "What Swedish pop duo consisting of Marie Fredriksson and Per Gessle scored monster hits with 'It Must Have Been Love' and 'Joyride'?",
                        "options": ["A) Ace of Base", "B) Roxette", "C) The Cardigans", "D) Army of Lovers"],
                        "a": "B) Roxette",
                        "notes": "Roxette had four US Billboard number-one singles."
                    },
                    {
                        "q": "Which American hip hop group released the 1992 dance party anthem 'Jump Around'?",
                        "options": ["A) Cypress Hill", "B) House of Pain", "C) Beastie Boys", "D) Run-DMC"],
                        "a": "B) House of Pain",
                        "notes": "Produced by DJ Muggs."
                    },
                    {
                        "q": "In 1994, which American punk rock trio released the smash hit album Dookie featuring 'Basket Case'?",
                        "options": ["A) The Offspring", "B) Blink-182", "C) Green Day", "D) Sum 41"],
                        "a": "C) Green Day",
                        "notes": "Billie Joe Armstrong, Mike Dirnt, and Tré Cool."
                    },
                    {
                        "q": "Which South African band had a giant hit in 1987 with the anti-conscription ballad 'Weeping', featuring the melody of 'Nkosi Sikelel' iAfrika'?",
                        "options": ["A) Bright Blue", "B) eVoid", "C) Cinema", "D) Petit Cheval"],
                        "a": "A) Bright Blue",
                        "notes": "Written by Dan Heymann, featuring Basil Coetzee on saxophone."
                    },
                    {
                        "q": "Who released the hit 1999 Latin pop anthem 'Livin' la Vida Loca'?",
                        "options": ["A) Enrique Iglesias", "B) Ricky Martin", "C) Marc Anthony", "D) Chayanne"],
                        "a": "B) Ricky Martin",
                        "notes": "Ignited the global Latin pop explosion."
                    },
                    {
                        "q": "Which American rock band fronted by Anthony Kiedis and Flea released the 1991 hit album Blood Sugar Sex Magik containing 'Under the Bridge'?",
                        "options": ["A) Foo Fighters", "B) Red Hot Chili Peppers", "C) Jane's Addiction", "D) Incubus"],
                        "a": "B) Red Hot Chili Peppers",
                        "notes": "Produced by Rick Rubin."
                    }
                ]
            },
            {
                "roundId": 4,
                "title": "Round 4: Fast Food Empires & Secret Recipes",
                "badge": "Round 4 • Pub Feasts",
                "theme": "Onion Rings, Rib Basting, Draughts & Secret Spices",
                "difficultyText": "Level 4: Feast Mode",
                "hostVibe": "Spur birthdays, secret sauces, and the best pub chow in town.",
                "questions": [
                    {
                        "q": "Which South African family steakhouse franchise is famous for its Native American-themed decor, kids' play areas, and signature basting sauce?",
                        "options": ["A) Dros", "B) Spur Steak Ranches", "C) Cattle Baron", "D) Mike's Kitchen"],
                        "a": "B) Spur Steak Ranches",
                        "notes": "Founded by Allen Ambor in Newlands, Cape Town in 1967."
                    },
                    {
                        "q": "What is the famous secret ingredient blend count famously advertised on Colonel Sanders' Kentucky Fried Chicken recipe?",
                        "options": ["A) 7 herbs and spices", "B) 11 herbs and spices", "C) 13 herbs and spices", "D) 15 herbs and spices"],
                        "a": "B) 11 herbs and spices",
                        "notes": "The Colonel's secret blend of 11 herbs and spices kept in a safe in Louisville, Kentucky."
                    },
                    {
                        "q": "What spicy Portuguese-style chicken franchise was founded in Rosettenville, Johannesburg in 1987 by Fernando Duarte and Robbie Brozin?",
                        "options": ["A) Barcelos", "B) Galito's", "C) Nando's", "D) Mochachos"],
                        "a": "C) Nando's",
                        "notes": "Named after Fernando's son Nando; now operating in over 30 countries."
                    },
                    {
                        "q": "What is the distinctive bread bun used in South African cuisine that is deep-fried from yeasted dough and often filled with curried mince?",
                        "options": ["A) Roosterkoek", "B) Vetkoek (Amagwinya)", "C) Mosbolletjie", "D) Potbrood"],
                        "a": "B) Vetkoek (Amagwinya)",
                        "notes": "Crispy golden outside, soft steamy dough inside, stuffed with curried mince."
                    },
                    {
                        "q": "Which cut of beef, famous in South American churrasco and increasingly popular at SA braais, has a thick fat cap and is called the rump cap?",
                        "options": ["A) Tomahawk", "B) Picanha", "C) Flank Steak", "D) Flat Iron"],
                        "a": "B) Picanha",
                        "notes": "Picanha (sirloin cap / rump cap): seasoned with coarse rock salt and skewered over coals."
                    },
                    {
                        "q": "In a bar, what non-alcoholic cocktail made with ginger ale, a dash of grenadine, and a maraschino cherry is named after a child movie star?",
                        "options": ["A) Roy Rogers", "B) Shirley Temple", "C) Arnold Palmer", "D) Virgin Mary"],
                        "a": "B) Shirley Temple",
                        "notes": "Invented at Chasen's in Beverly Hills for the young actress."
                    },
                    {
                        "q": "What is the primary flavor profile of the classic South African liqueur Van Der Hum?",
                        "options": ["A) Cape Naartjie / Tangerine", "B) Wild Peach", "C) Spearmint", "D) Marula"],
                        "a": "A) Cape Naartjie / Tangerine",
                        "notes": "Van Der Hum is flavored with Cape naartjie peels, brandy, and spices."
                    },
                    {
                        "q": "What popular burger topping consists of thinly sliced beef cured and dried, crumbled over the melted cheese?",
                        "options": ["A) Bacon bits", "B) Biltong shavings", "C) Pork crackling", "D) Droëwors coins"],
                        "a": "B) Biltong shavings",
                        "notes": "The biltong burger: a pub classic across South Africa."
                    },
                    {
                        "q": "Which Mexican distilled spirit must be produced specifically within the Mexican state of Jalisco and designated regions, unlike general Mezcal?",
                        "options": ["A) Tequila", "B) Pisco", "C) Cachaça", "D) Sotol"],
                        "a": "A) Tequila",
                        "notes": "All Tequilas are Mezcals, but only those made from blue agave in Jalisco (and limited municipalities) are Tequila."
                    },
                    {
                        "q": "What famous brand of hot sauce originated on Avery Island, Louisiana, and is aged in white oak whiskey barrels?",
                        "options": ["A) Frank's RedHot", "B) Sriracha", "C) Tabasco", "D) Cholula"],
                        "a": "C) Tabasco",
                        "notes": "Created by Edmund McIlhenny in 1868."
                    }
                ]
            },
            {
                "roundId": 5,
                "title": "Round 5: Wonders of the Ancient & Modern World",
                "badge": "Round 5 • World Wonders",
                "theme": "Pyramids, Colosseums, High Peaks & Ancient Empires",
                "difficultyText": "Level 5: Mastermind Round",
                "hostVibe": "Final round before tallying! Put on your thinking caps.",
                "questions": [
                    {
                        "q": "Which of the original Seven Wonders of the Ancient World is the only one that still largely stands intact today?",
                        "options": ["A) Colossus of Rhodes", "B) Great Pyramid of Giza", "C) Lighthouse of Alexandria", "D) Hanging Gardens of Babylon"],
                        "a": "B) Great Pyramid of Giza",
                        "notes": "Built around 2560 BC for Pharaoh Khufu; survived for over 4,500 years."
                    },
                    {
                        "q": "Approximately how old are the rocks that make up Table Mountain in Cape Town?",
                        "options": ["A) 5 million years old", "B) 60 million years old", "C) 600 million years old", "D) 2 billion years old"],
                        "a": "C) 600 million years old",
                        "notes": "Table Mountain's sandstone and granite base dates back over 500-600 million years, making it six times older than the Himalayas."
                    },
                    {
                        "q": "In which city stands the colossal Roman amphitheater known as the Colosseum, completed in 80 AD?",
                        "options": ["A) Athens", "B) Rome", "C) Naples", "D) Verona"],
                        "a": "B) Rome",
                        "notes": "The Flavian Amphitheatre, capable of holding up to 80,000 spectators."
                    },
                    {
                        "q": "What is the deepest known location in the world's oceans, plunging nearly 11,000 meters down in the western Pacific?",
                        "options": ["A) Puerto Rico Trench", "B) Mariana Trench (Challenger Deep)", "C) Java Trench", "D) Tonga Trench"],
                        "a": "B) Mariana Trench (Challenger Deep)",
                        "notes": "Challenger Deep reaches approximately 10,994 meters below sea level."
                    },
                    {
                        "q": "Which ivory-white marble mausoleum on the Yamuna river in Agra, India was commissioned in 1631 by Mughal Emperor Shah Jahan?",
                        "options": ["A) Amber Palace", "B) Taj Mahal", "C) Red Fort", "D) Hawa Mahal"],
                        "a": "B) Taj Mahal",
                        "notes": "Built to house the tomb of his favorite wife, Mumtaz Mahal."
                    },
                    {
                        "q": "What is the longest river in the world by traditional geographic consensus?",
                        "options": ["A) Amazon River", "B) Nile River", "C) Yangtze River", "D) Mississippi River"],
                        "a": "B) Nile River",
                        "notes": "Flowing roughly 6,650 km through northeastern Africa."
                    },
                    {
                        "q": "In which South American country would you find the ancient Incan citadel of Machu Picchu perched high in the Andes?",
                        "options": ["A) Chile", "B) Colombia", "C) Peru", "D) Bolivia"],
                        "a": "C) Peru",
                        "notes": "Built around 1450 AD above the Sacred Valley."
                    },
                    {
                        "q": "What is the capital city of Germany, reunited after the fall of the Wall in 1989?",
                        "options": ["A) Munich", "B) Frankfurt", "C) Berlin", "D) Hamburg"],
                        "a": "C) Berlin",
                        "notes": "Berlin is the largest city in Germany by population and area."
                    },
                    {
                        "q": "What colossal suspension bridge in San Francisco, painted in 'International Orange', opened to traffic in 1937?",
                        "options": ["A) Brooklyn Bridge", "B) Golden Gate Bridge", "C) Bay Bridge", "D) Manhattan Bridge"],
                        "a": "B) Golden Gate Bridge",
                        "notes": "Spans the Golden Gate strait connecting San Francisco to Marin County."
                    },
                    {
                        "q": "Which South African coastal road boasts the world's highest commercial bungee jump located at Bloukrans Bridge?",
                        "options": ["A) N1", "B) N2 Garden Route", "C) N3", "D) R62"],
                        "a": "B) N2 Garden Route",
                        "notes": "Bloukrans Bridge Bungee: 216 meters above the Bloukrans River on the N2."
                    }
                ]
            },
            {
                "roundId": 6,
                "title": "Sudden-Death Tie-Breakers",
                "badge": "Overtime • Closest Number",
                "theme": "Closest to the Pin Estimations",
                "difficultyText": "Overtime: Closest Number Takes 1st Place!",
                "hostVibe": "Tied teams: one numeric guess!",
                "questions": [
                    {
                        "q": "How many total runs were scored by both teams combined in the historic 438 cricket match between Australia and South Africa at the Wanderers in 2006?",
                        "options": ["A) 820 runs", "B) 872 runs", "C) 910 runs", "D) 950 runs"],
                        "a": "B) 872 runs",
                        "notes": "Australia 434 + South Africa 438 = 872 runs in 99.5 overs."
                    },
                    {
                        "q": "How many meters high is the Bloukrans Bridge bungee jump above the river?",
                        "options": ["A) 160 meters", "B) 180 meters", "C) 216 meters", "D) 250 meters"],
                        "a": "C) 216 meters",
                        "notes": "216 meters (709 feet)."
                    },
                    {
                        "q": "In what calendar year did AB de Villiers score his 31-ball world record century against the West Indies at the Wanderers?",
                        "options": ["A) 2013", "B) 2014", "C) 2015", "D) 2016"],
                        "a": "C) 2015",
                        "notes": "18 January 2015."
                    }
                ]
            }
        ]
    }

def get_set_7():
    return {
        "setId": 7,
        "setName": "Set 7: Durban to Dullstroom",
        "badge": "Set 7 • Road Trippers",
        "theme": "Ball Sports, Potjiekos Secrets, 2000s Hits & Mountain Ranges",
        "rounds": [
            {
                "roundId": 1,
                "title": "Round 1: Opening Round & Brain Warmers",
                "badge": "Round 1 • Easy",
                "theme": "Bar Games, Fun Facts & Everyday Trivia",
                "difficultyText": "Level 1: Pencils Ready",
                "hostVibe": "Welcome teams, introduce the round, get the points rolling.",
                "questions": [
                    {
                        "q": "In a standard game of darts, what color is the narrow outer ring that awards double points?",
                        "options": ["A) Red and Green", "B) Blue and Yellow", "C) Black and White", "D) Purple and Orange"],
                        "a": "A) Red and Green",
                        "notes": "Alternates between red and green on standard London bristle boards."
                    },
                    {
                        "q": "What is the chemical symbol for table salt?",
                        "options": ["A) H2O", "B) NaCl", "C) CO2", "D) KCl"],
                        "a": "B) NaCl",
                        "notes": "Sodium chloride (NaCl)."
                    },
                    {
                        "q": "How many degrees are there in a full circle?",
                        "options": ["A) 180 degrees", "B) 270 degrees", "C) 360 degrees", "D) 400 degrees"],
                        "a": "C) 360 degrees",
                        "notes": "A complete rotation is 360 degrees."
                    },
                    {
                        "q": "Which South African craft gin botanical gives pink gin its blush tint and floral flavor?",
                        "options": ["A) Rose water / Hibiscus", "B) Rooibos", "C) Strawberry syrup", "D) Pink peppercorn only"],
                        "a": "A) Rose water / Hibiscus",
                        "notes": "Hibiscus flowers or rose pelargonium impart natural pink hue."
                    },
                    {
                        "q": "What is the capital city of Portugal?",
                        "options": ["A) Porto", "B) Lisbon", "C) Faro", "D) Braga"],
                        "a": "B) Lisbon",
                        "notes": "Lisbon, located at the mouth of the Tagus River."
                    },
                    {
                        "q": "How many days are in the month of September?",
                        "options": ["A) 28 days", "B) 29 days", "C) 30 days", "D) 31 days"],
                        "a": "C) 30 days",
                        "notes": "'Thirty days hath September, April, June, and November...'"
                    },
                    {
                        "q": "In automotive engines, what does 'RPM' stand for?",
                        "options": ["A) Rate Per Minute", "B) Revolutions Per Minute", "C) Rotations Per Meter", "D) Road Power Measure"],
                        "a": "B) Revolutions Per Minute",
                        "notes": "Measures crankshaft rotational speed."
                    },
                    {
                        "q": "What famous board game challenges players to sink each other's aircraft carriers and submarines on a coordinate grid?",
                        "options": ["A) Battleship", "B) Sub Hunter", "C) Risk", "D) Mastermind"],
                        "a": "A) Battleship",
                        "notes": "'You sank my battleship!'"
                    },
                    {
                        "q": "Which primary color mixed with red makes orange?",
                        "options": ["A) Blue", "B) Yellow", "C) Green", "D) White"],
                        "a": "B) Yellow",
                        "notes": "Red + Yellow = Orange."
                    },
                    {
                        "q": "What is the common term in South Africa for a small, enclosed backyard barbecue space with a built-in chimney?",
                        "options": ["A) Braai room / Lapa", "B) Stoep", "C) Gazebo", "D) Boma"],
                        "a": "A) Braai room / Lapa",
                        "notes": "A dedicated braai room or lapa is the social center of any South African home."
                    }
                ]
            },
            {
                "roundId": 2,
                "title": "Round 2: Ball Sports, Tournaments & Stadiums",
                "badge": "Round 2 • Turf Wars",
                "theme": "Stadiums, World Cup Finals & Derby Clashes",
                "difficultyText": "Level 2: Stadium Master",
                "hostVibe": "Test their sporting knowledge from the pitch to the pitch-side bar.",
                "questions": [
                    {
                        "q": "What was the final score in the 2023 Rugby World Cup Final when South Africa defeated New Zealand in Paris?",
                        "options": ["A) 12 - 11", "B) 15 - 12", "C) 32 - 12", "D) 19 - 16"],
                        "a": "A) 12 - 11",
                        "notes": "Springboks 12 - All Blacks 11 at Stade de France on 28 October 2023."
                    },
                    {
                        "q": "In golf, what is the term for scoring three under par on a single hole (or a hole-in-one on a par 4)?",
                        "options": ["A) Eagle", "B) Albatross (Double Eagle)", "C) Condor", "D) Bogey"],
                        "a": "B) Albatross (Double Eagle)",
                        "notes": "An albatross is three strokes under par."
                    },
                    {
                        "q": "Which South African cricket captain led the Proteas to the number 1 Test ranking in the world in 2012 by beating England at Lord's?",
                        "options": ["A) Hansie Cronje", "B) Shaun Pollock", "C) Graeme Smith", "D) AB de Villiers"],
                        "a": "C) Graeme Smith",
                        "notes": "Graeme Smith captained South Africa to historic series victories in England and Australia."
                    },
                    {
                        "q": "What is the name of the stadium in Bloemfontein that serves as the home ground of the Free State Cheetahs?",
                        "options": ["A) Free State Stadium (Toyota Stadium)", "B) Griqua Park", "C) Outeniqua Park", "D) Buffalo City Stadium"],
                        "a": "A) Free State Stadium (Toyota Stadium)",
                        "notes": "Toyota Stadium in Bloemfontein."
                    },
                    {
                        "q": "In rugby union, what is the minimum distance the ball must travel forward from a kickoff restart before it can be played?",
                        "options": ["A) 5 meters", "B) 10 meters", "C) 15 meters", "D) 22 meters"],
                        "a": "B) 10 meters",
                        "notes": "The kickoff must cross the receiving team's 10-meter line."
                    },
                    {
                        "q": "Which South African female golfer won the Women's British Open at Sunningdale in 2007?",
                        "options": ["A) Lee-Anne Pace", "B) Ashleigh Buhai", "C) Paula Reto", "D) Sally Little"],
                        "a": "B) Ashleigh Buhai",
                        "notes": "Ashleigh Buhai later won the Women's Open in 2022 at Muirfield."
                    },
                    {
                        "q": "Which famous Springbok lock was known for his legendary punch during a test match against New Zealand and his ferocious partnership with Victor Matfield?",
                        "options": ["A) Bakkies Botha", "B) Mark Andrews", "C) Eben Etzebeth", "D) Lood de Jager"],
                        "a": "A) Bakkies Botha",
                        "notes": "Bakkies Botha: one of the most physically intimidating enforcers in rugby history."
                    },
                    {
                        "q": "In soccer, what is the name of the prestigious European club tournament won by Real Madrid a record 15 times?",
                        "options": ["A) UEFA Europa League", "B) UEFA Champions League", "C) Copa Libertadores", "D) FIFA Club World Cup"],
                        "a": "B) UEFA Champions League",
                        "notes": "Formerly the European Cup."
                    },
                    {
                        "q": "Which iconic South African lock forward became the most-capped Springbok player of all time in 2024, surpassing Victor Matfield's 127 caps?",
                        "options": ["A) Pieter-Steph du Toit", "B) Eben Etzebeth", "C) Franco Mostert", "D) Siya Kolisi"],
                        "a": "B) Eben Etzebeth",
                        "notes": "Eben Etzebeth won his 128th cap against Argentina in Nelspruit in September 2024."
                    },
                    {
                        "q": "In cricket, what color ball is traditionally used in day-night Test matches played under floodlights?",
                        "options": ["A) Red ball", "B) White ball", "C) Pink ball", "D) Yellow ball"],
                        "a": "C) Pink ball",
                        "notes": "The pink ball maintains visibility under lights while retaining red-ball durability."
                    }
                ]
            },
            {
                "roundId": 3,
                "title": "Round 3: Cinema Trivia & Screen Legends",
                "badge": "Round 3 • Cinema Gold",
                "theme": "The Godfather, Pulp Fiction, Lord of the Rings & Iconic Heroes",
                "difficultyText": "Level 3: Hollywood A-List",
                "hostVibe": "Movie buffs, this is your time to rack up maximum points.",
                "questions": [
                    {
                        "q": "Who directed the 1972 mafia masterpiece The Godfather?",
                        "options": ["A) Martin Scorsese", "B) Francis Ford Coppola", "C) Brian De Palma", "D) Sergio Leone"],
                        "a": "B) Francis Ford Coppola",
                        "notes": "Adapted from Mario Puzo's bestselling novel."
                    },
                    {
                        "q": "In the film Forrest Gump, what college football team did Forrest play for under coach Bear Bryant?",
                        "options": ["A) Alabama Crimson Tide", "B) LSU Tigers", "C) Georgia Bulldogs", "D) Florida Gators"],
                        "a": "A) Alabama Crimson Tide",
                        "notes": "'Run, Forrest, run!' for the University of Alabama."
                    },
                    {
                        "q": "Which actor portrayed the eccentric pirate Captain Jack Sparrow in Pirates of the Caribbean?",
                        "options": ["A) Orlando Bloom", "B) Johnny Depp", "C) Geoffrey Rush", "D) Colin Farrell"],
                        "a": "B) Johnny Depp",
                        "notes": "Johnny Depp earned an Oscar nomination for The Curse of the Black Pearl."
                    },
                    {
                        "q": "In the 1993 thriller The Fugitive, who played the wrongfully convicted Dr. Richard Kimble?",
                        "options": ["A) Tommy Lee Jones", "B) Harrison Ford", "C) Kevin Costner", "D) Michael Douglas"],
                        "a": "B) Harrison Ford",
                        "notes": "'I didn't kill my wife!' / 'I don't care!'"
                    },
                    {
                        "q": "Which 1994 prison drama starring Tim Robbins and Morgan Freeman is currently the top-rated movie of all time on IMDb?",
                        "options": ["A) The Green Mile", "B) The Shawshank Redemption", "C) Pulp Fiction", "D) Goodfellas"],
                        "a": "B) The Shawshank Redemption",
                        "notes": "Based on a Stephen King novella."
                    },
                    {
                        "q": "In The Lord of the Rings, what is the fictional volcanic mountain in Mordor where the One Ring was forged?",
                        "options": ["A) Mount Doom (Orodruin)", "B) Lonely Mountain", "C) Caradhras", "D) Orthanc"],
                        "a": "A) Mount Doom (Orodruin)",
                        "notes": "Where Frodo Baggins must cast the Ring into the fires."
                    },
                    {
                        "q": "Who played the eccentric British detective Sherlock Holmes in Guy Ritchie's 2009 action-mystery film?",
                        "options": ["A) Benedict Cumberbatch", "B) Robert Downey Jr.", "C) Jude Law", "D) Christian Bale"],
                        "a": "B) Robert Downey Jr.",
                        "notes": "Robert Downey Jr. won a Golden Globe for the performance."
                    },
                    {
                        "q": "In the hit comedy Anchorman, what is the full name of Will Ferrell's mustachioed 1970s news anchor?",
                        "options": ["A) Brian Fontana", "B) Ron Burgundy", "C) Champ Kind", "D) Brick Tamland"],
                        "a": "B) Ron Burgundy",
                        "notes": "'Stay classy, San Diego.'"
                    },
                    {
                        "q": "Which 1986 film starred Tom Cruise as naval aviator Maverick and featured Kenny Loggins' hit 'Danger Zone'?",
                        "options": ["A) Days of Thunder", "B) Top Gun", "C) Iron Eagle", "D) Cocktail"],
                        "a": "B) Top Gun",
                        "notes": "Directed by Tony Scott."
                    },
                    {
                        "q": "Which South African actor played the brutal villain Sharlto Copley's sidekick or featured as Wikus van de Merwe in District 9 (2009)?",
                        "options": ["A) Arnold Vosloo", "B) Sharlto Copley", "C) Neil Blomkamp", "D) Fana Mokoena"],
                        "a": "B) Sharlto Copley",
                        "notes": "Sharlto Copley starred as Wikus van de Merwe in Neill Blomkamp's breakout sci-fi hit."
                    }
                ]
            },
            {
                "roundId": 4,
                "title": "Round 4: Potjiekos Secrets & Braai Etiquette",
                "badge": "Round 4 • Potjie Master",
                "theme": "Cast Iron Pots, Wood Smoke, Marinades & Pub Eats",
                "difficultyText": "Level 4: Three-Legged Gold",
                "hostVibe": "Settle the potjie arguments once and for all!",
                "questions": [
                    {
                        "q": "What material is a traditional three-legged South African potjie pot made of?",
                        "options": ["A) Stainless steel", "B) Cast iron", "C) Copper", "D) Aluminum"],
                        "a": "B) Cast iron",
                        "notes": "Heavy cast iron retains and distributes gentle, even heat."
                    },
                    {
                        "q": "What is the process called of treating a new or rusty cast iron potjie pot with oil and heat to build a non-stick protective patina?",
                        "options": ["A) Curing / Seasoning", "B) Glazing", "C) Tempering", "D) Galvanizing"],
                        "a": "A) Curing / Seasoning",
                        "notes": "Coating with fat or oil and baking it creates a polymerized protective layer."
                    },
                    {
                        "q": "What popular South African dry snack is made from thin curls of seasoned beef dried until crunchy and brittle?",
                        "options": ["A) Biltong powder", "B) Biltong shavings / chips", "C) Crackling", "D) Chicharrón"],
                        "a": "B) Biltong shavings / chips",
                        "notes": "Thin biltong shavings are a favorite bar snack."
                    },
                    {
                        "q": "In a potjie, in what order should ingredients traditionally be layered from bottom to top?",
                        "options": [
                            "A) Soft greens at bottom, meat in middle, potatoes on top",
                            "B) Meat and onions at bottom, hard root vegetables middle, soft greens and mushrooms on top",
                            "C) Vegetables at bottom, meat on top",
                            "D) Everything mixed into a stew before lighting coals"
                        ],
                        "a": "B) Meat and onions at bottom, hard root vegetables middle, soft greens and mushrooms on top",
                        "notes": "Meat browns on bottom, potatoes cook in rising steam, soft greens stay intact on top."
                    },
                    {
                        "q": "What traditional Cape sweet-and-sour pickle made from green curried mangoes is served with curry and braais?",
                        "options": ["A) Chutney", "B) Atchar", "C) Sambal", "D) Piccalilli"],
                        "a": "B) Atchar",
                        "notes": "Mango atchar packed in spiced mustard oil."
                    },
                    {
                        "q": "Which famous Scottish whiskey region is renowned for producing heavily peated, smoky single malts like Laphroaig, Ardbeg, and Lagavulin?",
                        "options": ["A) Speyside", "B) Islay", "C) Highlands", "D) Lowlands"],
                        "a": "B) Islay",
                        "notes": "The Isle of Islay is legendary for its pungent, peaty maritime whiskies."
                    },
                    {
                        "q": "What South African biscuit is baked twice so that it becomes dry, hard, and perfect for dunking into hot coffee or rooibos tea?",
                        "options": ["A) Hertzoggie", "B) Ouma Rusk (Beskuit)", "C) Shortbread", "D) Ginger snap"],
                        "a": "B) Ouma Rusk (Beskuit)",
                        "notes": "Ouma Rusks: 'Dunk a friend, dunk an Ouma!'"
                    },
                    {
                        "q": "What French term describes cooking meat very slowly in its own rendered fat at low temperature?",
                        "options": ["A) Confit", "B) Braise", "C) Flambé", "D) Sous vide"],
                        "a": "A) Confit",
                        "notes": "Duck confit is the classic example."
                    },
                    {
                        "q": "Which South African craft cider brand produced in the Elgin Valley is named after the sound of apples being crushed?",
                        "options": ["A) Hunter's Dry", "B) Savanna Dry", "C) Cluver & Jack", "D) Sxollie"],
                        "a": "C) Cluver & Jack",
                        "notes": "Pioneered by Paul Cluver and Bruce Jack."
                    },
                    {
                        "q": "What is the common braai etiquette regarding who is permitted to turn the meat on the grid?",
                        "options": ["A) Anyone holding a beer", "B) Strictly the Braaimaster only", "C) The host's mother-in-law", "D) The guest who brought the tongs"],
                        "a": "B) Strictly the Braaimaster only",
                        "notes": "Never touch another man's tongs or turn another man's meat without express permission!"
                    }
                ]
            },
            {
                "roundId": 5,
                "title": "Round 5: Famous Landmarks & Great Explorers",
                "badge": "Round 5 • Expeditions",
                "theme": "Mountains, Rivers, Explorers & Engineering Marvels",
                "difficultyText": "Level 5: The Final Hurdle",
                "hostVibe": "Final round before the champions are crowned! Double-check your sheets.",
                "questions": [
                    {
                        "q": "What is the highest mountain range in Southern Africa, whose name means 'Dragon Mountains' in Afrikaans?",
                        "options": ["A) Swartberg", "B) Drakensberg (uKhahlamba)", "C) Magaliesberg", "D) Cederberg"],
                        "a": "B) Drakensberg (uKhahlamba)",
                        "notes": "uKhahlamba means 'Barrier of Spears' in Zulu; Drakensberg means Dragon Mountains."
                    },
                    {
                        "q": "Which natural curved cliff face in the Northern Drakensberg rises over 1,200 meters high and stretches five kilometers long?",
                        "options": ["A) Sentinel Peak", "B) The Amphitheatre", "C) Cathedral Peak", "D) Giant's Castle"],
                        "a": "B) The Amphitheatre",
                        "notes": "Home to the Tugela Falls, which plunge down the face of the Amphitheatre."
                    },
                    {
                        "q": "What man-made canal in Egypt connects the Mediterranean Sea to the Red Sea, opening a direct maritime route to Asia?",
                        "options": ["A) Panama Canal", "B) Suez Canal", "C) Corinth Canal", "D) Kiel Canal"],
                        "a": "B) Suez Canal",
                        "notes": "Opened in November 1869, eliminating the need to sail around Africa."
                    },
                    {
                        "q": "Which South African coastal road is world-famous for its cliffside curves, connecting Gordon's Bay to Rooi-Els along False Bay?",
                        "options": ["A) Chapman's Peak", "B) Clarence Drive (R44)", "C) Marine Drive", "D) Boyes Drive"],
                        "a": "B) Clarence Drive (R44)",
                        "notes": "Clarence Drive (R44) hugs the steep sea cliffs along False Bay."
                    },
                    {
                        "q": "What is the tallest building in the world today, located in Dubai, United Arab Emirates?",
                        "options": ["A) Shanghai Tower", "B) Burj Khalifa", "C) Taipei 101", "D) One World Trade Center"],
                        "a": "B) Burj Khalifa",
                        "notes": "Stands 828 meters (2,717 feet) tall."
                    },
                    {
                        "q": "What is the official currency of the United States of America?",
                        "options": ["A) US Dollar", "B) Pound", "C) Peso", "D) Franc"],
                        "a": "A) US Dollar",
                        "notes": "USD ($)."
                    },
                    {
                        "q": "Which famous explorer led the 1519 Spanish expedition that achieved the first circumnavigation of the Earth?",
                        "options": ["A) Christopher Columbus", "B) Ferdinand Magellan", "C) Marco Polo", "D) James Cook"],
                        "a": "B) Ferdinand Magellan",
                        "notes": "Magellan was killed in the Philippines; Juan Sebastián Elcano completed the voyage."
                    },
                    {
                        "q": "What is the capital city of Kenya?",
                        "options": ["A) Mombasa", "B) Nairobi", "C) Kisumu", "D) Nakuru"],
                        "a": "B) Nairobi",
                        "notes": "Nairobi: nicknamed the 'Green City in the Sun'."
                    },
                    {
                        "q": "What body of water separates the United Kingdom from the European mainland at France?",
                        "options": ["A) The North Sea", "B) The English Channel", "C) The Irish Sea", "D) The Baltic Sea"],
                        "a": "B) The English Channel",
                        "notes": "Connected beneath the seabed by the Channel Tunnel."
                    },
                    {
                        "q": "Which South African mountain range just north of Pretoria and Johannesburg is one of the oldest geological formations on Earth?",
                        "options": ["A) Magaliesberg", "B) Waterberg", "C) Soutpansberg", "D) Witwatersrand"],
                        "a": "A) Magaliesberg",
                        "notes": "The Magaliesberg is nearly 2.4 billion years old."
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
                        "q": "What is the total overall drop height of Tugela Falls in the Drakensberg in meters?",
                        "options": ["A) 750 meters", "B) 840 meters", "C) 948 meters", "D) 1,120 meters"],
                        "a": "C) 948 meters",
                        "notes": "948 meters (or 983m in recent re-surveys), widely recognized as the second highest (or highest) waterfall in the world."
                    },
                    {
                        "q": "How many test caps did Victor Matfield earn for the Springboks in his legendary rugby career?",
                        "options": ["A) 110 caps", "B) 120 caps", "C) 127 caps", "D) 135 caps"],
                        "a": "C) 127 caps",
                        "notes": "127 caps between 2001 and 2015."
                    },
                    {
                        "q": "In what calendar year did the Suez Canal officially open for navigation?",
                        "options": ["A) 1848", "B) 1869", "C) 1885", "D) 1902"],
                        "a": "B) 1869",
                        "notes": "Opened 17 November 1869."
                    }
                ]
            }
        ]
    }

if __name__ == '__main__':
    print("Testing Set 5, 6, 7 generation...")
    s5 = get_set_5()
    s6 = get_set_6()
    s7 = get_set_7()
    for s in [s5, s6, s7]:
        print(f"{s['setName']}: {len(s['rounds'])} rounds")
        for r in s['rounds']:
            print(f"  Round {r['roundId']}: {len(r['questions'])} questions")
