# This is the program for basic model or for pattern 
# this the basic
# what is basic maodel 1?
  
                

                # BASIC MODEL 1

#                        1
#                        1 2
#                        1 2 3
#                        1 2 3 4
#                        1 2 3 4 5


for i in range (1,6):   # It calculate the no. of rows as 6 is exluded that's why we use (1,6)
    for j in range (1,i+1):  # this for coloumn as the j is from 1-1,1-2,1-3,1-4,1-5 so we will print j for this
        print(j,end=' ')   # as the end = /n i.e. next line print so to stop it we use end = '' (i.e for space) and first it continue with exectution of j
    print()
