#!/bin/bash
set -e

case "$1" in
    base)
        # Run existing relativedelta tests (should pass)
        python -m pytest tests/test_relativedelta.py -v
        ;;
    new)
        # Run new total_months tests (should fail initially)
        python -m pytest challenge/test_total_months.py -v
        ;;
    *)
        echo "Usage: ./test.sh {base|new}"
        exit 1
        ;;
esac
