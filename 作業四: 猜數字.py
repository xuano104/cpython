#guess number
ans=65
guess=0
c=0
while (guess == 0):
    num=int(input('please input a number (1~100)='))
    c=c+1
    print('you guess=',num,'Times=',c)
    if num>65:
        print('to big')
    elif num<65:
        print('to small')
    else:
        guess=1
        print('Congratulations! You got it right.')
