from enum import Enum
from typing import List, Dict, Tuple
from AbhiksPython.hapBack import *


class proxMappings(Enum):
    '''
    Enumerated class for representing prox distance
    '''
    intimate = 'intimate'
    personal = 'personal'
    social = 'social'
    public_general = 'public_gen'
    public = 'public'

    def get_int(self) -> int:
        int_dict = {
            'intimate': 0,
            'personal': 1,
            'social': 2,
            'public': 3,
            'public_gen': 4
        }

        return int_dict[self.value]

    def get_str(self) -> str:
        return self.value

class ButtonType(Enum):
    '''
    Enumerated class for representing different button types for the GUI.
    '''
    static_type = 'static'
    dynamic_type = 'dynamic'
    prox_abs = 'prox_abs'
    prox_rel = 'prox_rel'
    feet_abs = 'feet_abs'
    feet_rel = 'feet_rel'

    # provides the appropriate int for the button type
    def get_int(self) -> int:
        int_dict: Dict = {
            'static': 0,
            'dynamic': 1,
            'prox_abs': 2,
            'prox_rel': 3,
            'feet_abs': 4,
            'feet_rel': 5

        }

        return int_dict[self.value]

    # provides the appropriate api call for the button type
    def get_api_call(self, dist: int, pattern_num: int):
        api_dict: Dict[List] = {
            'prox_abs': [a1, a2],
            'prox_rel': [r1, r2],
            'feet_abs': [a1, a2],
            'feet_rel': [r1, r2]
        }
        hs = hapserver()
        api_dict[self.value][pattern_num](dist, hs)

    # provides a Tuple of distances for button type
    def get_dist(self) -> Tuple:
        dist_dict: Dict[Tuple] = {
            'prox_abs': (proxMappings.intimate,
                         proxMappings.personal,
                         proxMappings.social,
                         proxMappings.public_general,
                         proxMappings.public),
            'prox_rel': (proxMappings.intimate,
                         proxMappings.personal,
                         proxMappings.social,
                         proxMappings.public_general,
                         proxMappings.public),
            'feet_abs': (5, 10, 15, 20, 25),
            'feet_rel': (5, 10, 15, 20, 25)
        }

        return dist_dict[self.value]




