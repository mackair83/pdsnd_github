import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city in CITY_DATA :
                print('\ncity:{}\n'.format(city))
                break
        else:
                print('That is not an appropriate selection. Please try again:')
                continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month do you like to analyze? from January to June or type 'all' to analyze all months\n").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june'] :
                print('\nmonth:{}\n'.format(month))
                break
        else:
                print('That is not an appropriate selection. Please try again:')
                continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of the week do you like to analyze? from Monday to Sunday or type 'all' to analyze all days of the week\n").lower()
        if day in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'] :
                print('\nday:{}\n'.format(day))
                break
        else:
                print('That is not an appropriate selection. Please try again:')
                continue

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
    df=pd.read_csv(CITY_DATA[city])

# convert the start time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()

# filter by month if applicable

    if month != 'all':

# use the index of the months list to get the corresponding int

        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1

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

    # TO DO: display the most common month
    common_month = df['month'].mode()
    print('The most common month is ', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()
    print('The most common day of week is ', common_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]

    print('The most common hour to start to travel is ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used Start Station:', common_start_station)

    # TO DO: display most commonly used end station

    common_end_station = df['End Station'].mode()[0]
    print("Most commonly used End station:", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    common_start_end_station = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]

    print('Most Common Combination of Start and End Stations:', common_start_end_station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()

    print(total_duration)

    # TO DO: display mean travel time
    average_trip_duration = df["Trip Duration"].mean()

    print(average_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:

    # TO DO: Display counts of user types
        print("Here are the counts of various user types:")

        user_types = df['User Type'].value_counts()

        print(user_types)

    # TO DO: Display counts of gender

        gender_count = df['Gender'].value_counts()

        print('The gender count is: ', gender_count)
    # to handle error if no gender data available
    except KeyError:

        print("No data available for the selected city")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        # Min
        earliest_year = df['Birth Year'].min()

        print('The earliest birth year: {}.\n'.format(earliest_year))
        # max
        latest_year = df['Birth Year'].max()

        print('The latest birth year: {}.\n'.format(latest_year))
        # common
        common_year = df['Birth Year'].mode()

        print('The most common birth year: {}.\n'.format(common_year))

        # to handle error if no birth year data available
    except KeyError:

        print("No gender birth year column for selected city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    while True:

        display_raw = input('\nWould you like to see next 5 rows of data? Please enter yes or no:').lower()

        if display_raw =='yes':

            row = 0

            print(df.iloc[:row+5])

            row += 5

        else:

            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
