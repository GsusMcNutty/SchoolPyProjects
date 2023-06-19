def room_dictionary():
    rooms = {'tower room': {'north': 'guard quarters'},

             'basement': {'east': 'kitchen'},

             'kitchen': {'north': 'dining room',
                         'south': 'servant quarters',
                         'east': 'guard quarters',
                         'west': 'basement'
                         },

             'sitting room': {'north': 'main hall',
                              'east': 'dining room',
                              'west': 'library'
                              },

             'dining room': {'west': 'sitting room',
                             'south': 'kitchen'
                             },

             'foyer': {'west': 'trophy hall',
                       'south': 'main hall'
                       },

             'library': {'north': 'study',
                         'east': 'sitting room'
                         },

             'study': {'north': 'trophy hall',
                       'south': 'library'
                       },

             'servant quarters': {'north': 'kitchen',
                                  'west': 'living quarters'
                                  },

             'living quarters': {'east': 'servant quarters',
                                 'west': 'garden'
                                 },

             'trophy hall': {'east': 'foyer',
                             'south': 'study'
                             },

             'garden': {'east': 'living quarters'},

             'guard quarters': {'south': 'tower room',
                                'west': 'kitchen'
                                },

             'main hall': {'north': 'foyer',
                           'south': 'sitting room'
                           }
             }
    return rooms


def get_rooms():
    return room_dictionary()


artifacts = {'kitchen': {'shield': "neh'ctik"},
             'dining room': {'amulet': "moor gnin'id"},
             'foyer': {'wristband': "re'yof"},
             'sitting room': {'icon': "moor gnit'tis"},
             'study': {'sword': "y'duts"},
             'library': {'wand': "y'rarb'il"}
             }


def get_artifacts():
    return artifacts


def command_list():
    command = ['move', 'wait', 'exit', 'quit', 'search', 'pickup', 'inventory', 'help', 'objectives']
    return command


def instructions():
    return ("Instructions:\n"
            "Move through each of the rooms in search of the 6 artifacts to defeat the villain.\n"
            "Movement is done by declaring the 'move' command, then a cardinal direction.\n"
            "You can search a room for anything of note by using the 'search' command.\n"
            "You can pick up an item by using the 'pickup' command.\n"
            "You can check your inventory at any time by using the 'inventory' command.\n"
            "Use the 'objectives' command to list the current remaining objectives.\n"
            "The 'wait' command can be used to set back to a default state.\n"
            "Commands may be inputted at any time to interrupt another.\n"
            "Type 'exit' or 'quit' to exit at any time.\n")
