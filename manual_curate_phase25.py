import json
import re
from pathlib import Path

ROOT = Path(r"c:\Users\abk931\Desktop\lefebvre")
BASE = json.loads((ROOT / "spindle_phase2_record.json").read_text(encoding="utf-8"))
TXT = (ROOT / "text.txt").read_text(encoding="utf-8")

clean = re.sub(r"^#.*$", " ", TXT, flags=re.M)
clean = re.sub(r"<[^>]*>", " ", clean)
clean = re.sub(r"\*", " ", clean)
clean = re.sub(r"\s+", " ", clean).strip()
words = re.findall(r"[A-Za-z']+", clean)

chunk_size, stride = 360, 90
chunks = []
for i in range(0, max(1, len(words) - chunk_size + 1), stride):
    ww = words[i : i + chunk_size]
    if not ww:
        continue
    chunks.append(
        {
            "id": len(chunks),
            "start": i,
            "end": i + len(ww) - 1,
            "text": " ".join(ww),
            "set": set(w.lower() for w in ww),
        }
    )

# Manual hand-curation notes/overrides for weaker lines.
# - optional chunk: force a better semantic chunk within allowed k+1..k+5 range
# - token_map: ordered preferred substitutes for that token, manually chosen.
MANUAL = {
    3: {"token_map": {"edge": ["outside", "limits"], "learn": ["know", "understand"], "first": ["first"]}},
    4: {"token_map": {"days": ["daily", "day"], "press": ["pressure", "press"], "breath": ["life", "living"]}},
    5: {"token_map": {"walk": ["go", "move"], "induced": ["induced", "induction"]}},
    9: {"token_map": {"answer": ["response", "respond"], "minor": ["small", "minute"], "rhythm": ["time"]}},
    10: {"token_map": {"youth": ["young", "youth"], "absorbs": ["absorb", "assimilation"], "fast": ["rapid", "fast"]}},
    11: {"token_map": {"wear": ["carry", "wear"], "signs": ["sign", "signs"], "obedience": ["order", "discipline"]}},
    14: {"token_map": {"difference": ["difference", "differences"], "meets": ["encounter", "meets"], "speed": ["rapid"]}},
    15: {"token_map": {"hear": ["voice", "heard"], "before": ["before"], "see": ["see", "visible"]}},
    17: {"token_map": {"read": ["read", "reading"], "prescribed": ["inscribed", "prescription"]}},
    18: {"token_map": {"write": ["writing", "write"], "back": ["return", "back"], "fragments": ["fragmentary", "fragment"]}},
    19: {"token_map": {"near": ["near"], "far": ["far"], "split": ["division", "split"], "body": ["life", "body"]}},
    20: {"token_map": {"mediation": ["mediation", "mediations"], "among": ["among"]}},
    21: {"token_map": {"class": ["class"], "strategy": ["strategy"], "redraws": ["draw", "redraw"], "route": ["road", "path"]}},
    22: {"token_map": {"return": ["return"], "pushed": ["expelled", "pushed"], "out": ["out"]}},
    26: {"token_map": {"refuse": ["refusal", "reject"], "logic": ["logic", "rationality"], "habitat": ["habitat"]}},
    27: {"token_map": {"claim": ["right", "claim"], "plastic": ["plasticity"], "space": ["space"], "living": ["life"]}},
    31: {"token_map": {"keep": ["keep"], "contradiction": ["contradictions", "contradiction"], "alive": ["living", "life"]}},
    32: {"token_map": {"move": ["move"], "through": ["through"], "isotopies": ["isotopies", "isotopy"], "breaks": ["rupture", "break"]}},
    33: {"token_map": {"meaning": ["meaning", "signification"], "leaks": ["leak"], "border": ["boundaries", "borders"]}},
    34: {"token_map": {"language": ["language"], "stutters": ["stammer"], "sings": ["voice", "song"]}},
    35: {"token_map": {"closes": ["close", "closed"], "open": ["open", "opening"]}},
    36: {"token_map": {"rots": ["rotting", "decay"], "desire": ["desire"], "persists": ["persist", "survives"]}},
    37: {"token_map": {"learn": ["learn"], "occupy": ["occupy", "appropriation"], "care": ["care"]}},
    39: {"token_map": {"legible": ["legible", "legibility"], "danger": ["risk", "danger"]}},
    40: {"token_map": {"blur": ["veiled", "blur"], "reappear": ["return", "reappearance"], "again": ["again"]}},
    44: {"token_map": {"margins": ["margins", "margin"], "turn": ["turn"], "centre": ["centrality", "centre"], "minute": ["minute", "moment"]}},
    47: {"token_map": {"answer": ["response", "answer"], "another": ["another", "other"], "writing": ["writing", "written"]}},
    50: {"token_map": {"page": ["page", "book"], "connect": ["connections", "connect", "link"]}},
}

def token_list(line: str):
    return [t.lower() for t in re.findall(r"[A-Za-z']+", line)]

def pick_match(token: str, ch: dict, preferred: list[str]):
    if token in ch["set"]:
        return {"token": token, "mode": "exact", "picked": token}
    for alt in preferred:
        alt = alt.lower()
        if alt in ch["set"]:
            return {"token": token, "mode": "syn", "picked": alt}
    # keep loose fragment fallback so every sentence can still be composed.
    if len(token) >= 6:
        frags = [token[:3], token[-3:]]
    elif len(token) >= 4:
        frags = [token[:2], token[-2:]]
    else:
        frags = [token]
    lower_text = ch["text"].lower()
    got = [f for f in frags if f in lower_text]
    if got:
        return {"token": token, "mode": "frag", "picked": "+".join(got)}
    return {"token": token, "mode": "miss", "picked": ""}

base_by_id = {r["id"]: r for r in BASE}
curated = []
prev_chunk = 0
for row in BASE:
    idx = row["id"]
    line = row["line"]
    toks = token_list(line)

    lo = min(len(chunks), prev_chunk + 1)
    hi = min(len(chunks), lo + 5)
    if lo >= len(chunks):
        lo, hi = max(0, len(chunks) - 5), len(chunks)
    cands = chunks[lo:hi]

    forced = MANUAL.get(idx, {}).get("chunk")
    if forced is not None:
        best_chunk = next((c for c in cands if c["id"] == forced), cands[0])
    else:
        # keep previous selected chunk if it still fits the allowed window, else first candidate.
        current = row["chunk_id"]
        best_chunk = next((c for c in cands if c["id"] == current), cands[0])

    if idx not in MANUAL:
        # Preserve existing line exactly if not manually curated.
        preserved = dict(base_by_id[idx])
        preserved["manual_curated"] = False
        preserved["manual_note"] = "Preserved from phase2.5 auto record."
        curated.append(preserved)
        prev_chunk = preserved["chunk_id"]
        continue

    tmap = MANUAL[idx].get("token_map", {})
    matches = []
    for t in toks:
        pref = tmap.get(t, [])
        if t not in pref:
            pref = [t] + pref
        matches.append(pick_match(t, best_chunk, pref))

    resolved = sum(1 for m in matches if m["mode"] in ("exact", "syn"))
    frags = sum(1 for m in matches if m["mode"] == "frag")
    cov = round(resolved / max(1, len(toks)), 2)
    soft = round((resolved + frags) / max(1, len(toks)), 2)
    status = "good" if cov >= 0.70 else ("partial" if cov >= 0.45 else "weak")

    curated.append(
        {
            "id": idx,
            "line": line,
            "status": status,
            "coverage": cov,
            "soft_coverage": soft,
            "token_count": len(toks),
            "resolved_count": resolved,
            "fragment_count": frags,
            "chunk_id": best_chunk["id"],
            "chunk_words": [best_chunk["start"], best_chunk["end"]],
            "matches": matches,
            "preview": " ".join(best_chunk["text"].split()[:40]) + " ...",
            "manual_curated": idx in MANUAL,
            "manual_note": "Hand-curated token preferences applied." if idx in MANUAL else "Retained from best chronological chunk.",
        }
    )
    prev_chunk = best_chunk["id"]

(ROOT / "spindle_phase2_5_manual_curated.json").write_text(
    json.dumps(curated, indent=2), encoding="utf-8"
)

summary = {
    "good": sum(1 for r in curated if r["status"] == "good"),
    "partial": sum(1 for r in curated if r["status"] == "partial"),
    "weak": sum(1 for r in curated if r["status"] == "weak"),
    "avg_coverage": round(sum(r["coverage"] for r in curated) / len(curated), 3),
    "avg_soft_coverage": round(sum(r["soft_coverage"] for r in curated) / len(curated), 3),
}
(ROOT / "spindle_phase2_5_manual_curated_summary.json").write_text(
    json.dumps(summary, indent=2), encoding="utf-8"
)

print("Wrote spindle_phase2_5_manual_curated.json")
print(summary)
