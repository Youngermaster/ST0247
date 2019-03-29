class Comuna:
    _boys = 0
    _girls = 0
    _young_men = 0
    _young_women = 0
    _men = 0
    _women = 0
    _older_men = 0
    _older_women = 0
    _difference_between_men_and_women = 0
    _population = 0

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
    def boys(self):
        """I'm the '_boys' property."""
        return self._boys

    @boys.setter
    def boys(self, value):
        self._boys = value

    @boys.deleter
    def boys(self):
        del self._boys

    @property
    def girls(self):
        """I'm the '_girls' property."""
        return self._girls

    @girls.setter
    def girls(self, value):
        self._girls = value

    @girls.deleter
    def girls(self):
        del self._girls

    @property
    def young_men(self):
        """I'm the '_young_men' property."""
        return self._young_men

    @young_men.setter
    def young_men(self, value):
        self._young_men = value

    @young_men.deleter
    def young_men(self):
        del self._young_men

    @property
    def young_women(self):
        """I'm the '_young_women' property."""
        return self._young_women

    @young_women.setter
    def young_women(self, value):
        self._young_women = value

    @young_women.deleter
    def young_women(self):
        del self._young_women
    
    @property
    def men(self):
        """I'm the '_men' property."""
        return self._men

    @men.setter
    def men(self, value):
        self._men = value

    @men.deleter
    def men(self):
        del self._men

    @property
    def women(self):
        """I'm the '_women' property."""
        return self._women

    @women.setter
    def women(self, value):
        self._women = value

    @women.deleter
    def women(self):
        del self._women

    @property
    def older_men(self):
        """I'm the '_older_men' property."""
        return self._older_men

    @older_men.setter
    def older_men(self, value):
        self._older_men = value

    @older_men.deleter
    def older_men(self):
        del self._older_men

    @property
    def older_women(self):
        """I'm the '_older_women' property."""
        return self._older_women

    @older_women.setter
    def older_women(self, value):
        self._older_women = value

    @older_women.deleter
    def older_women(self):
        del self._older_women

    @property
    def _difference_between_men_and_women(self):
        """I'm the '__difference_between_men_and_women' property."""
        return self.__difference_between_men_and_women

    @_difference_between_men_and_women.setter
    def _difference_between_men_and_women(self, value):
        self.__difference_between_men_and_women = value

    @_difference_between_men_and_women.deleter
    def _difference_between_men_and_women(self):
        del self.__difference_between_men_and_women

    def get_all_population():
        _population = _boys + _girls + _young_men + _young_women + _men + _women + _older_men + older_women
        return _population

    # def get