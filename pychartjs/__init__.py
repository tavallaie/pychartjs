class Extension:
    # Workaround to add arbitrary fields to pychartjs objects
    def __init__(self, base, **kwargs):
        self.base = base
        self.kwargs = kwargs
    def to_dict(self):
        res = self.base.to_dict()
        for k,v in self.kwargs.items():
            if type(v) is list:
                res[k] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in v]
            elif type(v) is dict:
                res[k] = {key: val.to_dict() if hasattr(val, 'to_dict') else val for key, val in v.items()}
            else:
                res[k] = v.to_dict() if hasattr(v, 'to_dict') else v
        return res
    def __getattr__(self, item):
        if item in self.kwargs:
            return self.kwargs[item]
        else:
            return getattr(self.base, item)
