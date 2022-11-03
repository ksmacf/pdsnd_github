### Date created
November 3rd 2022

### Project Title
US Bikeshare Data Analysis

### Description
Create a python script that is interactive and displays various statistics such as
- most frequent times of travel
- most popular stations and trip
- total and average trip duration
- Gender and Birth Year of bikeshare users
then ends with a prompt to show the data 5 rows at a time. <br/><br/>

Functions used:

1. *get_filters()*: Asks user to specify a city, month, and day to analyze.
	- Returns:
		- (str) city - name of the city to analyze
		- (str) month - name of the month to filter by, or "all" to apply no month filter
        - (str) day - name of the day of week to filter by, or "all" to apply no day filter
2. *load_data(city, month, day)*: Loads data for the specified city and filters by month and day if applicable.
    - Args:
        - (str) city - name of the city to analyze
        - (str) month - name of the month to filter by, or "all" to apply no month filter
        - (str) day - name of the day of week to filter by, or "all" to apply no day filter
    - Returns:
        - df - Pandas DataFrame containing city data filtered by month and day
3. *time_stats(df)*: Displays statistics on the most frequent times of travel.
4. *station_stats(df)*: Displays statistics on the most popular stations and trip.
5. *trip_duration_stats(df)*: Displays statistics on the total and average trip duration.
	- *trip_calc(time, word)*: Calculate the trip time into years, weeks, days, hours and minutes where applicable
        - Args:
        	- (int) time - travel time from the data given in seconds
            - (str) word - type of calculation made (mean or total) to be printed in the output
        - Returns:
            - res - print statement of the calculated values to show the user
6. *user_stats(df)*: Displays statistics on bikeshare users.  <br/>
	Note: Washington has missing columns for Gender and Birth Year so need to skip this if true.
	- Display counts of gender (there are only Male or Female)
	- Display earliest, most recent, and most common year of birth
7. *check5(df)*: Display 5 rows of raw data in incriments upon user request, else abort

### Files used
Python Script:
- Kenji MACFARLANE_bikeshare.py <br/>

Data (ignored in commits):
- chicago.csv
- new_york_city.csv
- washington.csv

### Credits
See detailed list in 'references.txt'

