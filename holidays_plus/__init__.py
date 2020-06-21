import holidays

def get_named(self, name):
    """ Find dates of holidays by name, returns a list of dates. """
    return [key for key in self if self[key] == name]
holidays.HolidayBase.get_named = get_named

def pop_named(self, name):
    """ Remove and return holidays by-name.  Returns a list of dates removed. """
    to_pop = self.get_named(name)
    if not to_pop:
        raise KeyError(name)

    to_return = []
    for key in to_pop:
        to_return.append(self.pop(key))
    return to_return
holidays.HolidayBase.pop_named = pop_named
