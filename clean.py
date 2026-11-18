import json, csv, re, sys

src = sys.argv[1] if len(sys.argv) > 1 else "komentar_prabowo.json"
out_base = sys.argv[2] if len(sys.argv) > 2 else "komentar_utama"

def bersihkan(t):
    t = re.sub(r"https?://\S+", " ", t)   # URL dibuang dulu agar tidak jadi sisa kata
    t = re.sub(r"[\W_]+", " ", t)          # semua selain huruf/angka (tanda baca, emoji, simbol) -> spasi
    return re.sub(r"\s+", " ", t).strip()  # rapikan spasi dan baris baru

rows = []
with open(src, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        c = json.loads(line)
        if c.get("reply"):                 # buang balasan, simpan komentar utama
            continue
        teks = bersihkan(c["text"])
        if not teks:                       # komentar yang isinya cuma emoji/tanda baca
            continue
        rows.append({"username": c["author"], "komentar": teks})

with open(out_base + ".csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=["username", "komentar"])
    w.writeheader()
    w.writerows(rows)

with open(out_base + ".json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

print(f"{len(rows)} komentar utama disimpan ke {out_base}.csv dan {out_base}.json")