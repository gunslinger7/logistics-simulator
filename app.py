import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import pandas as pd
import numpy as np
import calc
from scipy.interpolate import make_interp_spline    

# reaad the file to be calculated
xlsx = pd.read_excel('to-calc.xlsx')

# get the coloumn with the part names
parts = list(xlsx.loc[:]["Parts"])

# get the position of where the pick-up starts (to enbale varying the amount of parts hithout changing the code)
pick_up_index = parts.index("Pick-Up")

# calculate the pick-ups per month, also managing missing data (this one is used to plot the initial graph)
pp_month = sum(xlsx.iloc[pick_up_index,1:5].fillna(0))

# Plot and tune the 1st dynamic figure
fig , (ax,ax2) = plt.subplots(1,2)
plt.subplots_adjust(bottom=0.25)

week = np.array([x.replace("W","") for x in xlsx.columns[1:]])
costs = np.array(xlsx.iloc[pick_up_index+1][1:])

ax.set_xlabel("weeks")
ax.set_ylabel("Euros")
ax.tick_params(axis='x', labelsize=8)

l, =  ax.plot(week,costs, lw=2)
k, = ax.plot(week, np.full((len(week),), xlsx.iloc[12][1]/len(week)), color = 'darkred')

# plot the initial figure smoothed out 
cd1 = costs[0::5]
cdx = [x for x in range(len(week[0::5]))]

sploine = make_interp_spline(cdx , cd1)
n_x = np.linspace(0,9, 250)
n_y = sploine(n_x)

c, = ax2.plot(n_x, n_y, color="darkgreen")


# update prices when the slider is moved
def update_pickup(pickup, xlsx = xlsx, pickup_index = pick_up_index):
    '''
    Modify the current monthly pick-up value by distributing it over 4 weeks
    and cutting out from the last week if the amount is not divisible by 4.
    
    Calculate and update the grpahs.

    ''' 
    if pickup % 4 == 0:
        for x in xlsx.columns[1:]:
            xlsx.loc[pick_up_index,x]  = pickup/4
    else: 
        d = pickup
        pickup = int(pickup/4)+1
        c = 0
        for x in xlsx.columns[1:]:
            if c==3:
                xlsx.loc[pick_up_index,x]  = d - (pickup*3)
                c=0
            else: 
                xlsx.loc[pick_up_index,x] = pickup
                c+=1
    
    # Calculate the new values and update the xlsx file
    calc.update_changes(xlsx, save=True)
    print("Changed")
    cost =  np.array(xlsx.iloc[pick_up_index+1][1:])

    # Update the graphs
    l.set_ydata(cost)
    k.set_ydata(np.full((1, len(cost)), xlsx.iloc[pick_up_index+2][1]/len(cost)))
    fig.canvas.draw_idle()


# Create a slider
pax_slider = plt.axes([0.25,0.1,0.65,0.03], facecolor = 'lightgoldenrodyellow')
slider = Slider(pax_slider, "Picked up per Month", 50, 80, valinit=pp_month, valstep=1)
slider.on_changed(update_pickup)

# Set the proportions of the window
fig.set_size_inches(18,6)

plt.show()