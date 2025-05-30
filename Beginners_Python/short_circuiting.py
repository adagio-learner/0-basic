#Short Circuiting
is_Friend = True
is_user = True

#in case of or if first condition is true then interpreter does not check the second condition
#in case of and if first condition is false then interpreter does not check the second conditio
if is_Friend or is_user:
    print('best friends forever')
else:
    print('unknown')