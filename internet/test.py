import  sys
a=[0,1,2,3]
if 0 in a:
    print('yes')

b={'a':0,'b':1}
if 'a' in b:
    print('dict yes')

try:
    a=100/0
except Exception as e:
    print(e)

print(sys.argv[0])


