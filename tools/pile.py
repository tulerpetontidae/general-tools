class CircularList(list):
    """
    Making circular version of the list
    """
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs) 
        
    def cget(self, key):
        return self[key % len(self)]
    
    
def arange(start, stop, step=1, endpoint=True):
    """
    np.arange with fixed endpoint
    """
    arr = np.arange(start, stop, step)

    if endpoint and arr[-1]+step!=stop:
        arr = np.concatenate([arr,[stop]])

    return arr

def inverse_dict(d):
    """
    Invert the dict
    
    Parameters
    ----------
    d : dict
        Input dict {'key1': ['val1', 'val2', ...], ...}
    Returns
    -------
    dict
        Inverted dict {'val1': 'key1',  'val2': 'key1', ...}
    """
    d_inv = {}
    for k, vs in d.items():
        for v in vs:
            d_inv[v] = k
    return d_inv