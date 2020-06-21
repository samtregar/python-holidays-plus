# python-holidays-plus
Enhanced wrapper around the Python-Holidays library offering expanded functionality

This module adds a couple useful features to the Python holidays modules.  For example:

```python
import holidays
import holidays_plus

# holidays, but not the racist one
holidays = holidays.US()
holidays.pop_named("Columbus Day")

# wait, when is Martin Luther King Day this year?
days = holidays.get_named("Martin Luther King Day")
print("It's on {days[0]} this year.")
```

If you have ideas for additional functionality that might be added
here, please let me know by opening an issue or sending me a PR here:

https://github.com/samtregar/python-holidays-plus
