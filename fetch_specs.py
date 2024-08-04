import platform, psutil, math, json
from enum import Enum


# Bu dosya, donanım parça bilgilerini almak için gerekli kodları içerir.
# Daha fazla donanım parçası eklemek veya listeyi tablonuza uygun şekilde düzenlemek için bu dosyayı kullanabilirsiniz.

# -- Donanım parçalarını alma koduyla ilgili değişkenlerinizi buraya ekleyebilirsiniz. --

# Bu değişken, RAM'in veri tabanında yuvarlanmış tam sayı değeri olarak kaydedilmesini sağlar.
ROUND_RAM_GB = True


# -- Bu kısma donanım parça bilgilerini almak için gerekli kodları, ilgili metodlara yazabilirsiniz. --
# Yeni bir donanım bilgisi toplamak için buraya yeni bir metod ekleyin, metodunuzun içine almak istediğiniz donanım bilgisi için gereken kodu girin.
# **Dikkat:** Metodunuz topladığınız bilgiyi döndürmelidir.

def get_total_ram():
    total_ram = psutil.virtual_memory().total * (10 **-9)
    
    if(ROUND_RAM_GB): 
        total_ram = math.trunc(total_ram)
        
    return total_ram

def get_os():
    return platform.platform(terse=True)



# -- Bu liste veri tabanına yüklenecek bilgilerin bulunduğu listedir. Bu listede olmayan donanım bilgileri veri tabanına yüklenmeyecektir. --

# Listedeki ilk eleman, görüntülenme adını temsil etmektedir. Program arayüzündeki görüntüleme için kullanılır.
# İkinci eleman, Tabidoo veri tabanındaki kolon adıyla aynı olmalıdır.
# **Dikkat:** Bu değer veri tabanındakilerle aynı olmalıdır, aksi takdirde hatalar yaşanabilir veya program istenildiği gibi çalışmayabilir.
# Üçüncü eleman, yukarıda oluşturduğunuz metod olmalıdır. (Sonuna parantez koyulmalıdır)
Specs = [
    # Örnek bir eleman
    # ({İlk eleman}, {İkinci eleman}, {Üçüncü eleman}),
    
    ("Toplam Ram Miktari", "toplam_ram", get_total_ram()),
    ("Isletim Sistemi", "isletim_sistemi", get_os()),
]

# -- Bu alanı değiştirmeniz gerekmez --

def fetch_specs():
    specs = {}

    for spec in Specs:
        specs[spec[1]] = spec[2]
    
    return specs

def get_raw_specs():
    return Specs

def parse_for_api(specs):
    parsed_specs = {
        "fields":{
            
        }
    }
    
    for s in specs:
        parsed_specs["fields"][s] = specs[s]
    
    json_data = json.dumps(parsed_specs)
    
    return json_data