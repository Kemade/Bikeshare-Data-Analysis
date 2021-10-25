import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Months = ('january', 'february', 'march', 'april', 'may', 'june')

Weekdays = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
            'saturday')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "None" to apply no month filter
        (str) day - name of the day of week to filter by, or "None" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    while True:
        cities= ['chicago','new york city','washington']
        city= input("\n Which city would you like to analyse? (Chicago, New york city, Washington) \n").lower()
        if city in cities:
            break
        else:
            print("\n Please enter a valid city name")    


    # get user input for month (january, february, ... , june or none)
    while True:
        months= ['January','February','March','April','June','May','none']
        month = input("\n Which month would you like to consider? (January, February, March, April, May, June)? Type 'None' for no month filter\n").title()
        if month in months:
            break
        else:
            print("\n Please enter a valid month")    


    # get user input for day of week (monday, tuesday, ... sunday or none)
    while True:
        days= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','none']
        day = input("\n Which day of the week would you like to consider? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? Type 'None' for no day filter \n").title()         
        if day in days:
            break
        else:
            print("\n Please enter a valid day")    
    


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

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    df['hour'] = df['Start Time'].dt.hour
    
     # filter by month if applicable
    if month != 'none':
        # use the index of the months list to get the corresponding int
        month = month.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'none':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Uses mode method to find the most popular month
    popular_month = df['month'].mode()[0]

    print(f"Most Popular Month (1 = January,...,6 = June): {popular_month}")

    #Uses mode method to find the most popular day
    popular_day = df['day_of_week'].mode()[0]

    print(f"\nMost Popular Day: {popular_day}")

    #Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    #Uses mode method to find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print(f"\nMost Popular Start Hour: {popular_hour}")

    #Prints the time taken to perform the calculation
    #You will find this in all the functions involving any calculation
    #throughout this program
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
      
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start_station= df['Start Station'].mode()[0]
    print("The most commonly used Start Station is {}".format(pop_start_station))


    # display most commonly used end station
    pop_end_station= df['End Station'].mode()[0]
    print("The most commonly used End Station is {}".format(pop_end_station))

    # display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" "+"to"+" "+ df['End Station']
    pop_com= df['combination'].mode()[0]
    print("The most frequent combination of Start and End Station is {} ".format(pop_com))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the given fitered data is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the given fitered data is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts= df['User Type'].value_counts()
    print("The user types are:\n",user_counts)


    # Display counts of gender
    if city.title() == 'Chicago' or city.title() == 'New York City':
        gender_counts= df['Gender'].value_counts()
        print("\nThe counts of each gender are:\n",gender_counts)
    
    # Display earliest, most recent, and most common year of birth
        earliest= int(df['Birth Year'].min())
        print("\nThe oldest user is born of the year",earliest)
        most_recent= int(df['Birth Year'].max())
        print("The youngest user is born of the year",most_recent)
        common= int(df['Birth Year'].mode()[0])
        print("Most users are born of the year",common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    response= ['yes', 'no']
    rawdata = ''
    #counter variable is initialized as a tag to ensure only details from a particular point is displayed
    counter = 0
    while rawdata not in response:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes or  no")
        rawdata = input().lower()
        #the raw data from the df is displayed if user opts for it
        if rawdata == "yes":
            print(df.head())
        elif rawdata not in response:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #Extra while loop here to ask user if they want to continue viewing data
    while rawdata == 'yes':
        print("Do you wish to view raw data?")
        counter += 5
        rawdata = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if rawdata == "yes":
             print(df[counter:counter+5])
        elif rawdata != "yes":
             break

    print('-'*80)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        
        if restart == 'yes':
            main()
        
        elif restart == 'no':
        
            print('\nThe end!')
            return
        
if __name__ == "__main__":
    main()

