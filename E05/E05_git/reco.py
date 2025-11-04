import numpy as np
import pandas as pd
from functools import total_ordering

@total_ordering
class Hit:

    def __init__(self, modulo, sensore, time ):
        self.id_modulo = modulo
        self.id_sensore = sensore
        self.id_rivelazione = time

    def __lt__(self, other):
        if(self.id_rivelazione != other.id_rivelazione):
            return self.id_rivelazione < other.id_rivelazione
        
        elif (self.id_modulo != other.id_rivelazione):
            return self.id_modulo < other.id_modulo

        else:
            return self.id_sensore < other.id_sensore

    