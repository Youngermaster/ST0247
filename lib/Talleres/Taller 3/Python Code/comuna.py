class Comuna:

    _inversion = 0

    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        """I'm the '_name' property."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def inversion(self):
        """I'm the '_inversion' property."""
        return self._inversion

    @inversion.setter
    def inversion(self, value):
        self._inversion = value

    @inversion.deleter
    def inversion(self):
        del self._inversion
