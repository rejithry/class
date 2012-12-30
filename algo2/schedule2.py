#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RRAGHA
#
# Created:     28/12/2012
# Copyright:   (c) RRAGHA 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    jobs = []
    jobtimes = []
    f = open('c:\\jobs.txt' , 'r')
    head = 0
    for i in f:
        if head != 0:
            jobs.append([int(i.split(' ')[0]) / (int(i.split(' ')[1])*1.0), int(i.split(' ')[0]), int(i.split(' ')[1])])
        head += 1


    jobs.sort(key=lambda x: (x[0], x[1]), reverse=True)
    curtime = 0
    for i in jobs:
        print i
        jobtimes.append([i,(curtime + i[2])*i[1]])
        curtime = curtime + i[2]

    tot_time = 0

    for i in jobtimes:
        tot_time += i[1]

    print tot_time



if __name__ == '__main__':
    main()
