seconds_per_day=86400
seconds_per_hour=3600
seconds_per_minute=60
seconds=int(input("Enter the amount of seconds : "))

day= seconds/seconds_per_day
seconds=seconds%seconds_per_day

hour=seconds / seconds_per_hour
seconds=seconds % seconds_per_hour


minute=seconds / seconds_per_minute
seconds=seconds % seconds_per_minute

print("the equivalent amount duration is : ",  " %d : %02d : %02d : %02d " % (day,hour,minute, seconds) )
