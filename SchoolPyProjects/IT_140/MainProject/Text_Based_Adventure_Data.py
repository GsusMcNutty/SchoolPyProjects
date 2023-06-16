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


def command_list():
    commands = ['move', 'wait', 'exit', 'quit']
    return commands
