import re
pattern = "[a-z]([a-z](\d {1,2}| \d {[a-z]| \d {1,2} \s \d [a-z]{2}"
finished = false
while not finished:
  post_code = input("post code = ")
   if len(post_code) = 0:
    print(True)
   else:
    if re.match(pattern,post_code):
     print("valid post code")
   else :
     print('invalid')
