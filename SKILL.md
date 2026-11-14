---
name: swiss-ui-design
description: Design website and app interfaces in the Swiss / International Typographic Style — modular grid, asymmetric flush-start layouts, sans-serif type as the main image, few bold flat colors, active white space and real content — so the result reads as the work of a disciplined human designer, not a generic AI template. Use whenever the user wants to design, build, mock up, restyle or critique a landing page, website, web app, dashboard, mobile app screen or UI component and mentions Swiss style, Swiss school, International Typographic Style, grid-based, modernist, editorial, minimal, Müller-Brockmann or a Helvetica look — or asks for a UI that doesn't look AI-made. Handles Arabic (RTL) and English.
---

# Swiss UI Design

This skill turns the principles of the Swiss school into concrete UI decisions. The school's founding idea, from Ernst Keller, is that **the design solution must come out of the content of the problem**. Everything below follows from that: the grid is the logic, type is the image, color is a few strong planes with clear jobs, white space is structure, and nothing is decoration.

The second goal: the result **must not look AI-generated**. Generic AI interfaces share one look (centered hero, purple gradient, rounded cards with soft shadows, three icon features, vague copy). The Swiss style is close to the opposite of that look, so applying it with discipline solves most of the problem; Part 5 handles the rest.

**How this file is organized**
1. Workflow — the steps, in order
2. Grid, spacing, type and color — tokens, scales, palettes, layout recipes, base CSS
3. Arabic and RTL
4. Components
5. Not looking AI-made — the review checklist
6. Source: the Swiss school in brief (from the booklet *The Swiss School of Design*)

---

# Part 1 — Workflow

## 1. Start from the content

- Write down the **one thing** the screen exists for (one message, one action). It becomes the dominant element.
- Rank the rest into at most 3–4 levels of hierarchy.
- If the user gave no content, write **real, specific content** in the target language: realistic local names, exact numbers, dates, prices, places. Never lorem ipsum, never marketing filler ("Unlock the power of…", or its Arabic equivalent "discover the power of…"). Specific content is the strongest single sign that a human made the page. Tell the user which details are assumptions to replace.
- Write the copy the Swiss way: **objective and factual, free of the exaggerated claims of advertising and propaganda** (Meggs' definition of the style). The designer acts as a clear channel for the information, not as a salesperson. Facts, numbers, conditions and plain verbs persuade better here than adjectives.
- Decide language and direction. Arabic → `dir="rtl"` and apply Part 3, which changes alignment, fonts and line-height.

## 2. Choose a direction — on purpose

The Swiss school is not one look. Pick one of these directions, each based on the principles of a pioneer or a school (use the principles; never copy their posters):

| Direction | Character | Fits |
|---|---|---|
| **Zurich — Müller-Brockmann** | Rigorous grid, sometimes visible; objective tone; small precise type next to one large photo or abstract geometric form; a lot of white. | Documentation, dense apps, dashboards, institutions, finance |
| **Basel — Hofmann** | Black and white, high contrast, figure–ground, very few large shapes, type as form. | Culture, portfolios, events, architecture |
| **Ballmer** | Headings built on the grid, heavy weights, red + black, stacked words, structure made visible. | Brands, campaigns, launches, landing pages with attitude |
| **Keller** | Bold flat color fields, simple geometric shapes, oversized type cropped by the edge. | Consumer products, education, community, museums |
| **Basel object poster (Sachplakat)** | One object (the product, a tool, a dish, a device) shown huge, close-up and sharply photographed, with almost nothing else but a name. | Physical products, food, retail, hardware |
| **Photomontage (Herbert Matter)** | Photographs combined at dramatically different scales, cut on the grid, with type locked into them. | Tourism, places, events, media |

Background that helps the choice: the Swiss National Library describes two post-war camps, **Zurich = Concrete Art** (mathematical construction, pure geometric planes; Max Bill built the first true layout grid in the late 1930s) and **Basel = New Objectivity** (the object, the photograph, contrast of form). Keller himself taught no fixed style: he believed the solution should emerge from the content, so his own work is very diverse. The skill follows him: **the direction comes from the content, not from habit**.

Zurich is the "safe" choice and it is easy to fall into it every time; that makes every output look alike. Choose Zurich when the content is dense and functional. For landing pages, brands and campaigns, prefer Ballmer, Keller or Basel — they give the page **one strong moment** (a full field of strong color, a giant cropped word, a high-contrast shape) that a quiet page lacks. Tell the user in one line which direction you chose and why. Don't write it inside the interface.

## 3. Find the concept in the content

The Basel school put it this way (Kenneth Hiebert, a Hofmann student): an abstract structure is the vehicle for communication, and finding it forces you to **isolate the essence of the message** before any surface style. Do this in writing before you design:

1. List 5–8 **concrete facts** from the content: a number, a place, a physical object, a time, a process, a name, a contrast (before/after, small/large).
2. Write **three different concepts**, one sentence each, each built on a different fact. Example for a coworking space: (a) the building's address and floor plan as the image; (b) the day's 15 hours as a grid you book directly; (c) the actual objects — a desk, a key, a chair — shown huge (object poster).
3. Choose the one that is most specific to this product, the one that could not be moved to a competitor's page by changing the name. Say in one line which one you chose.

**The giant element must come from content, not from a call to action.** A giant imperative verb ("Book", "Start", or their Arabic equivalents) is a gimmick: it fits any product and quickly becomes the new template. Use a noun, number or name that only this product has: the place, the key figure, the object, the date.

## 4. Set the system before the layout

Fix the tokens in Part 2 first: the body line (size and line height), a grid derived from it (12/8/4 columns by default, or another number if the content calls for it), baseline unit (8px), one type family (or one Arabic + one Latin partner) with a steep scale, and color (paper, ink and 1–3 strong flat colors with assigned jobs, plus a grey ramp; see Color in Part 2).

## 5. Compose with asymmetry

The source describes balance through **distribution of visual forces, not symmetry**.

- Don't center the hero. Put a heavy element (huge headline, large photo, color field) against one side, balanced by white space and small text on the other.
- Use **unequal column spans**: 5+7, 4+8, 3+9, 2+6+4. Equal thirds everywhere is the AI default.
- Offset on purpose: headline on columns 1–9, intro on 7–11 below it, metadata on 1–3.
- Give each section a **different composition** on the same grid. Repeating "centered title + card grid" in every section is a strong AI tell.
- Before coding a section, write its spans as a comment (`/* hero: h1 1–10, meta 1–3, lead 6–11 */`). It keeps the grid honest.

## 6. Add the poster layer — what makes it Swiss, not just clean

This step is the difference between a Swiss design and a tidy one. The source itself notes that the Swiss principles became the foundation of modern UI. That means the **functional rules alone** (grid, hairlines, flush-left text, an index list, a stat strip, one accent) now produce something every design system already looks like. It is clean, but it isn't new and it isn't recognizably Swiss. What made the Swiss school distinctive was its **posters**: type used as image, bold color planes, geometry, scale tension and structure you can see. Bring that language into the interface.

The sources say the same thing from two sides. A study of flat design (Aristova & Vasilieva) traces flat web design back to the International Style, and warns that its spread makes websites uniform and weakens the identity of each site and institution. A design-history textbook notes that once the Swiss style became universal, its visual language became less innovative. The cure is not to drop the principles. It is to use them the way the original designers did, as a method for finding a specific form for each piece of content.

**Rule:** a landing page, a marketing site or a brand page needs **at least three signature moves**. One goes in the hero, and at least two more go in other sections. A product UI (dashboard, app) stays functional, but it gets **one** poster moment: the page header, the login screen, an empty state or a section divider.

**Signature moves** (each comes from a principle seen in the source's poster examples; use the principle and never reproduce a poster):

| # | Move | How in UI | CSS |
|---|---|---|---|
| 1 | **Letters as architecture** (Ballmer) | A word or initial built from grid modules: huge letters split by column lines, or letters assembled from squares. In Arabic, **square Kufic** is the natural equivalent, since it is script built on a grid. Use it for a wordmark or a hero word, drawn in SVG from squares and kept legible. | SVG `<rect>` on a module grid; `grid` of cells |
| 2 | **Giant cropped type** (Keller) | Headline larger than the viewport, cut by one or two edges. The page's identity is the word itself. | `font-size: 28vw; line-height: .8; margin-inline-start: -.05em;` section `overflow: clip` |
| 3 | **Interlocking type** (Hofmann) | Words stacked with negative leading so they touch or overlap, forming one typographic block. | `line-height: .75`, negative margins, `mix-blend-mode: multiply` on a second color |
| 4 | **Rotated plane** (Müller-Brockmann) | A block of content, a grid or a scatter of small squares placed on a plane turned 45° or 90°, against the straight grid. | `transform: rotate(-45deg)` on a wrapper; keep text inside readable or rotate 90° |
| 5 | **Figure–ground geometry** (Hofmann) | One large circle, half-circle or ring in ink or a strong palette color, cut by the screen edge. Text sits inside the shape or wraps it. | `border-radius: 50%` element / SVG, `clip-path`, `shape-outside` |
| 6 | **Vertical word column** (Ballmer) | A narrow full-height color column with one word set vertically. Arabic: rotate the whole word (never stack letters). | `writing-mode: vertical-rl`, `transform: rotate(180deg)` |
| 7 | **Color field + ink block** (Keller) | A whole section in a strong field color with a solid black rectangle holding the text, or two strong colors meeting edge to edge. | two blocks on the grid, no shadows |
| 8 | **Grid as content** (Müller-Brockmann) | Grid lines drawn on purpose, with data, numbers or text snapped into the cells. Use it for a timetable, a price grid or a section index. | borders on cells, or `repeating-linear-gradient` lines |
| 9 | **Scale tension in one line** | A 200px word next to 12px metadata on the same baseline. | flex with `align-items: baseline` |
| 10 | **Tonal over-type** | Two display words layered, one in light grey behind and one in ink or paper in front, offset on the grid. | absolute positioning inside a grid cell |
| 11 | **Object hero** (Basel Sachplakat) | One real object photographed close-up, larger than life, cut out or cropped tight, with only the name and one fact. | `object-fit: cover`, image spanning 8–12 columns, cropped by the edge |
| 12 | **Photomontage** (Matter) | Two or three photographs at very different scales (a detail huge, a wide view small) cut to grid fields, with type placed over or between them. | grid fields with `overflow: clip`, images aligned to field edges |
| 13 | **Confrontation** (Hofmann) | Two unlike elements meet on purpose: a letter against a geometric form, a dense text block against an empty field, a round shape against a straight grid, black against white. | two grid areas sharing an edge or overlapping by one field |
| 14 | **Programme** (Gerstner) | One rule generates variations: e.g. every item in a list uses the same grid, but its number, image or color field sits in a position computed from its data (index, size, date). | CSS variables per item, `grid-column` set from data |

Guidelines for the moves:
- **Commit to them.** A half-size version looks like a mistake. If the word is giant, make it truly giant.
- **Make them carry content.** The giant word should be the product's name, the key number, the place or the object, never a generic verb or decoration. Keller: the design comes from the content.
- **Vary them across sections**, and choose them to fit the direction (Ballmer → 1, 6, 8; Keller → 2, 7; Hofmann → 3, 5, 10, 13; Zurich → 4, 8, 9, 14; Basel object poster → 11; Matter → 12).
- **Don't reach for the same combination every time.** The table is a vocabulary, not a recipe. A giant cropped word plus a red section plus a vertical word is already turning into a formula. Pick the moves the concept from step 3 asks for. If the concept is a timetable, the grid itself (8) may be the whole hero. If it is an object, the photograph (11) is.
- **Keep it accessible.** The real text stays as real text: the giant word is the actual `<h1>`, or a decorative duplicate is `aria-hidden` while the real heading remains. Rotated text is short. Contrast stays at AA.
- **Arabic is an advantage here.** Arabic letterforms are strong shapes. Heavy Kufi weights, cropped words, interlocking word blocks and square-Kufic wordmarks give a look that Latin-template designs can't have.

**Familiarity test** (run it on the screenshot): could this pass as an ordinary modern product page, with hairline lists, a stat row and an orange button, the kind of thing a design system produces by default? If yes, it isn't finished. Replace at least one "safe" section with a signature move.

## 7. Apply the five principles

1. **Grid** — balanced distribution, clear hierarchy, exact relations between text and images, and a system reusable across screens. Show the grid through alignment; draw it visibly only as an intentional element (Zurich, Ballmer).
2. **Simple type** — neutral sans-serif, readable in long text. Hierarchy from **size, weight and position**, not color, boxes or icons. Type can be the main image: a headline cropped by the viewport edge, oversized numerals, one huge word.
3. **Asymmetric arrangement** — step 5.
4. **White space** — active and structural: it groups (proximity instead of borders), focuses, and lets content breathe. Don't fill every column.
5. **Flush-start alignment** — start edge aligned, end ragged. Never justify body text, never center paragraphs. In Arabic the start edge is the right.

From the International Style in architecture, which the booklet names as the style's parent (Hitchcock & Johnson, MoMA 1932), three more rules translate directly to screens:
- **Volume, not mass.** Build with thin planes and surfaces (flat fields, hairlines), not heavy objects with shadows, bevels and depth.
- **Regularity, not symmetry.** The rhythm comes from the repeated structure of the grid, not from mirroring around a central axis.
- **Quality from proportion and precision, not applied ornament.** What makes the page beautiful is exact proportions, consistent spacing and technical perfection, not decoration added on top.

From Hofmann's *Graphic Design Manual*, the basic elements are **the dot, the line, and form**, plus **confrontation** (deliberate meetings of unlike elements, such as form and lettering). When a page needs a graphic element, build it from these before reaching for icons or illustration.

Also from the source: prefer **photography** over illustration, keep the voice **objective**, use **few colors at full strength** (limited in number, bold in use; see Color in Part 2), use **simple geometric shapes** (rectangle, circle, rule) when a graphic element is needed.

## 8. Build

- Default output: one self-contained HTML file with inline CSS (start from the base CSS in Part 2), semantic HTML, `lang` and `dir` set. If the project uses a framework (React, Tailwind, Next.js), follow it and map the tokens into its config.
- Fonts: Google Fonts with a system fallback (lists in Parts 2 and 3). Avoid the overused defaults (Inter, Poppins, Montserrat, Cairo, Tajawal) unless the project already uses them.
- **Images when you have no photography.** Don't fill large areas with empty grey placeholder blocks — on screen they read as unfinished dead space and pull attention from the content. Prefer, in this order: (a) a typographic composition (giant word or number), (b) a flat geometric composition or a strong color field, (c) a placeholder only where a real photo is clearly needed — kept proportional to its role (not half the screen), on the grid, with an honest caption like "Photo: the open hall, 4:5". Never AI-style 3D blobs, abstract gradients, or stock illustrations of people with laptops.
- Motion: minimal and functional — color/opacity transitions of 120–200ms; no parallax, no fade-up on every block, no hover scale.
- Accessibility is part of the style: WCAG AA contrast, visible focus (thick outline in the signal color), real `<button>`/`<a>`, labeled inputs, `prefers-reduced-motion` respected.
- Charts: if a dataviz skill is available, follow it for chart mechanics, but keep this skill's look where they conflict: **square bar ends** (no rounded caps), the series that matters in a strong palette color and the rest in grey/ink. A single huge hero number may use proportional figures; numbers in tables, axes and stat rows use tabular figures.

## 9. Review before delivering

1. If a browser is available (Playwright/Chromium), render at 1440px and 390px and look at the screenshots. Judge the picture, not the code. (If Google Fonts can't be reached, preview with local copies, e.g. `npm i @fontsource/<font>`, while the delivered file still links Google Fonts.)
2. Run the checklist in Part 5. Fix every failure.
3. Concept test (step 3): could this page be moved to a competitor by changing the name? If yes, the concept isn't specific enough.
4. Familiarity test (step 6): if it reads like a default design-system page, add or strengthen a signature move.
5. Squint test: one dominant element, a clear reading order, visible white space. If everything has the same weight, increase the contrast.
6. Edge test: element edges sit on column lines; vertical gaps come from the spacing scale.
7. Mobile test: no horizontal overflow from multi-column rows (stat strips, stage filters, tabs). Wide tables and schedules may scroll sideways inside their own container, with a short hint.

## 10. Deliver

Keep the interface clean: no captions like "Swiss-style design" or "inspired by Müller-Brockmann" inside the UI. In the message: one or two lines on the direction and the main composition choice, and the list of assumed content to replace. If the user is learning, add a short note on which principle drove which decision.

## Critiquing or "Swiss-ifying" an existing design

1. Find the implicit grid (or note that there is none).
2. List problems in this order: hierarchy → grid and alignment → type → white space → color → decoration and AI tells.
3. Give each a concrete fix (column spans, sizes, tokens), not general advice.
4. If rebuilding, keep the content and brand essentials (logo, main color joining the palette) and rebuild the structure.

---

# Part 2 — Grid, spacing, type and color

## Grid

| Breakpoint | Columns | Gutter | Outer margin |
|---|---|---|---|
| ≥ 1200px | 12 | 24px | `clamp(24px, 5vw, 80px)` |
| 768–1199px | 8 | 20px | 32px |
| < 768px | 4 | 16px | 20px |

- Let the grid fill the screen (max ≈1440px or full-bleed). A narrow centered column with empty side bands looks like a template.
- CSS Grid: `grid-template-columns: repeat(var(--cols), minmax(0, 1fr))`; place children with `grid-column: 3 / span 8`. Don't let elements auto-flow into equal cells.
- **Derive the grid from the type** (Müller-Brockmann, *Grid Systems*). Set body size and line height first. Then make every vertical measure a multiple of that line: field heights = N lines, vertical gaps between fields = 1–2 lines. Column widths come from a comfortable measure for the body text. In CSS: `--line: 28px; grid-auto-rows: calc(var(--line) * 4); row-gap: var(--line);`.
- **Fields for images.** Images, charts and statistics span 1, 2, 3 or 4 fields. The smallest image equals the smallest field. Use **few image sizes**: the fewer the differences, the calmer the page. Size each image by its **importance to the subject**, not by what fills the space.
- **Each project gets its own grid study.** 12 columns is a sensible default for the web, but a page about one object might work better on 5 or 6 columns, and a dense timetable on 15. Choose the grid from the content.
- The grid also carries meaning: **layout should show how pieces of information relate**, like a table does. Match it with semantic HTML: `<table>` for tabular data, `<dl>` for term–value pairs (specs, prices, hours), `<ol>` for sequences.
- In RTL, CSS Grid mirrors automatically (column 1 is on the right). Write spans once.

## Spacing

Base 8px. Steps: `4 · 8 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 192`. Inside components 4–24; between related blocks 32–64; between sections 96–192. **Contrast in spacing creates rhythm**: a tight cluster next to a large gap is Swiss; the same 24px everywhere is AI.

## Type families (Latin)

- System: `"Helvetica Neue", Helvetica, Arial, sans-serif` — honest and very Swiss.
- Google Fonts grotesques: **Schibsted Grotesk**, **Archivo** (width axis; narrow cuts suit Ballmer), **Hanken Grotesk**, **Instrument Sans**, **Public Sans**, **Familjen Grotesk**, **IBM Plex Sans**. Check tabular-figure support if the page is number-heavy (Archivo and IBM Plex have it).
- Mono for codes and timestamps only: IBM Plex Mono, JetBrains Mono.
- Avoid as defaults: Inter, Poppins, Montserrat, Roboto, Open Sans — the "AI default", no character.
- **Think in one family.** Univers (Frutiger, 1957) was among the first typefaces designed as a full system of weights and widths, so a whole document could use one design. Do the same: one family, with weights and widths chosen as a system (e.g. 400 text / 500 labels / 800 display), not several fonts. Max Bill favored Akzidenz in the **medium** weight; a medium weight for text and labels often looks more Swiss than regular.
- **Exhaust type before adding anything else.** Swiss designers held that adding imagery or decoration before exploring what type alone can do is wasteful. Try a typographic solution first.

## Type scales

**Interface (apps, dashboards):** caption 12/16 w500 · meta/table 14/20 · body 16/24 (Arabic 17/30) · lead 20/28 · section title 28–32 w600–700 lh 1.15 · page title 44–56 w700 lh 1.05.

**Editorial (landing pages):**
| Token | Size | Notes |
|---|---|---|
| display | `clamp(56px, 11vw, 200px)` | One per page; w700–900; lh 0.9–1.0 (Arabic 1.1–1.25); tracking −0.02 to −0.04em (Latin only) |
| h1 | `clamp(40px, 6vw, 96px)` | |
| h2 | `clamp(28px, 3.2vw, 48px)` | |
| lead | 20–24px | max 40ch |
| body | 16–18px | max 65ch (Arabic ≈60ch) |
| meta | 12–13px | Latin: uppercase + 0.06em tracking; Arabic: w500–600, no tracking |

The jump from display to lead should be 5× or more — that tension is what makes a page look designed.

## Typesetting

- `text-align: start`; no justify, no centered paragraphs. Measure 45–70 characters.
- Two or three weights only. Hierarchy by size, weight, position — not color.
- `font-variant-numeric: tabular-nums` for tables, stats, prices, times.
- Real punctuation: en dash for ranges (2024–2026), “ ” in English; guillemets and the Arabic comma and question mark in Arabic.
- Index numbers (01, 02, 03) in the meta size for lists and sections.
- A headline may be wider than the screen and cropped by the edge — once per page.

## Color — few colors, full strength

Swiss color is **limited in number and bold in strength**. The booklet calls Keller's colors strong and describes the mature 1950s style as using limited colors. The cited sources say the same from both sides: sparing use of color (House of Switzerland), "unusual color combinations" (Smashing Magazine), "vibrant contrasting color" in Keller's work. The posters in the booklet show it: Keller's orange ground with deep red and green, Ballmer's blue and black, and red, black and grey; Müller-Brockmann's full orange cover, his black poster with a little red, and red, yellow and blue squares on near-white; Hofmann's red letters on white.

So color is not a timid accent on a white page. It is **flat, saturated, and used in large planes**.

**Rules**
- **Palette = paper + ink + 1–3 strong flat colors.** Never more. No tints of everything, no pastel range, no gradients.
- **Use color as structure.** A whole section, a full-height column, a large circle or the full background of the hero can be a solid color field. Large flat planes of strong color are Swiss. A page that is all white with one small colored button is timid, not Swiss.
- **Give each color a job.** For example, the *field* color carries the composition (backgrounds, blocks, shapes), and the *signal* color marks action or state. If the field is red, the button on it is ink, not red.
- **Contrast of hue and value, not of decoration.** Put colors next to each other as hard-edged planes: orange against black, blue against red, red against grey. Unusual pairings are allowed, and they are part of the tradition.
- **Product UI is calmer.** Dashboards and apps keep large neutral working areas. Strong color goes to one poster moment (header, login, empty state), to navigation or section identity, and to data. It does not go behind dense tables.
- **One color per meaning across the product.** If orange means "open orders", it never means anything else.
- **A brand color joins the palette** as the field or signal color. Add at most one or two partners chosen for contrast with it.

**Palettes drawn from the source posters** (starting points: pick one, then adjust; don't copy a poster):

| Palette | Colors | Character |
|---|---|---|
| Keller — museum | orange `#F05A1A` · wine `#8E1B2E` · green `#1F6B4A` · ink | warm, bold, unusual |
| Ballmer — building | blue `#0047BB` · ink · paper | cold, constructive |
| Ballmer — office | red `#E30613` · ink · grey `#B9B7AE` | industrial, loud |
| Müller-Brockmann — film | ink as the ground · paper type · warm grey `#8C8A80` · small red `#E30613` | dark, cinematic |
| Müller-Brockmann — concert | near-white · red `#E30613` · yellow `#F2B705` · blue `#1E5AA8` · ink, all in small units | musical, rhythmic |
| Müller-Brockmann — grid book | orange `#EE6B2F` field · paper hairlines · ink type | systematic, warm |
| Hofmann — Basel | paper · ink · one red `#E30613` | austere, high contrast |

**Text on color fields** (contrast on paper `#F4F2EC` / ink `#111111`, checked against WCAG):
- Orange, yellow, light grey, pink fields → **ink text** (orange `#F05A1A`: ink 5.6:1, paper only 3.0:1).
- Blue, green, wine, deep red fields → **paper text** (blue `#0047BB`: paper 7.2:1).
- Swiss red `#E30613`: paper text 4.4:1 passes only for **large/bold text** (≥24px, or ≥19px bold). For body text on red use deep red `#C8102E` (paper 5.3:1) or put the text in an ink or paper block on the red field.
- Body text always needs 4.5:1, large display text 3:1. Check every pairing; strong color is no excuse for unreadable text.

**Still not allowed:** gradients as color effects, glass, glows, colored shadows, opacity washes as decoration, neon on dark. Technical patterns are fine (e.g. `repeating-linear-gradient` hatching for unavailable slots). Neutral subtle shadows only where the platform needs elevation (menus, dialogs). A dark theme uses ink as the ground with the same strong palette.

## Layout recipes (12 columns; mirror automatically in RTL)

- **A. Offset headline** — meta 1–2 · h1 3–11 · lead 7–11 one row below · CTA 7–9.
- **B. Split 5/7** — text 1–5, image 6–12 bleeding to the edge; first text baseline aligned with image top.
- **C. Giant word** — one word/number at display size, cropped by the edge; small meta at 10–12 on its baseline.
- **D. Index list** (replaces feature cards) — number 1 · title 2–5 · description 6–10 · meta/link 11–12; 1px rule above each row; no boxes, no icons.
- **E. Stat strip** — 3–4 big tabular numbers on unequal spans (1–4, 5–7, 8–9, 10–12), small label below.
- **F. Color field** — section in a strong field color, display heading, text on 2–7, one circle or rectangle on the free side.
- **G. Visible grid** — thin rules on column lines with type snapped to them; once, with intention.
- **H. Sidebar index** (docs, dashboards) — nav 1–2/1–3 sticky · content 3/4–10 · notes 11–12.
- **Mobile (4 cols)** — headline 1–4 · body 1–4 or 2–4 · meta 3–4 at the end edge · index numbers in col 1 with text in 2–4.

## Base CSS (copy in and adjust)

```css
:root{
  --paper:#f4f2ec; --ink:#111; --ink-2:#555; --rule:#d9d9d6;
  --field:#f05a1a;   /* main strong color: whole sections, blocks, shapes */
  --field-2:#1f6b4a; /* optional second strong color */
  --signal:#e30613;  /* action / state; use ink for buttons that sit on a red field */
  --font:"Schibsted Grotesk","Helvetica Neue",Helvetica,Arial,sans-serif;
  /* Arabic: "IBM Plex Sans Arabic","IBM Plex Sans",system-ui,sans-serif */
  --s-1:4px;--s-2:8px;--s-3:16px;--s-4:24px;--s-5:32px;--s-6:48px;--s-7:64px;--s-8:96px;--s-9:128px;--s-10:192px;
  --cols:12; --gutter:24px; --margin:clamp(20px,5vw,80px);
  --t-meta:13px; --t-base:17px; --t-lead:clamp(19px,1.6vw,24px);
  --t-h2:clamp(28px,3.2vw,48px); --t-h1:clamp(40px,6vw,96px); --t-display:clamp(56px,11vw,200px);
  --lh-body:1.55; --lh-head:1.05; --lh-display:.92;
}
:lang(ar){--lh-body:1.8;--lh-head:1.3;--lh-display:1.15}
@media (max-width:1199px){:root{--cols:8;--gutter:20px}}
@media (max-width:767px){:root{--cols:4;--gutter:16px}}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--font);
  font-size:var(--t-base);line-height:var(--lh-body);text-align:start;-webkit-font-smoothing:antialiased}
h1,h2,h3,p{margin:0}
.grid{display:grid;grid-template-columns:repeat(var(--cols),minmax(0,1fr));column-gap:var(--gutter);padding-inline:var(--margin)}
.display{font-size:var(--t-display);line-height:var(--lh-display);font-weight:800;letter-spacing:-.035em}
.h1{font-size:var(--t-h1);line-height:var(--lh-head);font-weight:700;letter-spacing:-.02em}
.h2{font-size:var(--t-h2);line-height:1.12;font-weight:700}
.lead{font-size:var(--t-lead);line-height:1.4;max-width:40ch}
.meta{font-size:var(--t-meta);line-height:1.4;font-weight:500;color:var(--ink-2)}
.num{font-variant-numeric:tabular-nums}
:lang(ar) :is(.display,.h1,.h2,.meta){letter-spacing:0;text-transform:none}
.rule{border:0;border-block-start:1px solid var(--rule)} .rule-heavy{border-block-start:6px solid var(--ink)}
.btn{display:inline-block;padding:14px 24px;background:var(--ink);color:var(--paper);font:inherit;font-weight:700;
  border:0;border-radius:0;text-decoration:none;cursor:pointer;transition:background-color .15s}
.btn:hover{background:var(--signal)}
:focus-visible{outline:3px solid var(--signal);outline-offset:2px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
```

---

# Part 3 — Arabic and RTL

Translate the **intent** of each Swiss rule, not its letter.

**Direction and alignment**
- `<html lang="ar" dir="rtl">`. Grid and Flexbox mirror automatically.
- The source's "left alignment" means **flush to the start of the line** → in Arabic, **flush right, ragged left**. Use `text-align: start`, never `left`/`right`.
- Logical properties everywhere: `margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `border-inline-start`.
- The heavy element usually starts at the right edge; white space opens toward the left.
- "Next / more" arrows point **←**. Clocks, play icons and logos don't flip. Dropdown chevrons point down.

**Fonts**
| Font | Character | Latin partner |
|---|---|---|
| **IBM Plex Sans Arabic** | Neutral, rational, many weights; closest to Helvetica-like neutrality | IBM Plex Sans |
| **Noto Kufi Arabic** | Geometric Kufi, strong heavy weights; great display (Ballmer, Keller) | Archivo, Schibsted Grotesk |
| **Readex Pro** | Low contrast, wide, technical | built in |
| **Alexandria** | Geometric, confident display weights | built in |
| **Noto Sans Arabic** | Plain, very readable for long text and dense apps | Noto Sans, Public Sans |

Avoid **Cairo** and **Tajawal** as defaults — the Arabic equivalent of Inter. Put both languages in one stack: `font-family: "IBM Plex Sans Arabic", "IBM Plex Sans", system-ui, sans-serif;`

**Typesetting Arabic**
- **No letter-spacing** (it breaks letter joins), no uppercase, no faux italics; emphasize by weight, size or the signal color.
- No kashida stretching, no justified body.
- Line-height: body 1.7–1.9; headings 1.25–1.4; display at least 1.1–1.25 — Latin-style tight leading (0.9) clips tall letters (lam, kaf, ta), deep descenders (ya, ain, nun) and diacritics. Check the render.
- Arabic looks smaller at the same size: body 17–18px, meta ≥13px. Measure ≈50–65 characters.
- Display: one short heavy word cropped by the edge works very well (short words of two or three letters, such as the Arabic words for art, market or house). Heavy Kufi weights (Noto Kufi Arabic 800–900, Alexandria 800–900) are the strongest for poster moves; **Reem Kufi** (Google Fonts, geometric Kufi) suits wordmarks.
- Square Kufic is Arabic script built on a grid, so it is the closest Arabic match to Ballmer. For a wordmark or a hero word, draw it in SVG from equal squares on a module grid. Keep it short (2–4 letters), legible, and give it a real text label (`aria-label`).
- Vertical text: never stack Arabic letters; stack **words** one per line, or rotate a whole word with `writing-mode`.

**Numbers and punctuation**
- One numeral system per product: Western digits (common in Saudi digital products) or Arabic-Indic digits for formal/editorial. Don't mix on one screen. Tabular figures in tables.
- Separators: a comma with Western digits (1,284) or the Arabic thousands separator with Arabic-Indic digits. Use the Arabic comma, semicolon and question mark, and guillemets for quotes.
- Dates: day, Arabic month name, year (e.g. 11 November 2026, written in Arabic); Hijri if the context needs it — consistently.
- Currency: the number followed by the Arabic abbreviation or word for riyal; wrap Latin fragments, phone numbers, emails, URLs and IBANs in `<bdi>` or `dir="ltr"` so order doesn't break. LTR inputs (email, phone) get `dir="ltr"`.
- Bilingual layouts: give each language its own columns and its own start edge (Arabic flush right, English flush left) instead of centering both — a strong Swiss composition in itself.

**Copy**: short, objective, concrete simplified Modern Standard Arabic; no English-calqued phrasing and no filler (the Arabic equivalents of "discover the power of", "elevate your experience", "innovative solutions"). If the `ux-araby` skill is available, use it for microcopy.

---

# Part 4 — Components

Same rules everywhere: on the grid, flush-start, square, hierarchy by type, separation by white space and rules, a small palette of strong flat colors.

- **Navigation** — wordmark (product name in the main font, bold) at the start edge; plain text links on grid columns, not a centered pill bar; current page by weight 700 **or** a 2px rule **or** the signal color (pick one). Mobile: a text button "Menu" (in the interface language) opening a full-screen list of large, numbered links.
- **Buttons** — rectangle, radius 0–2px, ink or signal fill, weight 600–700, one primary per view. Secondary: text link with arrow (→ LTR, ← RTL) or 1px outline. Hover: color swap or underline, no scale or shadow. Labels say what happens: "Book an appointment", "Download the report (PDF, 2.4 MB)".
- **Hero** — offset headline, split with photo, giant word, color field, or a data hero with one large number ("2,418 beneficiaries"). Never the centered default.
- **Lists instead of cards** — rows with 1px rules; columns: index · title · description · meta/link; the whole row clickable with a color or arrow change on hover. Visual item grids (products, people): image + caption cells sharing top lines, no boxes, no shadows.
- **Tables** — header in the meta size w600 with a 1–2px ink rule; body rows 1px rules; no zebra, no vertical borders; numbers tabular and end-aligned, text start-aligned; row height 48–56px (36–40 dense).
- **Forms** — labels above, flush-start; inputs with a 1px border (radius ≤2px, height 48px) or bottom border only — one style; focus → 2px signal border; errors as text in the signal color with a clear message ("Mobile number must start with 05"); fields on the grid; submit aligned to the field start edge.
- **Stats** — big tabular numbers, label below, a rule above the group, unequal spans, specific numbers with a date or source line.
- **Quotes** — one quote, large, flush-start, name and role in the meta size. No avatar carousel, no stars.
- **Pricing** — a comparison table, or columns divided by rules; the recommended plan marked by its name or top rule in the signal color. No scaled middle card, no ribbon.
- **Footer** — on the same grid; wordmark + one line on 1–4, link groups on unequal spans, legal line in the meta size; a full ink block closes a page well. Social links as words.
- **Dashboards** — sidebar as a numbered text list; large flush-start page title; filters as text controls in the meta row; KPIs as a stat strip, not colored cards; charts with one highlighted series, thin axes, direct labels; tables for detail.
- **Mobile app screens** — large flush-start title (28–34px bold); list rows with hairlines and meta at the end edge; tab bar with text labels (simple icons optional), active tab by ink + weight, no pill; primary action as a full-width rectangle at the bottom; sheets with square corners and a rule under the title.
- **Empty states and feedback** — a short sentence on what's missing plus one button (no sad-box illustration); alerts as a rectangle with a 4px start-edge bar in the signal color; loading as a thin progress rule or grid-matching skeleton blocks.

---

# Part 5 — Not looking AI-made

Generated UIs average many templates and land at the statistical middle: centered, rounded, soft, purple, symmetric, vague. A human designer makes **specific decisions** a template wouldn't: an unusual column span, a word cropped by the edge, a real number, a strong contrast in scale. Every fix below moves from the average toward a specific decision.

| Area | Tell | Swiss fix |
|---|---|---|
| Layout | Centered hero: pill badge "✨ New" → centered headline → subtitle → two buttons → screenshot in a gradient frame | Asymmetric hero (recipe A/B/C/F), one CTA, flush-start |
| Layout | Every section = centered title + subtitle + equal card grid | Different composition per section on the same grid |
| Layout | Three equal feature cards with icon-in-circle | Index list (recipe D) |
| Layout | Equal ⅓/¼ columns, same 24px gap everywhere | Unequal spans; spacing contrast |
| Layout | Bento grid of rounded tiles | Modular grid with shared edges and rules |
| Layout | 3 pricing cards, middle one scaled, "Most popular" | Comparison table |
| Surface | Purple/indigo gradients, gradient text, mesh blobs, glows | Paper + ink + 1–3 strong flat colors used as planes |
| Color | Pastel rainbow of tints, or an all-white page with one small accent button | Few colors at full strength, used as large fields |
| Surface | Glassmorphism, backdrop blur | Solid surfaces |
| Surface | `rounded-2xl` + soft shadow on everything | Radius 0–2px; separation by white space and rules |
| Surface | Neon dark mode by default | Light paper by default |
| Surface | Dot patterns, noise, floating shapes | Remove; geometry only if it carries the composition |
| Surface | Large empty grey placeholder blocks | Typographic or geometric composition; small captioned placeholder only where a photo is needed |
| Motion | Hover scale + bigger shadow; fade-up on every block | Color/underline change; no scroll animation |
| Type | Inter/Poppins/Montserrat (Cairo/Tajawal in Arabic) | A grotesque with character |
| Type | All headlines ≈40–48px, timid scale | One dramatically large display size |
| Type | Centered or justified paragraphs | Flush-start, ragged-end |
| Type | Color for hierarchy; purple highlighted words | Size, weight, position; color only with a meaning |
| Icons | Emoji as icons; an icon on every line | Words, numbers, or simple geometric marks |
| Images | 3D renders, AI art, "people with laptops" | Real photography cropped to the grid, or flat geometry |
| Proof | Avatar circles + 5 stars; invented logo cloud | One real quote set large, or nothing |
| Copy | "Unlock, Elevate, Seamless, Supercharge, All-in-one", and their Arabic equivalents ("discover the power of", "innovative solutions", "seamless experience", "integrated platform", "a qualitative leap") | Plain: what it does, for whom, how much, when |
| Copy | Round fake stats "10,000+ users", "99.9% uptime" | Specific numbers with context ("1,284 orders this week"), or none |
| Copy | Lorem ipsum, John Doe, Acme | Realistic local names and data |
| Identity | "Clean minimal" page made only of hairline lists, a stat row and one accent button: tidy but generic, like any design system | Add the poster layer (Part 1, step 6) |
| Copy | Same-length subtitle under every headline; hype and exclamation marks | Vary; calm objective voice |

**Human signals to add** (several of them): small metadata (dates, version or issue numbers, location, "updated" stamps, index numbers); captions under images; one oversized element; a rule system (1px hairlines + one heavier 4–8px rule); tabular numerals and correct punctuation; unequal spans and deliberate offsets; restraint — remove one more thing before delivering.

**Final pass**
- [ ] One dominant element per screen; each section composed differently.
- [ ] The concept comes from a specific content fact; the giant element is a noun, number or name only this product has (not a CTA verb).
- [ ] Grid derived from the type: vertical measures are multiples of the body line; images use few sizes, sized by importance.
- [ ] Poster layer present: ≥3 signature moves on marketing pages, ≥1 on product UI; it would not pass as a default design-system page.
- [ ] Every edge on a column line; every gap from the spacing scale.
- [ ] Flush-start text; no centered paragraphs, no justified body.
- [ ] One family (or Arabic + Latin pair), max three weights.
- [ ] Paper, ink and 1–3 strong flat colors used as planes, each with one job; text on every field passes contrast; no gradient effects, glass or glows; corners ≤2px; no decorative shadows.
- [ ] No emoji icons, invented logos, fake testimonials, hype words or dead placeholder areas.
- [ ] Content specific, in the right language; assumptions listed for the user.
- [ ] Mobile keeps asymmetry and hierarchy, with no horizontal overflow.
- [ ] AA contrast, visible focus, semantic HTML, `lang`/`dir` set.

---

# Part 6 — Source: the Swiss school in brief

Condensed from the booklet *The Swiss School of Design*. Use it to justify a decision or to explain the style to the user.

**What it is.** The Swiss style — also called the International Typographic Style — is a systematic visual method that formed between the 1930s and 1950s and became one of the most influential movements in graphic design. Its foundations: **simplicity, clarity, objectivity, readability**; grid-based structure; asymmetric compositions; sans-serif type (Akzidenz Grotesk, Helvetica); photography preferred to illustration as more objective. It grew from Constructivism, De Stijl and the Bauhaus, which rejected Art Nouveau and Art Deco ornament for a rational language that **puts function above form**. Two centers: **Basel** (Armin Hofmann — basic forms and visual contrast) and **Zurich** (Josef Müller-Brockmann — grids and strict order). Early works used **type as the main visual element**, not only as a carrier of text. After WWII, international trade needed clear, objective design, and the style spread as a shared visual language.

**Roots.** Ernst Keller began teaching at the Zurich School of Applied Arts in 1918 and set the first principles; he trained a generation including Müller-Brockmann. Other roots: the Arts and Crafts idea of reforming applied arts, the German (1907) and Swiss (1913) Werkbund with their focus on function and industrial form, Julius de Pretere's school reforms (1906–1908) toward industrial and applied design, and Jan Tschichold's *Die neue Typographie* (1928) — grid organization, functional alignment, standardized typography.

**Timeline.** 1900–1930: Bauhaus removes ornament; Constructivism brings organized composition, strong contrast and the line as an independent element. 1930–1950: precise organization and the grid as the tool for building a design; design as research, experiment and order. 1950s: the mature style — clear grids, balanced spacing, sans-serif, limited color, focus on reading; Helvetica born in 1957. 1960s on: *Grid Systems in Graphic Design* (Müller-Brockmann) — the first systematic method for building grids; **design must rest on logic and clear construction, not on taste or visual feeling**; spread to posters, identities, magazines, ads, transport systems. 1990s–today: grids and clarity lead web and app design and become the basis of UI and UX.

**Pioneers.**
- **Ernst Keller (1891–1968)** — intellectual founder: "the design solution must emerge from the content of the problem." Function, clarity, economy of form; simple geometric shapes, strong colors (vibrant contrasting color), direct images.
- **Théo Ballmer (1902–1965)** — among the first to use grids in composition, drawing on Constructivism and abstract art; visual rigor, dense geometric elements, simple form for a clear message. Letters built on a visible square grid, red and black.
- **Josef Müller-Brockmann (1914–1996)** — the icon of grids and visual order; strict abstraction, large images with direct symbolism, personal expression set aside for objectivity; co-editor of *Neue Grafik* from 1959.
- **Armin Hofmann (1920–2020)** — Basel; high contrast, balance of light and shadow, carefully studied abstract forms; author of *Graphic Design Manual*.

**The five principles (Chapter 5).**
1. **Grid** — balanced distribution; clear information hierarchy; exact relations between text and images; easy reuse of the system across platforms.
2. **Simple fonts** — sans-serif as a functional element before a decorative one; Helvetica's neutrality, high clarity, suitability for long text, and no bias toward any culture or language.
3. **Asymmetric arrangement** — free the composition from traditional symmetry; balance by distributing visual forces; inner rhythm through non-parallel elements.
4. **White space** — a visual element, not empty space: improves balance, focuses attention, creates clarity and simplicity, lets content breathe; in digital interfaces it directs attention and sets reading priority.
5. **Left (start) alignment** — eases reading, gives a logical structure to visual sequence, strengthens clarity and reduces distraction, works naturally with the grid. In Arabic: flush right.

**What the cited sources add** (studied from the booklet's references):
- *Meggs, A History of Graphic Design*: the style = visual unity through **asymmetric organization on a mathematically constructed grid**; **objective photography and copy**, free of the exaggerated claims of propaganda and advertising; sans-serif set **flush left, ragged right**. Designers saw themselves not as artists but as objective channels for important information, and saw design as a socially useful activity.
- *Müller-Brockmann, Grid Systems*: grid fields measured in lines of text; gutters of one or more lines; images of 1–4 fields; few image sizes = a calmer design; image size by importance; each job needs its own grid study; the grid brings clarity, faster reading, better recall, and objective argument; it is an ethos of order and responsibility.
- *Hitchcock & Johnson, The International Style*: volume over mass; regularity over symmetry; intrinsic elegance, technical perfection and fine proportion instead of applied ornament.
- *Smashing Magazine, Lessons From Swiss Style* (2009): clarity and usability first; whitespace so the layout's organization shows at a glance; remove instead of adding separators and icons; the grid as a semantic layer that shows how information relates (with matching semantic HTML); explore type fully before adding other material; size contrast makes oversized words the entry points; photography as a serious tool; Gerstner's flexible grids for computational systems.
- *Print Magazine*: core values cleanliness, readability, objectivity; content over decoration; grids can combine with ratios (thirds, golden section); Akzidenz-Grotesk (1896), Univers (1954/57, one of the first full type families), Helvetica (1957); Keller taught that design adapts to content; Hofmann and Ruder founded the Basel school (1947); Max Bill and Otl Aicher's Ulm school added semiotics.
- *Aristova & Vasilieva, flat design and the International Style*: flat web design inherits the style's universalism, clarity, modular grid, white backgrounds, geometric elements and large images, and warns that its spread **makes sites uniform and weakens their identity**.
- *Hofmann, Graphic Design Manual*: the dot, the line, confrontation (meetings of unlike elements such as form and lettering), letters and signs; the Basel method isolates the message's essence before any surface style.
- *Color across the sources*: the booklet credits Keller with strong colors and the 1950s style with limited colors; House of Switzerland notes sparing use of color; Smashing Magazine notes unusual color combinations; course notes on Keller's Rietberg poster note vibrant contrasting color. Together: **few colors, at full strength, as flat planes**.
- Swiss poster history: Zurich = Concrete Art, Basel = New Objectivity (Swiss National Library); the Basel **object poster** (Sachplakat) shows one object larger than life; Herbert Matter's **photomontage** posters of the 1930s.

Sources cited by the booklet: Hollis, *Swiss Graphic Design* (2001); Meggs, *A History of Graphic Design* (1998); Müller-Brockmann, *Grid Systems in Graphic Design* (1981); Vasileva, "The Swiss Style: Its Prototypes, Origins and the Regulation Problem" (*Terra Artis*, 2021); Hitchcock & Johnson, *The International Style* (1932); MoMA collection pages. Further reading used here: Hofmann, *Graphic Design Manual* (1965); Aristova & Vasilieva, flat design and the International Style (Kazan Federal University repository); Smashing Magazine (2009); Print Magazine; neugraphic.com excerpt of *Grid Systems*.
