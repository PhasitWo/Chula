using System;
using System.Collections;
using System.Collections.Generic;
using System.Net.Http.Headers;

class Program
{
    const long MAXN = 999_999_999;
    public static long[] spf = new long[MAXN];
    static void Sieve(out int operationCNT)
    {
        operationCNT = 0;
        for (int i = 1; i < MAXN; ++i)
        {
            spf[i] = i;
            operationCNT++;
        }
        for (int i = 2; i < MAXN; ++i) // Fixed loop condition
        {
            if (spf[i] == i)
            {
                if (i * i > MAXN)
                    break;
                for (int j = i * i; j < MAXN; j += i)
                {
                    if (spf[j] == j)
                    {
                        spf[j] = i;
                        operationCNT++;
                    }
                }
            }
        }
    }

    static List<long> PrimeFac(long n, out int operationCNT)
    {
        operationCNT = 0;
        List<long> ret = new List<long>();
        while (n != 1)
        {
            ret.Add(spf[n]);
            n /= spf[n];
            operationCNT++;
        }
        return ret;
    }

    static long FindGCD2(long m, long n, out int operationCNT)
    {
        operationCNT = 0;
        List<long> commonFac = new List<long>();
        List<long> m_fac = PrimeFac(m, out int m_operationCNT);
        List<long> n_fac = PrimeFac(n, out int n_operationCNT);

        int i = 0;
        int j = 0;
        long gcd_result = 1;
        while (i < m_fac.Count && j < n_fac.Count)
        {
            if (m_fac[i] == n_fac[j])
            {
                commonFac.Add(m_fac[i]);
                i++;
                j++;
                operationCNT += 1;
            }
            else if (m_fac[i] < n_fac[j])
            {
                i++;
                operationCNT += 1;
            }
            else
            {
                j++;
                operationCNT += 1;
            }
        }

        foreach (long factor in commonFac)
        {
            gcd_result *= factor;
        }
        operationCNT += m_operationCNT + n_operationCNT;
        return gcd_result;
    }

    static void Main()
    {
        Sieve(out int operationCNT);
        Console.WriteLine("sieve() done");
        long[,] testcase = {
            {30, 15}, {20, 72}, {72, 88},{58, 77}, {92, 80},
            {286, 544}, {985, 716}, {839, 433}, {471, 561}, {269, 749},
            {1888, 1224}, {3164, 6996}, {6253, 5431},{4390, 2874}, {5017, 7615},
            {76241, 57606}, {74766, 64553}, {12322, 50440}, {34726, 92155}, {14785, 19817},
            {672270, 431511}, {694404, 256785}, {975922, 532283},{279392, 946230}, {906443, 392685},
            {2226412, 8648878}, {6061228, 5546440}, {1691980, 1414558},{3234496, 7268362}, {8356954, 3705742},
            {81786288, 61052652}, {21535993, 91675657}, {26586591, 78851391},{68575643, 45017255}, {45991767, 77583796},
            {459917672, 775837965}, {265865917, 788513914}, {685756433, 450172557},{785756437, 102475659}, {504857673, 354879547}
        };
        var average_cnt = new List<float>();
        int temp = 0;
        for (int i = 0; i < testcase.GetLength(0) ; i++) {
            operationCNT = 0;
            FindGCD2(testcase[i, 0], testcase[i, 1], out operationCNT);
            if ((i+1) % 5 == 0) {
                average_cnt.Add((float) temp/5);
                temp = 0;
            } 
            else {
                temp += operationCNT;
            }
        }
        Console.WriteLine("[{0}]", string.Join(", ", average_cnt));
    }
}