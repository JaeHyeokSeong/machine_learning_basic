# from travel import *
#
# print("11-4_모듈 직접 실행 practise\n")
#
# travel_to = japan.JapanPackage()
# travel_to.product()

import travel.japan
import inspect
import random

travel_to = travel.japan.JapanPackage()
travel_to.product()

print(inspect.getfile(travel.japan))
print(inspect.getfile(random))
