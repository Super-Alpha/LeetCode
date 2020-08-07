# Time：2020/5/414:45
def fizzBuzz(n):
    result = []
    for i in range(1,n + 1):
        if i % 3 == 0 and i%5 != 0:
            result.append("Fizz")
        elif i % 5 == 0 and i%3 != 0:
            result.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        else:
            result.append(str(i))
    return result
def countPrimes(n):
  # 小于n的质数个数
  if n < 3:
      return 0
  prime = [1]*n
  prime[0] = prime[1] = 0
  for i in range(2,int(n**0.5)+1):
      if prime[i]==1:
          prime[i*i:n:i] = [0]*len(prime[i*i:n:i])
  return sum(prime)
#print(countPrimes(10))
def isPowerOfThree(n):
    if n==1:
        return True
    elif n==0:
        return False
    elif n%3 == 0:
        return isPowerOfThree(n/3)
    else:
        return False
#print(isPowerOfThree(9))
def romanToInt(s="LVIII"):
    sum = 0
    convert = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

    for i in range(len(s) - 1):
        if convert[s[i]] < convert[s[i + 1]]:
            sum -= convert[s[i]]
        else:
            sum += convert[s[i]]
    sum += convert[s[-1]]
    return sum
#print(romanToInt())
def reverseBits(n=43261596):
    n = bin(n)
    s = str(n)
    s = s.lstrip("0b")
    s="0"*(32-len(s))+s
    result = 0
    for i in range(len(s)):
        result += int(s[i]) * (2 ** i)
    return result
#print(reverseBits())
def isValid(s="{[]}"):
    d={")":"(","}":"{","]":"["}
    l=[]
    for i in s:
        if i in d and d[i]==l[-1]:
            l.pop()
        else:
            l.append(i)
    return len(l)==0
print(isValid())