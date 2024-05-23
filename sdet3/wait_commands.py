#Wait commands
"""
time_sleep(0)- This not a wait coomand it is related to python

advantage
simple to use

disadvantage
Poor performance of the script
chances are there if element is not found in mentioned time limit then it will return a exception


1) Implicit wait
It will be always written below chrome driver opened statement. as it will auto apply to m all statement
It will be killed post clicking the browser by driver.quit()
If element is available within the time limit then it will proceed with the further program execution

advantage
single statement
performance will not be reduced


disadvantage
chances are there if element is not found in mentioned time limit then it will return a exception


Explicit wait
it is mostly used exlicit wait and also effective wait as mostly will be done on pp and dev environments
it is based on condition with time

advantages
it is more effective then implicit wait
but it needs to be mentioned at each and every place in form of object for ease of use

disadvantages
must be used at multiple places
difficult to use and write
"""

