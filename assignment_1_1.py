
#!/usr/bin/python
#

catalogue = {"pizza", "loukoumades", "dolmades", "hamburger", "tzaziki", "paidakia" }

catalogue_items = 0

for item in catalogue:
    print item
    catalogue_items = catalogue_items + 1

print '\n'
print 'total number of items: '+str(catalogue_items)