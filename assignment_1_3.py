
#!/usr/bin/python
#

catalogue = {"pizza", "loukoumades", "dolmades", "hamburger", "tzaziki", "paidakia" }

print 'Here is a complete DIY solution \n'

def count_chars(word):
  count = 0
  for c in word:
      count += 1
  return count
  
def reverse_word(word2):
  b = count_chars(word2)
  result = ''
  while (b>0):
    char = word2[b-1]
    result = result+char
    b -= 1
  print "the reverse of word '"+word2+"' is '"+result+"'"  

for item in catalogue:
  reverse_word(item)

print '\n'

print 'And here are some more elaborate and verbose solutions using built-in functions: '
print "Eg with [::1] \n"

def reverse_word(word):
  reversed_word = word[::-1]
  print 'if you reverse '+word+' you get: '+reversed_word

for item in catalogue:
  reverse_word(item)

print '\n'

print "and without [::1] but with xrange instead \n"

def reverse_word2(word2):
  result = ''
  for i in xrange(len(word2)-1, -1, -1):
     result += word2[i]
  print 'if you reverse '+word2+' you get: '+result

for item in catalogue:
  reverse_word2(item)

print '\n'

print "and without [::1] or xrange but instead with reversed \n"

def reverse_word3(word3):
  result = ''
  for i in reversed(word3):
     result += i
  print 'if you reverse '+word3+' you get: '+result

for item in catalogue:
  reverse_word3(item)

