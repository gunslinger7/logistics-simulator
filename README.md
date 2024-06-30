# Logistics Simulator

Calculates logistic costs, visualizes data and lets try out differnet scenarios.

## General:

Uses excel files of specific form remembers shipped components in the order they were shipped. 

Delivery and Pick-Up happen on the same day - Sunday, and the commponents that were shipped first are picked-up first. It calculates weekly costs, displays the data and shows the average cost per week. Lets you vary the monthly Pick-Up amount via a slider, see the changes in real-time, and saves the changes when the window is closed (if desired). 

Later I will add another slider that will let vary the distribution of pick-up amount within the month (e.g. pick up more items in the beginning of the month and less in the end of it).

## Trying it out:

* This is the file of standard form that needs to be calculated:
![Screenshot (67)](https://github.com/gunslinger7/logistics-simulator/assets/167663925/9bb66ca4-d695-4225-a5e3-ea3fe916271b)


* This is the result:

  ![Screenshot (65)](https://github.com/gunslinger7/logistics-simulator/assets/167663925/fd8b81fb-193f-4539-b8a0-1e8a5410b27e)

You can see the changes in real time:

![Screenshot (62)](https://github.com/gunslinger7/logistics-simulator/assets/167663925/e69a8a8b-b51e-4cf3-820d-2250b847872f)


![Screenshot (63)](https://github.com/gunslinger7/logistics-simulator/assets/167663925/a60393b6-1930-47bd-9d4c-1938b69d7a04)


Sadly, updating splines in real-time is not supported by matplotlib.


## End thoughts:

I think this app may be very useful for those who would like to minimize their costs of shipping (or maximize their profits from storage XD ). The app is also very flexible - lets you vary the amount of parts and weeks only by modifying the excel file.

Still, I think doing this manually takes too much effort and patience which is why I'm planning to use an agent and reinforcement learning because it seems that this task could be simplified to a game of minimizing the cost or maximizing the reward.
