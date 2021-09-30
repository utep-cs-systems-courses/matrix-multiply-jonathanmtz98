Report
Jonathan Martinez

Doing this assignment was a little hard, since I had to correct first assignment in order to run this one.
I encountered a big problem when doing the assignment. The problem I had is that I didn't know how to use pymp.Parallel() and how did it function.
I got stuck making my program to work, but once I understood that it could be just added to the for loop, life became easier.


When I ran the program, I did it with different threads, as mentioned(1 thread, 2 threads, 4 threads, and 8 threads), which gave me these outputs:

1 thread 
444444444 444444444 444444444 444444444 444444444 444444444 444444444 444444444 444444444 
Running time: 2.244999266999912

2 threads 
444444444 444444444 444444444 444444444 444444444 444444444 444444444 444444444 444444444 
Running Time: 2.7318823519997386

4 threads
444444444 444444444 444444444 444444444 444444444 444444444 444444444 444444444 444444444 
Elapsed Time: 3.8441474819996984 Seconds Averaged Time per test: 3.971191839099947

8 threads Test 9 444444444 444444444 444444444 444444444 444444444 444444444 444444444 444444444 444444444 
Elapsed Time: 9.744584342954145

What is happening here?
When we run more threads, the program takes more time to run and output values
Is it normal?
Yes. It takes more times to run different threads since the number of jobs are increasing.

Finally, we were asked to provide our CPU info: I used Cygwin to compile everything. 
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 69
model name      : Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz
stepping        : 1
microcode       : 0x25
cpu MHz         : 2500.000
cache size      : 3072 KB
physical id     : 0
siblings        : 4
core id         : 0
cpu cores       : 2
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 18
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe constant_tsc arch_perfmon rep_good nopl xtopology cpuid aperfmperf pni pclmuldq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm epb fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt dtherm ida arat pln pts md_clear flush_l1d
bogomips        : 5000.00
clflush size    : 64
cache_alignment : 64
address sizes   : 39 bits physical, 48 bits virtual
power management:

processor       : 1
vendor_id       : GenuineIntel
cpu family      : 6
model           : 69
model name      : Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz
stepping        : 1
microcode       : 0x25
cpu MHz         : 2500.000
cache size      : 3072 KB
physical id     : 0
siblings        : 4
core id         : 0
cpu cores       : 2
apicid          : 1
initial apicid  : 1
fpu             : yes
fpu_exception   : yes
cpuid level     : 18
wp              : yes
