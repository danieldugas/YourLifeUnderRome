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
            {"kind": "commons", "key": "farming",
             "file": "File:Cherchel-Mosaic-lower-register.png",
             "caption": "Mosaic of ploughing and field labour, Cherchell (Caesarea), Roman Africa.",
             "why": "Emmer wheat, oxen and the agricultural year that governed his entire life.",
             "thumb_focus": "right"},
            {"kind": "commons", "key": "lararium",
             "file": "File:Lararium in the atrium of Casa del Menandro (Pompeii) (48442861451).jpg",
             "caption": "A household shrine (lararium), House of the Menander, Pompeii.",
             "why": "Titus worshipped the Lares at a shrine exactly like this before every planting."},
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
            {"kind": "commons", "key": "claudius-britannia",
             "file": "File:Aphrodisias Museum Claudius and Britannica 4638.jpg",
             "caption": "Marble relief of Claudius subduing Britannia, Sebasteion of Aphrodisias, c. 50 AD. Aphrodisias Museum, Turkey.",
             "why": "Imperial propaganda carved during Claudius's reign — the emperor overpowering a personified Britannia. One of the very few surviving period images of anything like a Briton woman, though the figure is a Greco-Roman idealization (an amazon-style caricature), not a portrait of a real one."},
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

# The 906–1000 band: lives this set does not profile.
UNREPRESENTED = {
    "roll_min": 906, "roll_max": 1000, "weight": 95,
    "label": "Unrepresented lives",
    "text": "Priests, gladiators, prostitutes, bandits, miners, nomadic pastoralists, "
            "imperial bureaucrats — and the many children who died before age five and "
            "never lived long enough to have a story in the adult sense.",
}


# --------------------------------------------------------------------------
# A hidden eleventh life. Not in the draft, not linked anywhere, not in the
# 1–1000 bands and not in the legend. The dice reach her about one throw in a
# million; a quiet token in the URL ("?alea=iacta" — "the die is cast", Caesar
# at the Rubicon) rigs every throw to find her. build.py renders her page to
# docs/lives/cleopatra.html and hands the dice a window.SECRET entry.
# --------------------------------------------------------------------------
SECRET = {
    "slug": "cleopatra",
    "name": "Cleopatra VII Philopator",
    "name_native": "Κλεοπάτρα Φιλοπάτωρ",
    "role": "Queen of Egypt",
    "place": "Alexandria",
    "era": "Late Ptolemaic Egypt",
    "era_range": "69–30 BC",
    "born": "69 BC, Alexandria, Ptolemaic Egypt",
    "died": "10/12 August 30 BC, Alexandria — age 39",
    "tags": ["Woman", "Pharaoh", "Ptolemaic dynasty", "Egypt", "One in a million"],
    "epitome": "Not a composite. The last Pharaoh of Egypt — the one life in a million "
               "the dice were never meant to give you.",
    # Dice wiring (read by build.py → lives-index.js → dice.js):
    "magic": "alea",       # a URL containing this token rigs every throw to her
    "odds": 1000000,       # ~1 in a million on an honest throw
    "tagline": "Last Pharaoh of Egypt · 69–30 BC · one throw in a million",
    "narrative": [
        "You are not a composite. Every other life in this roll was assembled out of "
        "demographic tables and the dust of a thousand ordinary people. You are one "
        "person, and you existed. The dice were never supposed to land here — you are "
        "the throw that comes up once in a million, the exception that proves how "
        "crushingly ordinary almost every Roman life really was. You are Cleopatra VII "
        "Philopator, last ruler of the [Ptolemaic dynasty](https://en.wikipedia.org/wiki/Ptolemaic_dynasty), last [Pharaoh](https://en.wikipedia.org/wiki/Pharaoh) of Egypt.",

        "**The house you were born into.** You are Macedonian Greek, not Egyptian by "
        "blood — your line descends from [Ptolemy I Soter](https://en.wikipedia.org/wiki/Ptolemy_I_Soter), one of [Alexander the Great](https://en.wikipedia.org/wiki/Alexander_the_Great)'s"
        "generals, who took Egypt when Alexander's empire was [carved up after 323 BC](https://en.wikipedia.org/wiki/Wars_of_the_Diadochi)."
        "For nearly three hundred years your family has ruled from [Alexandria](https://en.wikipedia.org/wiki/Alexandria), the"
        "greatest city of the age: the [Lighthouse on Pharos](https://en.wikipedia.org/wiki/Lighthouse_of_Alexandria), the [Library](https://en.wikipedia.org/wiki/Library_of_Alexandria) and the"
        "Museum, a [harbour that feeds Rome its grain](https://en.wikipedia.org/wiki/Cura_Annonae#Grain_from_Egypt). The Ptolemies are also a"
        "byword for murder. Siblings marry siblings and then kill them; your own "
        "history is a ledger of poisonings and exiles. You will play that game better "
        "than any of them.",

        "**A childhood among Romans and creditors.** You are born around 69 BC, a "
        "daughter of [Ptolemy XII](https://en.wikipedia.org/wiki/Ptolemy_XII_Auletes) — nicknamed Auletes, the flute-player — a king who "
        "keeps his throne only by borrowing staggering sums from Roman financiers and "
        "buying the favour of Roman senators. You grow up watching Egypt's independence "
        "leak away to Rome one loan at a time. You are formidably educated. [Plutarch](https://en.wikipedia.org/wiki/Plutarch)"
        "says you are [the first of your entire dynasty to bother learning Egyptian](https://en.wikipedia.org/wiki/Egyptian_language), and"
        "that your voice was an instrument you could turn to many languages — Greek, "
        "Egyptian, and the tongues of Ethiopians, Hebrews, Arabs, Syrians, Medes and "
        "Parthians, with rarely a need for an interpreter.",

        "**Caesar.** Your father dies in 51 BC and leaves the throne to you, about "
        "eighteen, jointly with your younger brother-husband Ptolemy XIII, about ten. "
        "It is no partnership; his courtiers drive you out. Then Rome's own civil war "
        "spills onto your shore: [Pompey the Great](https://en.wikipedia.org/wiki/Pompey), fleeing [Julius Caesar](https://en.wikipedia.org/wiki/Julius_Caesar), is murdered"
        "on the Egyptian beach as he steps from the boat. Caesar arrives in pursuit and "
        "you have yourself smuggled to him through the palace — the story says rolled "
        "inside a bedsack. You win him. Ptolemy XIII drowns in the Nile during the war "
        "that follows; you bear Caesar a son, [Caesarion](https://en.wikipedia.org/wiki/Caesarion), in 47 BC; and you spend his "
        "last years partly in Rome as his guest, until the daggers of the [Ides of March](https://en.wikipedia.org/wiki/Assassination_of_Julius_Caesar),"
        "44 BC, send you home.",

        "**Antony.** With Caesar dead, Rome is fought over by his heir [Octavian](https://en.wikipedia.org/wiki/Augustus) and his"
        "lieutenant [Mark Antony](https://en.wikipedia.org/wiki/Mark_Antony). In 41 BC Antony summons you to [Tarsus](https://en.wikipedia.org/wiki/Tarsus,_Mersin) and you arrive on"
        "a barge with gilded stern and purple sails, rowed to the sound of flutes — a "
        "piece of theatre Plutarch could not stop describing. For a decade you and "
        "Antony are allies and lovers against Octavian. You have three children with "
        "him: the twins [Alexander Helios](https://en.wikipedia.org/wiki/Alexander_Helios) and [Cleopatra Selene](https://en.wikipedia.org/wiki/Cleopatra_Selene_II), and [Ptolemy Philadelphus](https://en.wikipedia.org/wiki/Ptolemy_Philadelphus_(son_of_Cleopatra))."
        "At the [Donations of Alexandria](https://en.wikipedia.org/wiki/Donations_of_Alexandria) in 34 BC, Antony parcels out Rome's eastern"
        "provinces to your children as kings and queens — a gift that hands Octavian the "
        "propaganda he needs: a Roman general giving away the Republic to a foreign queen.",

        "**The end.** It comes apart at sea. In 31 BC your combined fleet is broken at "
        "[Actium](https://en.wikipedia.org/wiki/Battle_of_Actium) off the coast of Greece, and you and Antony flee back to Egypt. The "
        "following summer Octavian's army reaches Alexandria. Antony, told falsely that "
        "you are already dead, falls on his sword. You are captured, and rather than be "
        "led through Rome in Octavian's triumph you take your own life — by tradition "
        "the bite of an asp, the [Egyptian cobra](https://en.wikipedia.org/wiki/Egyptian_cobra), though poison is just as likely. You "
        "die in August of 30 BC, thirty-nine years old. Caesarion, Caesar's son and "
        "your co-ruler, is hunted down and killed; \"two Caesars are too many.\" Egypt "
        "becomes a [Roman province](https://en.wikipedia.org/wiki/Egypt_(Roman_province)), its grain and gold the foundation of the empire"
        "Octavian will rule as Augustus.",

        "**How you were remembered.** The victors wrote you down. To Augustus's poets "
        "you are the drunken Eastern sorceress who unmanned a Roman, a danger the "
        "Republic was saved from — and that portrait, not the able administrator, naval "
        "commander and polyglot diplomat who nearly bent Rome's civil wars to Egypt's "
        "advantage, is mostly what survived. Only one of your children outlived the "
        "conquest in freedom: Cleopatra Selene, married off to [King Juba II](https://en.wikipedia.org/wiki/Juba_II) of"
        "[Mauretania](https://en.wikipedia.org/wiki/Mauretania), who named her own son Ptolemy and kept your dynasty's memory"
        "alive at the far western edge of the Roman world. The dice will almost "
        "certainly never bring anyone here again.",
    ],
    "what_shaped": "Three centuries of Ptolemaic dynastic murder, the bottomless wealth "
                   "of Egypt that Rome could not stop coveting, the death-throes of the "
                   "Roman Republic, and the Augustan propaganda machine that decided how "
                   "you would be remembered. And, more than any of it: the simple, vanishing "
                   "improbability of being you at all rather than one of the millions who "
                   "left no name.",
    "images": [
        {"kind": "commons", "key": "bust",
         "file": "File:Marble portrait head of Cleopatra VII, known as the 'Berlin Cleopatra'.jpg",
         "caption": "The 'Berlin Cleopatra' — a marble portrait head carved in her own lifetime, "
                    "c. 40–30 BC. Antikensammlung, Altes Museum, Berlin.",
         "why": "One of only two sculpted portraits securely identified as Cleopatra VII — the "
                "royal diadem and the 'melon' coiffure are her hallmarks. This is, as nearly as "
                "marble allows, her actual face."},
        {"kind": "commons", "key": "painting",
         "file": "File:Posthumous painted portrait of Cleopatra VII of Egypt, from Herculaneum, Italy.jpg",
         "caption": "Posthumous painted portrait of a red-haired royal woman wearing a diadem, "
                    "from Herculaneum — widely identified as Cleopatra VII.",
         "why": "Sealed under Vesuvius in 79 AD and thought to be the only surviving painted "
                "portrait of Cleopatra from the ancient world."},
        {"kind": "ai", "key": "alexandria",
         "alt": "The royal harbour of Alexandria at dusk: palace colonnades, warships, "
                "and the Pharos lighthouse beyond.",
         "caption": "The royal quarter of Alexandria — palaces on the harbour, the Library "
                    "nearby, and the Lighthouse of Pharos beyond.",
         "prompt": "The royal harbour of Ptolemaic Alexandria at golden dusk; marble palace "
                   "colonnades along the waterfront, a gilded royal barge, the great Pharos "
                   "lighthouse with its beacon in the distance, warships at anchor; a regal "
                   "woman in Hellenistic-Egyptian royal dress on a terrace; " + AI_STYLE},
    ],
    "sources": [
        {"title": "Cleopatra (VII)", "url": "https://en.wikipedia.org/wiki/Cleopatra"},
        {"title": "Ptolemaic Kingdom", "url": "https://en.wikipedia.org/wiki/Ptolemaic_Kingdom"},
        {"title": "Ptolemy XII Auletes", "url": "https://en.wikipedia.org/wiki/Ptolemy_XII_Auletes"},
        {"title": "Caesarion (Ptolemy XV)", "url": "https://en.wikipedia.org/wiki/Caesarion"},
        {"title": "Mark Antony", "url": "https://en.wikipedia.org/wiki/Mark_Antony"},
        {"title": "Donations of Alexandria (34 BC)", "url": "https://en.wikipedia.org/wiki/Donations_of_Alexandria"},
        {"title": "Battle of Actium (31 BC)", "url": "https://en.wikipedia.org/wiki/Battle_of_Actium"},
        {"title": "Cleopatra Selene II", "url": "https://en.wikipedia.org/wiki/Cleopatra_Selene_II"},
        {"title": "Library of Alexandria", "url": "https://en.wikipedia.org/wiki/Library_of_Alexandria"},
    ],
}
