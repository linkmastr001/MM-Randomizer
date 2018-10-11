import collections
from BaseClasses import Region, Location, Entrance, RegionType, Dungeon
from Items import ItemFactory


def create_dungeons(world):
    def make_dungeon(name, dungeon_regions_names, boss_key, small_keys, dungeon_items):
        dungeon_regions = [world.get_region(region) for region in dungeon_regions_names]

        dungeon = Dungeon(name, dungeon_regions, boss_key, small_keys, dungeon_items)
        for region in dungeon.regions:
            region.dungeon = dungeon
        return dungeon

    WF = make_dungeon(
        'Woodfall Temple',
       ['Woodfall Temple Beginning', 'Woodfall Temple Central Pillar'], 
       ItemFactory('Boss Key (Woodfall Temple)'), 
       ItemFactory(['Small Key (Woodfall Temple)'] * 1),
       ItemFactory(['Map (Woodfall Temple)', 'Compass (Woodfall Temple)']))

    SH = make_dungeon(
        'Snowhead Temple', 
        ['Snowhead Temple Beginning'], 
        ItemFactory('Boss Key (Snowhead Temple)'), 
        ItemFactory(['Small Key (Snowhead Temple)'] * 3), 
        ItemFactory(['Map (Snowhead Temple)', 'Compass (Snowhead Temple)']))

    GB = make_dungeon(
        'Great Bay Temple', 
        ['Great Bay Temple Beginning'], 
        ItemFactory('Boss Key (Great Bay Temple)'), 
        ItemFactory(['Small Key (Great Bay Temple)'] * 1), 
        ItemFactory(['Map (Great Bay Temple)', 'Compass (Great Bay Temple)']))

    ST = make_dungeon(
        'Stone Tower Temple', 
        ['Stone Tower Temple Beginning'], 
        ItemFactory('Boss Key (Stone Tower Temple)'), 
        ItemFactory(['Small Key (Stone Tower Temple)'] * 2), 
        ItemFactory(['Map (Stone Tower Temple)', 'Compass (Stone Tower Temple)']))

    world.dungeons = [WF, SH, GB, ST]


def create_regions(world):
    # TODO: finish out this whole thing (what I'm currently working on)
    world.regions = [
        create_ow_region('Beginning',[], ['Cursed Underground']),
        create_interior_region('Deku Flower Tutorial Area', [], ['Clock Tower Twisted Hallway']),
        create_interior_region('Clock Tower Basement',
            ['Remove the Cursed Mask', 'Song from HMS'],
            ['Clock Tower Exit', 'Clock Tower Twisted Hallway Backwards']),

        # TODO: Suffix Entrance to all of these
        create_ow_region('South Clock Town',
            ['SCT 20 Rupee Chest', 'Festival Tower Rupee Chest',
            'Clock Town Owl Statue', 'Clock Tower Platform HP', 'Clock Town Business Scrub'],
            ['To Clock Tower Basement', 'To Clock Tower Rooftop', 'South Mailbox',
            'SCT Top Exit to WCT', 'SCT Bottom Exit to WCT', 'SCT Exit to NCT',
            'SCT Bottom Exit to ECT', 'SCT Top Exit to ECT',
            'Clock Town South Gate', 'SCT Exit to Laundry Pool']),
        create_interior_region('Clock Tower Rooftop', ['Dropped Ocarina', 'Song from Skull Kid'], ['End of First Cycle', 'Moon Portal']),

        create_ow_region('East Clock Town',
            ['ECT 100 Rupee Chest', 'Deliver Letter to Mama To Postman'],
            ['To Honey and Darling', 'To Treasure Chest Shop', 'To Town Shooting Gallery', 'East Mailbox',
            'To Milk Bar', 'To Stock Pot Inn', 'To Stock Pot Inn Secret Entrance', 'To Mayors Office',
            'Bomber Bouncer', 'ECT Top Exit to SCT', 'ECT Bottom Exit to SCT',
            'ECT Exit to NCT', 'Clock Town East Gate']),
        create_interior_region('Honey and Darling',
            ['Honey and Darling Bombchu Bowling Prize', 'Honey and Darling Archery Prize',
            'Honey and Darling Basket Bomb Throw Prize', 'Honey and Darling Grand Champion'],
            ['Honey and Darling Exit']),
        create_interior_region('Treasure Chest Shop',
            ['Treasure Chest Game Goron Prize', 'Treasure Chest Game Human Prize',
             'Treasure Chest Game Zora Prize', 'Treasure Chest Game Deku Prize'], ['Treasure Chest Shop Exit']),
        create_interior_region('Town Shooting Gallery', ['Town Shooting Gallery Quiver Prize', 'Town Shooting Gallery HP Prize'], ['Town Shooting Gallery Exit']),
        create_interior_region('Milk Bar', ['Milk Bar Performance', 'Delivery to Mama Kafei'], ['Milk Bar Exit']),
        create_interior_region('Stock Pot Inn',
            ['Stock Pot Inn Key', 'Have you seen this man?',
            'Grandma Stories HP 1', 'Grandma Stories HP 2',
            'Toilet Hand HP', 'Your Room Rupee Chest', 'Anjus Room Rupee Chest',
            'We Shall Greet The Morning Together'],
            ['Stock Pot Inn Roof Exit', 'Stock Pot Inn Front Door']),
        create_interior_region('Mayors Office', ['Expert Person Solver Takes the Case', 'Mayor HP'], ['Mayors Office Exit']),
        create_interior_region('Bomber Tunnel', ['Bomber Tunnel Chest'], ['Bomber Tunnel Exit', 'Tunnel Balloon From ECT']),
        create_interior_region('Astral Observatory', ['Moon Cry'], ['Tunnel Balloon From Observatory', 'Astral Observatory Exit']),
        create_ow_region('Astral Observatory Deck', ['Moons Tear'], ['Observatory Deck to Inside', 'Astral Observatory Fence']),

        create_ow_region('West Clock Town',
            ['Bank 200 Rupee Prize', 'Bank HP', 'Rosa Sisters HP',
            'Hidden Owl Statue', 'Deliver Letter to Mama To Postman'],
            ['To Curiosity Shop', 'To Trading Post', 'To Bomb Shop',
            'To Post Office', 'To Lottery Shop', 'To Swordsmans School',
             'Clock Town West Gate', 'WCT Top Exit to SCT', 'WCT Bottom Exit to SCT']),
        create_ow_region('Mailbox', ['Deliver Letter to Kafei', 'Clock Town Mailbox HP']),
        create_interior_region('Curiosity Shop', ['Buy All Night Mask', 'Buy Bigger Bomb Bag'], ['Curiosity Shop Exit']),
        create_interior_region('Trading Post', [], ['Trading Post Exit']),
        create_interior_region('Bomb Shop', ['Buy Bomb Bag', 'Buy Bigger Bomb Bag'], ['Bomb Shop Exit']),
        create_interior_region('Post Office', ['Deliver Letter to Mama To Postman', 'Counting Is Hard'], ['Post Office Exit']),
        create_interior_region('Lottery Shop', [], ['Lottery Shop Exit']),
        create_interior_region('Swordsmans School', ['Sword School HP'], ['Swordsmans School Exit']),

        create_ow_region('North Clock Town',
            ['Bombers Notebook', 'Bomber Code', 'NCT Tree HP', 'Clock Town Tingle Clock Town Map',
            'Clock Town Tingle Woodfall Map', 'Foil Sakon', 'NCT Keaton HP'],
            ['To GF Clock Town', 'To Deku Playground', 'Clock Town North Gate',
            'NCT Exit to SCT', 'NCT Exit to ECT', 'North Mailbox']),
        # TODO: Don't know how to handle the clock town stray fairy right now
        # I think for now, we could just place checks on the fairy herself
        # But later we'll have Stray Fairy Pickups in the pool
        create_interior_region('Clock Town Fairy Shrine', ['Clock Town GF Magic Bar', 'Clock Town GF Mask'], ['Clock Town Fairy Shrine Exit']),
        create_interior_region('Deku Playground', ['Deku Challenge Day 1', 'Deku Challenge Day 2', 'Deku Challenge Day 3', 'Deku Playground HP'], ['Deku Playground Exit']),

        create_ow_region('Laundry Pool',
            ['Don Gero Town Frog', 'Listen To Guru Guru'],
            ['Curiosity Backroom Entrance', 'Laundry Pool Exit to SCT']),
        create_interior_region('Curiosity Shop Backroom', ['Keaton Mask From Kafei', 'Letter From Kafei', 'Pendant From Kafei'], ['Clock Town']),

        create_ow_region('Termina Field',
            ['Learn Kamaro Dance', 'TF Chest In The Grass', 'TF Chest On A Stump'],
            ['TF to Swamp', 'South Gate to Clock Town',
            'TF Mountain Icicles', 'North Gate to Clock Town',
            'TF Great Bay Gate', 'West Gate to Clock Town',
            'TF to Ikana', 'East Gate to Clock Town', 'TF to Obs Over Fence Maybe',
            'To TF Peahat Grotto', 'To TF Beehive Grotto', 'To East Pillar Grotto', 'To TF Business Scrub Grotto',
            'To Swamp Gossips', 'To Mountain Gossips', 'To Ocean Gossips',
            'To Canyon Gossips', 'To Dodongo Grotto', 'To TF Deku Baba Pit', 'TF To Milk Road']),
        create_grotto_region('TF Peahat Grotto', ['TF Peahat Grotto HP'], ['TF Peahat Grotto Exit']),
        create_grotto_region('TF Beehive Grotto', ['TF Beehive Grotto HP'], ['TF Beehive Grotto Exit']),
        create_grotto_region('TF East Pillar Grotto', ['TF East Pillar Bombchu Pit Chest'], ['TF East Pillar Grotto Exit']),
        create_grotto_region('TF Business Scrub Grotto', ['TF Business Scrub Grotto HP'], ['TF Business Scrub Grotto Exit']),
        create_grotto_region('Swamp Gossips', ['Swamp Gossip Check', '4 Gossip Stone HP'], ['Swamp Gossips Exit']),
        create_grotto_region('Mountain Gossips', ['Mountain Gossip Check', '4 Gossip Stone HP'], ['Mountain Gossips Exit']),
        create_grotto_region('Oceans Gossips', ['Ocean Gossip Check', '4 Gossip Stone HP'], ['Oceans Gossips Exit']),
        create_grotto_region('Canyon Gossips', ['Canyon Gossip Check', '4 Gossip Stone HP'], ['Canyon Gossips Exit']),
        create_grotto_region('TF Dodongo Grotto', ['TF Dodongo Grotto HP'], ['TF Dodongo Grotto Exit']),
        create_grotto_region('TF Deku Baba Pit', ['TF Deku Baba Pit Chest'], ['TF Deku Baba Pit Exit']),

        create_ow_region('Swamp Path', ['Swamp Path Bat Tree HP', 'Swamp Tingle Woodfall Map', 'Swamp Tingle Snowhead Map'],
                         ['Swamp Path To Termina Field', 'To Swamp Shooting Gallery',
                          'Swamp Path To Southern Swamp (Poisoned)', 'Swamp Path To Southern Swamp (Clean)',
                          'To Swamp Path Rupee Pit']),
        create_grotto_region('Swamp Path Rupee Pit', ['Swamp Path Rupee Pit Chest'], ['Swamp Path Rupee Pit Exit']),
        create_interior_region('Swamp Shooting Gallery', ['Swamp Shooting Gallery Quiver Prize', 'Swamp Shooting Gallery HP Prize'], ['Swamp Shooting Gallery Exit']),

        create_ow_region('Southern Swamp Tourist Region (Poisoned)', ['Swamp Tourist Roof HP', 'Swamp Owl Statue'],
                         ['Tourist Region to Swamp path', 'Swamp Big Octo From Tourist Region',
                          'Tourist Centre Big Octo', 'To Swamp Tourist Centre', 'Tourist Region To Potion Shop Region']),
        create_ow_region('Southern Swamp Potion Shop Region (Poisoned)', [],
                         ['Potion Shop Region to Tourist Region', 'Potion Shop Region To Potion Shop', 'To Lost Woods']),
        create_ow_region('Southern Swamp Deku Palace Region', [],
                         ['Palace Region to Tourist Region', 'Palace Region to Deku Palace', 'some other exits I think I dunno']),

        create_interior_region('Swamp Tourist Centre', ['Swamp Tourist Free Product', 'Pictograph Contest Winner'], ['Boat Ride', 'Southern Swamp']),
        create_ow_region('Boat Ride', [], ['Poison Swamp']),
        create_ow_region('Poison Swamp', [], ['Swamp Exit to Deku Palace', 'Swamp Spider House Entrance']),
        # TODO Give an exit
        create_interior_region('Swamp Spider House'),
        create_ow_region('Deku Palace', ['Deku Palace HP'], ['Deku Palace Back Entrance', 'Deku Palace Chamber Entrance']),
        create_interior_region('Deku Palace Royal Chamber'),
        create_interior_region('Deku Palace Shrine'),
        # TODO All of the Woodfall area
        create_interior_region('Woodfall',
            [],
            []),

        create_ow_region('Woodfall Owl Platform', [], ['Woodfall Temple Entrance', 'GF Woodfall', 'Woodfall']),

        create_dungeon_region('Woodfall Temple Lobby',
            ['Woodfall Temple Lobby Stray Fairy', 'Woodfall Temple Lobby Stray Fairy Chest'],
            ['Woodfall Temple Front Exit', 'Woodfall Temple Torch Platform']),
        create_dungeon_region('Woodfall Temple Lower 1F',
            ['Woodfall Temple Central Flower Pot Fairy', 'Woodfall Temple Beehive Stray Fairy',
            'Woodfall Temple Central Flower Deku Baba', 'Woodfall Temple Deku Flower Elevator Beehive'
            'Woodfall Temple Central Flower Stray Fairy Chest', 'Woodfall Temple Map Chest',
            'Woodfall Temple Small Key Chest'],
            ['Woodfall Temple Central Flower Torch', 'Woodfall Temple Small Key Door',
            'Woodfall Temple Deku Flower Elevator']),
        create_dungeon_region('Woodfall Temple Push Block Room',
            ['Woodfall Temple Skulltula Fairy', 'Woodfall Temple Push Block Beehive'
            'Woodfall Temple Push Block Bubble Fairy', 'Woodfall Temple Compass Chest'],
            ['Woodfall Temple Small Key Door Backwards', 'Woodfall Temple Spiderweb']),
        create_dungeon_region('Woodfall Temple Dark Puff Arena',
            ['Woodfall Temple Dark Puff Killing Prize'],
            ['Woodfall Temple Spiderweb Backwards', 'Woodfall Temple 2F Barred Door']),
        create_dungeon_region('Woodfall Temple Upper 1F',
            ['Woodfall Temple Central Flower Bubble Fairy', 'Woodfall Temple Bow Chest'],
            ['Woodfall Temple Stairs Backwards', 'Woodfall Temple Central Flower Barred Door']),
        create_dungeon_region('Woodfall Temple Gecko Arena',
            ['Woodfall Temple Boss Key Chest', 'Woodfall Temple Frog Get']),
        create_dungeon_region('Woodfall Temple Final Chamber',
            ['Woodfall Temple Lower East Bubble Fairy', 'Woodfall Temple Upper East Bubble Fairy',
            'Woodfall Temple West Bubble Fairy', 'Woodfall Temple Hot Bubble Fairy'],),

        create_interior_region('Woodfall Fairy Shrine', ['Woodfall GF Reward'], ['Woodfall']),

        # create_ow_region('Mountain Icicles', [], ['Termina Field North Exit', 'Termina Field From Mountain']),
        create_ow_region('Mountain Village Path South', [], ['Mountain Snowball Block', 'Mountain Path South Exit']),
        create_ow_region('Path to Mountain Village North', [], ['Mountain Path North Exit', 'Mountain Snowball Block']),
        create_ow_region('Mountain Village',
            ['Frog Choir'],
            ['Mountain Smithy', 'Goron Shrine', 'MV Exit to Snowhead',
            'MV Exit to Goron Village', 'MV Exit to Termina Field']),
        create_ow_region('Path to Goron Village'),
        create_ow_region('Outside Goron Village'),
        create_interior_region('Lens of Truth Cave'),
        create_interior_region('Goron Village'),
        create_interior_region('Goron Shrine'),
        create_ow_region('Path to Snowhead'),
        create_ow_region('Snowhead'),
        create_interior_region('Snowhead Fairy Shrine', ['Snowhead GF Reward'], ['Snowhead Spire']),

        create_ow_region('Great Bay Coast'),
        create_interior_region('Fisherman Hut'),
        create_interior_region('Oceanside Spider House'),
        create_interior_region('Marine Research Lab'),
        create_ow_region('Pirate Fortress'),
        create_interior_region('Pinnacle Rock'),
        create_ow_region('Zora Cape'),
        create_interior_region('Zora Hall'),
        create_interior_region('Zora Shop'),
        create_interior_region('Zora Hall Drummer Room'),
        create_interior_region('Zora Hall Lulu Room'),
        create_interior_region('Zora Hall Bassist Room'),
        create_interior_region('Zora Hall Pianist Room'),
        create_interior_region('Waterfall Rapids', ['Beaver Bottle', 'Beaver HP']),
        create_interior_region('Great Bay Fairy Shrine', ['Great Bay GF Reward'], ['Great Bay Fairy Ledge']),

        create_ow_region('Path to Ikana'),
        create_ow_region('Ikana Graveyard', ['Captains Chest'],
            ['SoS Grave Grotto', 'HP Grave Grotto', 'Dampe Grave Grotto', 'Dampe Door']),
        create_interior_region('Dampe Grave'),
        create_grotto_region('Storms Grave'),
        create_grotto_region('Heart Piece Grave'),
        create_interior_region('Sakon Hideout'),
        create_interior_region('Secret Shrine'),
        create_interior_region('Poe Sister House'),
        create_interior_region('Spoop Cave'),
        create_interior_region('Music Box House'),
        create_interior_region('Bottom of the Well'),
        create_ow_region('Ikana Castle'),
        create_ow_region('Stone Tower'),
        create_interior_region('Stone Tower Fairy Shrine', ['Stone Tower GF Reward'], ['Ikana Canyon'])
    ]
    world.regions.extend([
        create_dungeon_region('Woodfall Temple Lobby',
            [],
            ['Woodfall Temple Lobby Ledge', 'Woodfall Temple Front Exit']),
        create_dungeon_region('Woodfall Temple First Floor',
            [],
            ['Woodfall Temple Small Key Door', 'Woodfall Temple Wooden Flower']),
        create_dungeon_region('Woodfall Temple Push Block Bridge Room',
            [],
            ['Woodfall Temple Upstairs Spiderweb']),
        create_dungeon_region('Woodfall Temple Dark Puff Gauntlet',
            [],
            ['Woodfall Temple ']),
    ])
    world.initialize_regions()

def create_ow_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Overworld, locations, exits)

def create_interior_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Interior, locations, exits)

def create_dungeon_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Dungeon, locations, exits)

def create_grotto_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Grotto, locations, exits)

def _create_region(name, type, locations=None, exits=None):
    ret = Region(name, type)
    if locations is None:
        locations = []
    if exits is None:
        exits = []

    for exit in exits:
        ret.exits.append(Entrance(exit, ret))
    for location in locations:
        address, address2, default, type = location_table[location]
        ret.locations.append(Location(location, address, address2, default, type, ret))
    return ret

# TODO: addresses, SO many addresses, and more
location_table = {
    'Remove the Cursed Mask': (None, None, None, 'Mask'),
    'SCT 20 Rupee Chest': (None, None, None, 'Chest'),
    'Festival Tower Rupee Chest': (None, None, None, 'Chest'),
    'ECT 100 Rupee Chest': (None, None, None, 'Chest'),
    'WFT Map Chest': (None, None, None, 'Chest'),
    'WFT Small Key Chest': (None, None, None, 'Chest'),
    'WFT Compass Chest': (None, None, None, 'Chest'),
    'WFT Bow Chest': (None, None, None, 'Chest'),
    'WFT Boss Key Chest': (None, None, None, 'Chest'),
    'Clock Town Owl Statue': (None, None, None, 'Statue'),
    'Milk Road Owl Statue': (None, None, None, 'Statue'),
    'Swamp Owl Statue': (None, None, None, 'Statue'),
    'Woodfall Owl Statue': (None, None, None, 'Statue'),
    'Song from Skull Kid': (None, None, None, 'Song'),
    'Song from HMS': (None, None, None, 'Song'),
    'Song from Romani': (None, None, None, 'Song'),
    'Song from Monkey': (None, None, None, 'Song'),
    'Song on Owl Tablet': (None, None, None, 'Song'),
    'Song from Baby Goron': (None, None, None, 'Song'),
    'Song from Baby Zoras': (None, None, None, 'Song'),
    'Song in Composer Grave': (None, None, None, 'Song'),
    'Song from Igos': (None, None, None, 'Song'),
    'Song from the Giants': (None, None, None, 'Song'),
    'Town Deku Salesman': (None, None, None, 'NPC'),
    'Swamp Deku Salesman': (None, None, None, 'NPC'),
    'Mountain Deku Salesman': (None, None, None, 'NPC'),
    'Ocean Deku Salesman': (None, None, None, 'NPC'),
    'Canyon Deku Salesman': (None, None, None, 'NPC'),
    'Song from Goron Elder': (None, None, None, 'NPC'),
    'Love on the Balcony': (None, None, None, 'Collectable'),
    "Claim Odolwa's Remains": (None, None, None, 'Collectable'),
    "Claim Odolwa's Heart": (None, None, None, 'Collectable'),
    "Claim Goht's Remains": (None, None, None, 'Collectable'),
    "Claim Goht's Heart": (None, None, None, 'Collectable'),
    "Claim Gyorg's Remains": (None, None, None, 'Collectable'),
    "Claim Gyorg's Heart": (None, None, None, 'Collectable'),
    "Claim Odolwa's Remains": (None, None, None, 'Collectable'),
    "Claim Odolwa's Heart": (None, None, None, 'Collectable'),
    'Defeat Odolwa': (None, None, None, 'Event'),
    'Defeat Goht': (None, None, None, 'Event'),
    'Defeat Gyorg': (None, None, None, 'Event'),
    'Defeat Twinmold': (None, None, None, 'Event'),
    'Song from Giants': (None, None, None, 'Song'),
    'WFT Lobby Floating Fairy': (None, None, None, 'SF'),
    'WFT Central Flower Deku Baba': (None, None, None, 'SF'),
    'WFT Central Flower Corner Pot': (None, None, None, 'SF'),
    'WFT Deku Flower Elevator Beehive': (None, None, None, 'SF'),
    'WFT Bridge Skulltula': (None, None, None, 'SF'),
    'WFT Bridge Room Beehive': (None, None, None, 'SF'),
    'WFT Dark Puff Battle Arena Chest': (None, None, None, 'SFC'),
    'WFT Under Poison Bridge': (None, None, None, 'SF'),
    'WFT Central Flower Bubble Fairy': (None, None, None, 'SF'),
    'WFT Central Room Switch Chest': (None, None, None, 'SFC'),
    'WFT Lower East Bubble Fairy': (None, None, None, 'SF'),
    'WFT Upper East Bubble Fairy': (None, None, None, 'SF'),
    'WFT West Bubble Fairy': (None, None, None, 'SF'),
    'WFT Hot Bubble Fairy': (None, None, None, 'SF'),
    'WFT Lobby Fairy Chest': (None, None, None, 'SFC'),
    'SH SF1': (None, None, None, 'SF-SH'),
    'SH SF2': (None, None, None, 'SF-SH'),
    'SH SF3': (None, None, None, 'SF-SH'),
    'SH SF4': (None, None, None, 'SF-SH'),
    'SH SF5': (None, None, None, 'SF-SH'),
    'SH SF6': (None, None, None, 'SF-SH'),
    'SH SF7': (None, None, None, 'SF-SH'),
    'SH SF8': (None, None, None, 'SF-SH'),
    'SH SF9': (None, None, None, 'SF-SH'),
    'SH SF10': (None, None, None, 'SF-SH'),
    'SH SF11': (None, None, None, 'SF-SH'),
    'SH SF12': (None, None, None, 'SF-SH'),
    'SH SF13': (None, None, None, 'SF-SH'),
    'SH SF14': (None, None, None, 'SF-SH'),
    'SH SF15': (None, None, None, 'SF-SH'),
    'GB SF1': (None, None, None, 'SF-GB'),
    'GB SF2': (None, None, None, 'SF-GB'),
    'GB SF3': (None, None, None, 'SF-GB'),
    'GB SF4': (None, None, None, 'SF-GB'),
    'GB SF5': (None, None, None, 'SF-GB'),
    'GB SF6': (None, None, None, 'SF-GB'),
    'GB SF7': (None, None, None, 'SF-GB'),
    'GB SF8': (None, None, None, 'SF-GB'),
    'GB SF9': (None, None, None, 'SF-GB'),
    'GB SF10': (None, None, None, 'SF-GB'),
    'GB SF11': (None, None, None, 'SF-GB'),
    'GB SF12': (None, None, None, 'SF-GB'),
    'GB SF13': (None, None, None, 'SF-GB'),
    'GB SF14': (None, None, None, 'SF-GB'),
    'GB SF15': (None, None, None, 'SF-GB'),
    'ST SF1': (None, None, None, 'SF-ST'),
    'ST SF2': (None, None, None, 'SF-ST'),
    'ST SF3': (None, None, None, 'SF-ST'),
    'ST SF4': (None, None, None, 'SF-ST'),
    'ST SF5': (None, None, None, 'SF-ST'),
    'ST SF6': (None, None, None, 'SF-ST'),
    'ST SF7': (None, None, None, 'SF-ST'),
    'ST SF8': (None, None, None, 'SF-ST'),
    'ST SF9': (None, None, None, 'SF-ST'),
    'ST SF10': (None, None, None, 'SF-ST'),
    'ST SF11': (None, None, None, 'SF-ST'),
    'ST SF12': (None, None, None, 'SF-ST'),
    'ST SF13': (None, None, None, 'SF-ST'),
    'ST SF14': (None, None, None, 'SF-ST'),
    'ST SF15': (None, None, None, 'SF-ST'),
    'Open the Moon': (None, None, None, 'Event')
    }

#TODO: Shops
# Castle Town Potion Shop Item 1': (shop_address(3, 0), None, 0x30, 'Shop', 0x31, 'the Market'),
