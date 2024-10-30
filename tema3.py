meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

cata_ceafa_era_la_inceput = meniu.count("ceafa")
cata_ceafa_s_a_comandat = comenzi.count("ceafa")
cati_papanasi_erau_la_inceput = meniu.count("papanasi")
cati_papanasi_s_au_comandat = comenzi.count("papanasi")
cat_guias_era_la_inceput = meniu.count("guias")
cat_guias_s_a_comandat = comenzi.count("guias")

stoc_tavi = len(tavi)

while studenti and comenzi:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    tava = tavi.pop(0)
    print(f"Studentul {student} a comandat {comanda}.")
    istoric_comenzi.append([student, comanda])

print(f"S-au comandat {cati_papanasi_s_au_comandat} papanasi, {cata_ceafa_s_a_comandat} ceafa si {cat_guias_s_a_comandat} guias.")

tavi_ramase = stoc_tavi - len(tavi)
print(f"Mai sunt {tavi_ramase} tavi.")

ceafa_ramasa = (cata_ceafa_era_la_inceput - cata_ceafa_s_a_comandat) > 0
papanasi_ramas = (cati_papanasi_erau_la_inceput - cati_papanasi_s_au_comandat) > 0
guias_ramas = (cat_guias_era_la_inceput - cat_guias_s_a_comandat) > 0

print(f"Mai este ceafa: {ceafa_ramasa}.\nMai sunt papanasi: {papanasi_ramas}.\nMai sunt guias: {guias_ramas}.")

