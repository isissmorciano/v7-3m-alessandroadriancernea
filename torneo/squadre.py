# Una squadra è rappresentata da un dizionario con:
# - `nome`: nome della squadra
# - `città`: città di provenienza
# - `giocatori`: numero di giocatori in rosa
# - `vittorie`: numero di partite vinte
# - `pareggi`: numero di pareggi
# - `sconfitte`: numero di partite perse
# - `gol_segnati`: totale goal fatti
# - `gol_subiti`: totale goal subiti

squadra: dict = {
    "nome": "Milan",
    "città": "Milano",
    "giocatori": 23,
    "vittorie": 0,
    "pareggi": 0,
    "sconfitte": 0,
    "gol_segnati": 4,
    "gol_subiti": 1
}

def crea_squadra(nome, città, giocatori):
    #    Crea una squadra con statistiche iniziali a 0.
    s1 = crea_squadra["Inter", "Milano", 23]
    s2 = crea_squadra("Milan", "Milano", 22)
    s3 = crea_squadra("Juventus", "Torino", 25)
    s4 = crea_squadra("Roma", "Roma", 20)
    s5 = crea_squadra("Napoli", "Napoli", 21)
    s6 = crea_squadra("Lazio", "Roma", 19)
    return s1, s2, s3, s4, s5, s6

def info_squadra(squadra):
#        Restituisce una stringa formattata con tutte le informazioni della squadra.  
#    Es: `"Inter (Milano) | 10 gol | 25 vittorie, 3 pareggi, 2 sconfitte"`
    s1 = info_squadra("Inter", "Milano", 23, 25, 3, 2, 10, 5)
    s2 = info_squadra("Milan", "Juventus", 22, 25, 3, 2, 10, 5)
    s3 = info_squadra("Juventus", "Torino", 22, 25, 3, 2, 10, 5)
    s4 = info_squadra("Roma", "Roma", 22, 25, 3, 2, 10, 5)
    s5 = info_squadra("Napoli", "Napoli", 22, 25, 3, 2, 10, 5)
    s6 = info_squadra("Lazio", "Roma", 22, 25, 3, 2, 10, 5)
    return s1, s2, s3, s4, s5, s6

def punti_squadra(squadra):
    #    Calcola i punti totali: vittorie * 3 + pareggi * 1.
    punti1 = squadra["vittorie"] * 3 + squadra["pareggi"] * 1
    return punti1

def differenza_reti(squadra):
    #    Calcola la differenza tra gol segnati e gol subiti.
    # diff1 = squadra(gol_segnati, gol_subiti)
    diff = squadra["gol_segnati"] - squadra["gol_subiti"]
    return diff

def aggiorna_statistiche(squadra, gol_segnati, gol_subiti):
#        Aggiorna i dati della squadra dopo una partita:
#    - Se `gol_fatti > gol_subiti`: +1 vittoria
#    - Se `gol_fatti == gol_subiti`: +1 pareggio
#    - Se `gol_fatti < gol_subiti`: +1 sconfitta
#    - Aggiorna gol segnati e subiti
    stats = squadra
    if squadra["gol_segnati"] > squadra["gol_subiti"]:
        squadra["vittorie"] + 1
    elif squadra["gol_segnati"] == squadra["gol_subiti"]:
        squadra["pareggi"] + 1
    elif squadra["gol_segnati"] < squadra["gol_subiti"]:
        squadra["sconfitte"] + 1



# print(differenza_reti)
# differenza_reti()

# print(differenza_reti(qualcosa))
print(aggiorna_statistiche(squadra, gol_segnati, gol_subiti))