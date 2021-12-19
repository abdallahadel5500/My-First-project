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
    
    city = str(input("\n enter the name of city you want to see its date?(chicago, new york city, washington)")).lower()
    while True:
        if city == "chicago":
            break
        elif city =="new york city":
            break
        elif city =="washington":
            break
        else:
            city=str(input('\n plz enter the name of the city like (chicago, new york city, washington)')).lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input("\n Enter any one of the first 6 months or enter All to select all 6 months ?(plz enter the number of the month if you dont want to filter by month plz enter all)")).lower()    
    if month =='january':
        month=1
    elif month =='february':
        month=2
    elif month =='march':
        month=3
    elif month =='april':
        month=4
    elif month =='may':
        month=5
    elif month =='june':
        month=6
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =  str(input("\n enter the number of day of week you want to see its date?(the number of the day(1,2,3,4,5,6,7 if you dont want to filter by day plz enter all)")).lower()
    if day =='sunday':
        day=1
    elif day =='monday':
        day=2
    elif day =='tuesday':
        day=3
    elif day ==' wednesday':
        day=4
    elif day =='thursday':
        day=5
    elif day ==' friday':
        day=6
    elif day =='saturday':
        day=7
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
    while True:
        try:
            df = pd.read_csv(CITY_DATA[city])
            df['Start Time']=pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')
            break
        except:
            city =str(input('\n plz enter the name of the city like (chicago, new york city, washington)')).lower()
    
    '''try :
        df = pd.read_csv(CITY_DATA[city])
        df['Start Time']=pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')
    except:
        city =str(input('\n plz enter the name of the city like (chicago, new york city, washington)')).lower'''
   
    df['month']=pd.DatetimeIndex(df['Start Time']).month
    df['day']=df['Start Time'].dt.dayofweek
    while True:
        
        try:
            if month != 'all':
                month =int(month)
            else:
                month =0
            if month == 1:
                df=df[df['month']==1]
            elif month == 2:
                df=df[df['month']==2]
            elif month == 3:
                df=df[df['month']==3]
            elif month == 4:
                df=df[df['month']==4]
            elif month == 5:
                df=df[df['month']==5]
            elif month == 6:
                df=df[df['month']==6]
            break
        except:
            month = str(input('\n enter the number of the month(1,2,3,4,5,6) if you dont want to filter by month plz enter all')).lower()        
    while True:
        
        try:
            if day != 'all':
                day = int(day)
            else:
                day=0            
            if day == 1:
                df=df[df['day']==1]
            elif day == 2:
                df=df[df['day']==2]
            elif day == 3:
                df=df[df['day']==3]
            elif day == 4:
                df=df[df['day']==4]
            elif day == 5:
                df=df[df['day']==5]
            elif day == 6:
                df=df[df['day']==6]
            elif day == 7:
                df=df[df['day']==7]
            break
        except:
            day = str (input('plz enter the number of the day you want (1,2,3,4,5,6,7) if you dont want to filter by day plz enter all')).lower()
    df['hour']=pd.DatetimeIndex(df['Start Time']).hour
   
     
                

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month\n"+str (df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("the most common day\n"+str( df['day'].mode()[0]))

    # TO DO: display the most common start hour
    print("the most common hour\n"+str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print ("\n the most commonly used start satation: "+str(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print ("\n the most commonly used end satation: "+str(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('the most frequent combination of start station and end station trip: '+ str (df.groupby(['End Station','Start Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time: '+str (df['Trip Duration'].sum()) )

    # display mean travel time
    print('mean travel time: '+str (df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('the counts of user types:\n'+str (df['User Type'].value_counts()))
    try:
        # Display counts of gender
        print('the counts of gender:\n'+str(df['Gender'].value_counts()))

    except:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    try:
        # Display earliest, most recent, and most common year of birth
        print ('the earliest year of birth :\n'+str (df['Birth Year'].min())+'\nthe most recent year of birth :\n'+str (df['Birth Year'].max()) +'\n and most common year of birth:\n'+str( df['Birth Year'].mode()[0]))
    except:
        print ('this stats cannot calculat its date of birth years')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    i = 0
    raw = str( input('Do you wnat to see 5 raws of the date set ?(yes or no )')).lower()
    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            x =str(input("Do you want to see another 5 raws of date set? (yes or no)")).lower() # TO DO: convert the user input to lower case using lower() function
            if x !="yes"and x !='no':
                raw=str (input('plz enter the your answer like(yes , no)')).lower()
            elif x=='yes':
                i=i+5
                
                continue
            else:
                break
           
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
def main():
    while True:
        city, month, day = get_filters()
        
        
        df = load_data(city, month, day)
       
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
