'''
  To practice editing string
'''

def reverse(text):
  return text[::-1]
  
def is_palindrome(text):
  return text == reverse(text)

# The list of characters to be ignored
forbidden = (',', ' ', '?', '.', '/', '"', '(', ')', '[', ']', ';', ':')
user_input = input('Enter text: ')

for item in forbidden:
  user_input = user_input.replace(item, '')
  
if is_palindrome(user_input):
  print('Yes, it is a palindrome.')
else :
  print('No, it is not a palindrome.')
