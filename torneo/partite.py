from .squadre import aggiorna_statistiche

def crea_partita(squadra1, squadra2, gol1, gol2, data):
    p1 = crea_partita("Milan", "Inter", 2, 1, "2026-04-01")
    p2 = crea_partita("Juventus", "Roma", 3, 0, "2026-04-02")
    p3 = crea_partita("Napoli", "Lazio", 2, 2, "2026-04-03")
    p4 = crea_partita("Inter", "Juventus", 1, 1, "2026-04-08")
    p5 = crea_partita("Milan", "Roma", 2, 0, "2026-04-09")
    p6 = crea_partita("Napoli", "Juventus", 1, 2, "2026-04-10")
    p7 = crea_partita("Milan", "Lazio", 3, 1, "2026-04-15")
    p8 = crea_partita("Inter", "Napoli", 1, 1, "2026-04-16")
    return p1, p2, p3, p4, p5, p6, p7, p8

