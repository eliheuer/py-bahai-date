import datetime

# class Calendar(object):

now = datetime.datetime.today()

print("{:%H:%M:%S}".format(now))
print("{:%H:%M}".format(now))
print("{:%H}".format(now))
print(now.hour)
print(now.year)
print(now)


# Day-name, Month-name, Day-#, Year
