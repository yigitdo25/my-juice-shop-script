
# Python Basit Brute-Force (Juice Shop) — README

Bu depo, eğitim amaçlı basit bir parola deneme (brute-force) scripti içerir. Script, lokal veya izni olan bir Juice Shop örneğine (/rest/user/login endpoint) JSON POST isteği göndererek bir e-posta adresi için parola denemeleri yapar. Bu araç sadece kendi laboratuvar ortamında ve yazılı izinli hedeflerde kullanılmalıdır.



## Yasal Uyarı:İzinsiz brute-force saldırıları yasadışıdır. Bu projeyi yalnızca kendi VM/Docker ortamında, eğitim amaçlı ve etik sınırlar içinde kullanın.



  
## İçerik 
* bruteforce.py — parola deneme scripti (örnek)

 * test_wordlist.txt — test amaçlı örnek parola listesi (100 satır)

* README.md — bu dosya
## Gereksinimler
* Python 3.8+

* requests kütüphanesi

Opsiyonel (geliştirme için): virtualenv / VS Code
## Kurulum(adım adım)
1. Depoyu kopyalayın veya dosyaları projenin içine koyun:

git clone <repo-url>

cd <repo-folder>

2. (Önerilen) Sanal ortam oluştur ve aktif edin:

python -m venv .venv
 Linux/macOS

source .venv/bin/activate

 Windows (PowerShell)
.venv\Scripts\Activate.ps1

3. Gerekli Python paketini yükleyin:

pip install requests

4. Test wordlist (örneğin test_wordlist.txt) dosyasını hazırlayın veya kendi wordlist path’ini belirleyin.







  
## Kullanım
Scriptin başında şu değişkenleri kendi ortamına göre güncelleyin:

target_url = "http://localhost:3000/rest/user/login"

username = "admin@juice-sh.op"

wordlist_path = "/path/to/test_wordlist.txt"

Ardından scripti çalıştırın:

python bruteforce.py

Çıktı örneği:

* Başarısız denemeler için: [-] Tried password: 123456

* Başarılı deneme bulunduğunda: [+] Password found: TestPass123!



## Nasıl Çalışır ? (kısa özet)

1. Wordlist dosyasını satır satır okur.

2. Her satır için JSON payload oluşturur: {"email": username, "password": parola}.

3. POST isteği gönderir: target_url (ör. http://localhost:3000/rest/user/login).

4. Dönen cevabı kontrol eder; 200 döndü ve response içinde "authentication" anahtarı varsa başarılı kabul edip scripti sonlandırır.

5. Her denemeden sonra kısa gecikme (time.sleep(1)) uygulanır.
## Güvenlik & Etik Kuralları (mutlaka okuyun)
* SADECE izniniz olan hedeflerde çalıştırın (kendi Juice Shop VM'iniz gibi).

* Başka sunucular veya halka açık hizmetlerde denemeyin — yasal yaptırımla karşılaşabilirsiniz.

* Testleri düşük hız ve küçük wordlist ile başlatın (ör. time.sleep(1) veya daha büyük gecikme).
## Hatalar & Çözüm (kısa)
* ConnectionRefusedError / NameResolutionError
  * Hedef URL veya port yanlış; Juice Shop’un çalıştığından (npm start veya docker) ve target_url’in doğru olduğundan emin olun.
  * Eğer VM içinde çalışıyorsanız scripti VM içinde çalıştırın veya VM port   yönlendirmesini doğru ayarlayın. 

* FileNotFoundError: No such file or directory: '...wordlist.txt'

  * wordlist_path değişkenine doğru dosya yolunu yazın.

* Script hiç başarılı demiyor ama tarayıcıdan giriş oluyorsa

   * Başarı tespit yöntemi yanlış olabilir. DevTools → Network → login     response’ını kontrol edin; başarılı girişte dönen JSON anahtarlarını  (authentication, token vb.) scriptte kontrol edin.
   
## Önerilen geliştirmeler (ileride eklenebilecekler)
* requests.Session() kullanarak cookie/session yönetimi yapmak.

* --concurrency parametresi ile ThreadPoolExecutor ekleyerek paralel denemeler (lab ortamında dikkatli kullanın).

* --delay, --stop-on-success, --wordlist gibi CLI argümanları (argparse).

* Başarıyı daha güvenilir tespit etmek için JSON parse ve token kontrolü.

* Loglama (logging modülü) ve sonuçları JSON/CSV olarak kaydetme.

* CSRF token gerektiren hedefler için önceden GET ile token alma.
## Örnek: Lokal Juice Shop kurulum hatırlatması
* Node.js ile:
  
  git clone https://github.com/juice-shop/juice-shop.git

  cd juice-shop

  npm install

  npm start
  uyarı:tarayıcıda http://localhost:3000 açılmalı

* Alternatif:Docker Desktop ile:

  docker run -d -p 3000:3000 --name juice-shop bkimminich/juice-shop


## Lisans & Katkı
* Bu repo eğitim amaçlıdır. Açık kaynak lisansı olarak MIT (veya tercih ettiğiniz lisans) kullanılabilir.

* Katkılara açık — ama lütfen kötü niyetli kullanım teşvik etmeyin.