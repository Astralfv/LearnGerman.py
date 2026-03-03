import random

# =========================
# MESSAGGIO INIZIALE
# =========================
print("""
========================================
        QUIZ VERBI TEDESCHI 🇩🇪
========================================
Metti alla prova le tue conoscenze!

Per ogni verbo scrivi:
• Infinito
• Präteritum
• Perfekt

Creato da Astral (Alex) 🚀
Versione 2.0
========================================
""")

# =========================
# DIZIONARIO VERBI (50)
# =========================
verbi = {
    "andare": ("gehen", "ging", "ist gegangen"),
    "essere": ("sein", "war", "ist gewesen"),
    "avere": ("haben", "hatte", "hat gehabt"),
    "diventare": ("werden", "wurde", "ist geworden"),
    "venire": ("kommen", "kam", "ist gekommen"),
    "vedere": ("sehen", "sah", "hat gesehen"),
    "dare": ("geben", "gab", "hat gegeben"),
    "prendere": ("nehmen", "nahm", "hat genommen"),
    "mangiare": ("essen", "aß", "hat gegessen"),
    "bere": ("trinken", "trank", "hat getrunken"),
    "parlare": ("sprechen", "sprach", "hat gesprochen"),
    "leggere": ("lesen", "las", "hat gelesen"),
    "scrivere": ("schreiben", "schrieb", "hat geschrieben"),
    "dormire": ("schlafen", "schlief", "hat geschlafen"),
    "correre": ("laufen", "lief", "ist gelaufen"),
    "trovare": ("finden", "fand", "hat gefunden"),
    "rimanere": ("bleiben", "blieb", "ist geblieben"),
    "chiamare": ("rufen", "rief", "hat gerufen"),
    "aiutare": ("helfen", "half", "hat geholfen"),
    "pensare": ("denken", "dachte", "hat gedacht"),
    "sapere": ("wissen", "wusste", "hat gewusst"),
    "conoscere": ("kennen", "kannte", "hat gekannt"),
    "portare": ("tragen", "trug", "hat getragen"),
    "cadere": ("fallen", "fiel", "ist gefallen"),
    "iniziare": ("beginnen", "begann", "hat begonnen"),
    "vincere": ("gewinnen", "gewann", "hat gewonnen"),
    "perdere": ("verlieren", "verlor", "hat verloren"),
    "decidere": ("entscheiden", "entschied", "hat entschieden"),
    "guidare": ("fahren", "fuhr", "ist gefahren"),
    "incontrare": ("treffen", "traf", "hat getroffen"),
    "stare (in piedi)": ("stehen", "stand", "hat gestanden"),
    "sedersi": ("sitzen", "saß", "hat gesessen"),
    "mentire": ("lügen", "log", "hat gelogen"),
    "cantare": ("singen", "sang", "hat gesungen"),
    "nuotare": ("schwimmen", "schwamm", "ist geschwommen"),
    "tagliare": ("schneiden", "schnitt", "hat geschnitten"),
    "offrire": ("bieten", "bot", "hat geboten"),
    "chiudere": ("schließen", "schloss", "hat geschlossen"),
    "aprire": ("öffnen", "öffnete", "hat geöffnet"),
    "comprare": ("kaufen", "kaufte", "hat gekauft"),
    "bruciare": ("brennen", "brannte", "hat gebrannt"),
    "portare (trasporto)": ("bringen", "brachte", "hat gebracht"),
    "tenere": ("halten", "hielt", "hat gehalten"),
    "lasciare": ("lassen", "ließ", "hat gelassen"),
    "chiamarsi": ("heißen", "hieß", "hat geheißen"),
    "salire": ("steigen", "stieg", "ist gestiegen"),
    "affondare": ("sinken", "sank", "ist gesunken"),
    "tirare": ("ziehen", "zog", "hat gezogen"),
    "crescere": ("wachsen", "wuchs", "ist gewachsen")
}

# =========================
# SCELTA NUMERO DOMANDE
# =========================
tot_domande = int(input("Quanti verbi vuoi esercitare? (max 50): "))
punti = 0

# Mischia i verbi
lista_verbi = list(verbi.keys())
random.shuffle(lista_verbi)

# =========================
# QUIZ
# =========================
for i in range(tot_domande):
    italiano = lista_verbi[i]
    infinito, praeteritum, perfekt = verbi[italiano]

    print("\nDomanda", i+1, "/", tot_domande)
    print("Traduci il verbo:", italiano)

    risp_inf = input("Infinito: ")
    risp_praet = input("Präteritum: ")
    risp_perf = input("Perfekt: ")

    if (risp_inf == infinito and
        risp_praet == praeteritum and
        risp_perf == perfekt):
        print("✅ Corretto!")
        punti += 1
    else:
        print("❌ Sbagliato!")
        print("Corretto:", infinito, "-", praeteritum, "-", perfekt)

# =========================
# RISULTATI FINALI
# =========================
percentuale = (punti / tot_domande) * 100

print("\n========================================")
print("           RISULTATO FINALE")
print("========================================")
print("Risposte corrette:", punti, "/", tot_domande)
print("Percentuale:", round(percentuale, 2), "%")

# =========================
# CLASSIFICA
# =========================
if percentuale == 100:
    print("🏆 LEGGENDARIO DEL TEDESCO!")
elif percentuale >= 80:
    print("🥇 Esperto!")
elif percentuale >= 60:
    print("🥈 Buono!")
elif percentuale >= 40:
    print("🥉 Sufficiente!")
else:
    print("📚 Devi studiare ancora!")

print("\nGrazie per aver giocato!")
print("Creato da Astra (Alex) 🚀")
