#!/usr/bin/env python3
"""Assemble atlas.html, injecting the world-map paths extracted from the repo."""
import json

land   = open('_land.txt').read()
sphere = open('_sphere.txt').read()
coast  = open('_coast.txt').read()

# projection fitted from the existing region coordinates (residual < 0.7px)
PY = [3.048e-07, 1.50911e-05, -3.1195183055, 267.6541000389]
PS = [-8.72e-08, -0.0001292801, 6.92595e-05, 2.6898377856]

def poly(p, v):
    r = 0.0
    for c in p:
        r = r * v + c
    return r

def project(lat, lng):
    return round(500 + lng * poly(PS, lat), 2), round(poly(PY, lat), 2)

# ---------------------------------------------------------------- entries
# kind: artist | grant | prize | residency | network
# certainty: "held" = stated in the project's own files or well established
#            "check" = base or details should be verified before relying on it
E = [
 # ── artists: the career models ───────────────────────────────────────────
 dict(id="jsmith", name="Jean Smith", kind="artist", place="Vancouver, British Columbia",
   lat=49.28, lng=-123.12, certainty="held",
   brief="11×14 inch portraits at $100 USD, sold on Facebook since 2016. More than 1,500 sold. Left the day job. Surplus income directed toward founding a free artist residency.",
   why="The proof that small work is a different path rather than a lesser one. Priced for access as an explicitly political choice, descended from Fugazi's $5 shows. Monthly expenses of $1,000, with everything above that going to the fund.",
   take="What does not transfer: thirty-five years of cultural standing through Mecca Normal, and a New York Times Magazine feature in 2021. At peak she worked fifteen-hour days, seven days a week. What does transfer: named series, repeat collectors, and a fixed format that removes every pricing decision.",
   src=["Covered by CBC, The Tyee, the New York Times Magazine and Democracy Now"]),

 dict(id="cwinner", name="Caitlin Winner", kind="artist", place="United States",
   lat=42.25, lng=-73.79, certainty="check",
   brief="Painted at weekends while working in technology. A visible arc from roughly 2021 to 2025 through juried shows, prizes, a residency and press, then gallery representation.",
   why="The closest visible analogue to a practice run alongside a full-time career. Manifest biennial, the Royal Institute of Oil Painters, First Street Gallery, the Martha Boschen Porter Fund, a Vermont Studio Center residency, a cookbook commission, a Studio Visit cover, Hyperallergic, then Carrie Haddad and Galerie Mokum.",
   take="The order is the lesson. Juried shows and grants came first, press followed, representation followed that, and teaching sits on top of the credibility rather than substituting for it.",
   src=["Base location on this map is approximate and should be verified"]),

 dict(id="zfrank", name="Zoey Frank", kind="artist", place="United States",
   lat=40.58, lng=-105.08, certainty="check",
   brief="Gallery representation, grants and international prizes, with roughly one new online course a year at $185 to $350: taught live, recorded the same day, then sold as evergreen recordings.",
   why="The teaching model the Foundations plan is built against. Four sessions of about two and a half hours each, so around ten hours of delivery. Students find her by searching for what they want to learn rather than because they were already collectors.",
   take="Foundations runs eighteen hours against her ten, which is what supports a higher price. The risk is over-designing it. Version one should be closer to her format than to an institutional course.",
   src=["Base location on this map is approximate and should be verified"]),

 dict(id="fyukh", name="Flora Yukhnovich", kind="artist", place="London, United Kingdom",
   lat=51.51, lng=-0.13, certainty="held",
   brief="MA in 2017, found on Instagram by a dealer, seven-figure auction sales within four years, now with Hauser & Wirth alongside Victoria Miro.",
   why="Held in the atlas as the route that cannot be planned for and should not be treated as impossible either. What transfers is a singular visual language with real art-historical grounding.",
   take="Nothing about the sequence is reproducible. The grounding is. A body of work that is arguing with art history from the inside is legible to people who can move it, and that legibility is built rather than discovered.",
   src=[]),

 # ── artists: the inquiry ────────────────────────────────────────────────
 dict(id="muholi", name="Zanele Muholi", kind="artist", place="South Africa",
   lat=-29.86, lng=31.02, certainty="held",
   brief="Faces and Phases: over 500 portraits of Black lesbian and trans South Africans. Somnyama Ngonyama: self-portraits in which the photographed body takes the full frame without apology.",
   why="Week 09, Rupture. The work documents lives subject to rupture by systemic violence and turns that rupture into sovereignty rather than into evidence.",
   take="The full-frame decision is the argument. Nothing about the composition asks permission.",
   src=[]),

 dict(id="baez", name="Firelei Báez", kind="artist", place="New York, United States",
   lat=40.71, lng=-74.01, certainty="held",
   brief="Large-scale installations of figures merging with historical documents and cartographic records of colonial violence.",
   why="Phase III. The insistence that the body of the historically erased is also the body in mystical encounter. For the colonised subject the via negativa is the condition of survival made luminous rather than a chosen practice.",
   take="Painting directly onto archival documents makes the argument structurally rather than by depiction.",
   src=[]),

 dict(id="salcedo", name="Doris Salcedo", kind="artist", place="Bogotá, Colombia",
   lat=4.71, lng=-74.07, certainty="held",
   brief="Furniture embedded in concrete, rose petals filling the cracks of a plaza floor, chairs suspended on an institutional facade.",
   why="Week 39, non-extractive love as political grief. The work holds the disappeared and the murdered without monumentalising them and without asking anything of the viewer in return.",
   take="Refusing the monument is the ethical move, and it is a compositional decision before it is a political one.",
   src=[]),

 dict(id="fgt", name="Felix Gonzalez-Torres", kind="artist", place="New York, United States",
   lat=40.75, lng=-73.98, certainty="held",
   brief="Candy piles whose weight equals the weight of a partner who died of AIDS. The work is completed by being taken, and diminished by being received.",
   why="The most precise visual definition of non-extractive love in contemporary art. You cannot possess it. You can only receive it, and receiving it consumes it.",
   take="The direct challenge to a practice that sells objects. Whatever else the studies series is, it should know this work exists.",
   src=[]),

 dict(id="hwami", name="Kudzanai-Violet Hwami", kind="artist", place="London, United Kingdom",
   lat=51.53, lng=-0.10, certainty="held",
   brief="Large-scale paintings in which figures are fragmented, multiplied and reconstructed across intensely coloured surfaces.",
   why="Week 40. The wound as generative, held as a queer Zimbabwean visual practice. The body marked by exclusion has been given, by that marking, a particular quality of vision.",
   take="Fragmentation used as construction rather than as damage.",
   src=["Exhibited at Victoria Miro, the MCA Chicago, and included in the 2019 Venice Biennale"]),

 dict(id="tlewis", name="Tau Lewis", kind="artist", place="Toronto, Canada",
   lat=43.65, lng=-79.38, certainty="held",
   brief="Hand-sewn sculptural figures made from found and reclaimed leather, fabric and hair.",
   why="Week 04, trauma metabolized. The work understands metabolising as literal stitching, the broken material made whole through sustained manual attention.",
   take="The nearest artist on this map geographically, and one of the closest in method. Sustained manual attention is the whole technique.",
   src=["Exhibited at MoMA PS1 and the Museum of Arts and Design, and included in the 2022 Whitney Biennial"]),

 dict(id="kusama", name="Yayoi Kusama", kind="artist", place="Tokyo, Japan",
   lat=35.68, lng=139.69, certainty="held",
   brief="Seven decades of obsessive accumulation: dots, nets, infinity rooms. Living voluntarily in a psychiatric institution since 1977 and going to the studio every day.",
   why="Week 05, the difficult side of practice. The work is not made in spite of psychiatric disturbance. It is made from it, with rigorous discipline.",
   take="The daily studio attendance is the part worth taking. Discipline is what makes the difficult material usable rather than merely present.",
   src=[]),

 dict(id="halsey", name="Lauren Halsey", kind="artist", place="Los Angeles, United States",
   lat=33.98, lng=-118.29, certainty="held",
   brief="Carved hieroglyph columns, community structures, dense archival assemblages of South Central Los Angeles culture.",
   why="Week 28, the Engaged Path synthesis. Inner devotion and outer transformation held as one continuous act.",
   take="The studio is in the neighbourhood, and the work insists those two facts are inseparable. A practice rooted in a place rather than shipped from one.",
   src=[]),

 dict(id="syms", name="Martine Syms", kind="artist", place="Los Angeles, United States",
   lat=34.05, lng=-118.24, certainty="held",
   brief="Video and installation treating Black everyday life as archive, as theory, and as art: vernacular speech, casual gesture, domestic ritual.",
   why="Week 27, no specialness required. The ordinary is already doing the work and does not need elevating first.",
   take="The direct authority for a studies series built on the unremarkable.",
   src=[]),

 dict(id="morandi", name="Giorgio Morandi", kind="artist", place="Bologna, Italy",
   lat=44.49, lng=11.34, certainty="held",
   brief="Four decades painting the same small collection of bottles, jars and boxes on the same studio table, slightly rearranged, in shifting light.",
   why="Week 27. The most radical refusal of specialness available. Nothing new is required.",
   take="The historical case for a fixed format and a monthly rhythm. Constraint as the source rather than the limit.",
   src=[]),

 dict(id="kahlo", name="Frida Kahlo", kind="artist", place="Mexico City, Mexico",
   lat=19.43, lng=-99.13, certainty="held",
   brief="The Broken Column: the spine as a crumbling pillar, the body pierced by nails, a medical corset.",
   why="Week 40. A painting made from the darkest place that becomes, through the absolute refusal of comfort, something that has accompanied millions of people in their own darkness.",
   take="The wound is not the enemy of the work. It is its ground.",
   src=[]),

 dict(id="tillmans", name="Wolfgang Tillmans", kind="artist", place="Berlin, Germany",
   lat=52.52, lng=13.40, certainty="held",
   brief="Darkroom abstractions made without a camera, by exposing light-sensitive paper to light directly.",
   why="Week 40. What looks like damage is the record of a direct encounter between light and surface. The most intimate possible image, made with no apparatus in between.",
   take="Removing the apparatus is available in graphite too. A line made without an intention to depict is the same move.",
   src=[]),

 dict(id="popova", name="Maria Popova", kind="network", place="New York, United States",
   lat=40.68, lng=-73.94, certainty="held",
   brief="The Marginalian. The mentor for the writing, and the reason the register is what it is.",
   why="What is borrowed is a relationship rather than a style: writing from inside a question that is not finished with, holding several thinkers in the same room, letting them disagree, and trusting the reader to follow without being managed.",
   take="Intimacy with the question is the standard every Dear Ordinary post is measured against. Where the writing gets thin it is usually because it started explaining rather than staying inside the question.",
   src=[]),

 # ── opportunities: British Columbia ─────────────────────────────────────
 dict(id="bcac", name="BC Arts Council", kind="grant", place="Victoria, British Columbia",
   lat=48.43, lng=-123.37, certainty="held",
   brief="The provincial arts funder, with programs for individual artists including project assistance and professional development.",
   why="The closest significant funder geographically and the most natural first application. Provincial residency requirements are met, and a professional practice with an exhibition and teaching record is the applicant profile these programs are built around.",
   take="Amounts, streams and deadlines change annually and none are recorded here. Check the current round before building any plan on it. Ranked first among funders by hours returned, because a grant buys studio time and a sale consumes it.",
   src=["Verify the current programs, eligibility and deadlines directly"]),

 dict(id="vanfound", name="Vancouver Foundation", kind="grant", place="Vancouver, British Columbia",
   lat=49.28, lng=-123.11, certainty="held",
   brief="A community foundation making grants across the region, including in arts and culture.",
   why="Regional rather than discipline-specific, which sometimes suits a practice sitting between art, disability studies and counselling psychology better than an arts-only stream does.",
   take="Read the current priorities before assuming fit. Community foundations shift focus more often than arts councils do.",
   src=["Verify current programs and eligibility directly"]),

 dict(id="cityvan", name="City of Vancouver cultural grants", kind="grant",
   place="Vancouver, British Columbia", lat=49.26, lng=-123.14, certainty="held",
   brief="Municipal cultural grant programs supporting artists and organisations in the city.",
   why="Municipal money is often the least contested and the most accessible early, and a municipal grant on the record strengthens the provincial and federal applications that follow.",
   take="Check residency and eligibility carefully. Municipal programs are usually tied to the city boundary rather than the metropolitan area.",
   src=["Verify current programs and eligibility directly"]),

 dict(id="artsumbrella", name="Arts Umbrella", kind="network", place="Vancouver, British Columbia",
   lat=49.27, lng=-123.13, certainty="held",
   brief="Vancouver arts education organisation for children and young people. Part of every studies sale goes here.",
   why="Held in the atlas because it is already part of the practice rather than a target for it. The studies series funds a social good, which is the structure read correctly from Jean Smith's model.",
   take="This is a commitment rather than an opportunity. It is on the map so the map is honest about where the money goes.",
   src=[]),

 dict(id="ecuad", name="Emily Carr University", kind="network", place="Vancouver, British Columbia",
   lat=49.27, lng=-123.09, certainty="held",
   brief="Where the foundation year happened, and where seven years of staff work across three roles followed.",
   why="The network most likely to fill a first Foundations cohort, and a much easier ask than anything else on the list. The premise of the course comes directly from this curriculum.",
   take="Keep the institution out of any marketing language implying affiliation or endorsement. Her own experience is hers to teach, and seven years on staff means she will know exactly how that reads from the inside.",
   src=[]),

 dict(id="ssnap", name="Salt Spring National Art Prize", kind="prize",
   place="Salt Spring Island, British Columbia", lat=48.82, lng=-123.50, certainty="held",
   brief="A national juried art prize and exhibition held on Salt Spring Island.",
   why="A juried national exhibition within the province. Juried shows are the first step in the route that Winner and Frank both took, and this one is close enough to attend.",
   take="Verify the current cycle, entry requirements and fees. Juried prize calendars move.",
   src=["Verify the current cycle directly"]),

 # ── opportunities: national ─────────────────────────────────────────────
 dict(id="cca", name="Canada Council for the Arts", kind="grant", place="Ottawa, Canada",
   lat=45.42, lng=-75.70, certainty="held",
   brief="The federal arts funder. Explore and Create is the program stream most relevant to an individual visual artist developing a body of work.",
   why="The largest single source of funded studio hours available to a Canadian artist, and the one that most directly converts an application into time. Ranked first alongside the provincial council among all income options by hours returned.",
   take="Competitive, and stronger with an exhibition and grant record behind it, which is the argument for applying provincially and municipally first. Amounts and deadlines are not recorded here and should be checked against the current round.",
   src=["Verify current programs, eligibility and deadlines directly"]),

 dict(id="hnat", name="Hnatyshyn Foundation", kind="prize", place="Ottawa, Canada",
   lat=45.41, lng=-75.68, certainty="held",
   brief="A national foundation supporting Canadian artists through awards and grants.",
   why="National recognition of the kind that compounds. An award on the record changes how every subsequent application reads.",
   take="Check which programs are currently open and whether any require nomination rather than application.",
   src=["Verify current programs and nomination requirements directly"]),

 dict(id="kingston", name="Kingston Prize", kind="prize", place="Kingston, Ontario",
   lat=44.23, lng=-76.49, certainty="held",
   brief="A national competition for Canadian portraiture, exhibited and toured.",
   why="Directly aligned with a figurative and narrative practice. Portraiture is the specific subject rather than a category the work has to be argued into.",
   take="Verify the current cycle and whether it runs annually or biennially before planning a year around it.",
   src=["Verify the current cycle directly"]),

 dict(id="rbc", name="RBC Canadian Painting Competition", kind="prize", place="Toronto, Ontario",
   lat=43.64, lng=-79.39, certainty="check",
   brief="A national painting competition for emerging Canadian artists.",
   why="Held here as a national painting-specific prize aimed at the emerging category.",
   take="Confirm the competition is currently running and what its eligibility defines as emerging, since age and career-stage caps are common and change. Do not build a plan on this entry without checking it first.",
   src=["Status and eligibility both need verifying before use"]),

 # ── opportunities: international ────────────────────────────────────────
 dict(id="vsc", name="Vermont Studio Center", kind="residency", place="Johnson, Vermont",
   lat=44.64, lng=-72.68, certainty="held",
   brief="A residency programme for visual artists and writers, with fellowships available.",
   why="On Caitlin Winner's route, and one of the few residencies that a practice run alongside full-time work can realistically fit, because residencies are measured in weeks rather than months.",
   take="The constraint is not the application. It is finding a block of leave. Verify current session lengths and fellowship deadlines.",
   src=["Verify current sessions and fellowship deadlines directly"]),

 dict(id="manifest", name="Manifest", kind="prize", place="Cincinnati, Ohio",
   lat=39.10, lng=-84.51, certainty="held",
   brief="A gallery and drawing centre running international juried exhibitions and publications.",
   why="On Winner's route, and one of the more accessible international juried listings for an artist without representation.",
   take="Verify current calls, fees and the shipping requirements for accepted work, which for an artist in British Columbia is a real cost.",
   src=["Verify current calls and requirements directly"]),

 dict(id="rioc", name="Royal Institute of Oil Painters", kind="prize", place="London, United Kingdom",
   lat=51.51, lng=-0.13, certainty="held",
   brief="An annual open exhibition at the Mall Galleries in London.",
   why="On Winner's route. An international open exhibition with a long history and a clear submission process.",
   take="Verify the current call, fees and whether digital submission is accepted at the first stage. Shipping accepted work internationally is the practical constraint.",
   src=["Verify the current call and requirements directly"]),

 dict(id="firstst", name="First Street Gallery", kind="network", place="New York, United States",
   lat=40.74, lng=-74.00, certainty="held",
   brief="A New York artist-run gallery that has held national juried exhibitions.",
   why="On Winner's route. Artist-run spaces are where the exhibition record usually begins, and they are considerably more open than commercial representation.",
   take="Verify what the gallery currently runs and whether juried opportunities are still part of it.",
   src=["Verify current programming directly"]),
]

for e in E:
    e['x'], e['y'] = project(e['lat'], e['lng'])

data_json = json.dumps(E, ensure_ascii=False, separators=(',', ':'))

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="robots" content="noai, noimageai" />
<title>Atlas &middot; Studio Day</title>
<meta name="description" content="The artists the practice is oriented toward, and the grants, prizes and residencies that return hours to it." />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Asap:ital,wght@0,400;0,500;0,600;1,400&amp;display=swap" rel="stylesheet" />
<link rel="stylesheet" href="style.css" />
<style>
  :root{--land:#eceae7;--land-line:#dcd9d5;--coast:#c9c5c1;}
  .map-hold{position:relative;background:var(--panel);border:1px solid var(--hair);
    border-radius:8px;overflow:hidden;}
  .map{display:block;width:100%;height:auto;touch-action:none;cursor:grab;}
  .map.dragging{cursor:grabbing;}
  .sphere{fill:#ffffff;stroke:var(--coast);stroke-width:1;vector-effect:non-scaling-stroke;}
  .land{fill:var(--land);stroke:none;}
  .coast{fill:none;stroke:var(--coast);stroke-width:.9;vector-effect:non-scaling-stroke;}
  .mk{cursor:pointer;outline:none;}
  .mk .hit{fill:transparent;}
  .mk .halo{fill:var(--c);opacity:0;transition:opacity .2s var(--ease);}
  .mk:hover .halo,.mk.is-sel .halo{opacity:.22;}
  .mk .core{fill:var(--c);stroke:#fff;stroke-width:1.1;vector-effect:non-scaling-stroke;}
  .mk.is-sel .core{stroke-width:2;}
  .mk.is-dim{opacity:.18;pointer-events:none;}
  .zoom-controls{position:absolute;right:12px;bottom:12px;display:flex;flex-direction:column;gap:6px;}
  .zoombtn{width:30px;height:30px;border-radius:6px;border:1px solid var(--hair);
    background:var(--paper);color:var(--ink);font-size:15px;line-height:1;cursor:pointer;
    font-family:inherit;transition:all .2s var(--ease);}
  .zoombtn:hover{border-color:var(--stone);color:var(--ink-strong);}
  .legend{display:flex;flex-wrap:wrap;gap:14px;margin:16px 0 0;}
  .lg{display:inline-flex;align-items:center;gap:7px;font-size:11.5px;color:var(--stone);}
  .lg .sw{width:9px;height:9px;border-radius:50%;}
  .lg .sw.sq{border-radius:2px;}
  .certnote{font-size:12.5px;color:var(--stone);margin:10px 0 0;}
  .roster{border-top:1px solid var(--hair);padding-top:16px;}
  .roster summary{font-size:11px;letter-spacing:.16em;text-transform:uppercase;
    color:var(--stone);font-weight:600;cursor:pointer;padding:6px 0;}
  .roster h3{font-size:13px;font-weight:600;margin:22px 0 8px;letter-spacing:.02em;}
  .roster p{font-size:14.5px;margin:0 0 12px;}
  .roster .rn{font-weight:600;color:var(--ink-strong);}
</style>
</head>
<body>
  <div class="wrap">

    <nav class="topbar" aria-label="Studio Day">
      <a class="mark" href="index.html">Studio&nbsp;Day</a>
      <div class="navlinks">
        <a href="atlas.html" aria-current="page">Atlas</a>
        <a href="writing.html">Writing</a>
        <a href="documentation.html">Documentation</a>
        <a href="year.html">The Year</a>
        <a href="studies.html">Studies</a>
        <a href="teaching.html">Teaching</a>
      </div>
    </nav>

    <header class="hero">
      <p class="eyebrow"><span>Atlas</span><span class="status">One map, two layers</span></p>
      <h1>The people, and the <em>hours they make possible</em></h1>
      <p class="lede">Two things worth holding in the same view. The artists the work is in conversation with, and the funders, prizes and residencies that return hours to a practice run alongside a career. They sit on one map because the second follows the first. The route that Winner and Frank both took runs through juried shows, grants and residencies before it reaches anything else.</p>
    </header>

    <section class="stage" aria-label="The atlas">
      <div>
        <div class="controls">
          <div class="chips" id="kindfilter" role="group" aria-label="Filter the atlas"></div>
          <span class="count" id="count"></span>
        </div>
        <div class="map-hold">
          <svg class="map" id="map" viewBox="0 0 1000 536" role="group" aria-label="World map of artists and opportunities">
            <g id="viewport">
              <path class="sphere" d="__SPHERE__" />
              <path class="land" d="__LAND__" />
              <path class="coast" d="__COAST__" />
              <g id="markers"></g>
            </g>
          </svg>
          <div class="zoom-controls">
            <button class="zoombtn" id="zoom-in" aria-label="Zoom in">+</button>
            <button class="zoombtn" id="zoom-out" aria-label="Zoom out">&minus;</button>
            <button class="zoombtn" id="zoom-reset" aria-label="Reset view">&#8634;</button>
          </div>
        </div>
        <div class="legend" id="legend"></div>
        <p class="certnote">Drag to move, scroll to zoom. Entries marked <span class="flag">verify</span> hold a detail that has not been confirmed, usually a base location or a current funding round.</p>
      </div>

      <div class="panel" id="panel" aria-live="polite">
        <p class="panel-empty" id="panel-empty">Choose a marker. Artists open with why they are held here and what actually transfers to the studio. Opportunities open with what they are, whether they fit, and what has to be checked before anything is planned around them.</p>
        <div id="panel-content" hidden></div>
      </div>
    </section>

    <section class="essay">
      <h2>Why funders and artists share a map</h2>
      <p>The binding constraint on this practice is paid hours rather than audience or talent. Twenty-five thousand dollars of grant money and twenty-five thousand of print sales are not equivalent, because the grant returns hours and the sales consume them. Ranked by hours returned: grants, institutional commissioning, teaching priced to institutions rather than hobbyists, then retail.</p>
      <p>The artists on this map who built sustainable practices did it in a particular order. Juried shows, prizes, grants, residencies and press came first. Gallery representation followed. Teaching arrived as the income that follows credibility rather than as the thing that builds it. None of the first three built a career through an e-commerce funnel.</p>
      <p>Jean Smith took a genuinely different route to a real outcome, and it is on this map for that reason. Small work is not a lesser path.</p>

      <h2>What is not available</h2>
      <p>A research-creation PhD or MFA is not on this map because it is not on the table. The education path runs from an MSc in Disability Studies to an MA in Counselling Psychology toward registration, and then a PhD. Academia will not fund studio time along the way. The practice is funded by a professional career and runs alongside years of part-time graduate study.</p>
      <p>The coherence is real even so. Disability studies, counselling psychology and a thesis on the body as the site of the sacred are one inquiry approached from three directions. Week one argues that you cannot sense another person's inner life if you were trained to ignore your own, which is a counselling claim, a disability studies claim and a painting claim at once.</p>

      <h2>How to use the opportunity layer</h2>
      <p>No amounts and no deadlines are recorded anywhere on this page. Both change every year, and a reference document holding stale figures is worse than one holding none, because stale figures get trusted.</p>
      <p>What is recorded is what each one is, whether it fits this practice, and what has to be verified before a year is planned around it. Apply municipally and provincially before federally, because a grant record makes every subsequent application read differently.</p>

      <h2>Held here but not placed</h2>
      <p>Joy Kinna is part of the reference material and is not on the map, because her base is not recorded anywhere in the project files and guessing at it would put an unverified claim on a document meant to be trusted. The model taken from her practice is the one already in use: a portfolio site, a PDF catalogue of originals sold by reply, and a separate print store linked from it.</p>
    </section>

    <section class="essay">
      <h2>Read it as a list</h2>
      <details class="roster">
        <summary>Open every entry as text</summary>
        <div id="rosterbody"></div>
      </details>
    </section>

    <footer>
      <span class="copy">&copy; 2026 Andrea Robin Studio</span>
      <div class="fnav">
        <a href="index.html">Studio Day</a>
        <a href="writing.html">Writing</a>
        <a href="year.html">The Year</a>
      </div>
    </footer>

  </div>

<script id="atlas-data" type="application/json">__DATA__</script>
<script>
(function(){
"use strict";

var KINDS = {
  artist:    {label:"Artists",            color:"#7d7469", shape:"circle"},
  network:   {label:"Network",            color:"#a2917a", shape:"circle"},
  grant:     {label:"Grants",             color:"#7f938c", shape:"square"},
  prize:     {label:"Prizes",             color:"#8496a0", shape:"square"},
  residency: {label:"Residencies",        color:"#8f8798", shape:"square"}
};

var E = JSON.parse(document.getElementById("atlas-data").textContent);
var byId = {};
E.forEach(function(e){ byId[e.id] = e; });

var svg = document.getElementById("map");
var vp = document.getElementById("viewport");
var markers = document.getElementById("markers");
var panelEmpty = document.getElementById("panel-empty");
var panelContent = document.getElementById("panel-content");
var filterWrap = document.getElementById("kindfilter");
var legend = document.getElementById("legend");
var countEl = document.getElementById("count");

var view = {x:0, y:0, k:1};
var activeKind = "all";
var selectedId = null;

function apply(){
  vp.setAttribute("transform",
    "translate(" + view.x + "," + view.y + ") scale(" + view.k + ")");
}

function buildMarkers(){
  markers.innerHTML = E.map(function(e){
    var K = KINDS[e.kind];
    var shape = K.shape === "square"
      ? '<rect class="core" x="-4.2" y="-4.2" width="8.4" height="8.4" rx="1.4"/>'
      : '<circle class="core" r="4.6"/>';
    return '<g class="mk" data-id="' + e.id + '" transform="translate(' + e.x + ',' + e.y + ')" ' +
           'style="--c:' + K.color + '" tabindex="0" role="button" aria-label="' + e.name + '">' +
           '<circle class="halo" r="13"/>' + shape +
           '<circle class="hit" r="13"/></g>';
  }).join("");

  Array.prototype.forEach.call(markers.querySelectorAll(".mk"), function(g){
    g.addEventListener("click", function(ev){ ev.stopPropagation(); select(g.getAttribute("data-id")); });
    g.addEventListener("keydown", function(ev){
      if (ev.key === "Enter" || ev.key === " "){ ev.preventDefault(); select(g.getAttribute("data-id")); }
    });
  });
}

function buildFilters(){
  var html = '<button class="chip is-active" data-kind="all" aria-pressed="true">Everything</button>';
  Object.keys(KINDS).forEach(function(k){
    html += '<button class="chip" data-kind="' + k + '" aria-pressed="false">' +
            '<span class="dot" style="background:' + KINDS[k].color + '"></span>' +
            KINDS[k].label + '</button>';
  });
  filterWrap.innerHTML = html;
  Array.prototype.forEach.call(filterWrap.querySelectorAll(".chip"), function(b){
    b.addEventListener("click", function(){
      activeKind = b.getAttribute("data-kind");
      Array.prototype.forEach.call(filterWrap.querySelectorAll(".chip"), function(o){
        var on = o === b;
        o.classList.toggle("is-active", on);
        o.setAttribute("aria-pressed", on ? "true" : "false");
      });
      applyFilter();
    });
  });

  legend.innerHTML = Object.keys(KINDS).map(function(k){
    return '<span class="lg"><span class="sw' + (KINDS[k].shape === "square" ? " sq" : "") +
           '" style="background:' + KINDS[k].color + '"></span>' + KINDS[k].label + '</span>';
  }).join("");
}

function applyFilter(){
  var n = 0;
  Array.prototype.forEach.call(markers.querySelectorAll(".mk"), function(g){
    var e = byId[g.getAttribute("data-id")];
    var on = activeKind === "all" || e.kind === activeKind;
    g.classList.toggle("is-dim", !on);
    if (on) n++;
  });
  countEl.textContent = n + (n === 1 ? " entry" : " entries");
}

function select(id){
  selectedId = id;
  var e = byId[id];
  if (!e) return;
  Array.prototype.forEach.call(markers.querySelectorAll(".mk"), function(g){
    g.classList.toggle("is-sel", g.getAttribute("data-id") === id);
  });

  var flag = e.certainty === "check" ? '<span class="flag">verify</span>' : "";
  var src = e.src && e.src.length
    ? '<h3>Notes</h3><ul class="srclist">' +
      e.src.map(function(s){ return "<li>" + s + "</li>"; }).join("") + "</ul>"
    : "";
  var isArtist = e.kind === "artist" || e.kind === "network";

  panelEmpty.hidden = true;
  panelContent.hidden = false;
  panelContent.innerHTML =
    '<p class="p-eyebrow">' + KINDS[e.kind].label + " \\u00b7 " + e.place + "</p>" +
    '<h2 class="p-title">' + e.name + flag + "</h2>" +
    '<div class="tabs" role="tablist">' +
      '<button class="tab is-active" data-l="a" role="tab">In brief</button>' +
      '<button class="tab" data-l="b" role="tab">' + (isArtist ? "Why it is here" : "Fit") + "</button>" +
      '<button class="tab" data-l="c" role="tab">' + (isArtist ? "What transfers" : "Before applying") + "</button>" +
    "</div>" +
    '<div class="layer" data-l="a"><p>' + e.brief + "</p>" + src + "</div>" +
    '<div class="layer" data-l="b" hidden><p>' + e.why + "</p></div>" +
    '<div class="layer" data-l="c" hidden><p>' + e.take + "</p></div>";

  var tabs = panelContent.querySelectorAll(".tab");
  Array.prototype.forEach.call(tabs, function(t){
    t.addEventListener("click", function(){
      Array.prototype.forEach.call(tabs, function(o){ o.classList.toggle("is-active", o === t); });
      Array.prototype.forEach.call(panelContent.querySelectorAll(".layer"), function(l){
        l.hidden = l.getAttribute("data-l") !== t.getAttribute("data-l");
      });
    });
  });
}

/* pan and zoom */
var dragging = false, last = null, moved = false;
function rel(ev){
  var r = svg.getBoundingClientRect();
  var t = ev.touches ? ev.touches[0] : ev;
  return {x:(t.clientX - r.left) / r.width * 1000, y:(t.clientY - r.top) / r.width * 1000};
}
svg.addEventListener("mousedown", function(ev){
  dragging = true; moved = false; last = rel(ev); svg.classList.add("dragging");
});
window.addEventListener("mouseup", function(){ dragging = false; svg.classList.remove("dragging"); });
svg.addEventListener("mousemove", function(ev){
  if (!dragging || !last) return;
  var p = rel(ev);
  view.x += p.x - last.x; view.y += p.y - last.y;
  last = p; moved = true; apply();
});
svg.addEventListener("wheel", function(ev){
  ev.preventDefault();
  var f = ev.deltaY < 0 ? 1.15 : 0.87;
  var p = rel(ev);
  var nk = Math.max(1, Math.min(9, view.k * f));
  view.x = p.x - (p.x - view.x) * (nk / view.k);
  view.y = p.y - (p.y - view.y) * (nk / view.k);
  view.k = nk; apply();
}, {passive:false});
svg.addEventListener("touchstart", function(ev){ dragging = true; last = rel(ev); }, {passive:true});
svg.addEventListener("touchmove", function(ev){
  if (!dragging || !last) return;
  var p = rel(ev);
  view.x += p.x - last.x; view.y += p.y - last.y;
  last = p; apply();
}, {passive:true});
svg.addEventListener("touchend", function(){ dragging = false; }, {passive:true});

function zoomBy(f){
  var nk = Math.max(1, Math.min(9, view.k * f));
  view.x = 500 - (500 - view.x) * (nk / view.k);
  view.y = 268 - (268 - view.y) * (nk / view.k);
  view.k = nk; apply();
}
document.getElementById("zoom-in").addEventListener("click", function(){ zoomBy(1.35); });
document.getElementById("zoom-out").addEventListener("click", function(){ zoomBy(0.74); });
document.getElementById("zoom-reset").addEventListener("click", function(){
  view = {x:0, y:0, k:1}; apply();
  selectedId = null;
  Array.prototype.forEach.call(markers.querySelectorAll(".mk"), function(g){ g.classList.remove("is-sel"); });
  panelContent.hidden = true; panelEmpty.hidden = false;
});

function buildRoster(){
  var body = document.getElementById("rosterbody");
  body.innerHTML = Object.keys(KINDS).map(function(k){
    var list = E.filter(function(e){ return e.kind === k; });
    if (!list.length) return "";
    return '<h3 style="color:' + KINDS[k].color + '">' + KINDS[k].label + "</h3>" +
      list.map(function(e){
        return "<p><span class=\\"rn\\">" + e.name + ".</span> " + e.place + ". " +
               e.brief + " " + e.why + " " + e.take + "</p>";
      }).join("");
  }).join("");
}

buildMarkers();
buildFilters();
applyFilter();
buildRoster();
apply();
})();
</script>
</body>
</html>
'''

out = (HTML
       .replace('__SPHERE__', sphere)
       .replace('__LAND__', land)
       .replace('__COAST__', coast)
       .replace('__DATA__', data_json))
open('atlas.html', 'w').write(out)
print("atlas.html written:", len(out), "bytes,", len(E), "entries")
