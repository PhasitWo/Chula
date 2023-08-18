import math
import matplotlib.pyplot as plt

operationCNT = 0

def primeFac1(num):
    global operationCNT  # Declare operationCNT as global

    factor = []

    while num % 2 == 0:
        factor.append(2)
        num = num / 2
        operationCNT += 1

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factor.append(i)
            num = num / i
            operationCNT += 1

    if num > 2:
        factor.append(num)

    return factor

def findGCD1(m, n):
    global operationCNT
    commonFac = []
    m_fac = primeFac1(m)
    n_fac = primeFac1(n)

    i = 0
    j = 0
    gcd_result = 1
    while i < len(m_fac) and j < len(n_fac):
        if m_fac[i] == n_fac[j]:
            commonFac.append(m_fac[i])
            i += 1
            j += 1
            operationCNT += 1
        elif m_fac[i] < n_fac[j]:
            i += 1
            operationCNT += 1
        else:
            j += 1
            operationCNT += 1
    for i in commonFac:
        gcd_result *= i

    return gcd_result

def sieve():
  # Calculating SPF (Smallest Prime Factor) for every number till n.
  global spf
  global operationCNT
  MAXN = 1000000
  spf = [0 for i in range(MAXN)]
  # marking smallest prime factor for every number to be itself.
  for i in range(1, MAXN):
      spf[i] = i
      operationCNT += 1
  for i in range(2, MAXN):
      # checking if i is prime
      if (spf[i] == i):
          # marking SPF for all numbers divisible by i
          # j start from i*i because ==> ex. let i = 5;
          # 1x5, 2x5, **3x5**, 4x5, see that 3x5 spf is 3
          # so we don't want to mess with that
          # or in other word, we want to start marking SPF
          # from number that actually has i as SPF
          for j in range(i * i, MAXN, i):
              # marking spf[j] if it is not previously marked
              if (spf[j] == j):
                  spf[j] = i
                  operationCNT += 1

def primeFac2(n):
    global operationCNT
    ret = list()
    while (n != 1):
        ret.append(spf[n])
        n = n // spf[n]
        operationCNT += 1
    return ret

def findGCD2(m,n):
    global operationCNT

    commonFac = []
    m_fac = primeFac2(m)
    n_fac  = primeFac2(n)

    i = 0
    j = 0
    gcd_result = 1
    while (i<len(m_fac)) and (j<len(n_fac)):
      if m_fac[i] == n_fac[j]:
        commonFac.append(m_fac[i])
        i += 1
        j += 1
        operationCNT += 1

      elif (m_fac[i] < n_fac[j]):
        i += 1
        operationCNT += 1
      else:
        j += 1
        operationCNT += 1
    #Step 4: หา gcd
    for i in commonFac:
        gcd_result *= i
    return gcd_result

def findGCD3(m,n):
  global operationCNT
  operationCNT += 1
  if m == 0:
    return n
  if n == 0:
    return m
  if m>n: return findGCD3(m % n, n)
  elif m == n :return findGCD3(m, n)
  elif m < n : return findGCD3(m, n % m)

testcase = [
    (30, 15), (20, 72), (72, 88),(58, 77), (92, 80),
    (286, 544), (985, 716), (839, 433), (471, 561), (269, 749),
    (1888, 1224), (3164, 6996), (6253, 5431),(4390, 2874), (5017, 7615),
    (76241, 57606), (74766, 64553), (12322, 50440), (34726, 92155), (14785, 19817), 
    (672270, 431511), (694404, 256785), (975922, 532283),(279392, 946230), (906443, 392685), 
    (2226412, 8648878), (6061228, 5546440), (1691980, 1414558),(3234496, 7268362), (8356954, 3705742), 
    (81786288, 61052652), (21535993, 91675657), (26586591, 78851391),(68575643, 45017255), (45991767, 77583796), 
    (459917672, 775837965), (265865917, 788513914), (685756433, 450172557),(785756437, 102475659), (504857673, 354879547), 
    (4737418245, 9465215337), (7384184877, 6565315335),(6531741823, 8795491761), (5865583711, 9535851393), (6954464645, 8017257569), 
    (84184418245, 65310172575),(58659151391, 85756451391), (57564301725, 74851857673), (59917672487, 88512663377), (65315344641, 98418485851),
    (789176724879, 659151396733), (659117416437, 946585181391), (653184188245, 758331017965), (841818235337, 767318488245), (953525754641, 658518571823)
]

# test
def test(testcase, gcd_fucntion):
    global operationCNT
    average_cnt = []
    temp = 0
    for index, case in enumerate(testcase):
        operationCNT = 0
        gcd_fucntion(case[0], case[1])
        if (index+1) % 5 == 0:
            average_cnt.append(temp/5)
            temp = 0
        else:
            temp += operationCNT
    return average_cnt

average_cnt_method1 = test(testcase, findGCD1)
average_cnt_method2 = [8.4, 7.2, 10.4, 9.4, 11, 11.8, 9.6, 10.4, None, None, None]
average_cnt_method3 = test(testcase, findGCD3)

print(average_cnt_method1)
print(average_cnt_method3)

# graph
x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12]
plt.plot(x, average_cnt_method1, color='r', label='method1 Naive')
plt.plot(x, average_cnt_method2, color='b', label='method2 Sieve')
plt.plot(x, average_cnt_method3, color='g', label='method3 Recursion')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("digit")
plt.ylabel("operation count")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()
