import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_line = np.array(range(min(df['Year']), 2051))
    y_line = res.slope * x_line + res.intercept
    ax.plot(x_line, y_line, color='orange')

    # Create second line of best fit
    res2 = linregress(df['Year'].loc[df['Year']>=2000],
                      df['CSIRO Adjusted Sea Level'].loc[df['Year']>=2000])
    x_line2 = np.array(range(2000, 2051))
    y_line2 = res2.slope * x_line2 + res2.intercept
    ax.plot(x_line2, y_line2, color='red')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()