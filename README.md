# python-holidays-plus
Enhanced add-on for the Python-Holidays library offering expanded functionality

This module adds a couple useful features to the Python holidays modules.  For example:

```python
import holidays
import holidays_plus

from datetime import datetime

# holidays, but not the racist one
our_holidays = holidays.US(years=[datetime.now().year])
our_holidays.pop_named("Columbus Day")

# wait, when is Martin Luther King Day this year?
(day,) = our_holidays.get_named("Martin Luther King Jr. Day")
print(f"Martin Luther King Jr. Day is on {day} this year.")
```

If you have ideas for additional functionality that might be added
here, please let me know by opening an issue or sending me a PR here:

https://github.com/samtregar/python-holidays-plus
