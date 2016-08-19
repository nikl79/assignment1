
#!/usr/bin/python
#

catalogue = {"pizza", "loukoumades", "dolmades", "hamburger", "tzaziki", "paidakia" }

a_counter = 0
e_counter = 0
i_counter = 0
o_counter = 0
u_counter = 0

def letter_counter(word, char):
  count = 0
  for c in word:
    if char == c:
      count += 1
  return count

for item in catalogue:
   a_counter = a_counter + letter_counter(item, 'a')
   e_counter = e_counter + letter_counter(item, 'e')
   i_counter = i_counter + letter_counter(item, 'i')
   o_counter = o_counter + letter_counter(item, 'o')
   u_counter = u_counter + letter_counter(item, 'u')
    
print 'The letter A appears : '+str(a_counter) 
print 'The letter E appears : '+str(e_counter) 
print 'The letter I appears : '+str(i_counter) 
print 'The letter O appears : '+str(o_counter) 
print 'The letter U appears : '+str(u_counter) 


print
print 'Solution with Join'

import string

catalogue_string = string.join(list(catalogue))

a_counter = 0
e_counter = 0
i_counter = 0
o_counter = 0
u_counter = 0

for l in catalogue_string:
  if l == 'a': a_counter += 1
  elif l == 'e': e_counter += 1
  elif l == 'i': i_counter += 1
  elif l == 'o': o_counter += 1
  elif l == 'u': u_counter += 1
  
print 'The letter A appears : '+str(a_counter) 
print 'The letter E appears : '+str(e_counter) 
print 'The letter I appears : '+str(i_counter) 
print 'The letter O appears : '+str(o_counter) 
print 'The letter U appears : '+str(u_counter) 
