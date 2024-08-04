import fetch_specs as fs, requests, sys, os, keyboard
from colorama import Cursor

# Bu değişken, toplanan verilerin komut istemcisinde gösterilip gösterilmeyeceğine karar verir.
DISPLAY_SPECS = True


# Buraya kendi Tabidoo API anahtarınızı girin.
API_KEY = ""
# Buraya verileri eklemek istediğiniz tablonun bulunduğu uygulamanın adını (ID'sini) girin.
APP_ID = ""
# Buraya verilerin ekleneceği tablonun ID'sini girin.
TABLE_ID = ""
# Bu sabiti değiştirmeniz gerekmez.
URL = "https://app.tabidoo.cloud/api/v2/apps/"+APP_ID+"/tables/"+TABLE_ID+"/data?dataResponseType=All"


headers = {
  'Authorization': f'Bearer {API_KEY}',
  'Content-Type': 'application/json'
}

specs = fs.fetch_specs()

parsed_specs = fs.parse_for_api(specs)

print("Butun sistem bilgisi toplandi")
print("-----------------------------\n")

if(DISPLAY_SPECS):
  raw_specs = fs.get_raw_specs()
    
  print("Toplanan Bilgiler")
  print("-----------------")
  for spec in raw_specs:
    print(str(spec[0]) + " = " + str(spec[2]))
  print("-----------------\n")
  pass

while(True):
  ans = input("Bu verileri tabidoo ortamina yuklemek istedigine emin misin (e/h): ")
  
  if ans == 'e' or ans == "evet":
    break
  elif ans == 'h' or ans == "hayır":
    quit()
  
  sys.stdout.write(Cursor.UP(1))
  sys.stdout.write('\r' + ' ' * (os.get_terminal_size().columns - 1) + '\r')
  sys.stdout.flush()


res = requests.post(URL, data=parsed_specs, headers=headers)

if(res.status_code == 200):
  print("Bilgiler tabidoo ortamina basariyla yuklendi.")
else:
  print("Bir sorun olustu.")
  print("Hata kodu: " + str(res.status_code))
  print("Hata kodlarinin anlamlarini bu linkden gorebilirsiniz: https://tabidoo.docs.apiary.io/#introduction/handle-errors/http-status-codes")

print("\nCikmak icin herhangi bir tusa basin...")
keyboard.read_event()
quit()