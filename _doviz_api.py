import requests
import json

api_key= "9386a3c6eade9c30d4036f38"
api_url= f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("bozulan döviz türü:") #USD
alinan_doviz = input("alınan döviz türü:") #TRY
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyorsunuz:")) #ne kadar USD

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)


print("1 {0}={1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * sonuc_json["conversion_rates"][alinan_doviz], alinan_doviz))