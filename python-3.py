print("Hello")
print('hello', 'everyone')
print('hello'+ 'everyone')


print('hello', end='')
print('test')


a = 123
b = 'hello'
print(a,b)
print(a,456,b,'world')

print('Hello Python!')             
print("Nice to meet you.")        
print('Hello "Python"')            
print('Hello','Python!')          
print('Hello'+'Python!') 



print("화면에 직접 출력")        
print('ab\'c')   
print("ab'c")  
print("doesn't")             
print('does')                 
print('deosn\'t')              
print("'string'")              
print("\"string\"")            
print('"string"')             


s1 = '화면에 직접 출력'
s2 = 'ab\'c'
s3 = 'does'
print(s1)
print(s2)
print(s3)
print(s1[0])    # 첫 두글자
print(s2[1])    # 두 번쨰 글자
print(s3[1:3])
print(s3[-1])   # 마지막 글자
print(s3[-2])   # 뒤에서 두 번째


print(' ')
print(' ')
print(' ')
print(' ')



a = 2
b = 3.1456
c = a+b
print(a)
print(b)
print(c)
print(round(c,3))
print("%.4f" % (c))
print(a+b)
print(a,b,a+b,c)

d = 1e2
e = 1e-2
print(d)
print(e)

print(' ')
print(' ')
print(' ')
print(' ')

item1 = '사과'
price1 = 1000
item2 = '바나나'
price2 = 500
print(item1, price1)
print(item2, price2)

print(' ')
print(' ')
print(' ')
print(' ')

str1 = '{0}는 {1}원입니다.'
print(str1.format(item1, price1))
print(str1.format(item2, price2))

print(item1, price1, sep='*', end='/')
print(item2, price2)


print(' ')
print(' ')
print(' ')
print(' ')

str2 = '%s는 %d원입니다.'
print(str2%(item1, price1))
print(str2%(item2, price2))
