# Phase 2.6 Strict Spindle Extraction

- Smaller windows: 220-word chunks, 55-word stride
- Chronology: each line searches only chunk k+1..k+5
- Priority: exact/syn first, minimize misses, cap fragments to 1 per line

## 01. I enter the city as question.
- Status: **partial** (coverage 0.83, miss 1, fragments 0)
- Chunk: `1` (55-274)
- Matches: i->∅ (miss), enter->enter (exact), the->the (exact), city->city (exact), as->as (exact), question->questions (syn)

## 02. Urban reality names me, then erases me.
- Status: **weak** (coverage 0.29, miss 4, fragments 1)
- Chunk: `5` (275-494)
- Matches: urban->urban (exact), reality->reality (exact), names->nam (frag), me->∅ (miss), then->∅ (miss), erases->∅ (miss), me->∅ (miss)

## 03. At the edge, I learn outside first.
- Status: **weak** (coverage 0.43, miss 4, fragments 0)
- Chunk: `8` (440-659)
- Matches: at->∅ (miss), the->the (exact), edge->outside (syn), i->∅ (miss), learn->∅ (miss), outside->outside (exact), first->∅ (miss)

## 04. Industrial days press against my breath.
- Status: **weak** (coverage 0.5, miss 2, fragments 1)
- Chunk: `9` (495-714)
- Matches: industrial->industrial (exact), days->∅ (miss), press->pre (frag), against->against (exact), my->∅ (miss), breath->life (syn)

## 05. I walk the induced streets.
- Status: **weak** (coverage 0.4, miss 2, fragments 1)
- Chunk: `12` (660-879)
- Matches: i->∅ (miss), walk->∅ (miss), the->the (exact), induced->ind (frag), streets->streets (exact)

## 06. Use value flickers under exchange.
- Status: **partial** (coverage 0.6, miss 1, fragments 1)
- Chunk: `13` (715-934)
- Matches: use->use (exact), value->value (exact), flickers->ers (frag), under->∅ (miss), exchange->exchange (exact)

## 07. I keep what can be used, not sold.
- Status: **partial** (coverage 0.62, miss 3, fragments 0)
- Chunk: `16` (880-1099)
- Matches: i->∅ (miss), keep->∅ (miss), what->what (exact), can->can (exact), be->be (exact), used->∅ (miss), not->not (exact), sold->exchange (syn)

## 08. The centre calls itself order.
- Status: **partial** (coverage 0.6, miss 1, fragments 1)
- Chunk: `17` (935-1154)
- Matches: the->the (exact), centre->centrality (syn), calls->cal (frag), itself->itself (exact), order->∅ (miss)

## 09. I answer with a minor rhythm.
- Status: **weak** (coverage 0.33, miss 3, fragments 1)
- Chunk: `18` (990-1209)
- Matches: i->∅ (miss), answer->ans (frag), with->with (exact), a->a (exact), minor->∅ (miss), rhythm->∅ (miss)

## 10. Youth absorbs the city too fast.
- Status: **weak** (coverage 0.33, miss 3, fragments 1)
- Chunk: `22` (1210-1429)
- Matches: youth->you (frag), absorbs->∅ (miss), the->the (exact), city->city (exact), too->∅ (miss), fast->∅ (miss)

## 11. I wear its signs, not its obedience.
- Status: **weak** (coverage 0.43, miss 3, fragments 1)
- Chunk: `24` (1320-1539)
- Matches: i->∅ (miss), wear->∅ (miss), its->its (exact), signs->∅ (miss), not->not (exact), its->its (exact), obedience->nce (frag)

## 12. In the suburb I lose urban consciousness.
- Status: **weak** (coverage 0.43, miss 3, fragments 1)
- Chunk: `25` (1375-1594)
- Matches: in->in (exact), the->the (exact), suburb->sub (frag), i->∅ (miss), lose->∅ (miss), urban->urban (exact), consciousness->∅ (miss)

## 13. In the core I return to encounter.
- Status: **weak** (coverage 0.43, miss 3, fragments 1)
- Chunk: `26` (1430-1649)
- Matches: in->in (exact), the->the (exact), core->∅ (miss), i->∅ (miss), return->∅ (miss), to->to (exact), encounter->enc (frag)

## 14. Difference meets difference at speed.
- Status: **weak** (coverage 0.2, miss 3, fragments 1)
- Chunk: `29` (1595-1814)
- Matches: difference->nce (frag), meets->∅ (miss), difference->∅ (miss), at->at (exact), speed->∅ (miss)

## 15. I hear centrality before I see it.
- Status: **weak** (coverage 0.29, miss 4, fragments 1)
- Chunk: `34` (1870-2089)
- Matches: i->∅ (miss), hear->∅ (miss), centrality->centrality (exact), before->ore (frag), i->∅ (miss), see->∅ (miss), it->it (exact)

## 16. The wall is text; the text is wall.
- Status: **weak** (coverage 0.5, miss 4, fragments 0)
- Chunk: `35` (1925-2144)
- Matches: the->the (exact), wall->∅ (miss), is->is (exact), text->∅ (miss), the->the (exact), text->∅ (miss), is->is (exact), wall->∅ (miss)

## 17. I read what was prescribed to me.
- Status: **weak** (coverage 0.29, miss 4, fragments 1)
- Chunk: `36` (1980-2199)
- Matches: i->∅ (miss), read->∅ (miss), what->∅ (miss), was->was (exact), prescribed->pre (frag), to->to (exact), me->∅ (miss)

## 18. Then I write back in fragments.
- Status: **weak** (coverage 0.33, miss 3, fragments 1)
- Chunk: `37` (2035-2254)
- Matches: then->∅ (miss), i->∅ (miss), write->∅ (miss), back->back (exact), in->in (exact), fragments->fra (frag)

## 19. Near order / far order split my body.
- Status: **weak** (coverage 0.29, miss 4, fragments 1)
- Chunk: `40` (2200-2419)
- Matches: near->∅ (miss), order->ord (frag), far->far (exact), order->∅ (miss), split->∅ (miss), my->∅ (miss), body->life (syn)

## 20. I become mediation among mediations.
- Status: **weak** (coverage 0.2, miss 3, fragments 1)
- Chunk: `41` (2255-2474)
- Matches: i->∅ (miss), become->ome (frag), mediation->∅ (miss), among->among (exact), mediations->∅ (miss)

## 21. Class strategy redraws my route.
- Status: **weak** (coverage 0.0, miss 4, fragments 1)
- Chunk: `42` (2310-2529)
- Matches: class->cla (frag), strategy->∅ (miss), redraws->∅ (miss), my->∅ (miss), route->∅ (miss)

## 22. I return where I was pushed out.
- Status: **weak** (coverage 0.14, miss 5, fragments 1)
- Chunk: `43` (2365-2584)
- Matches: i->∅ (miss), return->∅ (miss), where->∅ (miss), i->∅ (miss), was->∅ (miss), pushed->hed (frag), out->out (exact)

## 23. The right appears as cry first.
- Status: **weak** (coverage 0.33, miss 3, fragments 1)
- Chunk: `46` (2530-2749)
- Matches: the->the (exact), right->∅ (miss), appears->app (frag), as->as (exact), cry->∅ (miss), first->∅ (miss)

## 24. Then demand, then practice.
- Status: **weak** (coverage 0.0, miss 3, fragments 1)
- Chunk: `47` (2585-2804)
- Matches: then->∅ (miss), demand->and (frag), then->∅ (miss), practice->∅ (miss)

## 25. Not habitat: to inhabit.
- Status: **weak** (coverage 0.5, miss 1, fragments 1)
- Chunk: `50` (2750-2969)
- Matches: not->not (exact), habitat->tat (frag), to->to (exact), inhabit->∅ (miss)

## 26. I refuse the logic of habitat.
- Status: **weak** (coverage 0.33, miss 3, fragments 1)
- Chunk: `51` (2805-3024)
- Matches: i->∅ (miss), refuse->∅ (miss), the->the (exact), logic->log (frag), of->of (exact), habitat->∅ (miss)

## 27. I claim the plastic space of living.
- Status: **partial** (coverage 0.71, miss 2, fragments 0)
- Chunk: `56` (3080-3299)
- Matches: i->∅ (miss), claim->∅ (miss), the->the (exact), plastic->plastic (exact), space->spaces (syn), of->of (exact), living->living (exact)

## 28. A cafe, a corner, a small centrality.
- Status: **partial** (coverage 0.57, miss 2, fragments 1)
- Chunk: `61` (3355-3574)
- Matches: a->a (exact), cafe->∅ (miss), a->a (exact), corner->cor (frag), a->a (exact), small->∅ (miss), centrality->core (syn)

## 29. A place consumed / a place reclaimed.
- Status: **good** (coverage 1.0, miss 0, fragments 0)
- Chunk: `62` (3410-3629)
- Matches: a->a (exact), place->place (exact), consumed->consumption (syn), a->a (exact), place->place (exact), reclaimed->appropriated (syn)

## 30. The planner says coherence.
- Status: **weak** (coverage 0.25, miss 2, fragments 1)
- Chunk: `63` (3465-3684)
- Matches: the->the (exact), planner->pla (frag), says->∅ (miss), coherence->∅ (miss)

## 31. I keep contradiction alive.
- Status: **weak** (coverage 0.0, miss 3, fragments 1)
- Chunk: `64` (3520-3739)
- Matches: i->∅ (miss), keep->∅ (miss), contradiction->con (frag), alive->∅ (miss)

## 32. I move through isotopies and breaks.
- Status: **weak** (coverage 0.33, miss 3, fragments 1)
- Chunk: `67` (3685-3904)
- Matches: i->∅ (miss), move->∅ (miss), through->through (exact), isotopies->ies (frag), and->and (exact), breaks->∅ (miss)

## 33. Meaning leaks at every border.
- Status: **weak** (coverage 0.2, miss 3, fragments 1)
- Chunk: `68` (3740-3959)
- Matches: meaning->mea (frag), leaks->∅ (miss), at->at (exact), every->∅ (miss), border->∅ (miss)

## 34. Urban language stutters, then sings.
- Status: **weak** (coverage 0.2, miss 3, fragments 1)
- Chunk: `72` (3960-4179)
- Matches: urban->urban (exact), language->age (frag), stutters->∅ (miss), then->∅ (miss), sings->∅ (miss)

## 35. The system closes; I open.
- Status: **weak** (coverage 0.2, miss 3, fragments 1)
- Chunk: `73` (4015-4234)
- Matches: the->the (exact), system->tem (frag), closes->∅ (miss), i->∅ (miss), open->∅ (miss)

## 36. The old core rots; desire persists.
- Status: **weak** (coverage 0.17, miss 4, fragments 1)
- Chunk: `76` (4180-4399)
- Matches: the->the (exact), old->∅ (miss), core->∅ (miss), rots->∅ (miss), desire->des (frag), persists->∅ (miss)

## 37. I learn to occupy with care.
- Status: **weak** (coverage 0.5, miss 3, fragments 0)
- Chunk: `77` (4235-4454)
- Matches: i->∅ (miss), learn->∅ (miss), to->to (exact), occupy->occupy (exact), with->with (exact), care->∅ (miss)

## 38. To occupy is to become legible.
- Status: **good** (coverage 0.83, miss 0, fragments 1)
- Chunk: `78` (4290-4509)
- Matches: to->to (exact), occupy->occupy (exact), is->is (exact), to->to (exact), become->ome (frag), legible->legible (exact)

## 39. To become legible is danger.
- Status: **partial** (coverage 0.6, miss 1, fragments 1)
- Chunk: `79` (4345-4564)
- Matches: to->to (exact), become->bec (frag), legible->∅ (miss), is->is (exact), danger->danger (exact)

## 40. I blur, reappear, blur again.
- Status: **weak** (coverage 0.0, miss 4, fragments 1)
- Chunk: `80` (4400-4619)
- Matches: i->∅ (miss), blur->∅ (miss), reappear->rea (frag), blur->∅ (miss), again->∅ (miss)

## 41. Art is not ornament; it is claim.
- Status: **partial** (coverage 0.57, miss 2, fragments 1)
- Chunk: `81` (4455-4674)
- Matches: art->∅ (miss), is->is (exact), not->not (exact), ornament->ent (frag), it->it (exact), is->is (exact), claim->∅ (miss)

## 42. A claim is a relation, not a logo.
- Status: **partial** (coverage 0.62, miss 2, fragments 1)
- Chunk: `82` (4510-4729)
- Matches: a->a (exact), claim->cla (frag), is->is (exact), a->a (exact), relation->∅ (miss), not->not (exact), a->a (exact), logo->∅ (miss)

## 43. I gather others at the margin
- Status: **weak** (coverage 0.5, miss 2, fragments 1)
- Chunk: `87` (4785-5004)
- Matches: i->∅ (miss), gather->her (frag), others->people (syn), at->∅ (miss), the->the (exact), margin->outskirts (syn)

## 44. Margins turn centre for a minute.
- Status: **weak** (coverage 0.5, miss 2, fragments 1)
- Chunk: `89` (4895-5114)
- Matches: margins->mar (frag), turn->∅ (miss), centre->centre (exact), for->for (exact), a->a (exact), minute->∅ (miss)

## 45. In that minute, the city is ours.
- Status: **partial** (coverage 0.71, miss 1, fragments 1)
- Chunk: `90` (4950-5169)
- Matches: in->in (exact), that->that (exact), minute->ute (frag), the->the (exact), city->city (exact), is->is (exact), ours->∅ (miss)

## 46. Then power writes over us again.
- Status: **weak** (coverage 0.33, miss 4, fragments 0)
- Chunk: `91` (5005-5224)
- Matches: then->then (exact), power->∅ (miss), writes->∅ (miss), over->over (exact), us->∅ (miss), again->∅ (miss)

## 47. We answer with another writing.
- Status: **weak** (coverage 0.4, miss 2, fragments 1)
- Chunk: `94` (5170-5389)
- Matches: we->∅ (miss), answer->ans (frag), with->with (exact), another->another (exact), writing->∅ (miss)

## 48. Not final: urban becoming.
- Status: **weak** (coverage 0.5, miss 1, fragments 1)
- Chunk: `95` (5225-5444)
- Matches: not->not (exact), final->final (exact), urban->∅ (miss), becoming->ing (frag)

## 49. Right as practice, not gift.
- Status: **weak** (coverage 0.2, miss 3, fragments 1)
- Chunk: `96` (5280-5499)
- Matches: right->∅ (miss), as->∅ (miss), practice->pra (frag), not->not (exact), gift->∅ (miss)

## 50. Page for page: we still connect.
- Status: **weak** (coverage 0.33, miss 3, fragments 1)
- Chunk: `99` (5445-5664)
- Matches: page->∅ (miss), for->for (exact), page->∅ (miss), we->∅ (miss), still->still (exact), connect->con (frag)
