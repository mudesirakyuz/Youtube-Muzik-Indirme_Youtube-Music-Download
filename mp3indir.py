from pytube import YouTube
import os

link = "https://www.youtube.com/watch?v=UYkJhjlLdwY"
os.mkdir("İndirilenler")
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