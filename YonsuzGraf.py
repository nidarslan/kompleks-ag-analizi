#1. Eigenvector Merkeziyet Ölçütü Hesaplama 
#a. Eigenvector merkeziyet ölçütünün başlangıç vektörünü sabit (hepsi 1), derece,
#yakınlık ve aradalık ölçütleri ile ayrı ayrı belirleyip yönsüz üçer graf üzerinde
#eigenvector merkeziyeti hesaplatmak.
#b. Eigenvector değerlerinin; derece, yakınlık ve aradalık değerleri ile korelasyonunu
#hesaplatmak


import networkx as nx #networkx kütüphanesini import ettik.

#Yonsuz 3 tane farkli sekillerde graflar olusturduk.
G1= nx.lollipop_graph(100,5)
G2=nx.barabasi_albert_graph(100,1)
G3= nx.barbell_graph(50,2)

# Korelasyon icin fonksiyonumuz

#İlk olarak ortalama bulabilmek için ortalamaBul adlı fonksiyon oluşturduk.
def ortalamaBul(deger): #"deger" adlı degisken tanimladik.
    veriAdedi = len(deger) 
    if veriAdedi <= 1:
        return deger
    else:
        return sum(deger) / veriAdedi
#len() ile fonksiyonun veri sayısını bulduk ve 1 veya 1 den kücükse deger oldugu gibi döner.
#1 den buyukse degerin toplam rakamlarını sayiya böler ve ortalamayi bulur.


def korelasyonBul(deger_1, deger_2):
    # Adim1 eger degiskenler icindeki adetler aynı değilse islemlere devam etmeme durumu assert ile belirtilir.
    assert len(deger_1) == len(deger_2)
    # Adim2 veri adetlerini bir degiskene tanımlanır ve assert yardımı ile eger adet 0 ise islemlere devam etmeme durumunu belirtilir.
    veri_adedi = len(deger_1)
    assert veri_adedi > 0
    # Adim3 ortalamaBul fonksiyonlariyla islem yapilir.
    deger_1_ortalama = ortalamaBul(deger_1)
    deger_2_ortalama = ortalamaBul(deger_2)
    deger_olasilik = 0
    deger_1_d_2 = 0
    deger_2_d_2 = 0
    for deger in range(veri_adedi): #herbir degisken ile islemler yapilir.
        deger_1_d = deger_1[deger] - deger_1_ortalama
        deger_2_d = deger_2[deger] - deger_2_ortalama
        deger_olasilik += deger_1_d * deger_2_d
        deger_1_d_2 += deger_1_d * deger_1_d
        deger_2_d_2 += deger_2_d * deger_2_d
    # Adim4  korelasyon formülündeki matematiksel islemler yapılır. 
    #Bulunan degerlerin carpiminin karekökü alinarak veri adedine bölünür ve korelasyon katsayısı bulunur.
    return deger_olasilik / (deger_1_d_2 * deger_2_d_2)**.5


calistir = [G1,G2,G3] #olusturdugumuz 3 yönsüz grafi liste halinde calistira atadik.
for i in range(len(calistir)): #for dongusu sayesinde calistira atadigimiz üc graf icin istenilenleri yaptik.
     
    #calistir[i] ---> bu kısımlarda bu sekilde kullanma sebebimiz
    #liste icindeki G1, G2, G3 graflarinda sirayla gezindik.
    #İstenilenleri elde ettik.
    
    DERECE = nx.degree_centrality(calistir[i]) #derece merkeziyeti hesaplatmak.
    YAKINLIK = nx.closeness_centrality(calistir[i], u=None, distance=None, wf_improved=True) #yakınlık hesaplatmak.
    ARADALIK= nx.betweenness_centrality(calistir[i], k=None, normalized=True, weight=None, endpoints=False, seed=None) #aradalık hesaplatmak.
    OZVEKTOR = nx.eigenvector_centrality(calistir[i], max_iter=100, tol=1e-06, nstart=None, weight=None) #ozvektor hesaplatmak.

    
    nx.draw(calistir[i], with_labels = True) #Oluşan grafları çizdirir.
    
    #Ozvektor icin merkeziyet ölçütünün başlangıç vektörünü 
    #derece, yakınlık ve aradalık ölçütleri ile ayrı ayrı belirlemek için
    #nstart değerine tek tek DERECE, YAKINLIK, ARADALIK degerlerini verdik.
    OZVEKTORDERECE = nx.eigenvector_centrality(calistir[i], max_iter=100, tol=1e-06, nstart=DERECE, weight=None)
    OZVEKTORYAKINLIK = nx.eigenvector_centrality(calistir[i], max_iter=100, tol=1e-06, nstart=YAKINLIK, weight=None)
    OZVEKTORARADALIK = nx.eigenvector_centrality(calistir[i], max_iter=100, tol=1e-06, nstart=ARADALIK, weight=None)
    
    
    #print ile tek tek istenilen değerleri yazdirdik.
    print(calistir[i]," GRAFI İÇİN-------------------")
    print("Aradalık" ,"\n",ARADALIK,"\n")
    print("Derece " ,"\n",DERECE,"\n")
    print("Yakınlık ","\n" ,YAKINLIK,"\n")
    print("Özvektör " ,"\n",OZVEKTOR,"\n")
    print("Derece başlangıç değeri ile hesaplanmış ÖZVEKTÖR: " ,"\n",OZVEKTORDERECE,"\n")
    print("Yakınlık başlangıç değeri ile hesaplanmış ÖZVEKTÖR: ","\n" ,OZVEKTORYAKINLIK,"\n")
    print("Derece başlangıç değeri ile hesaplanmış ÖZVEKTÖR: ","\n" ,OZVEKTORARADALIK,"\n")

# korelasyon hesabi icin değişkenlerin tanımlanması
    a = OZVEKTOR
    b = ARADALIK
    c = DERECE
    d = YAKINLIK
    e = OZVEKTORDERECE
    f = OZVEKTORARADALIK
    g = OZVEKTORYAKINLIK
    
    
    #print ile korelasyonlari hesaplattik.
    print("AYNI DEĞİŞKENLE KORELASYON ", korelasyonBul(a,a))
    print("KORELASYON DERECE İÇİN ", korelasyonBul(e,c))
    print("KORELASYON ARADALIK İÇİN ", korelasyonBul(f,b))
    print("KORELASYON YAKINLIK İÇİN ", korelasyonBul(g,d))



