# Phase 2 Spindle Extraction Record

- Source: `text.txt` cleaned to plain text.
- Chunking: 360 words, stride 90 (overlapping co-visible approximation).
- Matching order: exact -> synonym -> fragment fallback.
- Cursor policy: strict chronological progression; for line n, search only chunks k+1..k+5 where k is previous selected chunk.
- Fallback policy: if none of the 5 chunks are strong, choose best scoring chunk among those same 5.

## 01. I enter the city as question.
- Status: **good** (exact+syn coverage 0.83, with fragments 1.0)
- Resolution: 5/6 exact-or-syn, 1 fragment
- Chunk: `1` (words 90-449)
- Matches: i->i (frag), enter->enter (exact), the->the (exact), city->city (exact), as->as (exact), question->questions (syn)
- Chunk preview: System is fashionable as much in thought as in terminologies and language Now all systems tend to close off reflection to block off horizon This work wants to break up systems not to substitute another system but to open up ...

## 02. Urban reality names me, then erases me.
- Status: **partial** (exact+syn coverage 0.57, with fragments 1.0)
- Resolution: 4/7 exact-or-syn, 3 fragment
- Chunk: `3` (words 270-629)
- Matches: urban->urban (exact), reality->reality (exact), names->called (syn), me->me (frag), then->then (exact), erases->ses (frag), me->me (frag)
- Chunk preview: does not only propose to critically analyse thoughts and activities related to urbanism It s aim is to allow its problems to enter into consciousness and political policies From the theoretical and practical situation of problems from the problematic concerning ...

## 03. At the edge, I learn outside first.
- Status: **weak** (exact+syn coverage 0.43, with fragments 1.0)
- Resolution: 3/7 exact-or-syn, 4 fragment
- Chunk: `6` (words 540-899)
- Matches: at->at (exact), the->the (exact), edge->ed+ge (frag), i->i (frag), learn->le+rn (frag), outside->outside (exact), first->fi+st (frag)
- Chunk preview: eminent urban creations the most beautiful oeuvres of urban life we say beautiful because they are oeuvres rather than products date from epochs previous to that of industrialization There was the oriental city linked to the Asiatic mode of production ...

## 04. Industrial days press against my breath.
- Status: **weak** (exact+syn coverage 0.33, with fragments 0.83)
- Resolution: 2/6 exact-or-syn, 3 fragment
- Chunk: `7` (words 630-989)
- Matches: industrial->industrial (exact), days->da (frag), press->pr+ss (frag), against->aga (frag), my->∅ (miss), breath->life (syn)
- Chunk preview: to commerce crafts and banking It absorbed merchants who had previously been quasi nomadic and relegated outside the city When industrialization begins and capitalism in competition with a specifically industrial bourgeoisie is born the city is already a powerful reality ...

## 05. I walk the induced streets.
- Status: **weak** (exact+syn coverage 0.4, with fragments 1.0)
- Resolution: 2/5 exact-or-syn, 3 fragment
- Chunk: `8` (words 720-1079)
- Matches: i->i (frag), walk->wa (frag), the->the (exact), induced->ind+ced (frag), streets->streets (exact)
- Chunk preview: for what remained of exchange economies maintained by wandering merchants From the growing surplus product of agriculture to the detriment of feudal lords cities accumulate riches objects treasures virtual capitals There already existed in these urban centres a great monetary ...

## 06. Use value flickers under exchange.
- Status: **partial** (exact+syn coverage 0.6, with fragments 1.0)
- Resolution: 3/5 exact-or-syn, 2 fragment
- Chunk: `9` (words 810-1169)
- Matches: use->use (exact), value->value (exact), flickers->ers (frag), under->un+er (frag), exchange->exchange (exact)
- Chunk preview: techniques and oeuvres works of art monuments This city is itself oeuvre a feature which contrasts with the irreversible tendency towards money and commerce towards exchange and products Indeed the oeuvre is use value and the the product is exchange ...

## 07. I keep what can be used, not sold.
- Status: **partial** (exact+syn coverage 0.62, with fragments 1.0)
- Resolution: 5/8 exact-or-syn, 3 fragment
- Chunk: `10` (words 900-1259)
- Matches: i->i (frag), keep->ke+ep (frag), what->what (exact), can->can (exact), be->be (exact), used->us+ed (frag), not->not (exact), sold->exchange (syn)
- Chunk preview: of their development centralize wealth powerful groups invest unproductively a large part of their wealth in the cities they dominate At the same time banking and commercial capital have already made wealth mobile and has established exchange networks enabling the ...

## 08. The centre calls itself order.
- Status: **partial** (exact+syn coverage 0.6, with fragments 1.0)
- Resolution: 3/5 exact-or-syn, 2 fragment
- Chunk: `11` (words 990-1349)
- Matches: the->the (exact), centre->centrality (syn), calls->ca+ls (frag), itself->itself (exact), order->or+er (frag)
- Chunk preview: capitalises enriched by commerce banking usury The outcome is that society as a whole made up of the city the country and the institutions which regulate their relations tend to constitute themselves as a network of cities with a certain ...

## 09. I answer with a minor rhythm.
- Status: **weak** (exact+syn coverage 0.33, with fragments 1.0)
- Resolution: 2/6 exact-or-syn, 4 fragment
- Chunk: `14` (words 1260-1619)
- Matches: i->i (frag), answer->ans+wer (frag), with->th (frag), a->a (exact), minor->mi+or (frag), rhythm->time (syn)
- Chunk preview: of belonging Political confrontations between the minuto popolo the popolo grosso the aristocracy and the oligarchy have the city as their battle ground their stake These groups are rivals in their love of the city As for the rich and ...

## 10. Youth absorbs the city too fast.
- Status: **weak** (exact+syn coverage 0.33, with fragments 0.83)
- Resolution: 2/6 exact-or-syn, 3 fragment
- Chunk: `16` (words 1440-1799)
- Matches: youth->th (frag), absorbs->abs (frag), the->the (exact), city->city (exact), too->∅ (miss), fast->st (frag)
- Chunk preview: value the origins of a virtual predominance and revalorization of use In the urban system we are attempting to analyse action is exercized over specific conflicts between use value and exchange value between mobilization of wealth in silver and in ...

## 11. I wear its signs, not its obedience.
- Status: **weak** (exact+syn coverage 0.43, with fragments 1.0)
- Resolution: 3/7 exact-or-syn, 4 fragment
- Chunk: `17` (words 1530-1889)
- Matches: i->i (frag), wear->we+ar (frag), its->its (exact), signs->si+ns (frag), not->not (exact), its->its (exact), obedience->nce (frag)
- Chunk preview: the initiatives of banking and commercial capitalism The coporarion does not only regulate a craft Each enters into an organic whole the corporate system regulates the distribution of actions and activities over urban space streets and neighbourhoods and urban time ...

## 12. In the suburb I lose urban consciousness.
- Status: **partial** (exact+syn coverage 0.57, with fragments 1.0)
- Resolution: 4/7 exact-or-syn, 3 fragment
- Chunk: `22` (words 1980-2339)
- Matches: in->in (exact), the->the (exact), suburb->suburbs (syn), i->i (frag), lose->lo+se (frag), urban->urban (exact), consciousness->con+ess (frag)
- Chunk preview: materials labour Since settlement outside of cities is not satisfactory for entrepreneurs as soon as it is possible industry comes closer to urban centres Inversely the city prior to industrialization accelerates the process in particular it enables the rapid growth ...

## 13. In the core I return to encounter.
- Status: **partial** (exact+syn coverage 0.57, with fragments 0.86)
- Resolution: 4/7 exact-or-syn, 2 fragment
- Chunk: `25` (words 2250-2609)
- Matches: in->in (exact), the->the (exact), core->core (exact), i->i (frag), return->∅ (miss), to->to (exact), encounter->enc+ter (frag)
- Chunk preview: city assaults it takes it ravages it It tends to break up the old cores by taking them over This does not prevent the extension of urban phenomena cities and agglomerations industrial towns and suburbs with the addition of shanty ...

## 14. Difference meets difference at speed.
- Status: **weak** (exact+syn coverage 0.4, with fragments 1.0)
- Resolution: 2/5 exact-or-syn, 3 fragment
- Chunk: `27` (words 2430-2789)
- Matches: difference->nce (frag), meets->me+ts (frag), difference->nce (frag), at->at (exact), speed->rapid (syn)
- Chunk preview: agglomeration which parallels it on the mainland Mestre This city among the most beautiful cities bequeathed to us from pre industrial times is threatened not so much by physical deterioration due to the sea or to its subsidence as by ...

## 15. I hear centrality before I see it.
- Status: **weak** (exact+syn coverage 0.29, with fragments 0.86)
- Resolution: 2/7 exact-or-syn, 4 fragment
- Chunk: `28` (words 2520-2879)
- Matches: i->i (frag), hear->he+ar (frag), centrality->core (syn), before->ore (frag), i->i (frag), see->∅ (miss), it->it (exact)
- Chunk preview: Greece are only places of tourist consumption and aesthetic pilgrimage Yet the organizational core of the city remains very strong Its surroundings of new neighbourhoods and semi shanty towns inhabited by uprooted and disorganized people confer it an exorbitant power ...

## 16. The wall is text; the text is wall.
- Status: **partial** (exact+syn coverage 0.5, with fragments 1.0)
- Resolution: 4/8 exact-or-syn, 4 fragment
- Chunk: `29` (words 2610-2969)
- Matches: the->the (exact), wall->wa+ll (frag), is->is (exact), text->te+xt (frag), the->the (exact), text->te+xt (frag), is->is (exact), wall->wa+ll (frag)
- Chunk preview: so on and so forth It is this fragile network always in danger of breaking which defines a type of urbanization without or with a weak industrialization but with a rapid extension of the agglomeration of property and speculation a ...

## 17. I read what was prescribed to me.
- Status: **weak** (exact+syn coverage 0.43, with fragments 1.0)
- Resolution: 3/7 exact-or-syn, 4 fragment
- Chunk: `31` (words 2790-3149)
- Matches: i->i (frag), read->re+ad (frag), what->what (exact), was->was (exact), prescribed->bed (frag), to->to (exact), me->me (frag)
- Chunk preview: phenomenon extends itself over a very large part of the territory of great industrial countries It happily crosses national boundaries the Megalopolis of Northern Europe extends from the Ruhr to the sea and even to English cities and from the ...

## 18. Then I write back in fragments.
- Status: **weak** (exact+syn coverage 0.33, with fragments 1.0)
- Resolution: 2/6 exact-or-syn, 4 fragment
- Chunk: `35` (words 3150-3509)
- Matches: then->then (exact), i->i (frag), write->te (frag), back->ba (frag), in->in (exact), fragments->nts (frag)
- Chunk preview: around one or several cities old and recent Such a description may lose what is essential Indeed the significance of the urban fabric is not limited to its morphology It is the support of a more or less intense more ...

## 19. Near order / far order split my body.
- Status: **weak** (exact+syn coverage 0.14, with fragments 0.71)
- Resolution: 1/7 exact-or-syn, 4 fragment
- Chunk: `36` (words 3240-3599)
- Matches: near->ne+ar (frag), order->or+er (frag), far->∅ (miss), order->or+er (frag), split->sp+it (frag), my->∅ (miss), body->life (syn)
- Chunk preview: values The best known elements of the urban system of objects include water electricity gas butane in the countryside not to mention the car the television plastic utensils modern furniture which entail new demands with regard to services Among the ...

## 20. I become mediation among mediations.
- Status: **weak** (exact+syn coverage 0.2, with fragments 1.0)
- Resolution: 1/5 exact-or-syn, 4 fragment
- Chunk: `37` (words 3330-3689)
- Matches: i->i (frag), become->become (exact), mediation->med+ion (frag), among->am+ng (frag), mediations->med+ons (frag)
- Chunk preview: to this rapid assimilation of things and representations coming from the city These are sociological trivialities which are useful to remember to show their implications Within the mesh of the urban fabric survive islets and islands of pure rurality often ...

## 21. Class strategy redraws my route.
- Status: **weak** (exact+syn coverage 0.0, with fragments 0.8)
- Resolution: 0/5 exact-or-syn, 4 fragment
- Chunk: `42` (words 3780-4139)
- Matches: class->cl+ss (frag), strategy->str (frag), redraws->red (frag), my->∅ (miss), route->ro+te (frag)
- Chunk preview: the urban urban society There is the urban fabric which carries this urbanness and centrality old renovated new Hence a disquieting problematic particularly if one wishes to go from analysis to synthesis from observations to a project the normative Must ...

## 22. I return where I was pushed out.
- Status: **weak** (exact+syn coverage 0.29, with fragments 1.0)
- Resolution: 2/7 exact-or-syn, 5 fragment
- Chunk: `47` (words 4230-4589)
- Matches: i->i (frag), return->ret (frag), where->where (exact), i->i (frag), was->was (exact), pushed->hed (frag), out->out (frag)
- Chunk preview: is still a visible witness to this before the Revolution it is an aristocratic quarter despite the tendency of the capital and the wealthy to drift towards the west an area of gardens and private mansions It took but a ...

## 23. The right appears as cry first.
- Status: **partial** (exact+syn coverage 0.67, with fragments 0.83)
- Resolution: 4/6 exact-or-syn, 1 fragment
- Chunk: `50` (words 4500-4859)
- Matches: the->the (exact), right->right (exact), appears->∅ (miss), as->as (exact), cry->cry (exact), first->fi+st (frag)
- Chunk preview: immediate periphery Former craftsmen and new proletarians penetrate right up to the heart of the city They live in slums but also in tenements where the better off live on the ground floors and the workers on the upper ones ...

## 24. Then demand, then practice.
- Status: **good** (exact+syn coverage 0.75, with fragments 1.0)
- Resolution: 3/4 exact-or-syn, 1 fragment
- Chunk: `54` (words 4860-5219)
- Matches: then->then (exact), demand->and (frag), then->then (exact), practice->practice (exact)
- Chunk preview: other finalities take place which justify in another way these gashes into urban life It should be noted that Haussmann did not achieve his goal One strong aspect of the Paris Commune is the strength of the return towards the ...

## 25. Not habitat: to inhabit.
- Status: **good** (exact+syn coverage 1.0, with fragments 1.0)
- Resolution: 4/4 exact-or-syn, 0 fragment
- Chunk: `55` (words 4950-5309)
- Matches: not->not (exact), habitat->habitat (exact), to->to (exact), inhabit->inhabit (exact)
- Chunk preview: the second half of the century influential people that is rich or powerful or both sometimes ideologues Le Play with ideas strongly marked by religions Catholic and Protestant sometimes informed politicians belonging to the centre right and who moreover do ...

## 26. I refuse the logic of habitat.
- Status: **weak** (exact+syn coverage 0.33, with fragments 1.0)
- Resolution: 2/6 exact-or-syn, 4 fragment
- Chunk: `56` (words 5040-5399)
- Matches: i->i (frag), refuse->use (frag), the->the (exact), logic->lo+ic (frag), of->of (exact), habitat->hab+tat (frag)
- Chunk preview: community village or city Urban life had among other qualities this attribute It gave the right to inhabit it allowed townsmen citizens to inhabit It is thus that mortals inhabit while they save the earth while they wait for the ...

## 27. I claim the plastic space of living.
- Status: **weak** (exact+syn coverage 0.43, with fragments 1.0)
- Resolution: 3/7 exact-or-syn, 4 fragment
- Chunk: `57` (words 5130-5489)
- Matches: i->i (frag), claim->cl+im (frag), the->the (exact), plastic->pla+tic (frag), space->sp+ce (frag), of->of (exact), living->life (syn)
- Chunk preview: a very complex whole which was and remains the city to project it over the ground not without showing and signifying in this manner the society for which they provide an ideology and a practice Certainly suburbs were created under ...

## 28. A cafe, a corner, a small centrality.
- Status: **partial** (exact+syn coverage 0.57, with fragments 1.0)
- Resolution: 4/7 exact-or-syn, 3 fragment
- Chunk: `59` (words 5310-5669)
- Matches: a->a (exact), cafe->ca+fe (frag), a->a (exact), corner->ner (frag), a->a (exact), small->small (exact), centrality->cen+ity (frag)
- Chunk preview: implications They were not proposing to demoralize the working classes but on the contrary to moralize it They considered it beneficial to involve the workers individuals and families into a hierarchy clearly distinct from that which rules in the firm ...

## 29. A place consumed / a place reclaimed.
- Status: **partial** (exact+syn coverage 0.5, with fragments 0.83)
- Resolution: 3/6 exact-or-syn, 2 fragment
- Chunk: `60` (words 5400-5759)
- Matches: a->a (exact), place->pl+ce (frag), consumed->consumption (syn), a->a (exact), place->pl+ce (frag), reclaimed->∅ (miss)
- Chunk preview: the role of owner occupied housing A remarkably successful operation although its political consequences were not always those anticipated by its promoters Nevertheless a result was achieved predicted or otherwise conscious or unconscious Society orients itself ideologically and practically towards ...

## 30. The planner says coherence.
- Status: **partial** (exact+syn coverage 0.5, with fragments 1.0)
- Resolution: 2/4 exact-or-syn, 2 fragment
- Chunk: `61` (words 5490-5849)
- Matches: the->the (exact), planner->planning (syn), says->sa (frag), coherence->nce (frag)
- Chunk preview: from places of production available from a sector of habitation for scattered firms the proletariat will allow its creative capacity to diminish in its conscience Urban consciousness will vanish In France the beginnings of the suburb are also the beginnings ...

## 31. I keep contradiction alive.
- Status: **weak** (exact+syn coverage 0.25, with fragments 1.0)
- Resolution: 1/4 exact-or-syn, 3 fragment
- Chunk: `65` (words 5850-6209)
- Matches: i->i (frag), keep->ke+ep (frag), contradiction->con+ion (frag), alive->living (syn)
- Chunk preview: not necessarily become a public service It surfaces into social consciousness as a right It is acknowledged in fact by the indignation raised by dramatic cases and by the discontent engendered by the crisis Yet it is not formally or ...

## 32. I move through isotopies and breaks.
- Status: **weak** (exact+syn coverage 0.17, with fragments 0.83)
- Resolution: 1/6 exact-or-syn, 4 fragment
- Chunk: `66` (words 5940-6299)
- Matches: i->i (frag), move->mo+ve (frag), through->ugh (frag), isotopies->iso+ies (frag), and->and (exact), breaks->∅ (miss)
- Chunk preview: the Left will be satisfied with demanding more housing Moreover what guides public and semi public initiatives is not a conception of urban planning it is simply the goal of providing as quickly as possible at the least cost the ...

## 33. Meaning leaks at every border.
- Status: **weak** (exact+syn coverage 0.2, with fragments 1.0)
- Resolution: 1/5 exact-or-syn, 4 fragment
- Chunk: `67` (words 6030-6389)
- Matches: meaning->ing (frag), leaks->le (frag), at->at (exact), every->ev+ry (frag), border->der (frag)
- Chunk preview: of habitat There is a sort of plasticity which allows for modifications and appropriations The space of the house fence garden various and available corners leaves a margin of initiative and freedom to inhabit limited but real State rationality is ...

## 34. Urban language stutters, then sings.
- Status: **weak** (exact+syn coverage 0.4, with fragments 1.0)
- Resolution: 2/5 exact-or-syn, 3 fragment
- Chunk: `68` (words 6120-6479)
- Matches: urban->urban (exact), language->lan+age (frag), stutters->ers (frag), then->then (exact), sings->si (frag)
- Chunk preview: appropriation by groups and individuals of the conditions of their existence It is also a complete way of living functions prescriptions daily routine which is inscribed and signifies itself in this habitat The villa habitat has proliferated in the suburban ...

## 35. The system closes; I open.
- Status: **weak** (exact+syn coverage 0.4, with fragments 1.0)
- Resolution: 2/5 exact-or-syn, 3 fragment
- Chunk: `69` (words 6210-6569)
- Matches: the->the (exact), system->system (exact), closes->ses (frag), i->i (frag), open->op+en (frag)
- Chunk preview: badly opposed was added speculation in apartments when these were in to ownership Thus housing entered into property wealth and urban land into exchange value Restrictions were disappearing If one defines urban reality by dependency vis a vis the centre ...

## 36. The old core rots; desire persists.
- Status: **weak** (exact+syn coverage 0.33, with fragments 1.0)
- Resolution: 2/6 exact-or-syn, 4 fragment
- Chunk: `74` (words 6660-7019)
- Matches: the->the (exact), old->old (exact), core->co+re (frag), rots->ro+ts (frag), desire->des+ire (frag), persists->per (frag)
- Chunk preview: cent of French people aspire to be owner occupiers of a house while a strong majority also declare themselves to be satisfied with social housing estates The outcome is not important here What should be noted is that consciousness of ...

## 37. I learn to occupy with care.
- Status: **weak** (exact+syn coverage 0.17, with fragments 0.83)
- Resolution: 1/6 exact-or-syn, 4 fragment
- Chunk: `75` (words 6750-7109)
- Matches: i->i (frag), learn->le+rn (frag), to->to (exact), occupy->∅ (miss), with->wi+th (frag), care->ca+re (frag)
- Chunk preview: analysis than the source of conflict expressed by the end of the city and by the extension of a mutilated and deteriorated but real urban society The suburbs are urban within a dissociated morphology the empire of separation and scission ...

## 38. To occupy is to become legible.
- Status: **partial** (exact+syn coverage 0.5, with fragments 0.83)
- Resolution: 3/6 exact-or-syn, 2 fragment
- Chunk: `76` (words 6840-7199)
- Matches: to->to (exact), occupy->∅ (miss), is->is (exact), to->to (exact), become->bec+ome (frag), legible->ble (frag)
- Chunk preview: ravage pre existing urban reality destroying it through practice and ideology to the point of extirpating it from reality and consciousness Led by a class strategy industrialization acts as a negative force over urban reality the urban social is denied ...

## 39. To become legible is danger.
- Status: **weak** (exact+syn coverage 0.4, with fragments 0.8)
- Resolution: 2/5 exact-or-syn, 2 fragment
- Chunk: `78` (words 7020-7379)
- Matches: to->to (exact), become->ome (frag), legible->ble (frag), is->is (exact), danger->∅ (miss)
- Chunk preview: need for an urban theory to embellish their cities What sufficed was the pressure exercised by the people on their masters and the presence of a civilization and style which enabled the wealth derived from the labour of the people ...

## 40. I blur, reappear, blur again.
- Status: **weak** (exact+syn coverage 0.0, with fragments 1.0)
- Resolution: 0/5 exact-or-syn, 5 fragment
- Chunk: `79` (words 7110-7469)
- Matches: i->i (frag), blur->bl+ur (frag), reappear->rea (frag), blur->bl+ur (frag), again->ag+in (frag)
- Chunk preview: but also underpinned by reasonings which had been given shape Its democratic generalizations later gave way to a rationalism of opinions and attitudes Each citizen was expected to have a reasoned opinion on every fact and problem concerning him this ...

## 41. Art is not ornament; it is claim.
- Status: **partial** (exact+syn coverage 0.57, with fragments 1.0)
- Resolution: 4/7 exact-or-syn, 3 fragment
- Chunk: `82` (words 7380-7739)
- Matches: art->art (frag), is->is (exact), not->not (exact), ornament->ent (frag), it->it (exact), is->is (exact), claim->cl+im (frag)
- Chunk preview: strategy more or less justified by an ideology Rationalism which purports to extract from its own analyses the aim pursued by these analyses is itself an ideology The notion of system overlays that of strategy To critical analysis the system ...

## 42. A claim is a relation, not a logo.
- Status: **good** (exact+syn coverage 0.75, with fragments 1.0)
- Resolution: 6/8 exact-or-syn, 2 fragment
- Chunk: `83` (words 7470-7829)
- Matches: a->a (exact), claim->cl+im (frag), is->is (exact), a->a (exact), relation->relations (syn), not->not (exact), a->a (exact), logo->lo+go (frag)
- Chunk preview: point of view of a technicist rationalism the results on the ground of the processes examined above represent only chaos In the reality which they critically observe suburbs urban fabric and surviving cores these rationalists do not recognize the conditions ...

## 43. I gather others at the margin
- Status: **partial** (exact+syn coverage 0.5, with fragments 0.83)
- Resolution: 3/6 exact-or-syn, 2 fragment
- Chunk: `84` (words 7560-7919)
- Matches: i->i (frag), gather->her (frag), others->others (exact), at->at (exact), the->the (exact), margin->∅ (miss)
- Chunk preview: is not a normal disorder How can it be established as norm and normality This is unconceivable This disorder is unhealthy The physician of modern society see himself as the physician of a sick social space Finality The cure It ...

## 44. Margins turn centre for a minute.
- Status: **weak** (exact+syn coverage 0.33, with fragments 1.0)
- Resolution: 2/6 exact-or-syn, 4 fragment
- Chunk: `85` (words 7650-8009)
- Matches: margins->ins (frag), turn->tu+rn (frag), centre->tre (frag), for->for (exact), a->a (exact), minute->min (frag)
- Chunk preview: the habitat underlying the disorder and apparent incoherence that he will take as point of departure towards the coherence of the real his coherent approaches There is in fact no single or unitary approach in planning thought but several tendencies ...

## 45. In that minute, the city is ours.
- Status: **good** (exact+syn coverage 0.71, with fragments 1.0)
- Resolution: 5/7 exact-or-syn, 2 fragment
- Chunk: `86` (words 7740-8099)
- Matches: in->in (exact), that->that (exact), minute->min (frag), the->the (exact), city->city (exact), is->is (exact), ours->ou+rs (frag)
- Chunk preview: of a pencil drawing One can therefore identify the following The planning of men of good will architects and writers Their thinking and projects imply a certain philosophy Generally they associate themselves to an old classical and liberal humanism This ...

## 46. Then power writes over us again.
- Status: **partial** (exact+syn coverage 0.5, with fragments 1.0)
- Resolution: 3/6 exact-or-syn, 3 fragment
- Chunk: `88` (words 7920-8279)
- Matches: then->then (exact), power->po+er (frag), writes->inscribed (syn), over->over (exact), us->us (frag), again->ag+in (frag)
- Chunk preview: then thrown as fodder to feed the appetites of consumers The planning of these administrators linked to the public State sector It sees itself as scientific It relies sometimes on a science sometimes on studies which call themselves synthetic pluri ...

## 47. We answer with another writing.
- Status: **weak** (exact+syn coverage 0.2, with fragments 1.0)
- Resolution: 1/5 exact-or-syn, 4 fragment
- Chunk: `90` (words 8100-8459)
- Matches: we->we (frag), answer->ans (frag), with->with (exact), another->her (frag), writing->ing (frag)
- Chunk preview: and analytical knowledge coming from different sciences are oriented towards a synthetic finality For all that one should not conceive an urban life having at its disposal information provided by the sciences of society These two aspects are confounded in ...

## 48. Not final: urban becoming.
- Status: **partial** (exact+syn coverage 0.5, with fragments 1.0)
- Resolution: 2/4 exact-or-syn, 2 fragment
- Chunk: `92` (words 8280-8639)
- Matches: not->not (exact), final->fi+al (frag), urban->urban (exact), becoming->bec+ing (frag)
- Chunk preview: posterity because publicity itself becomes ideology Parly II a new development gives birth to a new an of living a new lifestyle Daily life resembles a fairy tale Leave your coat in the cloakroom and feeling lighter do your shopping ...

## 49. Right as practice, not gift.
- Status: **partial** (exact+syn coverage 0.6, with fragments 1.0)
- Resolution: 3/5 exact-or-syn, 2 fragment
- Chunk: `93` (words 8370-8729)
- Matches: right->ri+ht (frag), as->as (exact), practice->practice (exact), not->not (exact), gift->gi (frag)
- Chunk preview: be happy Here is the context the setting the means of your happiness If you do not know how to grasp the happiness offered so as to make it your own don t insist A global strategy that is what ...

## 50. Page for page: we still connect.
- Status: **weak** (exact+syn coverage 0.33, with fragments 1.0)
- Resolution: 2/6 exact-or-syn, 4 fragment
- Chunk: `94` (words 8460-8819)
- Matches: page->pa+ge (frag), for->for (exact), page->pa+ge (frag), we->we (frag), still->still (exact), connect->con+ect (frag)
- Chunk preview: happiness through consumption joy by planning adapted to its new mission This planning programmes a daily life generating satisfactions especially for receptive and participating women A programmed and computerized consumption will become the rule and norm for the whole society ...
