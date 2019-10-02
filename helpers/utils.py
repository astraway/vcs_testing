import pandas as pd
from datetime import timezone, datetime
import sys


def calculate_quote_dates(original_end_date, duration=1, target_end_date=None, eos_date=None):
    # set original end date to today if it's empty
    if original_end_date is None:
        original_end_date = datetime.now()

    # begin date
    begin_date = pd.to_datetime(original_end_date) + pd.DateOffset(days=1)

    # end date
    if target_end_date:
        end_date = pd.to_datetime(target_end_date)
    else:
        end_date = pd.to_datetime(original_end_date) + pd.DateOffset(years=duration)

    # update end date if eos
    if eos_date is not None and eos_date!='1970-01-01':
        eos_date_date = pd.to_datetime(eos_date)
        if (eos_date_date - end_date).days < 0:
            end_date = eos_date_date

    # format dates
    begin_date = str(begin_date.replace(tzinfo=timezone.utc).isoformat())
    end_date = str(end_date.replace(tzinfo=timezone.utc).isoformat())

    return begin_date, end_date


def calculate_date_diff(start_date, end_date):
    print(abs((end_date-start_date).days))


def get_method_name():
    return sys._getframe(1).f_code.co_name
