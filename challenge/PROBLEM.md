# Add `total_months()` Method to relativedelta

## Background

The `relativedelta` class in python-dateutil is a powerful tool for representing time intervals. Unlike `datetime.timedelta`, it can handle calendar-based intervals like years and months. However, while `timedelta` provides a convenient `total_seconds()` method to get the total duration in seconds, `relativedelta` lacks a similar method for getting the total number of months.

## Problem Statement

Implement a `total_months()` method for the `relativedelta` class that returns the total number of months represented by the relativedelta object.

The method should:

1. Calculate the total months by combining the `years` and `months` attributes
2. Return an integer value representing the total months
3. Handle both positive and negative values correctly
4. Return 0 when the relativedelta has no years or months component

## Expected Behavior

```python
from dateutil.relativedelta import relativedelta

# Basic usage
relativedelta(months=5).total_months()           # Returns: 5
relativedelta(years=2).total_months()            # Returns: 24
relativedelta(years=1, months=2).total_months()  # Returns: 14

# Negative values
relativedelta(years=-1, months=-3).total_months()  # Returns: -15
relativedelta(months=-6).total_months()            # Returns: -6

# Zero case
relativedelta().total_months()                     # Returns: 0

# With other components (days, hours, etc. are ignored)
relativedelta(years=1, months=2, days=15).total_months()  # Returns: 14
relativedelta(days=30, hours=5).total_months()            # Returns: 0
```

## Important Notes

- The `total_months()` method only considers the `years` and `months` attributes
- Days, hours, minutes, seconds, and microseconds cannot be reliably converted to months without a reference date, so they are not included in the calculation
- The method should follow the existing patterns in the `relativedelta` class

## Repository Information

- **Repository**: [dateutil/dateutil](https://github.com/dateutil/dateutil)
- **Commit**: `e081f6725fbb49cae6eedaab7010f517e8490859b`
- **File to modify**: `src/dateutil/relativedelta.py`
