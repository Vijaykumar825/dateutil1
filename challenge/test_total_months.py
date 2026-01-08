"""
Tests for the total_months() method of relativedelta.

These tests should FAIL on the original commit and PASS after the solution is applied.
"""
import pytest
from dateutil.relativedelta import relativedelta


class TestTotalMonths:
    """Test suite for relativedelta.total_months() method."""

    def test_total_months_basic_months_only(self):
        """Test total_months with only months specified."""
        delta = relativedelta(months=5)
        assert delta.total_months() == 5

    def test_total_months_years_only(self):
        """Test total_months with only years specified."""
        delta = relativedelta(years=2)
        assert delta.total_months() == 24

    def test_total_months_years_and_months(self):
        """Test total_months with both years and months."""
        delta = relativedelta(years=1, months=2)
        assert delta.total_months() == 14

    def test_total_months_negative_values(self):
        """Test total_months with negative years and months."""
        delta = relativedelta(years=-1, months=-3)
        assert delta.total_months() == -15

    def test_total_months_negative_months_only(self):
        """Test total_months with only negative months."""
        delta = relativedelta(months=-6)
        assert delta.total_months() == -6

    def test_total_months_zero(self):
        """Test total_months returns 0 for empty relativedelta."""
        delta = relativedelta()
        assert delta.total_months() == 0

    def test_total_months_ignores_days(self):
        """Test that total_months ignores days component."""
        delta = relativedelta(years=1, months=2, days=15)
        assert delta.total_months() == 14

    def test_total_months_only_days_returns_zero(self):
        """Test total_months returns 0 when only days/hours are set."""
        delta = relativedelta(days=30, hours=5)
        assert delta.total_months() == 0

    def test_total_months_mixed_sign(self):
        """Test total_months with mixed positive years and negative months."""
        delta = relativedelta(years=2, months=-3)
        assert delta.total_months() == 21  # 24 - 3

    def test_total_months_large_values(self):
        """Test total_months with large year values."""
        delta = relativedelta(years=100, months=6)
        assert delta.total_months() == 1206

    def test_total_months_from_date_difference(self):
        """Test total_months from relativedelta created from two dates."""
        from datetime import date
        dt1 = date(2018, 8, 1)
        dt2 = date(2017, 6, 1)
        delta = relativedelta(dt1, dt2)
        assert delta.total_months() == 14  # 1 year + 2 months

    def test_total_months_return_type(self):
        """Test that total_months returns an integer."""
        delta = relativedelta(years=1, months=2)
        result = delta.total_months()
        assert isinstance(result, int)
