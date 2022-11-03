import time
import pandas as pd
import numpy as np
# Set display option for when users want to check the data in their console
# as per https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Which City (Chicago, New York City, Washington) do you wish to check?\n\n").lower()
            cities = ['chicago', 'new york city', 'washington']
            if city not in cities:
                print('\nSorry, don\'t recognize it. Please try again\n')
                continue
            else:
                print("\nOkay, {} it is!\n".format(city.upper()))
                break
            break
        except NameError:
            print('\nSorry, don\'t recognize it. Please try again\n')
        except KeyboardInterrupt:
            print('\n No input taken\n')

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Which month do you wish to check?\n\nYou can choose between January to June, or select 'all' if you do not which to select\n\n").lower()
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if month == 'all':
                print("\nOkay, ALL MONTHS it is!\n")
                break
            elif month not in months:
                print('\nSorry, don\'t recognize it. Please try again\n')
                continue
            else:
                print("\nOkay, {} it is!\n".format(month.upper()))
                break
            break
        except NameError:
            print('\nSorry, don\'t recognize it. Please try again\n')
        except KeyboardInterrupt:
            print('\n No input taken\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Which day of the week do you wish to check?\n\nYou can choose any single day, or select 'all' if you do not which to select\n\n").lower()
            dow = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            if day == 'all':
                print("\nOkay, ALL DAYS it is!\n")
                break
            elif day not in dow:
                print('\nSorry, don\'t recognize it. Please try again\n')
                continue
            else:
                print("\nOkay, {} it is!\n".format(day.upper()))
                break
            break
        except NameError:
            print('\nSorry, don\'t recognize it. Please try again\n')
        except KeyboardInterrupt:
            print('\n No input taken\n')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mcm = df['month'].mode()[0]
    if mcm == 1:
        print('\nThe most commonly month is: January\n')
    elif mcm == 2:
        print('\nThe most commonly month is: February\n')
    elif mcm == 3:
        print('\nThe most commonly month is: March\n')
    elif mcm == 4:
        print('\nThe most commonly month is: April\n')
    elif mcm == 5:
        print('\nThe most commonly month is: May\n')
    else:
        print('\nThe most commonly month is: June\n')

    # display the most common day of week
    mcdow = df['day_of_week'].mode()[0]
    print("\nThe most common day of week is: " + mcdow + "\n")


    # display the most common start hour
    mch = df['Start Time'].dt.hour.mode()[0]
    if mch == 12:
        print("\nThe most commonly start hour is: {} pm\n".format(mch))
    elif mch >= 12:
        print("\nThe most commonly start hour is: {} pm\n".format(mch - 12))
    elif mch == 24:
        print("\nThe most commonly start hour is: 12 am\n")
    else:
        print("\nThe most commonly start hour is: {} am\n".format(mch))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mcst = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station is: {}\n".format(mcst))

    # display most commonly used end station
    mcet = df['End Station'].mode()[0]
    print("\nThe most commonly used End station is: {}\n".format(mcet))

    # display most frequent combination of start station and end station trip
    mcstoet = ('FROM ' + '\'' + df['Start Station'] + '\'' +' TO ' + '\'' + df['End Station']+'\'').mode()[0]
    print("\nThe most frequent combination of start station and end station trip is:\n {}\n".format(mcstoet))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Create a function instead of repeating the calculations to convert date-time from seconds
    ### I could not find a good package for this so it was quicker if I made this myself
    def trip_calc(time, word):
        """ 
        Calculate the trip time into years, weeks, days, hours and minutes where applicable
        
        Args:
            (int) time - travel time from the data given in seconds
            (str) word - type of calculation made (mean or total) to be printed in the output
        Returns:
            res - print statement of the calculated values to show the user
        """
        years = time // 31536000
        y_rem = time % 31536000
        weeks = y_rem // 604800
        w_rem = y_rem % 604800
        days = w_rem // 86400
        d_rem = w_rem % 86400
        hours = d_rem // 3600
        h_rem = d_rem % 3600
        minutes = h_rem // 60
        m_rem = h_rem % 60
    
        if years != 0:
            res = print("\nThe {} travel time is calculated to be:\n {} years, {} weeks, {} days, {} hours, {} minutes and {} seconds\n".format(word, years, weeks, days, hours, minutes, m_rem))
        elif weeks != 0:
            res = print("\nThe {} travel time is calculated to be:\n {} weeks, {} days, {} hours, {} minutes and {} seconds\n".format(word, weeks, days, hours, minutes, m_rem))
        elif days != 0:
            res = print("\nThe {} travel time is calculated to be:\n {} days, {} hours, {} minutes and {} seconds\n".format(word, days, hours, minutes, m_rem))
        elif hours != 0:
            res = print("\nThe {} travel time is calculated to be:\n {} hours, {} minutes and {} seconds\n".format(word,hours, minutes, m_rem))
        else:
            res = print("\nThe {} travel time is calculated to be:\n {} minutes and {} seconds\n".format(word, minutes, m_rem))

        return res

    # display total travel time
    duration = df['Trip Duration'].sum() # in seconds
    ### Calculate in years, weeks, days, hours, minutes and remainder
    trip_calc(duration, 'total')

    # display mean travel time
    mean_travel = int(df['Trip Duration'].mean().round()) # in integer format
    trip_calc(mean_travel, 'mean')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df['User Type'].value_counts()
    sub = user_counts['Subscriber']
    cus = user_counts['Customer']
    while True:
        try:
            dep = user_counts['Dependent']
            # There is only one entry within the entire data so need to account for it with this loop
            break
        except:
            dep = 0
            break

    print("\nThe number of users for the type Subscriber, Customer and Dependent is:\n {}, {} and {}, respectively.".format(sub, cus, dep))


    # Display counts of gender (there are only Male or Female)
    ### Washington has missing columns for Gender and Birth Year so need to skip this if true.
    try:
        user_gender = df['Gender'].value_counts()
        male = user_gender['Male']
        female = user_gender['Female']
        nans = df['Gender'].isna().sum()
        print("\nThe number of Male users are {}.\nThe number of Female users are {}.\nThose that did not choose to disclose are {}.\n".format(male, female, nans))
    except:
        print("\nWoops, looks like they didn\'t collect data for Gender!\n")
        
    # Display earliest, most recent, and most common year of birth
    ### Washington has missing columns for Gender and Birth Year so need to skip this if true.
    try:
        yob = df['Birth Year'].dropna().astype(int)
        moyob = yob[yob.sort_values().head(1).index[0]]
        mryob = yob[yob.sort_values(ascending = False).head(1).index[0]]
        mcyob = yob.mode()[0]
        print("\nThe earliest year of birth is {}.\nThe most recent year of birth is {}.\nThe most common year of birth is {}.\n".format(moyob, mryob, mcyob))
    except:
        print("\nWoops, looks like they didn\'t collect data for Birth Year!\n")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def check5(df):
    """ Display 5 rows of raw data in incriments upon user request, else abort """

    last_idx = 0
    check_next = input('\nWould you like to check the first 5 lines of raw data? Enter yes or no.\n\n')
    if check_next.lower() != 'yes':
        print("\nOkay, I hope this helped! :D\n")
    else:
        while check_next.lower() == 'yes':
            print(df[last_idx: last_idx + 5])
            last_idx += 5
            check_next = input('\nWould you like to check the next 5 lines of raw data? Enter yes or no.\n\n')
            if check_next.lower() == 'yes':
                if last_idx < len(df):
                    continue
                else:
                    print("\nWhoops! Looks like that was the last of the raw data! :( \n")
                    break
            else:
                print("\nOkay, I hope this helped! :D\n")
                break 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        check5(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("\nOkay, I hope this helped! :D\n")
            break


if __name__ == "__main__":
	main()