class Feature:
    def __init__(self, value, ftype, start_weight=10, change_rate=1, current_weight=10):
        self.value = value
        self.ftype = ftype
        self.start_weight = start_weight
        self.change_rate = change_rate
        self.current_weight = current_weight
    def __str__(self):
        return f'({self.value}-{self.current_weight})'
    def serialize(self):
        return {
            'value': self.value,
            'ftype': self.ftype,
        }
