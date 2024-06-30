import pandas as pd
import numpy as np

#price pre tonn per day
PRICE = 0.3

#component weights
WEIGHTS = [88066, 94492, 62091, 28594, 86000, 85500, 85000, 73000, 66500]

#read the file
def update_changes(xlsx , save=False, PRICE=PRICE, WEIGHTS = WEIGHTS):
    
    # Important index variables
    parts = list(xlsx.loc[:]["Parts"])
    pick_up = parts.index("Pick-Up")+1
    cost_ind =  pick_up+1
    total_cost_ind = cost_ind+1

    
    part_names = [value for value in xlsx.iloc[0:pick_up-1]['Parts']]

    # dictionary containing [component name : its weight] pair
    price = dict(zip(part_names,WEIGHTS))

    # list replicating storage but remembering the order of delivered components
    logistics_line = []

    # compute the weekly cost given the list of components currently in storage
    def compute_cost(storage):
        tonns = 0
        for name in storage:

            tonns+=price[name]
        return tonns*7*PRICE/1000


    for colm in xlsx.columns[1:]:
        for key, value in zip(part_names,xlsx[str(colm)][:pick_up-1]):

            # handle missing data
            if pd.isna(value) == False:
                for t in range(int(value)):
                    logistics_line.append(key)

        # Get the number of components picked-up while also handling missing data
        if pd.isna(xlsx.iloc[pick_up-1][colm]):
            out_bound = 0
        else:
            out_bound = int(xlsx.iloc[pick_up-1][colm])

        # remove the initial out_bound amount of components as they are picked-up the same day
        logistics_line = logistics_line[out_bound:]

        # compute the weekly cost and assign it to the corresponding cell
        xlsx.loc[cost_ind-1,colm] = compute_cost(logistics_line)

    # Calculate the total sum and assign it
    total_sum = sum(xlsx.iloc[cost_ind-1].values[1:])
    

    xlsx.iloc[total_cost_ind-1,1] = int(total_sum)

    # Save the file
    
    if save == True:
        xlsx.to_excel('calced   .xlsx', index=False)
    
    
    
    

if __name__ == "__main__":
    update_changes(pd.read_excel("calc.xlsx"), save=True)