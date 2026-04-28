import json
import re
from pathlib import Path

root = Path(r"c:\Users\abk931\Desktop\lefebvre")
data = json.loads((root / "spindle_phase2_record.json").read_text(encoding="utf-8"))
txt = (root / "text.txt").read_text(encoding="utf-8")
clean = re.sub(r"^#.*$", " ", txt, flags=re.M)
clean = re.sub(r"<[^>]*>", " ", clean)
clean = re.sub(r"\*", " ", clean)
clean = re.sub(r"\s+", " ", clean).strip()
words = re.findall(r"[A-Za-z']+", clean)

chunk_size, stride = 360, 90
chunks = []
for i in range(0, max(1, len(words) - chunk_size + 1), stride):
    w = words[i : i + chunk_size]
    if w:
        chunks.append(
            {
                "id": len(chunks),
                "start": i,
                "end": i + len(w) - 1,
                "set": set(x.lower() for x in w),
                "text": " ".join(w),
            }
        )

prev = 0
for r in data:
    line_id = r["id"]
    tokens = [t.lower() for t in re.findall(r"[A-Za-z']+", r["line"])]
    lo = min(len(chunks), prev + 1)
    hi = min(len(chunks), lo + 5)
    if lo >= len(chunks):
        lo, hi = max(0, len(chunks) - 5), len(chunks)
    cands = chunks[lo:hi]
    if r["status"] != "good":
        print(f"Line {line_id:02d} {r['status']} current chunk {r['chunk_id']}")
        for ch in cands:
            ex = sum(1 for t in tokens if t in ch["set"])
            print(f"  chunk {ch['id']}: exact {ex}/{len(tokens)} :: {' '.join(ch['text'].split()[:18])} ...")
    prev = r["chunk_id"]
