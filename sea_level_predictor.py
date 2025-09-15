import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',')
    df.columns = df.columns.str.replace(' ','', regex=True).str.lower()
    

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['year'], df['csiroadjustedsealevel'])

    # Create first line of best fit
    slope1, intercept1, r_value, p_value, std_err = linregress(df['year'], df['csiroadjustedsealevel'])
    years_extended = range(1880, 2050)
    line_1 = [slope1 * year + intercept1 for year in years_extended]
    plt.plot(years_extended, line_1, 'r', label='Best line 1880-2050')    
      
    # Create second line of best fit
    recent_years_df = df[df['year'] >= 2000]
    slope2, intercept2, r_value, p_value, std_err = linregress(recent_years_df['year'], recent_years_df['csiroadjustedsealevel'])
    recent_years = range(2000, 2050)
    line_2 = [slope2 * year + intercept2 for year in recent_years]
    plt.plot(recent_years, line_2, 'g', label='Best fit line (2000-2050)')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()