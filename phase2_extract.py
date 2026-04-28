import json
import re
from pathlib import Path

ROOT = Path(r"c:\Users\abk931\Desktop\lefebvre")
TXT = (ROOT / "text.txt").read_text(encoding="utf-8")

LINES = [
    "I enter the city as question.",
    "Urban reality names me, then erases me.",
    "At the edge, I learn outside first.",
    "Industrial days press against my breath.",
    "I walk the induced streets.",
    "Use value flickers under exchange.",
    "I keep what can be used, not sold.",
    "The centre calls itself order.",
    "I answer with a minor rhythm.",
    "Youth absorbs the city too fast.",
    "I wear its signs, not its obedience.",
    "In the suburb I lose urban consciousness.",
    "In the core I return to encounter.",
    "Difference meets difference at speed.",
    "I hear centrality before I see it.",
    "The wall is text; the text is wall.",
    "I read what was prescribed to me.",
    "Then I write back in fragments.",
    "Near order / far order split my body.",
    "I become mediation among mediations.",
    "Class strategy redraws my route.",
    "I return where I was pushed out.",
    "The right appears as cry first.",
    "Then demand, then practice.",
    "Not habitat: to inhabit.",
    "I refuse the logic of habitat.",
    "I claim the plastic space of living.",
    "A cafe, a corner, a small centrality.",
    "A place consumed / a place reclaimed.",
    "The planner says coherence.",
    "I keep contradiction alive.",
    "I move through isotopies and breaks.",
    "Meaning leaks at every border.",
    "Urban language stutters, then sings.",
    "The system closes; I open.",
    "The old core rots; desire persists.",
    "I learn to occupy with care.",
    "To occupy is to become legible.",
    "To become legible is danger.",
    "I blur, reappear, blur again.",
    "Art is not ornament; it is claim.",
    "A claim is a relation, not a logo.",
    "I gather others at the margin",
    "Margins turn centre for a minute.",
    "In that minute, the city is ours.",
    "Then power writes over us again.",
    "We answer with another writing.",
    "Not final: urban becoming.",
    "Right as practice, not gift.",
    "Page for page: we still connect.",
]

SYN = {
    "question":["problem","questions"], "erases":["destroy","disappear"], "outside":["outskirts","edge","periphery"],
    "streets":["street"], "used":["use","useful"], "sold":["exchange","value"], "centre":["center","centrality","core"],
    "rhythm":["time","daily"], "suburb":["suburbs","suburban"], "consciousness":["awareness"],
    "encounter":["meeting","meetings"], "difference":["differences"], "speed":["fast","rapid"], "centrality":["centre","core"],
    "wall":["walls"], "text":["writing","written"], "prescribed":["inscribed"], "fragments":["fragmentary"],
    "split":["division"], "body":["life"], "mediation":["mediations"], "route":["road","path","streets"],
    "cry":["demand"], "practice":["practical"], "inhabit":["inhabiting"], "plastic":["plasticity"],
    "space":["spatial","spaces"], "living":["life"], "cafe":["bistro"], "consumed":["consumption"],
    "reclaimed":["reconstitution"], "planner":["planning"], "contradiction":["contradictions"],
    "isotopies":["isotopy"], "breaks":["rupture","discontinuities"], "meaning":["signification"],
    "border":["boundaries","borders"], "language":["logos"], "stutters":["stammer"], "sings":["heard"],
    "closes":["close"], "open":["opening"], "rots":["rotting"], "persists":["survives"], "occupy":["appropriation"],
    "legible":["legibility"], "danger":["dangers"], "blur":["veiled"], "reappear":["return"], "art":["oeuvre"],
    "ornament":["ornamentation"], "claim":["right"], "relation":["relations"], "logo":["logos"], "gather":["gathering"],
    "others":["groups","people"], "margin":["margins","outskirts"], "minute":["moment"], "ours":["our"],
    "writes":["writing","write","inscribed"], "final":["ending"], "becoming":["becoming"], "gift":["granted"],
    "page":["book"], "connect":["connections"]
}

# Per-line manual boosts for phase 2.5 (index is 1-based line id).
LINE_SYN = {
    2: {"names": ["called", "name"], "erases": ["erased", "erase", "efface"]},
    4: {"breath": ["life", "living", "body"]},
    5: {"walk": ["go", "move"], "induced": ["induction", "induced"]},
    9: {"minor": ["small", "minute"], "rhythm": ["time", "times"]},
    11: {"obedience": ["order", "ordered", "discipline"]},
    14: {"speed": ["rapid", "fast", "quick"]},
    17: {"prescribed": ["inscribed", "prescription"]},
    18: {"fragments": ["fragment", "fragmentary"]},
    21: {"redraws": ["draw", "drawn", "redraw"], "route": ["road", "path"]},
    22: {"pushed": ["expelled", "excluded", "pushed"]},
    27: {"plastic": ["plasticity"], "living": ["life"]},
    29: {"reclaimed": ["reclaim", "reappropriated", "appropriated"]},
    31: {"alive": ["life", "living"]},
    32: {"breaks": ["rupture", "break", "fracture"]},
    34: {"stutters": ["stammer", "hesitate"], "sings": ["song", "voice"]},
    36: {"rots": ["rotting", "decay"], "persists": ["persist", "survives"]},
    39: {"danger": ["risk", "dangers"]},
    40: {"reappear": ["return", "reappearance"]},
    42: {"logo": ["logos", "sign"]},
    44: {"minute": ["moment"]},
    49: {"gift": ["given", "granted"]},
    50: {"connect": ["connection", "connections", "link"]},
}

def toks(s: str):
    # Phase 2.5 requirement: match every word in each line, including function words.
    return [t for t in re.findall(r"[A-Za-z']+", s.lower())]

def clean_text(s: str):
    s = re.sub(r"^#.*$", " ", s, flags=re.M)
    s = re.sub(r"<[^>]*>", " ", s)
    s = re.sub(r"\*", " ", s)
    return re.sub(r"\s+", " ", s).strip()

words = re.findall(r"[A-Za-z']+", clean_text(TXT))
chunk_size, stride = 360, 90
chunks = []
for i in range(0, max(1, len(words) - chunk_size + 1), stride):
    chunk_words = words[i : i + chunk_size]
    if chunk_words:
        chunks.append({"id": len(chunks), "start": i, "end": i + len(chunk_words) - 1, "text": " ".join(chunk_words), "set": set(w.lower() for w in chunk_words)})

cursor = 0
results = []
for idx, line in enumerate(LINES, 1):
    tt = toks(line)
    # Chronological constraint (phase 2.5): search only k+1..k+5.
    lo = min(len(chunks), cursor + 1)
    hi = min(len(chunks), lo + 5)
    if lo >= len(chunks):
        lo = max(0, len(chunks) - 5)
        hi = len(chunks)
    cands = chunks[lo:hi]
    best = None
    best_score = -1
    best_hits = []
    for ch in cands:
        hits, score = [], 0
        lower_text = ch["text"].lower()
        for t in tt:
            if t in ch["set"]:
                hits.append((t, "exact", t)); score += 3; continue
            found = False
            local_syn = list(SYN.get(t, []))
            local_syn.extend(LINE_SYN.get(idx, {}).get(t, []))
            for s in local_syn:
                if s in ch["set"]:
                    hits.append((t, "syn", s)); score += 2; found = True; break
            if found:
                continue
            frags = [t[:3], t[-3:]] if len(t) >= 6 else ([t[:2], t[-2:]] if len(t) >= 4 else [t])
            present = [f for f in frags if f in lower_text]
            if present:
                hits.append((t, "frag", "+".join(present))); score += 1
            else:
                hits.append((t, "miss", ""))
        if score > best_score:
            best, best_score, best_hits = ch, score, hits
        elif score == best_score and best is not None:
            # Tie-break toward stronger exact/syn ratio for manual quality.
            cur_resolved = sum(1 for _, m, _ in hits if m in ("exact", "syn"))
            best_resolved = sum(1 for _, m, _ in best_hits if m in ("exact", "syn"))
            if cur_resolved > best_resolved:
                best, best_hits = ch, hits
    solved = sum(1 for _, m, _ in best_hits if m in ("exact", "syn"))
    softened = sum(1 for _, m, _ in best_hits if m == "frag")
    coverage = round(solved / max(1, len(tt)), 2)
    soft_coverage = round((solved + softened) / max(1, len(tt)), 2)
    status = "good" if coverage >= 0.70 else ("partial" if coverage >= 0.45 else "weak")
    results.append({
        "id": idx, "line": line, "status": status, "coverage": coverage,
        "soft_coverage": soft_coverage,
        "token_count": len(tt),
        "resolved_count": solved,
        "fragment_count": softened,
        "chunk_id": best["id"], "chunk_words": [best["start"], best["end"]],
        "matches": [{"token": a, "mode": b, "picked": c} for a, b, c in best_hits],
        "preview": " ".join(best["text"].split()[:40]) + " ..."
    })
    cursor = best["id"]

md = [
    "# Phase 2 Spindle Extraction Record",
    "",
    "- Source: `text.txt` cleaned to plain text.",
    f"- Chunking: {chunk_size} words, stride {stride} (overlapping co-visible approximation).",
    "- Matching order: exact -> synonym -> fragment fallback.",
    "- Cursor policy: strict chronological progression; for line n, search only chunks k+1..k+5 where k is previous selected chunk.",
    "- Fallback policy: if none of the 5 chunks are strong, choose best scoring chunk among those same 5.",
    "",
]
for r in results:
    mm = ", ".join(f"{m['token']}->{m['picked'] or '∅'} ({m['mode']})" for m in r["matches"])
    md += [
        f"## {r['id']:02d}. {r['line']}",
        f"- Status: **{r['status']}** (exact+syn coverage {r['coverage']}, with fragments {r['soft_coverage']})",
        f"- Resolution: {r['resolved_count']}/{r['token_count']} exact-or-syn, {r['fragment_count']} fragment",
        f"- Chunk: `{r['chunk_id']}` (words {r['chunk_words'][0]}-{r['chunk_words'][1]})",
        f"- Matches: {mm}",
        f"- Chunk preview: {r['preview']}",
        "",
    ]

(ROOT / "spindle_phase2_record.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
(ROOT / "spindle_phase2_record.md").write_text("\n".join(md), encoding="utf-8")
print(f"Wrote {len(results)} spindle records.")
