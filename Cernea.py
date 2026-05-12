import matplotlib.pyplot as plt
import numpy as np

s1 = crea_squadra("Inter", "Milano", 23)
s2 = crea_squadra("Milan", "Milano", 22)
s3 = crea_squadra("Juventus", "Torino", 25)
s4 = crea_squadra("Roma", "Roma", 20)
s5 = crea_squadra("Napoli", "Napoli", 21)
s6 = crea_squadra("Lazio", "Roma", 19)

p1 = crea_partita("Milan", "Inter", 2, 1, "2026-04-01")
p2 = crea_partita("Juventus", "Roma", 3, 0, "2026-04-02")
p3 = crea_partita("Napoli", "Lazio", 2, 2, "2026-04-03")
p4 = crea_partita("Inter", "Juventus", 1, 1, "2026-04-08")
p5 = crea_partita("Milan", "Roma", 2, 0, "2026-04-09")
p6 = crea_partita("Napoli", "Juventus", 1, 2, "2026-04-10")
p7 = crea_partita("Milan", "Lazio", 3, 1, "2026-04-15")
p8 = crea_partita("Inter", "Napoli", 1, 1, "2026-04-16")

partite = [p1, p2, p3, p4, p5, p6, p7, p8]

for partita in partite:


plt.figure(10, 6)
plt.title("Classifiche Torneo - Punti per Squadra")
plt.plot()
plt.xlabel("Squadra")
plt.ylabel("Punti")
plt.grid(True)




plt.savefig("Istogramma_classifiche_torneo")
plt.show()