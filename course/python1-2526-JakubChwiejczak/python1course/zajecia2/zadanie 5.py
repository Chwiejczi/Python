import json

with open("teksty.json", encoding="utf-8") as file:
    plik = json.load(file)

teksty = str(plik["teksty"])
teksty = (
    teksty.replace("[", "")
    .replace("]", "")
    .replace("{", "")
    .replace("}", "")
    .replace(":", "")
    .replace("'tekst1'", "")
    .replace("'tekst2'", "")
    .replace("'tekst3'", "")
    .replace("'tekst4'", "")
    .replace("'tekst5'", "")
)
teksty = teksty.lower()
teksty = teksty.split()
for i in range(len(teksty)):
    teksty[i] = teksty[i].replace(".", "").replace(",", "")
    teksty[i] = teksty[i][0].upper() + teksty[i][1:-1] + teksty[i][-1].upper()
teksty = [slowo for slowo in teksty if "a" in slowo.lower()]
# zrobione w ten sposob, bo slowniki nie moga miec zduplikowanych kluczy
tekstyKlucze = list(dict.fromkeys(teksty))

wystapienia = {}
for slowo in tekstyKlucze:
    wystapienia[slowo] = teksty.count(slowo)


with open("teksty.json", "w", encoding="utf-8") as file:
    json.dump(wystapienia, file, ensure_ascii=False, indent=4)
    json.dump(tekstyKlucze, file, ensure_ascii=False, indent=4)
    json.dump(teksty, file, ensure_ascii=False, indent=4)
