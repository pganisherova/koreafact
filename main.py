from fastapi import FastAPI
import random

app = FastAPI()

facts = [
    "Koreya dunyodagi eng tez internet tezliklaridan biriga ega.",
    "Janubiy Koreya texnologiya va innovatsiyalar bilan mashhur.",
    "K-pop va koreys seriallari butun dunyoda mashhur.",
    "Seul — Janubiy Koreyaning poytaxti va eng katta shahri.",
    "Koreyada ta'lim tizimi juda rivojlangan.",
    "Kimchi Koreyaning eng mashhur an’anaviy taomlaridan biridir.",
    "Koreyada zamonaviy osmono‘par binolar va tarixiy saroylar yonma-yon joylashgan.",
    "Jamoat transporti juda rivojlangan va samarali ishlaydi.",
    "Koreys alifbosi Hangul XV asrda yaratilgan.",
    "Janubiy Koreya elektronika ishlab chiqarishda yetakchi davlatlardan biri.",
    "Samsung va LG Koreyaning mashhur kompaniyalari hisoblanadi.",
    "Koreyada o‘yinlar va e-sport madaniyati juda rivojlangan.",
    "Qahva madaniyati Koreyada juda ommalashgan.",
    "Koreyada to‘rt fasl aniq ajralib turadi.",
    "Kuz faslida Koreyada rang-barang barglar juda chiroyli ko‘rinadi.",
    "Koreyaning katta qismi tog‘lardan iborat.",
    "Jeju oroli mashhur sayyohlik maskanidir.",
    "Koreys taomlari ko‘pincha guruch, sabzavot va go‘shtdan iborat bo‘ladi.",
    "Chuseok va Seollal Koreyaning an’anaviy bayramlaridir.",
    "Taekwondo Koreyaning an’anaviy jang san’atidir.",
    "Koreya juda raqamlashtirilgan davlat hisoblanadi.",
    "Mobil to‘lovlar Koreyada keng tarqalgan.",
    "Ko‘cha taomlari Koreyada juda mashhur.",
    "Koreys kosmetika mahsulotlari butun dunyoda mashhur.",
    "Koreyada o‘rtacha umr davomiyligi yuqori.",
    "DMZ Shimoliy va Janubiy Koreyani ajratib turadi.",
    "Koreyada ko‘plab UNESCO meros obyektlari mavjud.",
    "Hanbok — Koreyaning an’anaviy kiyimi.",
    "Koreys seriallari global auditoriyani jalb qiladi.",
    "Hangul yozuvi o‘rganish uchun nisbatan oson hisoblanadi.",
    "Koreya ilmiy-tadqiqotlarga katta sarmoya kiritadi.",
    "Jamoat xavfsizligi Koreyada yuqori darajada.",
    "Metro va poyezd tizimi juda rivojlangan.",
    "Busan Janubiy Koreyaning yirik shaharlaridan biridir.",
    "Koreyslar teri parvarishiga katta e’tibor berishadi.",
    "Koreys barbekyusi mashhur ovqatlanish usulidir.",
    "N Seoul Tower mashhur diqqatga sazovor joylardan biridir.",
    "Koreyada yuqori texnologiyali shaharlar ko‘p.",
    "Ta’limda raqobat juda yuqori.",
    "Koreya kuchli pop madaniyatga ega.",
    "Yetkazib berish xizmatlari juda tez ishlaydi.",
    "Koreyada ko‘plab kino va seriallar ishlab chiqariladi.",
    "Qishda Koreyada juda sovuq va qor yog‘adi.",
    "Koreya an’anaviy qadriyatlar va zamonaviy hayotni uyg‘unlashtirgan.",
    "Shaharlarda bepul Wi-Fi keng tarqalgan.",
    "Tibbiyot tizimi rivojlangan va sifatli.",
    "Turizm Koreya iqtisodiyotining muhim qismi hisoblanadi.",
    "Yil davomida turli festivallar o‘tkaziladi.",
    "Koreya eksportga yo‘naltirilgan iqtisodiyotga ega.",
    "Koreyada mehnat intizomi va ish madaniyati yuqori."
]
@app.get("/")
def test():
    return {
        "fact": random.choice(facts)
    }