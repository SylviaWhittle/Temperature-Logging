#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import axes, figure, plot, xticks
from matplotlib import dates as mdates
import seaborn as sb
import os
from datetime import datetime

# Get the absolute file path for this script
# FileDir = os.path.dirname(os.path.realpath('__file__'))

# File with data in it
# file1 = 'C09 - XRAY.txt'

# Join the two paths together
# filename = os.path.join(FileDir, file1)


backgroundcolour = (30/255, 70/255, 90/255, 0.9)
axescolour = (1, 1, 1, 0.6)
plotcolour = (1, 0.4, 0.3)

# Create figure

fig = plt.figure()
fig.patch.set_facecolor(backgroundcolour)
figure(figsize=(20, 16), dpi=100)
fig.patch.set_facecolor(backgroundcolour)
fig.patch.set_alpha(1)

dataFolder = './Temperature Data'
count = 1
for filename in os.listdir(dataFolder):
    print(filename)

    # Read data from file
    data = pd.read_csv(dataFolder + "/" + filename, encoding='latin1')
    dates = data["Time"]

    formatted_dates = []
    for date in dates:
        formatted_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        formatted_dates.append(formatted_date)

    temps = data["Celsius(°C)"]

    # Create subplot
    # ax = fig.add_subplot(111)
    ax = fig.add_subplot(3, 1, count)

    ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))

    ax.plot(formatted_dates, temps, color = plotcolour)
    fig.autofmt_xdate()

    ax.grid(True)
    ax.set_xlabel("Day (September 2021)")
    ax.set_ylabel("Temperature °C")
    ax.title.set_text(filename)
    # Colour
    ax.set_facecolor(backgroundcolour)
    ax.spines['top'].set_color(axescolour)
    ax.spines['bottom'].set_color(axescolour)
    ax.spines['left'].set_color(axescolour)
    ax.spines['right'].set_color(axescolour)
    ax.tick_params(axis='x', colors=axescolour)
    ax.tick_params(axis='y', colors=axescolour)
    ax.xaxis.label.set_color(axescolour)
    ax.yaxis.label.set_color(axescolour)
    ax.title.set_color(axescolour)

    count += 1

    

fig.set_figheight(8)
fig.set_figwidth(8)
fig.tight_layout()
plt.show()



# %%
fig = plt.figure()
fig.patch.set_facecolor(backgroundcolour)

fig.patch.set_facecolor(backgroundcolour)
fig.patch.set_alpha(1)

data = pd.read_csv('Temperature Data/C09 - XRAY.txt', encoding='latin1')
dates = data["Time"]

formatted_dates = []
for date in dates:
    formatted_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    formatted_dates.append(formatted_date)

formatted_dates = formatted_dates[len(formatted_dates)-100:]

temps = data["Celsius(°C)"]
temps = temps[len(temps)-100:]

# Create subplot
# ax = fig.add_subplot(111)
ax = fig.add_subplot(1, 1, 1)

# ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
# ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

ax.plot(formatted_dates, temps, color = plotcolour)
fig.autofmt_xdate()

ax.grid(True)
ax.set_xlabel("Day (September 2021)")
ax.set_ylabel("Temperature °C")
ax.title.set_text(filename)
# Colour
ax.set_facecolor(backgroundcolour)
ax.spines['top'].set_color(axescolour)
ax.spines['bottom'].set_color(axescolour)
ax.spines['left'].set_color(axescolour)
ax.spines['right'].set_color(axescolour)
ax.tick_params(axis='x', colors=axescolour)
ax.tick_params(axis='y', colors=axescolour)
ax.xaxis.label.set_color(axescolour)
ax.yaxis.label.set_color(axescolour)
ax.title.set_color(axescolour)

figure(figsize=(20, 6), dpi=80)
fig.tight_layout(pad=20.0)
plt.show()
# %%
