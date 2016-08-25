## Hashcat

**Hashcat:** Multi-thread destekli, kompleks yapılı OpenCL kullanan bir GPU Brute Force Aracıdır.

  **Hashcat'de Kullanılan Brute Force Teknikleri:**
   * Brute Force Attack
   * Dictionary Attack
   * Hybrid Attack
   * Combinator Attack
   * Mask Attack
   * Rule-Based Attack
   
***Hashcat Kullanım Örnekleri:***
  ```
    => hashcat -a 7 example.hash ?d?d?d?d example.dict 
    => hashcat -a 7 example.hash example.dict ?d?d?d?d
    => hashcat -a 1 -m0 example.hash example.dict example.dict
    => hashcat -a 7 example0.hash -1 "abcdef12345" "?1?1?1?1" example.dict
  ```
