# Abbreviation	Time Zone Name
# UTC	Coordinated Universal Time
# GMT	Greenwich Mean Time
# EDT	Eastern Daylight Time (US/Eastern)
# EST	Eastern Standard Time (US/Eastern)
# CDT	Central Daylight Time (US/Central)
# CST	Central Standard Time (US/Central)
# MDT	Mountain Daylight Time (US/Mountain)
# MST	Mountain Standard Time (US/Mountain)
# PDT	Pacific Daylight Time (US/Pacific)
# PST	Pacific Standard Time (US/Pacific)
# BST	British Summer Time
# CEST	Central European Summer Time
# CET	Central European Time
# EEST	Eastern European Summer Time
# EET	Eastern European Time
# IST	Indian Standard Time
# JST	Japan Standard Time
# AEDT	Australian Eastern Daylight Time
# AEST	Australian Eastern Standard Time


# from datetime import datetime
# import pytz
#
# # Input date-time string
# input_date_string = "10:17:29 Aug 28, 2023 PDT"
#
# # Define time zones
# source_timezone = pytz.timezone("US/Pacific")
# target_timezone = pytz.utc
#
# # Get your local timezone
# local_timezone = datetime.now(pytz.utc).astimezone().tzinfo
# print("Your local timezone:", local_timezone)
#
# # Extract the time zone abbreviation
# parts = input_date_string.split()
# tz_abbreviation = parts[-1]
# input_date_string = " ".join(parts[:-1])
#
# # Convert input string to datetime object
# input_datetime = datetime.strptime(input_date_string, "%H:%M:%S %b %d, %Y")
#
# # Set the source timezone
# input_datetime = source_timezone.localize(input_datetime)
#
# # Convert to target timezone (UTC)
# utc_datetime = input_datetime.astimezone(target_timezone)
#
# # Print the localized datetime
# print(input_datetime)
# print(utc_datetime)

from datetime import datetime

# Input date-time string
input_date_string = "10:17:29 Aug 28, 2023 PDT"

# Split the input string and get the date part
date_str = input_date_string.split()[1:-1]
date_str = " ".join(date_str)

# Convert date part to a datetime object
date_object = datetime.strptime(date_str, "%b %d, %Y")

# Print the extracted date
print("Date:", date_object.date())
