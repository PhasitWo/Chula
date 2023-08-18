using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http.Headers;

class Program
{
    const long MAXN = 999_999_999;
    public static long[] spf = new long[MAXN];
    static int operationCNT = 0;

    static List<long> PrimeFac1(long num)
    {
        List<long> factor = new List<long>();
        while (num % 2 == 0)
        {
            factor.Add(2);
            num /= 2;
            operationCNT++;
        }

        for (int i = 3; i <= Math.Sqrt(num); i += 2)
        {
            while (num % i == 0)
            {
                factor.Add(i);
                num = num / i;
                operationCNT++;
            }
        }

        if (num > 2)
        {
            factor.Add(num);
        }
        return factor;
    }

    static long FindGCD1(long m, long n)
    {
        List<long> commonFac = new List<long>();
        List<long> m_fac = PrimeFac1(m);
        List<long> n_fac = PrimeFac1(n);
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
                operationCNT++;
            }
            else if (m_fac[i] < n_fac[j])
            {
                i++;
                operationCNT++;
            }
            else
            {
                j++;
                operationCNT++;
            }
        }

        foreach (long factor in commonFac)
        {
            gcd_result *= factor;
        }

        return gcd_result;
    }

    static void Sieve()
    {
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

    static List<long> PrimeFac2(long n)
    {
        List<long> ret = new List<long>();
        while (n != 1)
        {
            ret.Add(spf[n]);
            n /= spf[n];
            operationCNT++;
        }
        return ret;
    }

    static long FindGCD2(long m, long n)
    {
        List<long> commonFac = new List<long>();
        List<long> m_fac = PrimeFac2(m);
        List<long> n_fac = PrimeFac2(n);

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
        return gcd_result;
    }

    static long FindGCD3(long m, long n)
    {
        operationCNT++;
        if (m == 0)
        {
            return n;
        }
        if (n == 0)
        {
            return m;
        }
        if (m > n)
        {
            return FindGCD3(m % n, n);
        }
        else if (m == n)
        {
            return FindGCD3(m, n);
        }
        else // m < n
        {
            return FindGCD3(m, n % m);
        }
    }
    static List<float> Test_ops_cnt(long[,] testcase, Func<long, long, long> gcd_fuction, bool limit_test_to9digits = false)
    {
        int limit = limit_test_to9digits ? 15 : 0;
        var average_cnt = new List<float>();
        int temp = 0;
        for (int i = 0; i < testcase.GetLength(0) - limit; i++)
        {
            operationCNT = 0;
            gcd_fuction(testcase[i, 0], testcase[i, 1]);
            if ((i + 1) % 5 == 0)
            {
                average_cnt.Add((float)temp / 5);
                temp = 0;
            }
            else
            {
                temp += operationCNT;

            }
        }
        return average_cnt;
    }

    static List<double> Test_time_used(long[,] testcase, Func<long, long, long> gcd_fuction, bool limit_test_to9digits = false)
    {
        int limit = limit_test_to9digits ? 15 : 0;
        var watch = new Stopwatch();
        var average_time = new List<double>();
        double temp = 0;
        for (int i = 0; i < testcase.GetLength(0) - limit; i++)
        {
            watch.Start();
            gcd_fuction(testcase[i, 0], testcase[i, 1]);
            watch.Stop();
            temp += watch.Elapsed.TotalNanoseconds;
            watch.Reset();
            if ((i + 1) % 5 == 0)
            {
                average_time.Add((double)temp / 5);
                temp = 0;
            }
        }
        return average_time;
    }
    static void Main()
    {
        Sieve();
        Console.WriteLine("sieve() done");

        long[,] testcase = {
        {30, 15}, {20, 72}, {72, 88},{58, 77}, {92, 80},
        {286, 544}, {985, 716}, {839, 433}, {471, 561}, {269, 749},
        {1888, 1224}, {3164, 6996}, {6253, 5431},{4390, 2874}, {5017, 7615},
        {76241, 57606}, {74766, 64553}, {12322, 50440}, {34726, 92155}, {14785, 19817},
        {672270, 431511}, {694404, 256785}, {975922, 532283},{279392, 946230}, {906443, 392685},
        {2226412, 8648878}, {6061228, 5546440}, {1691980, 1414558},{3234496, 7268362}, {8356954, 3705742},
        {81786288, 61052652}, {21535993, 91675657}, {26586591, 78851391},{68575643, 45017255}, {45991767, 77583796},
        {459917672, 775837965}, {265865917, 788513914}, {685756433, 450172557},{785756437, 102475659}, {504857673, 354879547},
        {4737418245, 9465215337}, {7384184877, 6565315335},{6531741823, 8795491761}, {5865583711, 9535851393}, {6954464645, 8017257569}, 
        {84184418245, 65310172575},{58659151391, 85756451391}, {57564301725, 74851857673}, {59917672487, 88512663377}, {65315344641, 98418485851},
        {789176724879, 659151396733}, {659117416437, 946585181391}, {653184188245, 758331017965}, {841818235337, 767318488245}, {953525754641, 658518571823}
        };
        // **Operation Count Test**
        List<float> average_cnt_method1 = Test_ops_cnt(testcase, FindGCD1);
        List<float> average_cnt_method2 = Test_ops_cnt(testcase, FindGCD2, true); // limit to 9 digits
        List<float> average_cnt_method3 = Test_ops_cnt(testcase, FindGCD3);
        Console.WriteLine("[{0}]", string.Join(", ", average_cnt_method1));
        Console.WriteLine("[{0}]", string.Join(", ", average_cnt_method2));
        Console.WriteLine("[{0}]", string.Join(", ", average_cnt_method3));



        // **Time Usage Test**
        List<double> average_time_method1 = Test_time_used(testcase, FindGCD1);
        List<double> average_time_method2 = Test_time_used(testcase, FindGCD2, true); // limit to 9 digits
        List<double> average_time_method3 = Test_time_used(testcase, FindGCD3);
        Console.WriteLine("[{0}]", string.Join(", ", average_time_method1));
        Console.WriteLine("[{0}]", string.Join(", ", average_time_method2));
        Console.WriteLine("[{0}]", string.Join(", ", average_time_method3));

    }
}

