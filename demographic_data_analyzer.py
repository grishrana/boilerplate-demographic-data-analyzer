import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    NO_OF_ROWS, NO_OF_COLUMNS=df.shape
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    mask_male=df['sex']=='Male'
    no_of_men=df[mask_male].shape[0]
    sum_of_age_men=df[mask_male]['age'].sum()
    average_age_men = round(sum_of_age_men/no_of_men,1)

    # What is the percentage of people who have a Bachelor's degree?
    mask_bachelor=df['education-num']==13
    percentage_bachelors = round((df[mask_bachelor].shape[0]/NO_OF_ROWS)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate
    mask_rich=df['salary']=='>50K'
    higher_education = df['education-num'].isin([13,14,16])
    lower_education = ~higher_education

    # percentage with salary >50K
    higher_education_rich = round((df[(mask_rich)&(higher_education)].shape[0]/df[higher_education].shape[0])*100,1)
    lower_education_rich = round((df[(mask_rich)&(lower_education)].shape[0]/df[lower_education].shape[0])*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask_min_workers=df['hours-per-week']==min_work_hours
    num_min_workers = df[mask_min_workers].shape[0]

    rich_percentage = round((df[(mask_min_workers)&(mask_rich)].shape[0]/num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    earning_country=df[mask_rich]['native-country'].value_counts()
    earning_country=earning_country.to_frame()
    earning_country['total_people']=df['native-country'].value_counts()
    earning_country['perc_rich']=round((earning_country['count']/earning_country['total_people'])*100,1)
    earning_country.sort_values(by='perc_rich',ascending=False,inplace=True)
    
    highest_earning_country = earning_country['perc_rich'].idxmax()
    highest_earning_country_percentage = round(earning_country['perc_rich'].iloc[0],1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask_India=df['native-country']=='India'
    occupation_in_India=df[(mask_India)&(mask_rich)]['occupation'].value_counts()
    
    top_IN_occupation = occupation_in_India.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
