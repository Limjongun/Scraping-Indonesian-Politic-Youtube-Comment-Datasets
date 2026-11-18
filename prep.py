import pandas as pd, re

df = pd.read_json("komentar_prabowo.json", lines=True)
print(df.columns.tolist(), len(df))

# anonimkan: buang identitas penulis
df = df[["cid", "text", "time_parsed", "votes", "reply"]].copy()
df.rename(columns={"time_parsed": "timestamp"}, inplace=True)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s", errors="coerce")
df["votes"] = pd.to_numeric(df["votes"], errors="coerce").fillna(0).astype(int)
df.to_csv("komentar_raw.csv", index=False, encoding="utf-8-sig")

def clean(t):
    t = str(t)
    t = re.sub(r"https?://\S+", " ", t)      # URL
    t = re.sub(r"@[\w\-\.]+", " ", t)        # mention
    t = re.sub(r"\s+", " ", t).strip()
    return t

df["text_clean"] = df["text"].apply(clean)

# buang komentar kosong/terlalu pendek, duplikat, dan spam judi
spam = r"\b(slot|gacor|maxwin|togel|judol|jp\s?\d+|daftar sekarang|wa\.me)\b"
df = df[df["text_clean"].str.len() >= 3]
df = df[~df["text_clean"].str.contains(spam, case=False, regex=True)]
df = df.drop_duplicates(subset="text_clean")

df.to_csv("komentar_clean.csv", index=False, encoding="utf-8-sig")
print("setelah cleaning:", len(df))