# -*- coding: utf-8 -*-
"""
Data for the Canada build of the Himu astrology site. Same principle as the
Bangladesh, USA and UK builds: a curated set of well-known cities, not a
page per town — with genuinely distinct copy per city and honest claims.
Blog section carries original, non-fabricated educational articles.
"""

PHONE = "+916901529861"
PHONE_DISPLAY = "+91 6901529861"
WA = "916901529861"
EMAIL = "support@tarotwithhimu.com"
SITE_BASE = "https://tarotwithhimu.github.io/best-astrologer-in-canada"  # placeholder — update to your real repo/domain

STUDIO_ADDRESS = {
    "streetAddress": "Anandapur Rd, Krishnanagar",
    "addressLocality": "Guwahati",
    "addressRegion": "Assam",
    "postalCode": "781005",
    "addressCountry": "IN",
}

# Grouped by province for the homepage city grid.
NATIONS = ["Ontario", "Quebec", "British Columbia", "Alberta", "Manitoba",
           "Saskatchewan", "Nova Scotia", "New Brunswick", "Newfoundland and Labrador"]

CITIES = [
    dict(name="Toronto", slug="toronto", nation="Ontario",
         hook="Canada's largest city and financial hub",
         blurb=("Toronto's fast pace and huge, multicultural population bring every kind of "
                "question to a session — career moves in a competitive market, cross-cultural "
                "relationships, and family decisions are all common. Sessions are booked over "
                "WhatsApp at whatever evening slot fits a Toronto schedule.")),
    dict(name="Ottawa", slug="ottawa", nation="Ontario",
         hook="the national capital",
         blurb=("Ottawa's clients often work structured, schedule-heavy government or public-"
                "sector jobs, so sessions here are usually booked a little in advance for a "
                "specific evening slot.")),
    dict(name="Mississauga", slug="mississauga", nation="Ontario",
         hook="one of Canada's largest suburban cities, next to Toronto",
         blurb=("Mississauga's large South Asian community means many clients here are already "
                "familiar with Vedic astrology and Kundli matching — sessions are conducted the "
                "same way for every client, over WhatsApp voice or video call.")),
    dict(name="Hamilton", slug="hamilton", nation="Ontario",
         hook="a city built on steel, now reinventing itself",
         blurb=("Hamilton's shift from heavy industry toward healthcare, education and the arts "
                "has brought a steady stream of career-transition questions to sessions here.")),
    dict(name="London", slug="london-ontario", nation="Ontario",
         hook="a mid-sized city in Southwestern Ontario",
         blurb=("London, Ontario's mix of students and established families means both quick "
                "tarot check-ins and full birth-chart sessions are popular here, booked the same "
                "simple way over WhatsApp.")),
    dict(name="Montreal", slug="montreal", nation="Quebec",
         hook="Canada's second-largest city and a bilingual cultural hub",
         blurb=("Montreal's clients bring a genuinely wide range of questions, often shaped by "
                "the city's mix of cultures and languages — love, career and family are all "
                "common themes in a session, conducted entirely online.")),
    dict(name="Quebec City", slug="quebec-city", nation="Quebec",
         hook="a historic provincial capital on the St. Lawrence River",
         blurb=("Quebec City clients often come to a first session curious about tarot before "
                "moving on to a fuller Vedic astrology reading if they want more depth — both are "
                "booked the same simple way, over WhatsApp.")),
    dict(name="Vancouver", slug="vancouver", nation="British Columbia",
         hook="a major Pacific coast city and tech hub",
         blurb=("Vancouver's tech-heavy economy and high cost of living both bring a lot of "
                "career and major-decision questions to a session — a full birth-chart reading "
                "is a popular choice here, booked entirely online.")),
    dict(name="Victoria", slug="victoria", nation="British Columbia",
         hook="the provincial capital, on Vancouver Island",
         blurb=("Victoria's slower pace doesn't change how a session works — clients still book "
                "a WhatsApp or video slot in advance, whether the question is about love, career "
                "or family.")),
    dict(name="Surrey", slug="surrey", nation="British Columbia",
         hook="one of the fastest-growing cities in the Vancouver area",
         blurb=("Surrey's large South Asian community brings frequent requests for Kundli "
                "matching and marriage compatibility readings, alongside the usual career and "
                "family questions.")),
    dict(name="Calgary", slug="calgary", nation="Alberta",
         hook="a major energy-sector hub at the foot of the Rockies",
         blurb=("Calgary's economy has long been tied to the energy sector, and career-timing "
                "questions linked to that industry are common in sessions here, conducted "
                "entirely online.")),
    dict(name="Edmonton", slug="edmonton", nation="Alberta",
         hook="Alberta's capital, known for its river valley",
         blurb=("Edmonton clients often bring focused questions about career changes and "
                "relocation decisions — a birth chart reading, with its long-term timing view, "
                "offers real perspective on both.")),
    dict(name="Winnipeg", slug="winnipeg", nation="Manitoba",
         hook="the heart of the Canadian Prairies",
         blurb=("Winnipeg clients often book sessions around the long winter months, when many "
                "people take stock of career and relationship decisions — all handled over a "
                "scheduled WhatsApp or video call.")),
    dict(name="Saskatoon", slug="saskatoon", nation="Saskatchewan",
         hook="the largest city in Saskatchewan",
         blurb=("Saskatoon's clients span both longtime residents and newer arrivals building new "
                "lives — exactly the kind of transition many clients bring to a tarot or "
                "astrology session, done entirely online.")),
    dict(name="Regina", slug="regina", nation="Saskatchewan",
         hook="Saskatchewan's capital city",
         blurb=("Regina clients book a reading the same way as anywhere else in Canada — a "
                "WhatsApp message with your question or birth details, and a call scheduled at a "
                "convenient time.")),
    dict(name="Halifax", slug="halifax", nation="Nova Scotia",
         hook="a historic Atlantic coast port city",
         blurb=("Halifax's clients often combine a tarot reading with a numerology check on a big "
                "decision — both are available in the same session if you'd like, booked over "
                "WhatsApp.")),
    dict(name="Saint John", slug="saint-john", nation="New Brunswick",
         hook="New Brunswick's oldest incorporated city",
         blurb=("Saint John clients bring the same range of questions as anywhere else — love, "
                "career and family — worked through over a scheduled WhatsApp video call.")),
    dict(name="St. John's", slug="st-johns", nation="Newfoundland and Labrador",
         hook="one of the oldest cities in North America",
         blurb=("St. John's sits at Canada's easternmost edge, and clients here book sessions the "
                "same way as anywhere else in the country — a WhatsApp message sets up a "
                "convenient time, regardless of the distance.")),
]

CITY_BY_SLUG = {c["slug"]: c for c in CITIES}
CITIES_BY_NATION = {n: [] for n in NATIONS}
for c in CITIES:
    CITIES_BY_NATION[c["nation"]].append(c)


# ---------------------------------------------------------------------------
# Blog — original, non-fabricated educational content. No claims about
# specific clients, no invented statistics, no reproduced third-party text.
# Five posts are universal; the Vastu post is adapted for Canadian housing.
# ---------------------------------------------------------------------------

BLOG_POSTS = [
    dict(
        slug="vedic-vs-western-astrology",
        title="Vedic Astrology vs Western Astrology: What's the Difference?",
        excerpt="Two systems, one sky — how Vedic and Western astrology calculate charts differently, and why it matters for your reading.",
        tag="Astrology Basics", icon="moon", read_minutes=5,
        body=[
            ("If you've compared your sun sign on a Western astrology app with what a Vedic "
             "astrologer tells you, you may have noticed they don't always match — and sometimes "
             "the two seem to describe quite different people. That's not an error on either side. "
             "It comes down to a genuinely different starting point for how each system measures "
             "the sky."),
            ("## The Core Difference: Tropical vs Sidereal",
             "Western astrology uses the <strong>tropical zodiac</strong>, which is fixed to the "
             "seasons — the first day of Aries always lines up with the spring equinox, regardless "
             "of where the constellations actually sit in the sky that year. Vedic astrology "
             "(Jyotish) uses the <strong>sidereal zodiac</strong>, which is fixed to the actual "
             "position of the constellations. Because of a slow wobble in the Earth's axis called "
             "precession, these two zodiacs have drifted apart by roughly 24 degrees over the "
             "centuries — which is why your Vedic sign is often one sign 'earlier' than your "
             "Western one."),
            ("## Different Emphasis, Different Tools",
             "Western astrology tends to focus on personality and psychology — what a chart says "
             "about who you are. Vedic astrology puts more weight on timing: the Dasha system maps "
             "out planetary periods across your life, which is why a Vedic reading often talks "
             "about *when* something is likely to unfold, not just *what* it might look like. Vedic "
             "charts also place heavy emphasis on the Moon sign (Rashi) rather than the Sun sign, "
             "since the Moon is considered to govern the mind and emotional nature."),
            ("## Which One Is 'Right'?",
             "Neither system is more correct than the other — they're built on different "
             "foundational choices and different traditions, each internally consistent. Many "
             "people find value in both: a Western chart for a snapshot of personality, and a "
             "Vedic chart for a longer-term view of timing and life direction. If you want a Vedic "
             "reading, the only thing you need is your date, time and place of birth — the more "
             "precise the birth time, the more accurate the chart."),
        ],
    ),
    dict(
        slug="what-is-a-kundli",
        title="What Is a Kundli (Birth Chart) and Why Does It Matter?",
        excerpt="A plain-English guide to what a Kundli actually shows, and what you need to get one drawn up accurately.",
        tag="Vedic Astrology", icon="moon", read_minutes=4,
        body=[
            ("A Kundli — also called a birth chart or natal chart — is a map of exactly where the "
             "Sun, Moon and planets were positioned at the precise moment and place you were born. "
             "It's the starting point for almost every kind of Vedic astrology reading, from career "
             "guidance to marriage matching."),
            ("## What a Kundli Shows",
             "A Kundli is divided into twelve houses, each representing a different area of life — "
             "career, relationships, health, family, wealth and so on — with the planets placed "
             "into whichever house they occupied at your birth. Where a planet sits, and which "
             "other planets it's positioned near or opposite, shapes how that area of your life "
             "tends to unfold."),
            ("## Why Your Exact Birth Time Matters",
             "The houses rotate roughly once every 24 hours, so even a difference of 15–20 minutes "
             "in birth time can shift which house a planet falls into — which can meaningfully "
             "change the reading. If you don't know your exact birth time, check your birth "
             "certificate or hospital records first; a rough estimate can still give a useful "
             "reading, but a precise one is always better."),
            ("## What You Can Actually Do With It",
             "A Kundli isn't just descriptive — it's used practically. The Dasha system built into "
             "it identifies which planetary period you're currently in, which is what lets an "
             "astrologer talk about timing rather than just general tendencies. It's also the "
             "basis for Kundli matching before marriage, and for identifying simple remedies "
             "(gemstones, colours, or routines) tied to a planet that needs strengthening."),
            ("If you'd like your Kundli read, message your date, time and place of birth on "
             "WhatsApp and it'll be prepared ahead of your session."),
        ],
    ),
    dict(
        slug="first-tarot-reading",
        title="How to Prepare for Your First Tarot Reading",
        excerpt="No candles or incense required — here's what actually helps you get the most out of a first tarot session.",
        tag="Tarot", icon="tarot", read_minutes=4,
        body=[
            ("A first tarot reading can feel like a mystery you're not sure how to prepare for. "
             "The good news is there isn't much you need to do — but a little thought beforehand "
             "makes the session more useful."),
            ("## Come With a Question, Not a Test",
             "Tarot works best with a real question you're sitting with — a relationship you're "
             "unsure about, a job offer you're weighing, a decision you keep putting off. Vague "
             "prompts like 'tell me my future' tend to produce vague answers. A specific question "
             "gives the cards something concrete to speak to."),
            ("## Open Questions Work Better Than Yes/No",
             "'Will I get the job?' gives you one bit of information. 'What do I need to understand "
             "about this job opportunity?' gives you something you can actually act on. Tarot is "
             "generally more useful for exploring a situation than for a flat prediction."),
            ("## You Don't Need to Believe in Anything Specific",
             "Tarot doesn't require a particular belief system to be useful — many people treat it "
             "as a structured way to reflect on a situation from angles they hadn't considered, "
             "prompted by the imagery and structure of the cards."),
            ("## What Actually Happens in a Session",
             "Over a WhatsApp voice or video call, you'll share your question, cards are drawn and "
             "laid out in a spread relevant to it, and the reading walks through what each position "
             "and card combination suggests. A typical first session runs about 30 minutes."),
            ("Bring one real question, an open mind, and that's genuinely all the preparation you "
             "need.")
        ],
    ),
    dict(
        slug="numerology-life-path-number",
        title="Numerology Basics: What Your Life Path Number Means",
        excerpt="How to calculate your life path number from your date of birth, and what the nine core numbers represent.",
        tag="Numerology", icon="number", read_minutes=4,
        body=[
            ("Numerology is built on a simple idea: the numbers in your date of birth aren't "
             "random — they can be reduced down to a single core digit that's said to describe "
             "your underlying nature and life direction. That number is your <strong>Life Path "
             "Number</strong>, and it's the most commonly used number in numerology."),
            ("## How to Calculate It",
             "Add together every digit in your full date of birth, then keep reducing the result "
             "down to a single digit. For example, someone born on 17 September 1990 would add "
             "1+7+0+9+1+9+9+0 = 36, then 3+6 = 9. Their Life Path Number is 9. (Two exceptions: "
             "11 and 22 are usually kept as 'Master Numbers' rather than reduced further, as they're "
             "considered to carry extra significance.)"),
            ("## What the Numbers Broadly Represent",
             "<strong>1</strong> — independence and leadership. <strong>2</strong> — partnership "
             "and diplomacy. <strong>3</strong> — creativity and self-expression. <strong>4</strong> "
             "— structure and discipline. <strong>5</strong> — freedom and change. <strong>6</strong> "
             "— responsibility and care for others. <strong>7</strong> — introspection and "
             "analysis. <strong>8</strong> — ambition and material achievement. <strong>9</strong> "
             "— idealism and completion."),
            ("## What It's Useful For",
             "On its own, a Life Path Number is a broad-strokes sketch — most people find it "
             "useful as a starting point rather than a complete picture. It's often combined with "
             "a name-number reading or a full Vedic astrology session for a fuller view, especially "
             "when someone is weighing a big decision like a name change, a business name, or a "
             "wedding date."),
        ],
    ),
    dict(
        slug="vastu-tips-canadian-home",
        title="Simple Vastu Tips for a Canadian Home, Condo or Apartment",
        excerpt="Vastu principles adapted for condos, bungalows and rentals — small, low-cost adjustments rather than renovations.",
        tag="Vastu", icon="home", read_minutes=4,
        body=[
            ("Vastu Shastra is a traditional Indian system of design principles aimed at aligning "
             "a home's layout and energy flow. Most guides assume you're designing a detached "
             "house from scratch, which isn't much help if you're in a rented apartment or a "
             "condo tower in a Canadian city. Here are a few adjustments that don't require any "
             "construction work."),
            ("## Start With the Entrance",
             "In Vastu, the main entrance is considered the point where energy enters the home. "
             "Keep it well lit, uncluttered, and free of boots and coats piled up right by the "
             "door — an easy habit to slip into during a long Canadian winter. A doormat and a "
             "small plant just inside, if you have the space, is a simple, low-cost touch."),
            ("## Declutter the Northeast Corner",
             "The northeast corner of a room or home is traditionally treated as important for "
             "clarity and calm. If you can identify it with a compass app, try to keep that corner "
             "relatively open and clutter-free rather than stacking boxes or bins there — a common "
             "spot for storing winter gear in a smaller apartment."),
            ("## Mind Where You Sleep and Work",
             "Where possible, position your bed so your head points south or east while sleeping, "
             "and set up a desk so you're facing east or north while working — both are considered "
             "supportive directions in Vastu. If your condo's layout doesn't allow it, don't force "
             "a renovation — small adjustments matter more than a perfect layout."),
            ("## Mirrors and the Kitchen",
             "Avoid placing a mirror directly facing the bed. In the kitchen, cooking while facing "
             "east is traditionally preferred if your stove's position allows it."),
            ("## When to Get a Proper Consultation",
             "These are safe, low-cost starting points. For anything bigger — buying a house, "
             "renovating, or troubleshooting a specific ongoing issue — a full Vastu consultation, "
             "done over a video call using your floor plan, gives far more tailored guidance than "
             "any general list can."),
        ],
    ),
    dict(
        slug="kundli-matching-marriage",
        title="Kundli Matching for Marriage: What It Actually Checks",
        excerpt="A breakdown of Ashtakoot Milan — the 36-point compatibility system used in Vedic marriage matching, and what it does and doesn't tell you.",
        tag="Vedic Astrology", icon="moon", read_minutes=5,
        body=[
            ("Kundli matching (also called Kundli Milan or horoscope matching) is a traditional "
             "part of arranging a Vedic-astrology-informed marriage. It's often reduced to 'do the "
             "numbers add up', but the system behind it is more specific than that."),
            ("## The Ashtakoot System",
             "The most common method, Ashtakoot Milan, compares eight specific factors between two "
             "birth charts — things like mental compatibility, health and vitality, and family "
             "temperament — each scored out of a set number of points, for a maximum possible "
             "total of 36. A commonly cited rough guideline is that 18 or more points suggests a "
             "reasonably compatible match, though this varies by region and by astrologer, and "
             "isn't a strict pass/fail line."),
            ("## It's Not Just a Score",
             "A raw number without context can be misleading. Certain individual factors — "
             "particularly ones related to temperament and health compatibility — are usually "
             "weighted more heavily in a proper reading than the total score alone. Two charts can "
             "score moderately and still be read as a strong match if the more heavily weighted "
             "factors align well, and vice versa."),
            ("## What About Mangal Dosha?",
             "Mangal Dosha (sometimes called 'Manglik') refers to a specific placement of Mars in "
             "a chart that's traditionally considered relevant to marital harmony. It's checked "
             "separately from the Ashtakoot score, and having it doesn't automatically rule out a "
             "match — there are recognised remedies and considerations an astrologer factors in."),
            ("## Getting a Reading Done",
             "For a proper Kundli matching session, both people's date, time and place of birth "
             "are needed. The reading covers the Ashtakoot breakdown, Mangal Dosha, and an overall "
             "read of how the two charts interact — not just a single number at the end."),
        ],
    ),
]

BLOG_BY_SLUG = {p["slug"]: p for p in BLOG_POSTS}
