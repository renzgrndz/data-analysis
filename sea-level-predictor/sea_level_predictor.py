import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data points')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = list(range(1880, 2051))
    plt.plot(years_extended, intercept + slope * pd.Series(years_extended), 'r', label='Fitted line 1880-2050')

    # Create second line of best fit starting from year 2000
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_extended_2000 = list(range(2000, 2051))
    plt.plot(years_extended_2000, intercept_2000 + slope_2000 * pd.Series(years_extended_2000), 'green', label='Fitted line 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Define xticks
    plt.xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])

    # Add legend
    plt.legend()

    # Save plot and return axis object
    plt.savefig('sea_level_plot.png')
    return plt.gca()

