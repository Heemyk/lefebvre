import json
import re
from pathlib import Path

ROOT = Path(r"c:\Users\abk931\Desktop\lefebvre")
SRC = ROOT / "spindle_phase2_5_manual_curated.json"
TXT = (ROOT / "text.txt").read_text(encoding="utf-8")
rows = json.loads(SRC.read_text(encoding="utf-8"))

clean = re.sub(r"^#.*$", " ", TXT, flags=re.M)
clean = re.sub(r"<[^>]*>", " ", clean)
clean = re.sub(r"\*", " ", clean)
clean = re.sub(r"\s+", " ", clean).strip()

word_matches = list(re.finditer(r"[A-Za-z']+", clean))
WORDS = [
    {"w": m.group(0).lower(), "s": m.start(), "e": m.end()}
    for m in word_matches
]
WORD_MAP = {}
for w in WORDS:
    WORD_MAP.setdefault(w["w"], []).append(w)

WINDOW = 800

def norm(x):
    return re.sub(r"[^a-z']+", "", (x or "").lower())

def token_candidates(token, picked, mode):
    token = norm(token)
    picked = norm(picked)
    out = []
    seen = set()

    def add_word(word, m):
        if not word:
            return
        for w in WORD_MAP.get(word, []):
            key = (w["s"], w["e"])
            if key in seen:
                continue
            seen.add(key)
            out.append({
                "corpusStart": w["s"],
                "corpusEnd": w["e"],
                "matchedWord": w["w"],
                "mode": m,
            })

    # preference: explicit picked, token, then fragments.
    if mode in ("syn", "exact"):
        add_word(picked or token, mode)
        add_word(token, "exact" if mode == "exact" else "syn")
    else:
        add_word(token, "exact")
        add_word(picked, "syn")

    frag_sources = []
    if picked:
        frag_sources.append(picked)
    if token:
        frag_sources.append(token)
    frags = []
    for s in frag_sources:
        if len(s) >= 6:
            frags.extend([s[:3], s[-3:]])
        elif len(s) >= 4:
            frags.extend([s[:2], s[-2:]])
        elif s:
            frags.append(s)
    # fragment candidates from actual words containing the fragment.
    for f in frags:
        if len(f) < 2:
            continue
        for w in WORDS:
            if f in w["w"]:
                key = (w["s"], w["e"])
                if key in seen:
                    continue
                seen.add(key)
                out.append({
                    "corpusStart": w["s"],
                    "corpusEnd": w["e"],
                    "matchedWord": w["w"],
                    "mode": "frag",
                })
    return out[:220]

def solve_row(row):
    entries = row.get("matches", [])
    if not entries:
        return row

    per_token = []
    for m in entries:
        cands = token_candidates(m.get("token", ""), m.get("picked", ""), m.get("mode", ""))
        per_token.append((m, cands))

    all_positions = sorted({c["corpusStart"] for _, cs in per_token for c in cs})
    if not all_positions:
        return row

    best = None
    for left in all_positions:
        right = left + WINDOW
        used = set()
        chosen = []
        resolved = 0
        frags = 0
        misses = 0
        for m, cands in per_token:
            pick = None
            for c in cands:
                if not (left <= c["corpusStart"] <= right):
                    continue
                key = (c["corpusStart"], c["corpusEnd"])
                if key in used:
                    continue
                pick = c
                break
            if pick:
                used.add((pick["corpusStart"], pick["corpusEnd"]))
                mode = pick["mode"]
                if mode in ("exact", "syn"):
                    resolved += 1
                elif mode == "frag":
                    frags += 1
                chosen.append({
                    "token": m.get("token", ""),
                    "mode": mode,
                    "picked": pick["matchedWord"] if mode != "frag" else m.get("picked", "") or pick["matchedWord"],
                    "corpusStart": pick["corpusStart"],
                    "corpusEnd": pick["corpusEnd"],
                })
            else:
                misses += 1
                chosen.append({
                    "token": m.get("token", ""),
                    "mode": "miss",
                    "picked": "",
                    "corpusStart": None,
                    "corpusEnd": None,
                })
        score = (resolved * 5) + (frags * 2) - (misses * 9)
        cand = {
            "score": score,
            "resolved": resolved,
            "frags": frags,
            "misses": misses,
            "matches": chosen,
            "clusterStart": left,
            "clusterEnd": right,
        }
        if best is None or cand["score"] > best["score"]:
            best = cand
        if misses == 0:
            break

    out = dict(row)
    out["matches"] = best["matches"]
    total = max(1, len(best["matches"]))
    cov = round(best["resolved"] / total, 2)
    soft = round((best["resolved"] + best["frags"]) / total, 2)
    out["coverage"] = cov
    out["soft_coverage"] = soft
    out["resolved_count"] = best["resolved"]
    out["fragment_count"] = best["frags"]
    out["miss_count"] = best["misses"]
    out["clusterCharStart"] = best["clusterStart"]
    out["clusterCharEnd"] = best["clusterEnd"]
    out["clusterCharSpan"] = best["clusterEnd"] - best["clusterStart"]
    out["proximity800_resolved"] = best["misses"] == 0
    out["status"] = "good" if cov >= 0.7 else ("partial" if cov >= 0.45 else "weak")
    return out

new_rows = [solve_row(r) for r in rows]
(ROOT / "spindle_phase2_5_manual_curated.json").write_text(json.dumps(new_rows, indent=2), encoding="utf-8")
summary = {
    "total": len(new_rows),
    "all_tokens_resolved": sum(1 for r in new_rows if r.get("proximity800_resolved")),
    "avg_coverage": round(sum(r.get("coverage", 0) for r in new_rows) / max(1, len(new_rows)), 3),
    "avg_soft_coverage": round(sum(r.get("soft_coverage", 0) for r in new_rows) / max(1, len(new_rows)), 3),
    "max_span": max((r.get("clusterCharSpan", 0) for r in new_rows), default=0),
}
(ROOT / "spindle_phase2_5_manual_curated_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(summary)
