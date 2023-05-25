# import travel.thailand
#
# print("11-2 패키지 practise\n")
#
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# from travel.vietnam import VietnamPackage
#
# trip_to = ThailandPackage()
# trip_to.detail()
#
# trip_to = VietnamPackage()
# trip_to.detail()

from travel import *

trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to = thailand.ThailandPackage()
trip_to.detail()
