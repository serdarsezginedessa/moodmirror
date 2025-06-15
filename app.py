from flask import Flask, request, jsonify
import random

app = Flask(__name__)

öneriler = {
    "yorgun": [
        "Biraz dinlen, müzik dinle.",
        "Kısa bir yürüyüş yap.",
        "Gözlerini kapatıp 5 dakika derin nefes al."
    ],
    "mutlu": [
        "Bu anı kutla! Sevdiklerinle vakit geçir.",
        "En sevdiğin şarkıyı aç.",
        "Birine güzel bir mesaj gönder."
    ],
    "canı sıkılmış": [
        "Yeni bir kitap keşfet.",
        "Online bir kursa göz at.",
        "Yeni bir yemek tarifi dene."
    ],
    "stresli": [
        "5 dakikalık meditasyon yap.",
        "Telefonu bırakıp biraz dışarı çık.",
        "Derin nefes al ve kaslarını gevşet."
    ],
    "kararsız": [
        "Artı-eksi listesi yap.",
        "Kısa bir ara ver, sonra yeniden düşün.",
        "Bir arkadaşına danış."
    ],
    "film": [
        "Inception",
        "The Matrix",
        "Interstellar",
        "The Secret Life of Walter Mitty"
    ],
    "müzik": [
        "Lo-fi beats aç.",
        "En sevdiğin sanatçının yeni albümüne göz at.",
        "YouTube'da canlı konser ara."
    ],
    "kitap": [
        "1984 – George Orwell",
        "Hayvan Çiftliği – George Orwell",
        "Sapiens – Yuval Noah Harari",
        "Kürk Mantolu Madonna – Sabahattin Ali"
    ]
}


@app.route("/tavsiye", methods=["POST"])
def tavsiye():
    veri = request.json.get("durum", "").lower()

    for anahtar in öneriler:
        if anahtar in veri:
            return jsonify({"tavsiye": random.choice(öneriler[anahtar])})

    return jsonify({"tavsiye": "Genel olarak üretken kalmaya çalış. Yeni bir şey dene!"})


if __name__ == "__main__":
    app.run(debug=True)
# sdfönsjdngfkjsndsdfsdgsfg
