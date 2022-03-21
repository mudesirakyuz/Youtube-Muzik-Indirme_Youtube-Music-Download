from pytube import YouTube
import os

link = "Youtube müzik linkini buraya kopyala..."
os.mkdir("Indirilenler")
print("İndirilenler klasörü oluşturuldu...")
print("İndirme başlatılıyor...")
klasor = "İndirilenler"

try:
    yt = YouTube(link)
except:
    print("Bir şeyler ters gitti...")
    exit()
music=yt.streams.filter(only_audio=True).first()
print("İndiriliyor")
cikis=music.download(klasor)
baslangicyolu, _ =os.path.splitext(cikis)
print(baslangicyolu)
donustur=baslangicyolu+".mp3"
os.rename(cikis,donustur)
print("İndirme tamamlandı...")
