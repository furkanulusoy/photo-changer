import cv2
import numpy as np

# Arka planı kaldıracak fonksiyon
def arka_plan_kaldir(resim):
    # Resmin HSV renk uzayına dönüştürülmesi
    hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)

    # Arkaplan maskesi oluşturma
    mask = cv2.inRange(hsv, np.array([0, 0, 0]), np.array([180, 255, 255]))

    # Arka planı silme
    arka_plansiz_resim = cv2.bitwise_and(resim, resim, mask=mask)

    return arka_plansiz_resim

# Fotoğraf ekleme fonksiyonu
def fotograf_ekle(arka_plansiz_resim, fotograf):
    # Fotoğrafın boyutunu ayarlama
    fotograf = cv2.resize(fotograf, (arka_plansiz_resim.shape[1], arka_plansiz_resim.shape[0]))

    # Fotoğrafı arka plana ekleme
    sonuc = cv2.addWeighted(arka_plansiz_resim, 1.0, fotograf, 0.7, 0)

    return sonuc

# Kullanılacak resimlerin yolları
orijinal_resim_yolu = "P:\p\p.png"
fotograf_yolu = "P:\p\p.png"

# Resimleri okuma
orijinal_resim = cv2.imread(orijinal_resim_yolu)
fotograf = cv2.imread(fotograf_yolu)

# Arka planı kaldırma
arka_plansiz_resim = arka_plan_kaldir(orijinal_resim)

# Fotoğrafı ekleme
sonuc = fotograf_ekle(arka_plansiz_resim, fotograf)

# Sonucu gösterme
cv2.imshow("Sonuç", sonuc)
cv2.waitKey(0)
cv2.destroyAllWindows()


