### Bu Program Nedir?

Bu program, çalıştırıldığı bilgisayarın donanım bilgilerini toplayıp, bu bilgileri Tabidoo'da bir tabloya yüklemeyi sağlar.

### Nasıl Kişiselleştirilir?

Varsayılan olarak, bu program sadece bilgisayardaki toplam RAM ve işletim sistemi bilgilerini verir. Daha fazla detay eklemek için `fetch_specs.py` dosyasını düzenleyebilirsiniz.

### Nasıl Çalışır?

Bu program, alınan bilgileri doğru sırayla Tabidoo ortamındaki tabloya yerleştirir.

**Dikkat:** Alınan verilerin bulunduğu listenin, veri tabanındaki listedeki öğelerle aynı isimde olması önemlidir; aksi takdirde program doğru çalışmayabilir.

<sup>Detaylı bilgi için `fetch_specs.py` dosyasına bakın.</sup>

Kendi Tabidoo API key'inizi, Tabidoo uygulama ID'nizi ve verileri eklemek istediğiniz tablonun ID'sini `main.py` içindeki değişkenlere koyabilirsiniz.

### Nasıl Çalıştırılır / Derlenir?

Programı derlemek için, gerekli modülleri otomatik olarak pip üzerinden indiren ve tek bir çalıştırılabilir Windows dosyası (.exe) haline getiren `compile.exe` dosyasını çalıştırmanız gerekir.

Oluşan çalıştırılabilir `.exe` dosyası `./dist/main.exe` içinde olacaktır. Bu dosyayı bilgilerini almak istediğiniz ve Tabidoo'ya göndermek istediğiniz bilgisayara gönderip çalıştırdığınızda, bilgiler gerekli internet bağlantısı olduğu durumlarda Tabidoo veri tabanına iletilir.

Program kodunu her değiştirdiğinizde, `compile.exe` dosyasını çalıştırmanız gerekmektedir.
