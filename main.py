# THE MODULES

import twint as twitter
import pandas as data
import os
from datetime import datetime
import csv
import trnlp
import re
from collections import Counter


# VARIABLES
kullanci = 0
line_break = "\n ____________________________________________________________________________________________________________ \n"
hata_bool = False
special_characters = "!\"  # $%^&*()-+?_=':`,.\',<>/ :"
anlamsiz_words = ['ve', 'son', 'bir', 'ile', 'gün', 'kişi', 'yaş', '|'
                  'dakika', 'için', 'bin', 'bu', 'ed', 'al', 'daki̇kia', 'etti', 'et', 'iç', 'da']

user_accounts = [
    "Haberler",  # user 1         Haberler
    "dhainternet",  # user 2         Demirören Haber Ajansı
    "Haberturk",  # user 3         Habertürk
    "trthaber",  # user 4         TRT HABER
    "tgrthabertv",  # user 5         TGRT HABER
    "ihacomtr",  # user 6         İhlas Haber Ajansı
    "Haber7",  # user 7         Haber 7
    "ankahabera",  # user 8         ANKA Haber Ajansı
    "Haber",  # user 9         Haber
    "sondakika1921"  # user 10        SON DAKİKA HABERLERİ
]

users = [
    "Haberler",  # user 1
    "Demirören Haber Ajansı",  # user 2
    "Habertürk",  # user 3
    "TRT HABER",  # user 4
    "TGRT HABER",  # user 5
    "İhlas Haber Ajansı",  # user 6
    "Haber 7",  # user 7
    "ANKA Haber Ajansı",  # user 8
    "Haber",  # user 9
    "SON DAKİKA HABERLERİ"  # user 10
]

tweets = {
    "Haberler": [],
    "dhainternet": [],
    "Haberturk": [],
    "trthaber": [],
    "tgrthabertv": [],
    "ihacomtr": [],
    "Haber7": [],
    "ankahabera": [],
    "Haber": [],
    "sondakika1921": []
}


# FUNCTIONS


def tanim():

    os.system('color B')
    print("""
                                                                ////////////     //
                                       ////                   /////////////////////
                                       ///////               ///////////////////////
                                       ///////////           /////////////////////
                                        //////////////////   ////////////////////
                                       /  ///////////////////////////////////////
                                       //////////////////////////////////////////
                                        ////////////////////////////////////////
                                          /////////////////////////////////////
                                          //*/////////////////////////////////
                                            /////////////////////////////////
                                              /////////////////////////////
                                                   //////////////////////
                                              ////////////////////////
                                       ///////////////////////////
                                              /////////////


                                ██████████╗    █████████████████████████████████╗  @ by yousef yousef
                                ╚══██╔══██║    ████╚══██╔══╚══██╔══██╔════██╔══██╗ @ ÖN: 2018705133
                                   ██║  ██║ █╗ ████║  ██║     ██║  █████╗ ██████╔╝
                                   ██║  ██║███╗████║  ██║     ██║  ██╔══╝ ██╔══██╗
                                   ██║  ╚███╔███╔██║  ██║     ██║  █████████║  ██║
                                   ╚═╝   ╚══╝╚══╝╚═╝  ╚═╝     ╚═╝  ╚══════╚═╝  ╚═╝

        ██╗   ██╗   ███████╗   ██████╗    ██╗         █████╗    ███╗   ██╗    █████╗    ██╗        ██╗   ███████╗   ██╗
        ██║   ██║   ██╔════╝   ██╔══██╗   ██║        ██╔══██╗   ████╗  ██║   ██╔══██╗   ██║        ██║   ╚══███╔╝   ██║
        ██║   ██║   █████╗     ██████╔╝   ██║   ---  ███████║   ██╔██╗ ██║   ███████║   ██║        ██║     ███╔╝    ██║
        ╚██╗ ██╔╝   ██╔══╝     ██╔══██╗   ██║        ██╔══██║   ██║╚██╗██║   ██╔══██║   ██║        ██║    ███╔╝     ██║
         ╚████╔╝    ███████╗   ██║  ██║   ██║        ██║  ██║   ██║ ╚████║   ██║  ██║   ███████╗   ██║   ███████╗   ██║
          ╚═══╝     ╚══════╝   ╚═╝  ╚═╝   ╚═╝        ╚═╝  ╚═╝   ╚═╝  ╚═══╝   ╚═╝  ╚═╝   ╚══════╝   ╚═╝   ╚══════╝   ╚═╝

                                          """
          )


def soru():
    print(
        "\t\t\t\t\t seçtiğim alan [haberler hesabları]\n\t\tseçtiğim hesabları:\n")
    for sira, hesap in enumerate(users):
        if (sira == 9):
            print("\t\t\t", str((sira+1)), ". hesab:     ", hesap)
        else:
            print("\t\t\t", str((sira+1)), " . hesab:     ", hesap)

    print("""
    not:
dataset1 tüm tweetleri içerir
dataset2, aşağıdaki düzenlemelere ile tüm tweetleri içerir:
    - https linkleri olmadan
    - hashtag'ler olmadan
    - taglar olmadan
    - özel semboller olmadan
    - (sondakika) kelimesi olmadan 
    - tüm harfler küçük harfe dönüştürülür

                                    Lütfen bir işlem seçiniz:

                            1- [dataset1.csv] ve [dataset2.csv] dosyaları sıfırdan oluşturmak için

                            2- [dataset2.csv] içindeki verileri analiz yapmak için
                            

        """)
    kullanci = input("\t\t\t\t\t\t --> ")

    try:
        kullanci = int(kullanci)
        if (kullanci > 0 and kullanci < 3):
            return True, kullanci
        else:
            print(line_break, "\t\t\t\t\tLÜTFEN 1, 2 veya 3 GİRİNİZ\n")

            return False, 0

    except:
        print(line_break, "\t\t\t\t\tLÜTFEN SADECE SAYİ GİRİNİZ\n")
        return False, 0


def on_islemler(df, max_tweets):
    df_2 = df
    # tagları kaldırmak @ (kisi isimi ile)
    # karakter olmayain silmek
    # linkerli kaldirmak (https)
    # bütün harefleri küçüğe dünüştürmek
    # son dakkika silmek
    for i in range(len(df.columns)):
        for j in range(max_tweets):
            cash_array = df.iat[j, i].split()
            cash_array_1 = df_2.iat[j, i].split()
            for sira, kelime in enumerate(cash_array):

                # special characters
                kac_char_silindi = 0
                for sira2, character in enumerate(kelime):
                    if (character in special_characters):
                        cash_list = list(cash_array_1[sira])
                        cash_list[(sira2 - kac_char_silindi)] = ''
                        cash_array_1[sira] = ''.join(cash_list)
                        kac_char_silindi = kac_char_silindi + 1

                # https and tags
                if (kelime[0:5] == "https") or (kelime[0:1] == "@"):
                    cash_array_1[sira] = ""

               # lower case
                cash_array_1[sira] = cash_array_1[sira].lower()
                # son dakkika silmek

                if (cash_array_1[sira] == "sondakika"):
                    cash_array_1[sira] = ""

            df_2.iat[j, i] = ' '.join(cash_array_1)

    return df_2


def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False


def ODEV1():
    # clear data sets
    try:
        file = open("dataset1.csv", "w+")
        file.close
        file = open("dataset2.csv", "w+")
        file.close
    except:
        pass

    # make the file if it doesn't exist
    file = open("cash.csv", "a")
    file.close

    max_tweet_sayisi = 0

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    print("date and time =", dt_string)
    dt_string_array = dt_string.split("-")

    for hesab in user_accounts:

        # date
        gun = int(dt_string_array[0])
        ay = int(dt_string_array[1])
        yil = int(dt_string_array[2])-1  # 1 year

        while yil <= int(dt_string_array[2]):

            while ay <= 12:

                while gun <= 31:
                    try:

                        config = twitter.Config()

                        config.Username = hesab
                        config.User_full = True

                        config.Since = (
                            str(yil)+"-"+str(ay)+"-" + str(gun)+" 00:00:00")

                        print(str(yil)+"-"+str(ay) +
                              "-" + str(gun)+" 00:00:00")
                        gun = 1 + gun

                        config.Until = (
                            str(yil)+"-"+str(ay)+"-" + str(gun)+" 00:00:00")

                        print(str(yil)+"-"+str(ay)+"-" + str(gun)+" 00:00:00")

                        config.Store_csv = True
                        config.Output = "cash.csv"
                        # running search
                        twitter.run.Search(config)
                        if (yil == int(dt_string_array[2])) and (ay == int(dt_string_array[1])) and (gun == (int(dt_string_array[0])+1)):
                            break
                    except:
                        continue

                if (yil == int(dt_string_array[2])) and (ay == int(dt_string_array[1])) and (gun == (int(dt_string_array[0])+1)):
                    break
                gun = 1
                ay = ay + 1
            if (yil == int(dt_string_array[2])) and (ay == int(dt_string_array[1])) and (gun == (int(dt_string_array[0])+1)):
                break
            ay = 1
            yil = yil + 1
        try:
            df = data.read_csv('cash.csv', usecols=[10])
            x = 0
            while x < len(df):
                tweets[hesab].append(df.iloc[x, 0])
                x = x + 1
        except:
            pass

        # store the accoutn has more tweets
        if (max_tweet_sayisi < len(tweets[hesab])):
            max_tweet_sayisi = len(tweets[hesab])

        # clear cash
        file = open("cash.csv", "w+")
        file.close

    # now we have all tweets in tweets
    # empty elements so the len matches
    for x in tweets:
        y = max_tweet_sayisi - len(tweets[x])
        for _ in range(y):
            tweets[x].append("")

    # save it as data frame
    data_frame_tweets = data.DataFrame(tweets)
    # export to csv
    data_frame_tweets.to_csv('dataset1.csv', index=False)

    # dataset 2
    data_frame_tweets_2 = on_islemler(data_frame_tweets, max_tweet_sayisi)
    data_frame_tweets_2.to_csv('dataset2.csv', index=False)

    return 0


def ODEV2():
    words = {"Haberler": [],
             "dhainternet": [],
             "Haberturk": [],
             "trthaber": [],
             "tgrthabertv": [],
             "ihacomtr": [],
             "Haber7": [],
             "ankahabera": [],
             "Haber": [],
             "sondakika1921": []
             }
    words_kok = {"Haberler": [],
                 "dhainternet": [],
                 "Haberturk": [],
                 "trthaber": [],
                 "tgrthabertv": [],
                 "ihacomtr": [],
                 "Haber7": [],
                 "ankahabera": [],
                 "Haber": [],
                 "sondakika1921": []
                 }

    data_frame_tweets = data.read_csv('dataset2.csv')

    print("\n\n sözlülükler oluşturmaya başladı, lütfen bekleyin.... \n\n")
    for sira, i in enumerate(words):
        x = 0
        while x < (len(data_frame_tweets. index)):
            persentage = (round((x / len(data_frame_tweets. index)*100), 1))
            print('\r %', persentage,  end='', flush=True)
            if (str(data_frame_tweets.iat[x, sira]) != ""):
                cash_list = str(data_frame_tweets.iat[x, sira]).split()
                for kelimler in cash_list:
                    words[i].append(kelimler)
            x = x + 1
        print("\n\t\t", users[sira],
              " hesabın sözlüğü oluşturdu... kelime sayisi = ", len(words[i]))

    print(line_break, """

    Kelime sayısı yukarıda yazılmıştır, her bir hesab için kaç kelimeyi analiz etmek istiyorsun?

                (Tüm kelimeleri işlemek istiyorsanız [0] yazın, ancak bu uzun sürebilir)

    """)

    kac = input("\t\t\t --> ")
    try:
        kac = int(kac)
    except:
        print(line_break, "lütfen sadece sayı yazınız")
        input("......................")
    print(line_break, "sözlükte kelime ekleri silinecek (kökleri bulmak için); \n ")
    boll = False
    if (int(kac) == 0):
        boll = True
    for i in words:
        x = 0
        if (boll):
            kac = int(len(words[i]))

        while x <= kac:
            persentage = (round((x / kac*100), 1))
            print('\r %', persentage,  end='', flush=True)
            try:
                kelime = str(words[i][x])
                try:
                    kelime_0 = trnlp.find_stems(kelime)
                    kelime_0 = kelime_0[0]
                    kelime_0 = re.split('{|\(', kelime_0)
                    if (kelime_0[1] != "fiil)"):
                        kelime = str(kelime_0[0])
                except:
                    pass

                if kelime:
                    words_kok[i].append(kelime)
            except:
                pass

            x = x + 1

        print("\t\t\t ", i, " tamamlandı ... \n")

    while True:
        print(line_break, """

                kök sözlükleri oluşturması tamamlandı,

        1- tüm hesaplarda en çok tekrarlanan kelime listesi (10 lu) 
        2- belirli bir hesapta en çok tekrarlanan kelime listesi (10 lu)
        3- Genel en sık kullanılan ard arda 2 kelime listesi  (10 lu) 

        0- programı kapat

    """)
        cevap = input("\t\t\t -->")

        if (cevap == "0"):
            break
        if (cevap == "1"):
            allwords = []
            for z in words_kok:
                for j in words_kok[z]:
                    allwords.append(j)
            c = Counter(allwords)
            kac_words = 10
            tekrar = []
            sira_anlamsiz = []
            while len(tekrar) != 10:
                sira_anlamsiz = []
                tekrar = c.most_common(kac_words)
                for sira, i in enumerate(tekrar):
                    anlamsiz = str(i).split("'")

                    if (str(anlamsiz[1]) in anlamsiz_words) or (containsNumber(str(anlamsiz[1]))) or (str(anlamsiz[1])[0:3] == "dak"):
                        sira_anlamsiz.append(sira)

                sira_anlamsiz_1 = len(sira_anlamsiz)
                for i in sira_anlamsiz:
                    sira_anlamsiz_1 = sira_anlamsiz_1 - 1
                    tekrar.remove(tekrar[sira_anlamsiz[sira_anlamsiz_1]])

                kac_words = kac_words + 1

            for sira, i in enumerate(tekrar):
                print("\n\t hesablarda En çok tekrarlanan ", str(sira+1), ". kelime (ve tekrarlanma sayısı): ",
                      i)
            print(line_break)

        if (cevap == "2"):
            print(
                "\n\n\t\tbir hesab seçiniz:\n")
            for sira, hesap in enumerate(users):
                if (sira == 9):
                    print("\t\t\t", str((sira+1)), ". hesab:     ", hesap)
                else:
                    print("\t\t\t", str((sira+1)), " . hesab:     ", hesap)
            while True:
                try:
                    hangi_hesab = int(input(" \n \t\t\t--->"))
                    if (hangi_hesab > 0) and (hangi_hesab < 11):
                        break
                    else:
                        print("\n lüten 0-10 arasında bir sayı yaziniz")

                except:
                    print("\n lüten sayi yaziniz")
            hes = ""
            for sira, i in enumerate(user_accounts):
                if (int(hangi_hesab)-1) == sira:
                    hes = i
            allwords = []
            for j in words_kok[hes]:
                allwords.append(j)
            c = Counter(allwords)
            kac_words = 10
            tekrar = []
            sira_anlamsiz = []
            while len(tekrar) != 10:
                sira_anlamsiz = []
                tekrar = c.most_common(kac_words)
                for sira, i in enumerate(tekrar):
                    anlamsiz = str(i).split("'")

                    if (str(anlamsiz[1]) in anlamsiz_words) or (containsNumber(str(anlamsiz[1]))) or (str(anlamsiz[1])[0:3] == "dak"):
                        sira_anlamsiz.append(sira)

                sira_anlamsiz_1 = len(sira_anlamsiz)
                for i in sira_anlamsiz:
                    sira_anlamsiz_1 = sira_anlamsiz_1 - 1
                    tekrar.remove(tekrar[sira_anlamsiz[sira_anlamsiz_1]])

                kac_words = kac_words + 1
            hangi_hesab = int(hangi_hesab)
            hangi_hesab = hangi_hesab - 1
            for sira, i in enumerate(tekrar):
                print("\n\t", users[hangi_hesab], " hesab da En çok tekrarlanan ", str(sira+1), ". kelime (ve tekrarlanma sayısı): ",
                      i)
            print(line_break)

        if (cevap == "3"):
            cash_Str = ""
            ikili_words_kok = []
            for z in words_kok:
                for sira, j in enumerate(words_kok[z]):
                    try:
                        cash_Str = j + " " + str(words_kok[z][(sira+1)])
                    except:
                        pass
                    ikili_words_kok.append(cash_Str)
            c = Counter(ikili_words_kok)
            kac_words = 10
            tekrar = []
            sira_anlamsiz = []
            while len(tekrar) != 10:
                sira_anlamsiz = []
                tekrar = c.most_common(kac_words)
                for sira, i in enumerate(tekrar):
                    anlamsiz = str(i).split("'")

                    if (str(anlamsiz[1]) in anlamsiz_words) or (containsNumber(str(anlamsiz[1]))) or (str(anlamsiz[1])[0:3] == "dak"):
                        sira_anlamsiz.append(sira)

                sira_anlamsiz_1 = len(sira_anlamsiz)
                for i in sira_anlamsiz:
                    sira_anlamsiz_1 = sira_anlamsiz_1 - 1
                    tekrar.remove(tekrar[sira_anlamsiz[sira_anlamsiz_1]])

                kac_words = kac_words + 1

            for sira, i in enumerate(tekrar):
                print("\n\t hesablarda En çok tekrarlanan ", str(sira+1), ". kelime (ve tekrarlanma sayısı): ",
                      i)
            print(line_break)
    return 0


# THE CODE
tanim()


while (hata_bool == False):
    hata_bool, kullanci = soru()
print("---> ", kullanci, " seçtiniz", line_break)

if (kullanci == 1):
    ODEV1()
elif (kullanci == 2):
    ODEV2()


input(" Exit ..............................................")
