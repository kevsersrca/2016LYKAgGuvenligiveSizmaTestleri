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

### NTLM Hash ve Pass the Hash

**NTLM Hash:** Windowsdaki kullanıcı parolaları SAM dosyası altında NTLM hashleri alınarak tutulur. 
  * NTLM Hash Windows XP ve Sonrasında kullanılmaya başlamıştır. Daha öncesinde LM hash fonksiyonu kullanılıyordu.
 
***Pass the Hash:*** Windows makinalarda kullanılan domain yapısı sayesinde NTLM Hashler kırılmaya ihtiyaç duymadan makinelere login olmak için kullanılabilir. Bu amaçla Metasploit Framework'ün psexec exploit'i kullanılır.

 * Eğer domain yapısı içerisinde bulunan bir makinaya sızılırsa ve o makinaya daha önceden domain Admin login olmuş ise; o makinadan alınan hashdump ile domain adminin kullanıcı adı ve parola ntlm hashine ulaşılır. **(BINGO!)** Pass the Hash yöntemi ile o domain yapısındaki her makinaya domain adminin kullanıcı adı ve parola hashi kullanılarak erişilebilir.
