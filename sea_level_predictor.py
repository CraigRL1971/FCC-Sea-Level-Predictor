import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from csv file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.set_xbound(lower=1850, upper=2050)
    ax.set_xticks((1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0))
    ax.set_xticklabels(['1850.0', '1875.0', '1900.0', '1925.0', '1950.0', '1975.0', '2000.0', '2025.0', '2050.0', '2075.0'])
    
    # Create first line of best fit
    slope, intercept, x, y, z = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    del x, y, z
    x2 = list(range(1880, 2050, 1)) 
    y2 = [] 
    for year in x2: y2.append(intercept + slope*year)
    ax.plot(x2, y2, color='green')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000].copy()
    slope, intercept, x, y, z = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    del x, y, z 
    x2 = list(range(2000, 2050, 1))
    y2 = [] 
    for year in x2: y2.append(intercept + slope*year)
    ax.plot(x2, y2, color='red')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')    
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()