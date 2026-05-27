# -*- coding: utf-8 -*-
"""
Per-profile metadata that is NOT in the narrative draft:
  - era / region / tags (display chips)
  - images: curated real Wikimedia Commons artifacts (kind="commons") and
    AI daily-life scene slots (kind="ai"); license/attribution for the
    commons ones is pulled live by fetch_images.py from the Commons API.
  - sources: curated further-reading links (link-checked by build.py).

Keyed by the slug that build.py derives from the draft (slugify of the name).
"""

# Shared style suffix for the daily-life illustration prompts, so the illustrations
# read like period wall-painting and sit well beside real artifacts.
AI_STYLE = (
    "Ancient Roman fresco / wall-painting style, matte plaster texture with fine "
    "cracks, warm earth-tone palette of ochre, Pompeian red and umber, naturalistic "
    "but slightly stylized figures, historically accurate dress and setting, soft "
    "daylight, no text, no modern objects, no anachronisms."
)

# Site-wide dice imagery (real Roman dice) used on the landing page roller.
DICE_IMAGES = [
    {
        "key": "bone-dice",
        "file": "File:Roman bone dice from Silchester.jpg",
        "caption": "Roman bone dice excavated at Silchester (Calleva Atrebatum), Britain.",
        "why": "Romans gambled with bone dice (tesserae) and knucklebones (tali) — the everyday randomness behind this site's roll.",
    },
    {
        "key": "delos-dice",
        "file": "File:Dices Roman Museum Delos ZdeDelm220.jpg",
        "caption": "Roman-era dice from the Archaeological Museum of Delos.",
        "why": "Delos held the Mediterranean's largest slave market — the same throw of fortune that decided a life.",
    },
]

# Recurring "thematic" museum artifacts, shared across lives and placed above
# narrative paragraphs by theme (childhood, marriage, war, death, ...). Fetched
# once into docs/images/themes/<key>.* by fetch_images.py. All verified on the
# Wikimedia Commons API; licenses (PD / CC) are captured at fetch time.
THEME_IMAGES = {
    "childhood": {
        "file": "File:Sarcophagus Marcus Cornelius Statius Louvre Ma659 n1.jpg",
        "caption": "Sarcophagus of M. Cornelius Statius showing the stages of a Roman childhood, Louvre.",
        "why": "Birth, nursing, first steps and first lessons — the shape of a Roman childhood."},
    "children": {
        "file": "File:Children games Louvre Ma99.jpg",
        "caption": "Relief of children at play, Louvre.",
        "why": "Roman children and the games of those who survived infancy."},
    "marriage": {
        "file": "File:Aldobrandini Wedding.jpg",
        "caption": "The 'Aldobrandini Wedding', a Roman fresco of marriage preparations, Vatican.",
        "why": "Betrothal and marriage — the hinge around which most Roman lives turned."},
    "war": {
        "file": "File:Sarcophagus Portonaccio Massimo.jpg",
        "caption": "The Portonaccio battle sarcophagus, Romans and barbarians, Palazzo Massimo, Rome.",
        "why": "War was never more than a generation away for anyone living under Rome."},
    "marching": {
        "file": "File:Trajan's Column - NMR - panel 015 A.jpg",
        "caption": "Legionaries on campaign, relief cast from Trajan's Column, Rome.",
        "why": "The army on the move — the machine that made and guarded the frontiers."},
    "religion": {
        "file": "File:Suovetaurile Louvre.jpg",
        "caption": "A suovetaurilia (pig–sheep–bull) sacrifice relief, Louvre.",
        "why": "Sacrifice and public ritual stood at the centre of Roman religion."},
    "death": {
        "file": "File:Rilievo con corteo funebre, 20 ac-20 dc ca., da amiternum, 07 portantina.jpg",
        "caption": "A funeral procession bearing the deceased on a bier, relief from Amiternum.",
        "why": "Death and the rites that carried a Roman to the grave."},
    "writing": {
        "file": "File:Pompei - Sappho - MAN.jpg",
        "caption": "Fresco of a woman with stylus and wax tablets (the so-called 'Sappho'), Pompeii.",
        "why": "Letters, accounts and literacy — reading and writing in the Roman world."},
    "school": {
        "file": "File:Roman school.jpg",
        "caption": "A Roman schoolroom, relief from Neumagen.",
        "why": "Schooling and the teaching of the young."},
    "money": {
        "file": "File:Gold aureus coins.jpg",
        "caption": "Roman gold aurei.",
        "why": "Coin, pay and prices — the cash economy that reached every life."},
    "city": {
        "file": "File:Forum Romanum panorama.jpg",
        "caption": "The Roman Forum.",
        "why": "The monumental, crowded heart of a Roman city."},
    "agriculture": {
        "file": "File:Cherchel-Mosaic-lower-register.png",
        "caption": "Mosaic of ploughing and field labour, Cherchell (Caesarea), Roman Africa.",
        "why": "The farming year that fed the empire and governed rural life."},
}

# Site-wide inspiration / general reading (rendered on the credits/about page).
GENERAL_SOURCES = [
    {"title": "A Collection of Unmitigated Pedantry (ACOUP) — Bret Devereaux",
     "url": "https://acoup.blog/", "note": "Public-facing scholarship on the ancient world; the model for this project's source-linking."},
    {"title": "Roman demography — overview",
     "url": "https://en.wikipedia.org/wiki/Demography_of_the_Roman_Empire", "note": "Population structure and mortality behind the probability weights."},
    {"title": "Wikimedia Commons",
     "url": "https://commons.wikimedia.org/", "note": "Source of the museum photographs and artifacts used throughout, each credited on its page."},
]


META = {
    # ------------------------------------------------------------------ 1
    "titus-caecilius": {
        "era": "Late Republic", "era_range": "105–42 BC", "region": "Central Italy",
        "tags": ["Man", "Peasant smallholder", "Rural", "Italy", "Free citizen"],
        "epitome": "The default Roman life: subsistence farming, patronage, and war passing through every generation.",
        "images": [
            {"kind": "commons", "key": "lararium",
             "file": "File:Lararium in the atrium of Casa del Menandro (Pompeii) (48442861451).jpg",
             "caption": "A household shrine (lararium), House of the Menander, Pompeii.",
             "why": "Titus worshipped the Lares at a shrine exactly like this before every planting."},
            {"kind": "commons", "key": "farming",
             "file": "File:Cherchel-Mosaic-lower-register.png",
             "caption": "Mosaic of ploughing and field labour, Cherchell (Caesarea), Roman Africa.",
             "why": "Emmer wheat, oxen and the agricultural year that governed his entire life."},
            {"kind": "ai", "key": "homestead",
             "alt": "An Italian peasant family standing before their small farmhouse with goats and olive trees.",
             "caption": "His family before the farmstead — emmer fields, olive trees, a few goats.",
             "prompt": "A late-Republican Italian peasant family standing before a small stone-and-timber farmhouse in the hills near Arpinum; an older weathered farmer in a plain tunic, his wife, grown children; goats and olive trees; emmer wheat field behind; " + AI_STYLE},
        ],
        "sources": [
            {"title": "Roman agriculture", "url": "https://en.wikipedia.org/wiki/Roman_agriculture"},
            {"title": "ACOUP — Bread, How Did They Make It? Part I: Farmers!", "url": "https://acoup.blog/2020/07/24/collections-bread-how-did-they-make-it-part-i-farmers/"},
            {"title": "Social War (91–88 BC)", "url": "https://en.wikipedia.org/wiki/Social_War_(91%E2%80%9388_BC)"},
            {"title": "Sulla and the proscriptions", "url": "https://en.wikipedia.org/wiki/Sulla"},
            {"title": "Arpinum (Arpino)", "url": "https://en.wikipedia.org/wiki/Arpino"},
            {"title": "Lares and household religion", "url": "https://en.wikipedia.org/wiki/Lares"},
        ],
    },
    # ------------------------------------------------------------------ 2
    "kalasiris": {
        "era": "Late Republic", "era_range": "135–86 BC", "region": "Sicily",
        "tags": ["Man", "Enslaved", "Rural", "Sicily", "Born free, then property"],
        "epitome": "Captured as a child, shipped through Delos, worked to death on a Sicilian grain estate.",
        "images": [
            {"kind": "commons", "key": "estate",
             "file": "File:Dominus Julius mosaic in the Bardo National Museum(12240864473).jpg",
             "caption": "The 'Dominus Julius' mosaic, Bardo Museum, Tunis — a great estate and its labourers.",
             "why": "The latifundium economy that consumed enslaved field-hands like Kalasiris."},
            {"kind": "commons", "key": "captive",
             "file": "File:Roman Figurine of Bound Captive (FindID 413449).jpg",
             "caption": "Roman figurine of a bound captive (Portable Antiquities Scheme).",
             "why": "Enslavement through war and raiding — how a free Bithynian boy became property."},
            {"kind": "ai", "key": "ergastulum",
             "alt": "Enslaved labourers in a barracks at night on a Sicilian grain estate.",
             "caption": "The ergastulum — the barracks where estate slaves slept, sometimes chained.",
             "prompt": "Interior of a Roman latifundium slave barracks (ergastulum) at dusk in Sicily; gaunt labourers in single rough tunics resting on straw, an overseer's lamp; grain sacks; oppressive and dim; " + AI_STYLE},
        ],
        "sources": [
            {"title": "Slavery in ancient Rome", "url": "https://en.wikipedia.org/wiki/Slavery_in_ancient_Rome"},
            {"title": "ACOUP — Bread, Part II: Big Farms (the slave latifundia)", "url": "https://acoup.blog/2020/07/31/collections-bread-how-did-they-make-it-part-ii-big-farms/"},
            {"title": "Delos (the slave market)", "url": "https://en.wikipedia.org/wiki/Delos"},
            {"title": "First Servile War", "url": "https://en.wikipedia.org/wiki/First_Servile_War"},
            {"title": "Second Servile War", "url": "https://en.wikipedia.org/wiki/Second_Servile_War"},
            {"title": "Latifundium", "url": "https://en.wikipedia.org/wiki/Latifundium"},
            {"title": "Kingdom of Bithynia", "url": "https://en.wikipedia.org/wiki/Bithynia"},
        ],
    },
    # ------------------------------------------------------------------ 3
    "helene": {
        "era": "Antonine era", "era_range": "148–198 AD", "region": "Roman Egypt",
        "tags": ["Woman", "Peasant", "Rural", "Egypt", "Best-documented commoners"],
        "epitome": "A Fayum village wife whose tax receipts and portrait-painted neighbours still survive.",
        "images": [
            {"kind": "commons", "key": "fayum",
             "file": "File:Fayum mummy portrait (160-180 AD) - British museum, EA74710.jpg",
             "caption": "Fayum mummy portrait of a woman, c. 160–180 AD, British Museum.",
             "why": "\"The famous Fayum portraits are exactly the faces of people like you.\" — her own generation."},
            {"kind": "commons", "key": "sobek",
             "file": "File:Statue presenting a shrine with an image of the god Sobek, graywacke - Museo Egizio Turin C 3043 p01.jpg",
             "caption": "Statue with a shrine of the crocodile god Sobek, Museo Egizio, Turin.",
             "why": "Sobek was the traditional god of the Fayum that Helene worshipped."},
            {"kind": "ai", "key": "canal",
             "alt": "An Egyptian village woman hauling water beside an irrigation canal in the Fayum.",
             "caption": "Daily life: hauling water from the canal, mud-brick houses, the Fayum oasis.",
             "prompt": "An Egyptian peasant woman in plain linen beside a palm-lined irrigation canal in the Fayum oasis; mud-brick houses, a communal bread oven, chickens and a small vegetable garden; Roman-era Egypt 2nd century; " + AI_STYLE},
        ],
        "sources": [
            {"title": "Fayum mummy portraits", "url": "https://en.wikipedia.org/wiki/Fayum_mummy_portraits"},
            {"title": "Karanis", "url": "https://en.wikipedia.org/wiki/Karanis"},
            {"title": "Antonine Plague", "url": "https://en.wikipedia.org/wiki/Antonine_Plague"},
            {"title": "Egypt (Roman province)", "url": "https://en.wikipedia.org/wiki/Egypt_(Roman_province)"},
            {"title": "Sobek", "url": "https://en.wikipedia.org/wiki/Sobek"},
        ],
    },
    # ------------------------------------------------------------------ 4
    "petronia-iusta": {
        "era": "Flavian–Trajanic", "era_range": "55–112 AD", "region": "Rome",
        "tags": ["Woman", "Urban plebeian", "City", "Rome", "Daughter of a freedman"],
        "epitome": "Born in the Subura, fed by the grain dole, raised in a swaying insula above a million-person city.",
        "images": [
            {"kind": "commons", "key": "baker",
             "file": "File:Fresco portrait of the baker Terentius Neo and his wife, from Pompeii.jpg",
             "caption": "Fresco of the baker Terentius Neo and his wife, Pompeii.",
             "why": "Her father worked a bakery; this couple are the social world she came from."},
            {"kind": "commons", "key": "lamp",
             "file": "File:Terracotta oil lamp MET DP860.jpg",
             "caption": "Roman terracotta oil lamp, Metropolitan Museum of Art.",
             "why": "Petronia painted decorations on lamps exactly like this for a living."},
            {"kind": "commons", "key": "latrine",
             "file": "File:Ancient Roman Public Latrine, Ostia Antica (6075060094).jpg",
             "caption": "Public latrine, Ostia Antica.",
             "why": "The shared latrine — sanitation for the urban poor who had only a chamber pot at home."},
            {"kind": "ai", "key": "insula",
             "alt": "A crowded multi-storey Roman apartment block (insula) street in the Subura.",
             "caption": "Home: a fourth-floor room in a Subura insula, water carried up from the street.",
             "prompt": "A crowded street of tall multi-storey Roman apartment blocks (insulae) in the Subura of Rome; laundry and shopfronts below, a woman carrying water up narrow stairs, braziers, washing lines; first century AD; " + AI_STYLE},
        ],
        "sources": [
            {"title": "Subura", "url": "https://en.wikipedia.org/wiki/Subura"},
            {"title": "Insula (building)", "url": "https://en.wikipedia.org/wiki/Insula_(building)"},
            {"title": "Cura Annonae (the grain dole)", "url": "https://en.wikipedia.org/wiki/Cura_Annonae"},
            {"title": "Great Fire of Rome (64 AD)", "url": "https://en.wikipedia.org/wiki/Great_Fire_of_Rome"},
            {"title": "Year of the Four Emperors", "url": "https://en.wikipedia.org/wiki/Year_of_the_Four_Emperors"},
        ],
    },
    # ------------------------------------------------------------------ 5
    "gaius-vibius-celer": {
        "era": "Augustan–Tiberian", "era_range": "12 BC–31 AD", "region": "Rhine frontier",
        "tags": ["Man", "Legionary", "Military", "Germania", "Free citizen"],
        "epitome": "Twenty-five years under the eagles on the Rhine — and a transfer that spared him Teutoburg.",
        "images": [
            {"kind": "commons", "key": "caelius",
             "file": "File:Cenotaph of Marcus Caelius, 1st centurion of Legio XVIII, who fell in the war of Varus (Battle in the Teutoburg Forest (9 AD), LVR-LandesMuseum Bonn (9510859222).jpg",
             "caption": "Cenotaph of Marcus Caelius, centurion of Legio XVIII, lost in the Varus disaster, LVR-LandesMuseum Bonn.",
             "why": "Celer's legion XIX marched into Teutoburg; Caelius of XVIII died there. \"You had known men among those bones.\""},
            {"kind": "commons", "key": "kalkriese-mask",
             "file": "File:Kalkriese mask.jpg",
             "caption": "Iron cavalry face-mask found at Kalkriese, the Teutoburg battlefield.",
             "why": "Recovered from the killing ground itself — the physical residue of the ambush of 9 AD."},
            {"kind": "commons", "key": "diploma",
             "file": "File:Bronze military diploma MET DP105606.jpg",
             "caption": "Bronze Roman military diploma, Metropolitan Museum of Art.",
             "why": "On discharge Celer received a diploma like this, granting citizenship to his children."},
            {"kind": "ai", "key": "camp",
             "alt": "Roman legionaries building a marching camp at the edge of a German forest.",
             "caption": "Garrison life: building the nightly marching camp on the Rhine frontier.",
             "prompt": "Roman legionaries in segmented armour digging a ditch and raising a palisade for a marching camp at the misty edge of a German forest by the Rhine; tents in regulation rows, a mule; early first century AD; " + AI_STYLE},
        ],
        "sources": [
            {"title": "Battle of the Teutoburg Forest", "url": "https://en.wikipedia.org/wiki/Battle_of_the_Teutoburg_Forest"},
            {"title": "Legio XIX", "url": "https://en.wikipedia.org/wiki/Legio_XIX"},
            {"title": "Germanicus", "url": "https://en.wikipedia.org/wiki/Germanicus"},
            {"title": "Roman legion", "url": "https://en.wikipedia.org/wiki/Roman_legion"},
            {"title": "Military diploma", "url": "https://en.wikipedia.org/wiki/Roman_military_diploma"},
        ],
    },
    # ------------------------------------------------------------------ 6
    "publius-valerius-messalla": {
        "era": "Augustan–Claudian", "era_range": "20 BC–54 AD", "region": "Rome",
        "tags": ["Man", "Senator", "City", "Rome", "Patrician — 3 in 1000"],
        "epitome": "The top of the pyramid: vast wealth, the cursus honorum, and the lethal etiquette of the imperial court.",
        "images": [
            {"kind": "commons", "key": "togatus",
             "file": "File:Togato Barberini.jpg",
             "caption": "The 'Togatus Barberini' — a Roman holding busts of his ancestors (imagines).",
             "why": "At Messalla's funeral the imagines of his ancestors were paraded through the Forum."},
            {"kind": "commons", "key": "arapacis",
             "file": "File:Relief of the Ara Pacis Augustae with Procession-Uffizi.jpg",
             "caption": "Processional relief from the Ara Pacis Augustae, Rome.",
             "why": "The senatorial order on display — the world of dignitas Messalla had to perform in."},
            {"kind": "ai", "key": "atrium",
             "alt": "A Roman senator receiving clients in the marble atrium of his townhouse.",
             "caption": "The morning salutatio: a senator receiving clients in his atrium.",
             "prompt": "A wealthy Roman senator in a toga receiving a line of clients during the morning salutatio in the marble atrium of his domus; impluvium pool, ancestor busts in niches, a Greek secretary with a scroll; first century AD; " + AI_STYLE},
        ],
        "sources": [
            {"title": "Cursus honorum", "url": "https://en.wikipedia.org/wiki/Cursus_honorum"},
            {"title": "Roman Senate", "url": "https://en.wikipedia.org/wiki/Roman_Senate"},
            {"title": "Maiestas (treason trials)", "url": "https://en.wikipedia.org/wiki/Majestas"},
            {"title": "Sejanus", "url": "https://en.wikipedia.org/wiki/Sejanus"},
            {"title": "Valeria gens", "url": "https://en.wikipedia.org/wiki/Valeria_(gens)"},
        ],
    },
    # ------------------------------------------------------------------ 7
    "successus": {
        "era": "Early Empire", "era_range": "32–79 AD", "region": "Pompeii",
        "tags": ["Man", "Freedman", "Town", "Campania", "Manumitted slave"],
        "epitome": "A freed cook who ran a hot-food counter on Pompeii's main street — until Vesuvius.",
        "images": [
            {"kind": "commons", "key": "thermopolium",
             "file": "File:Thermopolium Lucius Vetutius Placidus Pompeii.jpg",
             "caption": "Thermopolium of Vetutius Placidus, on the Via dell'Abbondanza, Pompeii.",
             "why": "A hot-food-and-drink counter with embedded dolia on the exact street named in his story."},
            {"kind": "commons", "key": "tavern",
             "file": "File:Tavern scene from VI 14, 36 (Caupona of Salvius) by Geremia Discanno pub 1882.jpg",
             "caption": "Tavern scene fresco from the Caupona of Salvius, Pompeii (19th-c. reproduction).",
             "why": "Drinkers, dice and quarrels — the low-culture social world of his counter."},
            {"kind": "commons", "key": "cast",
             "file": "File:Pompeii Plaster cast of a victim.jpg",
             "caption": "Plaster cast of a victim of the 79 AD eruption, Pompeii.",
             "why": "How Successus's own death was preserved: a void in the ash, filled with plaster."},
            {"kind": "ai", "key": "counter",
             "alt": "A freedman serving hot food across a Pompeian thermopolium counter to customers.",
             "caption": "Business: serving stew and wine from the dolia to sailors and craftsmen.",
             "prompt": "A Roman freedman tavern-keeper ladling hot stew from terracotta dolia set into a masonry counter of a Pompeian thermopolium, customers leaning in, amphorae and frescoed walls, on a busy street; 1st century AD; " + AI_STYLE},
        ],
        "sources": [
            {"title": "Thermopolium", "url": "https://en.wikipedia.org/wiki/Thermopolium"},
            {"title": "Freedman (ancient Rome)", "url": "https://en.wikipedia.org/wiki/Freedman"},
            {"title": "Manumission", "url": "https://en.wikipedia.org/wiki/Manumission"},
            {"title": "Augustales", "url": "https://en.wikipedia.org/wiki/Augustales"},
            {"title": "Eruption of Mount Vesuvius in 79 AD", "url": "https://en.wikipedia.org/wiki/Eruption_of_Mount_Vesuvius_in_79_AD"},
        ],
    },
    # ------------------------------------------------------------------ 8
    "boudiga": {
        "era": "Claudian–Trajanic", "era_range": "42–103 AD", "region": "Roman Britain",
        "tags": ["Woman", "Native Briton", "Rural", "Britannia", "Subject, never citizen"],
        "epitome": "Born two years before the legions came; lived the slow, uneven Romanization of the Severn valley.",
        "images": [
            {"kind": "commons", "key": "gorgon",
             "file": "File:'Gorgon's Head' - Bath Temple Pediment.jpg",
             "caption": "The 'Gorgon's head' from the temple pediment of Sulis Minerva, Roman Baths, Bath.",
             "why": "Boudiga made a pilgrimage to Aquae Sulis, a day's journey from home."},
            {"kind": "commons", "key": "curse",
             "file": "File:A metal curse tablet (defixio) with a complaint about the theft of a Vilbia.jpg",
             "caption": "A lead curse tablet (defixio) from Bath, complaining of a theft.",
             "why": "She threw a curse tablet just like this into the sacred spring over a stolen possession."},
            {"kind": "commons", "key": "mosaic",
             "file": "File:Hunting Dogs Mosaic, Corinium Museum (Cirencester) (16178671784).jpg",
             "caption": "The 'Hunting Dogs' mosaic, Corinium Museum, Cirencester.",
             "why": "Corinium — the new Roman town that grew up beside her tribe's old territory."},
            {"kind": "ai", "key": "roundhouse",
             "alt": "A Romano-British family outside a thatched roundhouse with cattle in the Severn valley.",
             "caption": "Home: a thatched roundhouse, barley fields and cattle among the Dobunni.",
             "prompt": "A native British (Dobunni) family outside a large thatched roundhouse in the Severn valley; cattle, barley fields, a woman in Celtic dress with a bronze brooch, a Roman road in the distance; late 1st century AD; " + AI_STYLE},
        ],
        "sources": [
            {"title": "Roman Britain", "url": "https://en.wikipedia.org/wiki/Roman_Britain"},
            {"title": "Dobunni", "url": "https://en.wikipedia.org/wiki/Dobunni"},
            {"title": "Boudica", "url": "https://en.wikipedia.org/wiki/Boudica"},
            {"title": "Aquae Sulis (Bath)", "url": "https://en.wikipedia.org/wiki/Aquae_Sulis"},
            {"title": "Bath curse tablets", "url": "https://en.wikipedia.org/wiki/Bath_curse_tablets"},
            {"title": "Corinium Dobunnorum (Cirencester)", "url": "https://en.wikipedia.org/wiki/Corinium_Dobunnorum"},
        ],
    },
    # ------------------------------------------------------------------ 9
    "aurelius-diza": {
        "era": "Crisis of the 3rd c.", "era_range": "233–268 AD", "region": "Danube frontier",
        "tags": ["Man", "Auxiliary cavalry", "Military", "Pannonia", "Syrian provincial"],
        "epitome": "A Syrian trooper on the Danube through the worst half-century Rome ever survived.",
        "images": [
            {"kind": "commons", "key": "mithras",
             "file": "File:Tauroctony, British Museum.jpg",
             "caption": "Mithras slaying the bull (tauroctony), British Museum.",
             "why": "The mystery cult of Mithras was enormously popular among soldiers like Diza."},
            {"kind": "commons", "key": "coin",
             "file": "File:Antoninianus of Gallienus - Obverse.jpg",
             "caption": "Debased antoninianus of the emperor Gallienus (r. 253–268).",
             "why": "Diza was paid in coins like this — by the 260s under 5% silver, nearly worthless."},
            {"kind": "commons", "key": "tombstone",
             "file": "File:Tombstone of Aurelius Monimus.jpg",
             "caption": "Roman tombstone of Aurelius Monimus.",
             "why": "Diza named his son Aurelius Mokimos; auxiliary epitaphs like this fill the Intercisa cemetery."},
            {"kind": "ai", "key": "patrol",
             "alt": "Syrian auxiliary lancers patrolling the snowy Danube frontier by a Roman fort.",
             "caption": "Frontier duty: lance-armed cavalry patrolling the Danube near Intercisa.",
             "prompt": "Roman auxiliary cavalry in scale armour with long lances (contus) patrolling a snowy Danube riverbank beside a stone frontier fort; eastern faces, a standard, cold grey light, Pannonia; mid 3rd century AD; " + AI_STYLE},
        ],
        "sources": [
            {"title": "Crisis of the Third Century", "url": "https://en.wikipedia.org/wiki/Crisis_of_the_Third_Century"},
            {"title": "Battle of Naissus", "url": "https://en.wikipedia.org/wiki/Battle_of_Naissus"},
            {"title": "Mithraism", "url": "https://en.wikipedia.org/wiki/Mithraism"},
            {"title": "Intercisa", "url": "https://en.wikipedia.org/wiki/Intercisa"},
            {"title": "Constitutio Antoniniana", "url": "https://en.wikipedia.org/wiki/Constitutio_Antoniniana"},
            {"title": "Auxilia", "url": "https://en.wikipedia.org/wiki/Auxilia"},
        ],
    },
    # ------------------------------------------------------------------ 10
    "flavius-marcellinus": {
        "era": "Late Empire", "era_range": "375–421 AD", "region": "Constantinople",
        "tags": ["Man", "Bureaucrat", "City", "East", "Christian, Greek-speaking"],
        "epitome": "A Christian clerk in the vast late-Roman bureaucracy of a new capital that called itself Rome.",
        "images": [
            {"kind": "commons", "key": "missorium",
             "file": "File:Disco de Teodosio.jpg",
             "caption": "The Missorium of Theodosius I — the emperor amid his court and officials.",
             "why": "The hierarchy of the late-Roman state that Marcellinus served from its lower rungs."},
            {"kind": "commons", "key": "notitia",
             "file": "File:Notitia Dignitatum - Primicerius notariorum.jpg",
             "caption": "Page from the Notitia Dignitatum — insignia of the chief of the notaries.",
             "why": "The actual register of late-Roman offices; Marcellinus worked in a records bureau like this."},
            {"kind": "commons", "key": "walls",
             "file": "File:Theodosian Walls of Constantinople, Istanbul (24053561188).jpg",
             "caption": "The Theodosian Walls of Constantinople.",
             "why": "\"Constantinople was secure behind its massive walls\" while the West unravelled."},
            {"kind": "ai", "key": "office",
             "alt": "A late-Roman Christian clerk writing on a codex in a Constantinople records office.",
             "caption": "Work: drafting replies to petitions in the scrinium, salary often late.",
             "prompt": "A late-Roman Christian bureaucrat in a tunic with woven clavi writing with a reed pen on a codex at a desk in a Constantinople records office; scrolls and wax tablets, a small icon, a colonnade and church domes through a window; early 5th century AD; " + AI_STYLE},
        ],
        "sources": [
            {"title": "Battle of Adrianople (378)", "url": "https://en.wikipedia.org/wiki/Battle_of_Adrianople"},
            {"title": "Sack of Rome (410)", "url": "https://en.wikipedia.org/wiki/Sack_of_Rome_(410)"},
            {"title": "Notitia Dignitatum", "url": "https://en.wikipedia.org/wiki/Notitia_Dignitatum"},
            {"title": "Missorium of Theodosius I", "url": "https://en.wikipedia.org/wiki/Missorium_of_Theodosius_I"},
            {"title": "Walls of Constantinople", "url": "https://en.wikipedia.org/wiki/Walls_of_Constantinople"},
        ],
    },
}

# --------------------------------------------------------------------------
# Per-paragraph image strip.
#
# One entry per narrative paragraph (in order), placed above that paragraph at
# gallery-thumbnail size. Entry kinds, in priority order:
#   {"local": "paragraph_images/<file>", "caption":..., "credit":...}  commissioned art (copied in)
#   {"reuse": "<key>"}                       reuse one of this life's own `images` artifacts
#   {"theme": "<key>"}                       a shared THEME_IMAGES artifact
#   {"commons": {"key","file","caption","why"}}  a new paragraph-specific Commons artifact
#   None                                     explicit placeholder
# A missing/failed fetch also degrades to a placeholder at build time, so every
# paragraph always has something above it. Trailing comments name the paragraph.
# (List length must equal the life's narrative paragraph count; build.py warns otherwise.)
PARA = {
    "titus-caecilius": [
        {"reuse": "farming"},      # 1. (intro) — the most common Roman life: subsistence farming
        {"theme": "childhood"},    # 2. Childhood and family
        {"theme": "war"},          # 3. Youth and the Social War
        {"theme": "marriage"},     # 4. Marriage and adulthood
        {"theme": "money"},        # 5. Sulla and the proscriptions — grain prices, markets
        {"theme": "marching"},     # 6. Middle years and Caesar's civil war — armies through Italy
        {"theme": "death"},        # 7. Death
    ],
    "kalasiris": [
        {"theme": "agriculture"},  # 1. (intro) — a Sicilian grain estate
        {"reuse": "captive"},      # 2. Enslavement and transport
        {"reuse": "estate"},       # 3. Work — the great estate and its labourers
        {"theme": "war"},          # 4. The context of slave revolts (servile wars)
        {"theme": "marriage"},     # 5. Personal life — an informal union
        {"theme": "death"},        # 6. Death
    ],
    "helene": [
        {"theme": "writing"},      # 1. (intro) — her tax receipts and papyri survive
        {"theme": "childhood"},    # 2. Family and childhood
        {"theme": "marriage"},     # 3. Marriage
        {"theme": "children"},     # 4. Children and mortality
        {"theme": "death"},        # 5. The Antonine Plague
        {"theme": "agriculture"},  # 6. Daily life — canal, fields, village
        {"reuse": "sobek"},        # 7. Later years — her god Sobek
        {"commons": {"key": "fayum2",
                     "file": "File:Fayum mummy portrait (c. 200) - British museum, EA63396.jpg",
                     "caption": "Fayum mummy portrait of a man, c. 200 AD, British Museum.",
                     "why": "Mummy portraits were funerary — painted to accompany the dead like Helene."}},  # 8. Death
    ],
    "petronia-iusta": [
        {"theme": "city"},         # 1. (intro) — born in the Subura of Rome
        {"theme": "childhood"},    # 2. Childhood
        {"reuse": "lamp"},         # 3. Education and skills — she painted lamps
        {"commons": {"key": "fire",
                     "file": "File:Hubert Robert - The Fire of Rome - Google Art Project.jpg",
                     "caption": "Hubert Robert, 'The Fire of Rome' (18th c.), the burning city.",
                     "why": "The Great Fire of 64 AD tore through the crowded insulae she lived among."}},  # 4. The Great Fire
        {"theme": "marriage"},     # 5. Marriage and work
        {"theme": "children"},     # 6. Children
        {"theme": "war"},          # 7. The Year of Four Emperors — civil war
        {"reuse": "latrine"},      # 8. Daily life in the Flavian–Trajanic era
        {"theme": "death"},        # 9. Death
    ],
    "gaius-vibius-celer": [
        {"theme": "marching"},        # 1. (intro) — twenty-five years under the eagles
        {"reuse": "diploma"},         # 2. Enlistment — the army and citizenship
        {"theme": "war"},             # 3. Training and garrison life
        {"reuse": "caelius"},         # 4. The Teutoburg Forest — cenotaph of Caelius
        {"reuse": "kalkriese-mask"},  # 5. (aftermath) — a mask from the battlefield
        {"theme": "death"},           # 6. Germanicus's campaigns — burying the Teutoburg dead
        {"theme": "marriage"},        # 7. Personal life
        {"reuse": "diploma"},         # 8. Discharge and death — the discharge diploma
    ],
    "publius-valerius-messalla": [
        {"theme": "money"},        # 1. (intro) — top of the pyramid, vast wealth
        {"theme": "writing"},      # 2. Family and education
        {"reuse": "arapacis"},     # 3. Career — the cursus honorum (senatorial procession)
        {"theme": "city"},         # 4. The Augustan twilight and Tiberius
        {"theme": "money"},        # 5. Wealth and estates
        {"local": "paragraph_images/publius_family_portrait.png",
         "caption": "Publius Valerius Messalla with his wife and children — a commissioned portrait.",
         "credit": "Commissioned illustration"},  # 6. Marriage and family
        {"theme": "religion"},     # 7. The consulship and Claudius — consular sacrifices
        {"theme": "death"},        # 8. Death
    ],
    "successus": [
        {"reuse": "tavern"},       # 1. (intro) — the food, drink and dice of his counter
        {"theme": "city"},         # 2. Pompeii
        {"theme": "marriage"},     # 3. Personal life and social world
        {"commons": {"key": "earthquake",
                     "file": "File:Pompeian bas-relief, depicting the tilting buildings in the Forum of Pompeii during the AD 62 earthquake, AD 62-79, Exhibition “Pompeii And Santorini. Eternity In A Day” at the Scuderie Del Quirinale, Rome (49904946677).jpg",
                     "caption": "Pompeian relief of buildings toppling in the AD 62 earthquake.",
                     "why": "The 62 AD earthquake wrecked Pompeii seventeen years before Vesuvius finished it."}},  # 4. The earthquake of 62 AD
        {"commons": {"key": "graffiti",
                     "file": "File:Inscriptions found in Pompeii from VI XIV 37, 39, 40 by Geremia Discanno pub 1882.jpg",
                     "caption": "Painted notices and graffiti from a Pompeii street wall (1882 record).",
                     "why": "Pompeii's walls carried election notices, prices and graffiti like his."}},  # 5. Graffiti
        {"reuse": "cast"},         # 6. August 24, 79 AD — the eruption
        {"theme": "death"},        # 7. (closing)
    ],
    "boudiga": [
        {"theme": "agriculture"},  # 1. (intro) — the Severn valley before the legions
        {"theme": "childhood"},    # 2. Pre-conquest childhood
        {"theme": "war"},          # 3. The Claudian invasion
        {"reuse": "mosaic"},       # 4. Cultural transformation — the Roman town of Corinium
        {"theme": "marriage"},     # 5. Marriage and family
        {"commons": {"key": "boudica",
                     "file": "File:Boudicca Statue Westminster Bridge, London (7269568012).jpg",
                     "caption": "Thornycroft's 'Boadicea and Her Daughters', Westminster, London.",
                     "why": "The revolt of Boudica (60–61 AD) that nearly ended Roman Britain."}},  # 6. The Boudican revolt
        {"theme": "city"},         # 7. The long peace — Roman towns flourish
        {"reuse": "gorgon"},       # 8. Religion — the temple of Sulis Minerva at Bath
        {"theme": "death"},        # 9. Death
    ],
    "aurelius-diza": [
        {"theme": "marching"},     # 1. (intro) — a trooper on the Danube frontier
        {"theme": "war"},          # 2. The Crisis of the Third Century
        {"reuse": "mithras"},      # 3. Military life on the Danube — the soldiers' cult of Mithras
        {"commons": {"key": "ludovisi",
                     "file": "File:Grande Ludovisi sarcophagus.jpg",
                     "caption": "The Great Ludovisi sarcophagus, Romans fighting Goths, Palazzo Altemps, Rome.",
                     "why": "The Gothic wars that ravaged the Danube provinces in Diza's lifetime."}},  # 4. Gothic invasions
        {"reuse": "coin"},         # 5. Economic collapse — the debased antoninianus
        {"theme": "marriage"},     # 6. Personal life
        {"theme": "money"},        # 7. The Palmyrene secession and Gallienus
        {"reuse": "tombstone"},    # 8. Death — auxiliary tombstones fill the Intercisa cemetery
    ],
    "flavius-marcellinus": [
        {"theme": "city"},         # 1. (intro) — a clerk in the new capital, Constantinople
        {"theme": "childhood"},    # 2. Childhood
        {"theme": "school"},       # 3. Education
        {"reuse": "walls"},        # 4. Constantinople — the Theodosian walls
        {"theme": "war"},          # 5. The Battle of Adrianople
        {"reuse": "notitia"},      # 6. The fall of Rome and the divided empire (the Notitia lists both halves)
        {"theme": "marriage"},     # 7. Marriage and domestic life
        {"commons": {"key": "christian",
                     "file": "File:Sarcophagus of Junius Bassus.jpg",
                     "caption": "The Sarcophagus of Junius Bassus (359 AD), an early-Christian masterpiece, Rome.",
                     "why": "Christianity now framed every Roman life — and death — as it did Marcellinus's."}},  # 8. Religion and controversy
        {"theme": "death"},        # 9. Death
    ],
}

# Attach each para list onto its profile so build.py / fetch_images.py see it.
for _slug, _para in PARA.items():
    META[_slug]["para"] = _para


# The 906–1000 band: lives this set does not profile.
UNREPRESENTED = {
    "roll_min": 906, "roll_max": 1000, "weight": 95,
    "label": "Unrepresented lives",
    "text": "Priests, gladiators, prostitutes, bandits, miners, nomadic pastoralists, "
            "imperial bureaucrats — and the many children who died before age five and "
            "never lived long enough to have a story in the adult sense.",
}
