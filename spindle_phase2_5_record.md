# Phase 2.5 Spindle Extraction Record

- Source: `text.txt` cleaned to plain text.
- Chunking: 360 words, stride 90 (overlapping co-visible approximation).
- Matching order: exact -> synonym -> fragment fallback.
- Includes all words in each source line (content + function words).
- Cursor policy: forward windows only; out-of-order word use inside same chunk is allowed.

## 01. I enter the city as question.
- Status: **good**
- Coverage exact+syn: 1.0 | with fragments: 1.0
- Counts: exact 5, syn 1, frag 0, miss 0
- Phrase hits: enter the, the city
- Chunk: `0` (words 0-359)
- Matches: i->i (exact), enter->enter (exact), the->the (exact), city->city (exact), as->as (exact), question->questions (syn)
- Chunk preview: Preface Great things must be silenced or talked about with grandeur that is with cynicism and innocence I would claim as property and product of man all the beauty nobility which we have given to real or imaginary things Frederic ...

## 02. Urban reality names me, then erases me.
- Status: **good**
- Coverage exact+syn: 0.43 | with fragments: 1.0
- Counts: exact 3, syn 0, frag 4, miss 0
- Phrase hits: urban reality
- Chunk: `3` (words 270-629)
- Matches: urban->urban (exact), reality->reality (exact), names->na+es (frag), me->me (frag), then->then (exact), erases->ses (frag), me->me (frag)
- Chunk preview: does not only propose to critically analyse thoughts and activities related to urbanism It s aim is to allow its problems to enter into consciousness and political policies From the theoretical and practical situation of problems from the problematic concerning ...

## 03. At the edge, I learn outside first.
- Status: **good**
- Coverage exact+syn: 0.57 | with fragments: 1.0
- Counts: exact 4, syn 0, frag 3, miss 0
- Phrase hits: at the
- Chunk: `18` (words 1620-1979)
- Matches: at->at (exact), the->the (exact), edge->ed+ge (frag), i->i (frag), learn->le (frag), outside->outside (exact), first->first (exact)
- Chunk preview: towards a sort of crystallization and fixation Where this system consolidated itself capitalism and industrialization came late in Germany in Italy a delay full of consequences There is therefore a certain discontinuity between an emerging industry and its historical conditions ...

## 04. Industrial days press against my breath.
- Status: **good**
- Coverage exact+syn: 0.17 | with fragments: 1.0
- Counts: exact 1, syn 0, frag 5, miss 0
- Phrase hits: none
- Chunk: `25` (words 2250-2609)
- Matches: industrial->industrial (exact), days->da+ys (frag), press->pr+ss (frag), against->nst (frag), my->my (frag), breath->bre+ath (frag)
- Chunk preview: city assaults it takes it ravages it It tends to break up the old cores by taking them over This does not prevent the extension of urban phenomena cities and agglomerations industrial towns and suburbs with the addition of shanty ...

## 05. I walk the induced streets.
- Status: **good**
- Coverage exact+syn: 0.4 | with fragments: 1.0
- Counts: exact 2, syn 0, frag 3, miss 0
- Phrase hits: none
- Chunk: `27` (words 2430-2789)
- Matches: i->i (frag), walk->wa (frag), the->the (exact), induced->induced (exact), streets->str (frag)
- Chunk preview: agglomeration which parallels it on the mainland Mestre This city among the most beautiful cities bequeathed to us from pre industrial times is threatened not so much by physical deterioration due to the sea or to its subsidence as by ...

## 06. Use value flickers under exchange.
- Status: **good**
- Coverage exact+syn: 0.8 | with fragments: 1.0
- Counts: exact 4, syn 0, frag 1, miss 0
- Phrase hits: use value
- Chunk: `36` (words 3240-3599)
- Matches: use->use (exact), value->value (exact), flickers->fli+ers (frag), under->under (exact), exchange->exchange (exact)
- Chunk preview: values The best known elements of the urban system of objects include water electricity gas butane in the countryside not to mention the car the television plastic utensils modern furniture which entail new demands with regard to services Among the ...

## 07. I keep what can be used, not sold.
- Status: **good**
- Coverage exact+syn: 0.75 | with fragments: 1.0
- Counts: exact 4, syn 2, frag 2, miss 0
- Phrase hits: can be
- Chunk: `40` (words 3600-3959)
- Matches: i->i (frag), keep->ep (frag), what->what (exact), can->can (exact), be->be (exact), used->use (syn), not->not (exact), sold->exchange (syn)
- Chunk preview: gives a dull and mutilated version of what was the core of the old city at one and the same time commercial religious intellectual political and economic productive The notion and image of the commercial centre in fact date from ...

## 08. The centre calls itself order.
- Status: **good**
- Coverage exact+syn: 0.6 | with fragments: 1.0
- Counts: exact 3, syn 0, frag 2, miss 0
- Phrase hits: the centre
- Chunk: `40` (words 3600-3959)
- Matches: the->the (exact), centre->centre (exact), calls->ca (frag), itself->itself (exact), order->or+er (frag)
- Chunk preview: gives a dull and mutilated version of what was the core of the old city at one and the same time commercial religious intellectual political and economic productive The notion and image of the commercial centre in fact date from ...

## 09. I answer with a minor rhythm.
- Status: **partial**
- Coverage exact+syn: 0.33 | with fragments: 0.83
- Counts: exact 2, syn 0, frag 3, miss 1
- Phrase hits: with a
- Chunk: `55` (words 4950-5309)
- Matches: i->i (frag), answer->ans+wer (frag), with->with (exact), a->a (exact), minor->or (frag), rhythm-> (miss)
- Chunk preview: the second half of the century influential people that is rich or powerful or both sometimes ideologues Le Play with ideas strongly marked by religions Catholic and Protestant sometimes informed politicians belonging to the centre right and who moreover do ...

## 10. Youth absorbs the city too fast.
- Status: **partial**
- Coverage exact+syn: 0.33 | with fragments: 0.83
- Counts: exact 2, syn 0, frag 3, miss 1
- Phrase hits: the city
- Chunk: `55` (words 4950-5309)
- Matches: youth->th (frag), absorbs->rbs (frag), the->the (exact), city->city (exact), too-> (miss), fast->st (frag)
- Chunk preview: the second half of the century influential people that is rich or powerful or both sometimes ideologues Le Play with ideas strongly marked by religions Catholic and Protestant sometimes informed politicians belonging to the centre right and who moreover do ...

## 11. I wear its signs, not its obedience.
- Status: **good**
- Coverage exact+syn: 0.43 | with fragments: 1.0
- Counts: exact 3, syn 0, frag 4, miss 0
- Phrase hits: none
- Chunk: `55` (words 4950-5309)
- Matches: i->i (frag), wear->we+ar (frag), its->its (exact), signs->si+ns (frag), not->not (exact), its->its (exact), obedience->nce (frag)
- Chunk preview: the second half of the century influential people that is rich or powerful or both sometimes ideologues Le Play with ideas strongly marked by religions Catholic and Protestant sometimes informed politicians belonging to the centre right and who moreover do ...

## 12. In the suburb I lose urban consciousness.
- Status: **good**
- Coverage exact+syn: 0.71 | with fragments: 1.0
- Counts: exact 4, syn 1, frag 2, miss 0
- Phrase hits: in the suburb, in the, the suburb
- Chunk: `65` (words 5850-6209)
- Matches: in->in (exact), the->the (exact), suburb->suburban (syn), i->i (frag), lose->lo+se (frag), urban->urban (exact), consciousness->consciousness (exact)
- Chunk preview: not necessarily become a public service It surfaces into social consciousness as a right It is acknowledged in fact by the indignation raised by dramatic cases and by the discontent engendered by the crisis Yet it is not formally or ...

## 13. In the core I return to encounter.
- Status: **good**
- Coverage exact+syn: 0.57 | with fragments: 1.0
- Counts: exact 3, syn 1, frag 3, miss 0
- Phrase hits: in the
- Chunk: `70` (words 6300-6659)
- Matches: in->in (exact), the->the (exact), core->co+re (frag), i->i (frag), return->ret (frag), to->to (exact), encounter->meeting (syn)
- Chunk preview: urban reality has disappeared streets squares monuments meeting places Even the cafe the bistro has encountered the resentment of the builders of those large housing estates their taste for asceticism the reduction of to inhabit to habitat They had to ...

## 14. Difference meets difference at speed.
- Status: **good**
- Coverage exact+syn: 0.2 | with fragments: 1.0
- Counts: exact 1, syn 0, frag 4, miss 0
- Phrase hits: none
- Chunk: `70` (words 6300-6659)
- Matches: difference->nce (frag), meets->me+ts (frag), difference->nce (frag), at->at (exact), speed->sp+ed (frag)
- Chunk preview: urban reality has disappeared streets squares monuments meeting places Even the cafe the bistro has encountered the resentment of the builders of those large housing estates their taste for asceticism the reduction of to inhabit to habitat They had to ...

## 15. I hear centrality before I see it.
- Status: **good**
- Coverage exact+syn: 0.57 | with fragments: 1.0
- Counts: exact 3, syn 1, frag 3, miss 0
- Phrase hits: none
- Chunk: `70` (words 6300-6659)
- Matches: i->i (frag), hear->he+ar (frag), centrality->centre (syn), before->before (exact), i->i (frag), see->see (exact), it->it (exact)
- Chunk preview: urban reality has disappeared streets squares monuments meeting places Even the cafe the bistro has encountered the resentment of the builders of those large housing estates their taste for asceticism the reduction of to inhabit to habitat They had to ...

## 16. The wall is text; the text is wall.
- Status: **good**
- Coverage exact+syn: 0.5 | with fragments: 1.0
- Counts: exact 4, syn 0, frag 4, miss 0
- Phrase hits: none
- Chunk: `70` (words 6300-6659)
- Matches: the->the (exact), wall->ll (frag), is->is (exact), text->te (frag), the->the (exact), text->te (frag), is->is (exact), wall->ll (frag)
- Chunk preview: urban reality has disappeared streets squares monuments meeting places Even the cafe the bistro has encountered the resentment of the builders of those large housing estates their taste for asceticism the reduction of to inhabit to habitat They had to ...

## 17. I read what was prescribed to me.
- Status: **good**
- Coverage exact+syn: 0.43 | with fragments: 1.0
- Counts: exact 3, syn 0, frag 4, miss 0
- Phrase hits: what was
- Chunk: `86` (words 7740-8099)
- Matches: i->i (frag), read->re+ad (frag), what->what (exact), was->was (exact), prescribed->pre (frag), to->to (exact), me->me (frag)
- Chunk preview: of a pencil drawing One can therefore identify the following The planning of men of good will architects and writers Their thinking and projects imply a certain philosophy Generally they associate themselves to an old classical and liberal humanism This ...

## 18. Then I write back in fragments.
- Status: **good**
- Coverage exact+syn: 0.5 | with fragments: 1.0
- Counts: exact 2, syn 1, frag 3, miss 0
- Phrase hits: none
- Chunk: `87` (words 7830-8189)
- Matches: then->then (exact), i->i (frag), write->te (frag), back->ba (frag), in->in (exact), fragments->fragmentary (syn)
- Chunk preview: reflection the village the community the neighbourhood the townsman citizen who will be endowed with civic buildings etc They want to build buildings and cities to the human scale to its measure without conceiving that in the modern world man ...

## 19. Near order / far order split my body.
- Status: **partial**
- Coverage exact+syn: 0.57 | with fragments: 0.71
- Counts: exact 2, syn 2, frag 1, miss 2
- Phrase hits: none
- Chunk: `96` (words 8640-8999)
- Matches: near->ne+ar (frag), order->order (exact), far-> (miss), order->order (exact), split->division (syn), my-> (miss), body->life (syn)
- Chunk preview: can now be emphasized In order to take up a radically critical analysis and to deepen the urban problematic philosophy will be the starting point This will come as a surprise And yet has not frequent reference to philosophy been ...

## 20. I become mediation among mediations.
- Status: **good**
- Coverage exact+syn: 0.4 | with fragments: 1.0
- Counts: exact 2, syn 0, frag 3, miss 0
- Phrase hits: none
- Chunk: `103` (words 9270-9629)
- Matches: i->i (frag), become->become (exact), mediation->mediation (exact), among->am+ng (frag), mediations->med+ons (frag)
- Chunk preview: directed towards product The countryside both practical reality and representation will carry images of nature of being of the innate The city will carry images of effort of will of subjectivity of contemplation without these representations becoming disjointed from real ...

## 21. Class strategy redraws my route.
- Status: **weak**
- Coverage exact+syn: 0.2 | with fragments: 0.6
- Counts: exact 1, syn 0, frag 2, miss 2
- Phrase hits: none
- Chunk: `118` (words 10620-10979)
- Matches: class->class (exact), strategy->str (frag), redraws-> (miss), my-> (miss), route->ro+te (frag)
- Chunk preview: which cements the edifice by crowning it Consequently in the modern State the philosophical system becomes real in Hegel s philosophy the real acknowledge the rational The system has a double side philosophical and political Hegel discovers the historical moment ...

## 22. I return where I was pushed out.
- Status: **partial**
- Coverage exact+syn: 0.14 | with fragments: 0.71
- Counts: exact 1, syn 0, frag 4, miss 2
- Phrase hits: none
- Chunk: `118` (words 10620-10979)
- Matches: i->i (frag), return-> (miss), where->wh+re (frag), i->i (frag), was->was (exact), pushed->hed (frag), out-> (miss)
- Chunk preview: which cements the edifice by crowning it Consequently in the modern State the philosophical system becomes real in Hegel s philosophy the real acknowledge the rational The system has a double side philosophical and political Hegel discovers the historical moment ...

## 23. The right appears as cry first.
- Status: **partial**
- Coverage exact+syn: 0.5 | with fragments: 0.83
- Counts: exact 3, syn 0, frag 2, miss 1
- Phrase hits: none
- Chunk: `119` (words 10710-11069)
- Matches: the->the (exact), right->right (exact), appears->app (frag), as->as (exact), cry-> (miss), first->fi+st (frag)
- Chunk preview: and a becoming of the world of philosophy An initial repercussion there can no longer be a divide between philosophy and reality historical social political A second repercussion the philosopher no longer has independence he accomplishes a public function as ...

## 24. Then demand, then practice.
- Status: **good**
- Coverage exact+syn: 0.75 | with fragments: 1.0
- Counts: exact 3, syn 0, frag 1, miss 0
- Phrase hits: none
- Chunk: `133` (words 11970-12329)
- Matches: then->then (exact), demand->and (frag), then->then (exact), practice->practice (exact)
- Chunk preview: to find the global reminds us strangely of philosophy when it is not openly philosophical On the ocher hand the partial offers more positive but scattered facts Is it possible to extract from fragmentary sciences a science of the city ...

## 25. Not habitat: to inhabit.
- Status: **partial**
- Coverage exact+syn: 0.5 | with fragments: 0.75
- Counts: exact 2, syn 0, frag 1, miss 1
- Phrase hits: none
- Chunk: `133` (words 11970-12329)
- Matches: not->not (exact), habitat->tat (frag), to->to (exact), inhabit-> (miss)
- Chunk preview: to find the global reminds us strangely of philosophy when it is not openly philosophical On the ocher hand the partial offers more positive but scattered facts Is it possible to extract from fragmentary sciences a science of the city ...

## 26. I refuse the logic of habitat.
- Status: **good**
- Coverage exact+syn: 0.33 | with fragments: 1.0
- Counts: exact 2, syn 0, frag 4, miss 0
- Phrase hits: none
- Chunk: `133` (words 11970-12329)
- Matches: i->i (frag), refuse->ref+use (frag), the->the (exact), logic->lo+ic (frag), of->of (exact), habitat->tat (frag)
- Chunk preview: to find the global reminds us strangely of philosophy when it is not openly philosophical On the ocher hand the partial offers more positive but scattered facts Is it possible to extract from fragmentary sciences a science of the city ...

## 27. I claim the plastic space of living.
- Status: **good**
- Coverage exact+syn: 0.57 | with fragments: 1.0
- Counts: exact 4, syn 0, frag 3, miss 0
- Phrase hits: none
- Chunk: `134` (words 12060-12419)
- Matches: i->i (frag), claim->claim (exact), the->the (exact), plastic->pla+tic (frag), space->space (exact), of->of (exact), living->ing (frag)
- Chunk preview: a series of correlations The subject is suppressed Or the continues to assert the existence of the global one approaches and locates it either by extrapolations in the name of a discipline or by wagering on an interdisciplinary tactic One ...

## 28. A cafe, a corner, a small centrality.
- Status: **good**
- Coverage exact+syn: 0.57 | with fragments: 1.0
- Counts: exact 3, syn 1, frag 3, miss 0
- Phrase hits: none
- Chunk: `144` (words 12960-13319)
- Matches: a->a (exact), cafe->ca+fe (frag), a->a (exact), corner->cor+ner (frag), a->a (exact), small->sm+ll (frag), centrality->centre (syn)
- Chunk preview: remains for a particular philosophy of the city the symbol of urban society in general This is a typically ideological extrapolation To this ideology these philosophers add partial knowledge this purely ideological operation consisting in a passage a leap from ...

## 29. A place consumed / a place reclaimed.
- Status: **good**
- Coverage exact+syn: 0.67 | with fragments: 1.0
- Counts: exact 4, syn 0, frag 2, miss 0
- Phrase hits: none
- Chunk: `154` (words 13860-14219)
- Matches: a->a (exact), place->place (exact), consumed->con+med (frag), a->a (exact), place->place (exact), reclaimed->rec+med (frag)
- Chunk preview: urban phenomena The city always had relations with society as a whole with its constituting elements countryside and agriculture offensive and defensive force political power States etc and with its history it changes when society as a whole changes Yet ...

## 30. The planner says coherence.
- Status: **good**
- Coverage exact+syn: 0.5 | with fragments: 1.0
- Counts: exact 1, syn 1, frag 2, miss 0
- Phrase hits: none
- Chunk: `166` (words 14940-15299)
- Matches: the->the (exact), planner->planning (syn), says->sa+ys (frag), coherence->nce (frag)
- Chunk preview: environment Social relations are achieved from the sensible They cannot be reduced to this sensible world and yet they do not float in air they do not disappear into transcendence If social reality suggests forms and relations if it cannot ...

## 31. I keep contradiction alive.
- Status: **good**
- Coverage exact+syn: 0.0 | with fragments: 1.0
- Counts: exact 0, syn 0, frag 4, miss 0
- Phrase hits: none
- Chunk: `166` (words 14940-15299)
- Matches: i->i (frag), keep->ep (frag), contradiction->con+ion (frag), alive->al+ve (frag)
- Chunk preview: environment Social relations are achieved from the sensible They cannot be reduced to this sensible world and yet they do not float in air they do not disappear into transcendence If social reality suggests forms and relations if it cannot ...

## 32. I move through isotopies and breaks.
- Status: **good**
- Coverage exact+syn: 0.5 | with fragments: 1.0
- Counts: exact 2, syn 1, frag 3, miss 0
- Phrase hits: none
- Chunk: `166` (words 14940-15299)
- Matches: i->i (frag), move->mo+ve (frag), through->through (exact), isotopies->iso+ies (frag), and->and (exact), breaks->discontinuities (syn)
- Chunk preview: environment Social relations are achieved from the sensible They cannot be reduced to this sensible world and yet they do not float in air they do not disappear into transcendence If social reality suggests forms and relations if it cannot ...

## 33. Meaning leaks at every border.
- Status: **good**
- Coverage exact+syn: 0.2 | with fragments: 1.0
- Counts: exact 1, syn 0, frag 4, miss 0
- Phrase hits: none
- Chunk: `181` (words 16290-16649)
- Matches: meaning->ing (frag), leaks->le (frag), at->at (exact), every->ev+ry (frag), border->der (frag)
- Chunk preview: persist in many small or medium sized towns Many urban centres which today perpetuate or protect the image of centrality which might have disappeared without them are of very ancient origins This can explain without inasmuch legitimizing the illusion of ...

## 34. Urban language stutters, then sings.
- Status: **good**
- Coverage exact+syn: 0.4 | with fragments: 1.0
- Counts: exact 2, syn 0, frag 3, miss 0
- Phrase hits: urban language
- Chunk: `183` (words 16470-16829)
- Matches: urban->urban (exact), language->language (exact), stutters->ers (frag), then->th+en (frag), sings->si (frag)
- Chunk preview: space reduced to a residential function to that of a commercial centrality which brought a difference an enrichment But planners were only rediscovering the medieval city laid bare of its historical relation to the countryside of the struggle between the ...

## 35. The system closes; I open.
- Status: **good**
- Coverage exact+syn: 0.4 | with fragments: 1.0
- Counts: exact 2, syn 0, frag 3, miss 0
- Phrase hits: none
- Chunk: `183` (words 16470-16829)
- Matches: the->the (exact), system->system (exact), closes->ses (frag), i->i (frag), open->op+en (frag)
- Chunk preview: space reduced to a residential function to that of a commercial centrality which brought a difference an enrichment But planners were only rediscovering the medieval city laid bare of its historical relation to the countryside of the struggle between the ...

## 36. The old core rots; desire persists.
- Status: **partial**
- Coverage exact+syn: 0.33 | with fragments: 0.83
- Counts: exact 2, syn 0, frag 3, miss 1
- Phrase hits: none
- Chunk: `191` (words 17190-17549)
- Matches: the->the (exact), old-> (miss), core->co+re (frag), rots->ro+ts (frag), desire->desire (exact), persists->per (frag)
- Chunk preview: ideology At this point the city should be defined If it is true that the concept emerges little by little from these ideologies which convey it it must be conceived during this progress We therefore here propose a first definition ...

## 37. I learn to occupy with care.
- Status: **good**
- Coverage exact+syn: 0.33 | with fragments: 1.0
- Counts: exact 2, syn 0, frag 4, miss 0
- Phrase hits: none
- Chunk: `202` (words 18180-18539)
- Matches: i->i (frag), learn->le (frag), to->to (exact), occupy->occ (frag), with->with (exact), care->ca+re (frag)
- Chunk preview: and at the specific level by the prefecture of police and also by neighbourhood police stations without forgetting various police agencies acting either at a global level or in the subterranean shadow Religious ideology is signified at the highest level ...

## 38. To occupy is to become legible.
- Status: **good**
- Coverage exact+syn: 0.67 | with fragments: 1.0
- Counts: exact 4, syn 0, frag 2, miss 0
- Phrase hits: none
- Chunk: `204` (words 18360-18719)
- Matches: to->to (exact), occupy->occ (frag), is->is (exact), to->to (exact), become->become (exact), legible->leg+ble (frag)
- Chunk preview: voids It is so true that habitat does not make up the city and that it cannot be defined by this isolated function At the ecological level habitation becomes essential The city envelops it it is form enveloping chis space ...

## 39. To become legible is danger.
- Status: **good**
- Coverage exact+syn: 0.6 | with fragments: 1.0
- Counts: exact 3, syn 0, frag 2, miss 0
- Phrase hits: none
- Chunk: `213` (words 19170-19529)
- Matches: to->to (exact), become->bec+ome (frag), legible->ble (frag), is->is (exact), danger->danger (exact)
- Chunk preview: This is not without a great naivety If it is true that a Bororo village signifies and that the Greek city is full of meaning are we to build vast Bororo villages full of signs of Modernity Or restore the ...

## 40. I blur, reappear, blur again.
- Status: **good**
- Coverage exact+syn: 0.0 | with fragments: 1.0
- Counts: exact 0, syn 0, frag 5, miss 0
- Phrase hits: none
- Chunk: `213` (words 19170-19529)
- Matches: i->i (frag), blur->bl+ur (frag), reappear->rea+ear (frag), blur->bl+ur (frag), again->ag+in (frag)
- Chunk preview: This is not without a great naivety If it is true that a Bororo village signifies and that the Greek city is full of meaning are we to build vast Bororo villages full of signs of Modernity Or restore the ...

## 41. Art is not ornament; it is claim.
- Status: **good**
- Coverage exact+syn: 0.71 | with fragments: 1.0
- Counts: exact 5, syn 0, frag 2, miss 0
- Phrase hits: is not, it is
- Chunk: `213` (words 19170-19529)
- Matches: art->art (exact), is->is (exact), not->not (exact), ornament->ent (frag), it->it (exact), is->is (exact), claim->cl+im (frag)
- Chunk preview: This is not without a great naivety If it is true that a Bororo village signifies and that the Greek city is full of meaning are we to build vast Bororo villages full of signs of Modernity Or restore the ...

## 42. A claim is a relation, not a logo.
- Status: **good**
- Coverage exact+syn: 0.75 | with fragments: 1.0
- Counts: exact 6, syn 0, frag 2, miss 0
- Phrase hits: not a
- Chunk: `223` (words 20070-20429)
- Matches: a->a (exact), claim->cl+im (frag), is->is (exact), a->a (exact), relation->relation (exact), not->not (exact), a->a (exact), logo->lo+go (frag)
- Chunk preview: and perceive themselves according to this coercive rationality At the same time and at the same stroke the sector of owner occupation becomes the reference by which habitat and daily life are appreciated that practice is cloaked in make believe ...

## 43. I gather others at the margin
- Status: **good**
- Coverage exact+syn: 0.5 | with fragments: 1.0
- Counts: exact 2, syn 1, frag 3, miss 0
- Phrase hits: at the
- Chunk: `224` (words 20160-20519)
- Matches: i->i (frag), gather->her (frag), others->groups (syn), at->at (exact), the->the (exact), margin->gin (frag)
- Chunk preview: towards a system of significations which they often call planning it is not impossible for analysts of urban reality grouping together their piecemeal facts to constitute a somewhat different system of significations that they can also baptize planning while they ...

## 44. Margins turn centre for a minute.
- Status: **good**
- Coverage exact+syn: 0.67 | with fragments: 1.0
- Counts: exact 3, syn 1, frag 2, miss 0
- Phrase hits: for a
- Chunk: `224` (words 20160-20519)
- Matches: margins->ins (frag), turn->turn (exact), centre->centrality (syn), for->for (exact), a->a (exact), minute->min+ute (frag)
- Chunk preview: towards a system of significations which they often call planning it is not impossible for analysts of urban reality grouping together their piecemeal facts to constitute a somewhat different system of significations that they can also baptize planning while they ...

## 45. In that minute, the city is ours.
- Status: **good**
- Coverage exact+syn: 0.86 | with fragments: 1.0
- Counts: exact 5, syn 1, frag 1, miss 0
- Phrase hits: the city
- Chunk: `241` (words 21690-22049)
- Matches: in->in (exact), that->that (exact), minute->moment (syn), the->the (exact), city->city (exact), is->is (exact), ours->ou+rs (frag)
- Chunk preview: market exchange value and a rising capitalism This critical point is located in Western Europe around the sixteenth century Soon it is the arrival of the industrial city with its implications emigration of dispossed and disaggregated peasant populations cowards the ...

## 46. Then power writes over us again.
- Status: **good**
- Coverage exact+syn: 0.5 | with fragments: 1.0
- Counts: exact 3, syn 0, frag 3, miss 0
- Phrase hits: none
- Chunk: `241` (words 21690-22049)
- Matches: then->then (exact), power->po+er (frag), writes->tes (frag), over->over (exact), us->us (exact), again->ag+in (frag)
- Chunk preview: market exchange value and a rising capitalism This critical point is located in Western Europe around the sixteenth century Soon it is the arrival of the industrial city with its implications emigration of dispossed and disaggregated peasant populations cowards the ...

## 47. We answer with another writing.
- Status: **good**
- Coverage exact+syn: 0.6 | with fragments: 1.0
- Counts: exact 3, syn 0, frag 2, miss 0
- Phrase hits: none
- Chunk: `244` (words 21960-22319)
- Matches: we->we (frag), answer->answer (exact), with->with (exact), another->another (exact), writing->ing (frag)
- Chunk preview: neighbourhood and thus the domain of the architect to the general level scale of land use planning planned industrial production global urbanization passing over the city and the urban Mediation is placed into parentheses and the specific level is omitted ...

## 48. Not final: urban becoming.
- Status: **good**
- Coverage exact+syn: 0.75 | with fragments: 1.0
- Counts: exact 3, syn 0, frag 1, miss 0
- Phrase hits: none
- Chunk: `244` (words 21960-22319)
- Matches: not->not (exact), final->fi+al (frag), urban->urban (exact), becoming->becoming (exact)
- Chunk preview: neighbourhood and thus the domain of the architect to the general level scale of land use planning planned industrial production global urbanization passing over the city and the urban Mediation is placed into parentheses and the specific level is omitted ...

## 49. Right as practice, not gift.
- Status: **good**
- Coverage exact+syn: 0.6 | with fragments: 1.0
- Counts: exact 2, syn 1, frag 2, miss 0
- Phrase hits: none
- Chunk: `246` (words 22140-22499)
- Matches: right->ri (frag), as->as (exact), practice->practical (syn), not->not (exact), gift->gi (frag)
- Chunk preview: to themselves that is communications which do not go through existing networks and through institutions namely at the inferior level the immediate relations and at the superior level the political relations resulting from knowledge The answer given to reformist continuism ...

## 50. Page for page: we still connect.
- Status: **good**
- Coverage exact+syn: 0.5 | with fragments: 1.0
- Counts: exact 3, syn 0, frag 3, miss 0
- Phrase hits: we still
- Chunk: `252` (words 22680-23039)
- Matches: page->pa+ge (frag), for->for (exact), page->pa+ge (frag), we->we (exact), still->still (exact), connect->con+ect (frag)
- Chunk preview: these urban freedoms very early on In Europe as elsewhere one cannot attribute only to the growth of cities or only to problems of traffic difficulties which are both different and comparable Here and there from one part or another ...
