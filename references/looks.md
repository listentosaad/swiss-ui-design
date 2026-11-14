# Looks — ground, color scheme and image treatment

Open this file at **Step 4** of `SKILL.md`, before the layout. A **Look** is the decision a poster makes first: *what covers the sheet, which colors, and what the pictures are*. The direction (Zurich, Keller, Ballmer …) says how the page is built; the Look says how it is colored. Any direction can wear any Look.

**Source.** Five posters were studied: an author poster in yellow and indigo, the design magazine *form* (no. 271), an "International Typographic Style" poster in four color bands, a Vignelli poster of stacked colored mugs on black, and the Swissted gig-poster collection. Colors were sampled from the images and checked against WCAG; the CSS below was rendered and checked in Chromium at 1440px and 390px. **Take the system, never the poster**: no reuse of their words, objects (mugs, ladders, authors) or layouts. Build the same logic from this product's own content.

## What the five posters do that a timid page does not

| Study | What covers the sheet (measured) | Palette (sampled) | Type | Picture |
|---|---|---|---|---|
| Author poster | yellow ≈ 65–70%, indigo/navy mass ≈ 29% | `#FFC611` · indigo `#333370` · navy `#18193F` · warm white | one giant regular-weight word, ≈ 75% of the width; 12px metadata in two offset columns | duotone halftone, cut by two edges, one diagonal sweep |
| Magazine cover | white + one violet ink | ink `#4F2A7D` · periwinkle `#CFDBF1` · orchid `#BD9CBB` | giant bold lowercase masthead crossing the panel; cover lines and a colophon strip, all in the same violet | pastel panel split on a diagonal |
| Typographic-style poster | four full-bleed bands; red ≈ 44% | blue `#1248B0` · green `#097F28` · mustard `#EFB83E` · red `#E6040A` · black ink | each word sized to the full width, heavy, letters touching; crop marks; paper grain | none |
| Object poster | black ≈ 47%, spectrum ≈ 45% | `#FEBD01` `#007DD9` `#00B346` `#FF2B27` `#FE50FF` `#E6E7E9` `#3744C6` on `#070707` | white heavy name top-end; two tiny paragraphs rotated 90° | one object shape in 11 modules, touching, handles alternating sides |
| Gig-poster set | cream or black, per poster | pure red, cyan, yellow, green, purple, orange + ink | the band name as giant letters, a repeated word, overprint | circles, triangles, nested squares, diagonals |

**Seven things they share** (these are the rules behind Part 2 of `SKILL.md`):

1. **The ground is the color.** In three of five, strong flat color or black covers 83–97% of the sheet. The other two keep a paper ground but make the *ink* chromatic and add a large tinted panel. None is "cream page + one colored button".
2. **One relationship per piece**: complementary (yellow ↔ indigo), analogous (violet + periwinkle + orchid), a primary set on black ink, a spectrum on black, or cream + pure hues with overprint. Colors are never "a few nice ones".
3. **Full strength.** No grey mixed in, no opacity tints. The only pale colors are an analogous pair sitting beside a saturated ink.
4. **Every hue appears at least twice**, in different sizes or places. Once reads as an accident, twice as a system.
5. **One type color per surface** (white, black, or the chromatic ink). Type is not a second color layer.
6. **Planes touch.** Hard edges, no gaps, no borders, no shadows.
7. **Pictures are color-controlled**: duotone, halftone, tinted to the palette, or flat geometry. Never a natural-color photo dropped in.

And one scale rule: **whisper and shout**. 12px metadata next to a 300px word. Nothing in the middle.

## The five Looks

Choose by content. Do not use the same Look twice in a row. One Look per page: sections vary the composition, not the palette.

### Look 1 — Sun: a strong ground and its complement
- **For**: landing pages, events, culture, cafés, education. Warm, confident.
- **Tokens**: `--ground:#FFC611; --ink:#16154A; --c:#3A3A9C;`
- **Type**: navy `#16154A` on yellow = 10.8:1; indigo on yellow = 5.9:1. The poster sets *white on yellow* (1.57:1): that fails as UI text, so don't. White belongs on the indigo/navy plane (9.3:1 / 16.9:1). Giant word weight 400–500, tracking −0.05em.
- **Composition**: whisper (tagline 28px + two 12px metadata columns on offset spans) → shout (one giant noun or number, equal-width) → mass (a duotone/halftone plane cut by two edges with one diagonal edge).
- **UI**: hero; a later section inverted (indigo ground, yellow type 5.9:1). Buttons: navy on yellow, yellow on indigo.
- **Uses**: M1, M3 or M4, M8.

### Look 2 — Violet ink: one chromatic ink on white
- **For**: magazines, journals, reports, publishing, editorial products. Quiet power.
- **Tokens**: `--paper:#fff; --ink:#4F2A7D; --sky:#CFDBF1; --wall:#BD9CBB;`
- **Type**: *all* type is the violet: 10.7:1 on white, 7.7:1 on periwinkle, 4.4:1 on orchid (large text only). No black anywhere.
- **Composition**: a giant lowercase masthead crossing the top edge of an inset tinted panel; one cover line (a slash pair `Ebb/ جزر` works in Arabic); a bottom colophon strip: tiny data in columns, three or four bold items in the same ink.
- **Check with** `--paper-ground` (see `scripts/color_power.py`).
- **Uses**: M7, M10, M11.

### Look 3 — Primary bands: stacked full-bleed color
- **For**: fact-driven landing pages, campaigns, institutions, schedules. Loud, objective.
- **Tokens**: `--blue:#2F7BFF; --green:#0FA23A; --yellow:#EFB83E; --red:#E6040A; --ink:#0D0D0D;`
- **Type**: one ink on every band, as the poster does. UI-safe values: ink on `#2F7BFF` 5.0:1, on `#0FA23A` 5.8:1, on `#EFB83E` 10.7:1, on red 4.1:1 (large text only). The poster's deeper blue `#1248B0` and green `#097F28` need *white* text (8.1:1 / 5.2:1) instead.
- **Composition**: sections as bands, each holding **one line of facts sized to the full width** ("Four floors / 112 desks / 6 rooms"); the last band, double height, carries two columns of 14–17px lists and a two-line lockup at the bottom. Band height follows the word.
- **Uses**: M1, M2, M9.

### Look 4 — Black + spectrum: one module, many hues
- **For**: catalogs, booking, product families, categories. In dashboards, only the legend, header or navigation, never behind dense tables.
- **Tokens**: `--g:#0B0B0B;` + 6–9 of `#FEBD01 #007DD9 #00B346 #FF2B27 #FE50FF #E6E7E9 #3744C6`
- **Type**: white on black (19.7:1); ink on yellow/azure/green/red/magenta/grey (4.6–16:1); **white on `#3744C6`** (7.5:1). That blue is 2.6:1 against black, so it stays decoration, with no text on it.
- **Composition**: the product's own object drawn as one flat square-based shape, repeated, interlocking in staggered columns, touching, orientation alternating. **One hue = one meaning** (one room, one category) here and everywhere else in the product. The name, white and heavy, at the top end; one or two tiny paragraphs rotated 90° at the edge.
- **Uses**: M6, M10.

### Look 5 — Gig poster: cream or black + pure hues, overprint
- **For**: events, music, community, launches. Playful, graphic.
- **Tokens**: `--cream:#EFEBDD; --ink:#0D0D0D; --red:#E8212B; --cyan:#03AADD; --yellow:#FFD400; --purple:#6B126D;`
- **Type**: ink on cream 16.3:1, purple on cream 9.1:1, ink on cyan/yellow 7.2/13.6:1. Never red text on the red plane.
- **Composition**: one repeated word (3 lines), alternating ink and one hue; two large circles overprinted (yellow × cyan = green), a diagonal red plane; a 4-column row of small times and facts at the bottom.
- **Check with** `--paper-ground`.
- **Uses**: M1, M5, M8.

### More grounds, same method (to avoid yellow-and-indigo every time)
Text pairs are WCAG-checked; use the second color as a *plane*, not as text, unless a pair is listed.

| Ground | Second plane | Text |
|---|---|---|
| Orange `#FF6A13` | navy `#10163F` (6.1:1 against the orange) | ink on orange 6.8:1; white on navy 17:1 |
| Cobalt `#1D3BFF` | yellow `#FFD400` | white on cobalt 6.7:1; yellow on cobalt 4.7:1; ink on yellow 13.6:1 |
| Pink `#FF6FB1` | deep green `#0B4B2E` | ink on pink 7.6:1 |
| Vermilion `#FF4B1F` | cream `#F3EBDD` + ink | ink on vermilion 5.8:1 (white 3.3:1: large only) |
| Deep red `#C8102E` | pink `#FFB3C7` | white on red 5.9:1 |

To add a Look: choose the relationship (complementary, analogous, primary set, spectrum), keep ground colors at saturation ≥ 0.8 and value ≥ 0.9, assign one text color per field from a contrast check, then measure the screenshot with `scripts/color_power.py`.

## Mechanics (tested)

### M1 — Equal-width lockup
Each line is sized so it spans the full measure; the lines form one block of unequal sizes. Use 2–4 short lines of facts.

```html
<h1 class="fit"><span>Four floors</span><span>112 desks</span></h1>
```
```css
.fit>span{display:block;width:fit-content;white-space:nowrap;line-height:.82;
          font-size:clamp(40px,12vw,220px)}        /* the guess used when JS is off */
.fit>span+span{margin-top:.3em}                      /* room for descenders (p, y, g); .1em for caps and figures */
:lang(ar) .fit>span{line-height:1.15}                /* Arabic: no tight leading, no tracking */
.fit{letter-spacing:-.05em}                          /* heavy Latin: −.05 to −.07em; Arabic: 0 */
```
```js
const fit = () => document.querySelectorAll('.fit').forEach(el => {
  const lines = [...el.children], w = el.clientWidth;
  lines.forEach(l => l.style.fontSize = '100px');           // measure big: small sizes round glyph advances
  for (let pass = 0; pass < 2; pass++) {                    // kerning is not linear: measure, scale, measure again
    const k = lines.map(l => w / l.offsetWidth);                                             // all reads
    lines.forEach((l, i) => l.style.fontSize = parseFloat(l.style.fontSize) * k[i] + 'px'); // then all writes
  }
});
document.fonts.ready.then(fit); addEventListener('resize', fit);
```
Measured: every line ends at 99.9–100% of the container at 1440px and at 390px.
**Why not `text-fit`?** CSS `text-fit: grow per-line-all` exists (Chrome/Edge 150+) but keeps the computed `font-size` unchanged, so an `em` letter-spacing of −.065em collapses to about −1px and the tight tracking, the signature of this look, is lost; Firefox and Safari don't support it. A script that changes the real `font-size` looks the same everywhere. A first draft that measured at 16px was off by 10–25% (glyph advances round at small sizes); measuring at 100px with two passes fixed it.
**Arabic (tested with Noto Kufi Arabic 800, RTL, at 1440px and 390px):** every line fits at 99.9–100%, flush right. Keep `letter-spacing:0` and `line-height:1.15`. Two things to add: (1) a line that is entirely Latin or numeric, such as a time range, takes `dir="ltr"` on its own `<span>`; without it `06:00–23:00` is displayed as 23:00–06:00 in an RTL block, and an inline `<bdi>` inside a lockup is 1.9em tall; (2) put `overflow:clip` on the section that holds the lockups, because Kufi's tall font metrics extend the page's scroll area about 34px below the last line otherwise.
A very short word fitted to the full width becomes enormous (a 3-letter word at 1440px is about 700px tall). In bands, use words of five or more characters, or accept a shorter fit.

### M2 — Color bands
```css
.bands{display:grid;grid-template-rows:auto auto auto 1fr;min-height:100svh}   /* heights follow the words */
.band{padding:clamp(30px,3.2vw,46px) var(--margin)}
.band.blue{background:var(--blue)} /* … one class per hue, ink text on all */
```
A fixed band height crops a fitted word (tested); let the word set the height.

### M3 — Halftone (dots whose size follows the photo's tone)
A grey-to-black radial dot cell is *screened* with the inverted photo at half opacity, thresholded with `contrast()`, then an SVG filter turns white into the ink color and black into transparency, so the ground shows through.
```html
<div class="mass"><div class="ht"><img src="photo.jpg" alt=""></div></div>
<svg width="0" height="0" aria-hidden="true" style="position:absolute">
  <filter id="ht-ink" color-interpolation-filters="sRGB" x="0" y="0" width="100%" height="100%">
    <feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1 0 0 0 0" result="a"/>
    <feFlood style="flood-color:#16154A"/>            <!-- the ink hex goes here -->
    <feComposite in2="a" operator="in"/>
  </filter>
</svg>
```
```css
.mass{position:absolute;inset-inline:22% 0;inset-block-end:0;height:54%;background:var(--c);
      clip-path:polygon(0 100%,0 94%,9% 74%,24% 52%,46% 34%,72% 20%,100% 14%,100% 100%)}   /* diagonal sweep */
.ht{position:absolute;inset:0;isolation:isolate;background:#000;filter:contrast(60) url(#ht-ink)}
.ht img{display:block;width:100%;height:100%;object-fit:cover;filter:grayscale(1) invert(1) blur(1.2px);opacity:.5}
.ht::after{content:"";position:absolute;inset:0;mix-blend-mode:screen;
           background:radial-gradient(circle,#808080,#000) 0 0/7px 7px}   /* 6–9px cell */
```
Set `color-interpolation-filters="sRGB"` or the luminance mapping shifts. Always `alt=""` (decorative) and keep real text outside the mass.

### M4 — Duotone (a photo in two palette colors)
`tableValues` = `"dark light"` per channel, each hex byte ÷ 255. Example: navy `#16154A` → yellow `#FFC611`. Tested; the result is exactly the two colors, with no off-hue highlights (plain `multiply` + `lighten` blending shifts the highlights when the channels differ).
```html
<filter id="duo" color-interpolation-filters="sRGB">
  <feColorMatrix type="matrix" values=".333 .333 .333 0 0  .333 .333 .333 0 0  .333 .333 .333 0 0  0 0 0 1 0"/>
  <feComponentTransfer>
    <feFuncR type="table" tableValues="0.086 1.000"/>
    <feFuncG type="table" tableValues="0.082 0.776"/>
    <feFuncB type="table" tableValues="0.290 0.067"/>
  </feComponentTransfer>
</filter>
```
```css
.photo img{filter:url(#duo)}
```

### M5 — Overprint (planes multiply into a third color)
```css
.o{position:absolute;aspect-ratio:1;border-radius:50%;mix-blend-mode:multiply}   /* yellow × cyan = green; ink type under it darkens */
```
Make the circle with `border-radius` and `aspect-ratio`, not a stretched SVG (`preserveAspectRatio="none"` turned a circle into an ellipse in testing).

### M6 — Module with a cutout (one shape, many hues)
```css
.mod{position:relative;aspect-ratio:1;background:var(--c);color:var(--ink);padding:14px 16px;
     display:flex;justify-content:space-between;align-items:flex-start;font-weight:700}
.mod .door{position:absolute;inset-block-end:0;inset-inline-start:0;width:46%;aspect-ratio:1;
           background:var(--g);border-start-end-radius:100%}                      /* quarter disc, mirrors in RTL */
.mod.flip .door{inset-inline:auto 0;border-start-end-radius:0;border-start-start-radius:100%}
.stack{display:grid;grid-template-columns:repeat(3,1fr);align-items:start}
.stack .col{display:flex;flex-direction:column}
.stack .col:nth-child(2){margin-top:82%}   /* % margin = column width = one module: staggers the columns */
.stack .col:nth-child(3){margin-top:146%}
```
Keep text off the cutout (black label on the black cutout disappeared in testing): number and name sit at the top. Draw *this product's* object (a door-swing for rooms, a key, a chair, a plate), never a borrowed one.

### M7 — Masthead over a tinted panel
```css
.cover{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));grid-template-rows:auto 1fr auto}
.mast{grid-column:1/9;grid-row:1/3;align-self:start;z-index:3;font-weight:800;letter-spacing:-.045em}   /* equal-width */
.panel{grid-column:2/12;grid-row:1/3;margin-top:clamp(90px,12vw,180px);
       background:linear-gradient(168deg,var(--sky) 0 52%,var(--wall) 52%)}
```
Leave a little room above the masthead; with none, ascenders were cropped by the top edge and it read as an error.

### M8 — Diagonal plane
`clip-path:polygon(100% 0,0 0,100% 100%)` for a triangle; a polygon with a few points for a sweeping edge (see M3). One diagonal per page.

### M9 — Crop marks and grain (poster moment only)
```css
.marks::before{content:"";position:absolute;inset:0;z-index:4;pointer-events:none;
 background:
  linear-gradient(#000,#000) 0 22px/16px 1px no-repeat, linear-gradient(#000,#000) 22px 0/1px 16px no-repeat,
  linear-gradient(#000,#000) 100% 22px/16px 1px no-repeat, linear-gradient(#000,#000) calc(100% - 22px) 0/1px 16px no-repeat,
  linear-gradient(#000,#000) 0 calc(100% - 22px)/16px 1px no-repeat, linear-gradient(#000,#000) 22px 100%/1px 16px no-repeat,
  linear-gradient(#000,#000) 100% calc(100% - 22px)/16px 1px no-repeat, linear-gradient(#000,#000) calc(100% - 22px) 100%/1px 16px no-repeat}
.grain::after{content:"";position:absolute;inset:0;z-index:5;pointer-events:none;opacity:.10;mix-blend-mode:multiply;
 background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1.2 -.1'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
```
Grain only on flat color fields, ≤ 10%, never on text-heavy product screens. It is a print finish, not decoration.

### M10 — Rotated side text
`writing-mode:vertical-rl; font-size:12px; max-height:70vh`. Short paragraphs only. In Arabic rotate whole words; never stack letters.

### M11 — Bilingual slash pair
```html
<p class="line"><span lang="en">Ebb/</span> <bdi lang="ar" dir="rtl">جزر</bdi></p>
```
Arabic part: Noto Kufi Arabic 800, `letter-spacing:0`, `line-height:1.3`.

### Finishing details from the references (pick two or three, never all)
The em dash on titles and labels (`Floor 4—`, `OPEN DAILY—`); a year stamp in Roman numerals or an issue number (`MMXXVII—`, `No. 14`); two or three columns of 12px metadata on offset spans; a colophon strip; crop marks; a tiny rotated paragraph at the edge.

## Appendix — palettes taken from the booklet (muted starting points)

These came from the booklet's Keller/Ballmer/Müller-Brockmann/Hofmann posters. They are quieter than the Looks above; if you use one, still apply the rules in Part 2 (ground first, full strength, each hue twice).

| Palette | Colors |
|---|---|
| Keller — museum | orange `#F05A1A` · wine `#8E1B2E` · green `#1F6B4A` · ink |
| Ballmer — building | blue `#0047BB` · ink · paper |
| Ballmer — office | red `#E30613` · ink · grey `#B9B7AE` |
| Müller-Brockmann — film | ink ground · paper type · warm grey `#8C8A80` · small red `#E30613` |
| Müller-Brockmann — concert | near-white · red `#E30613` · yellow `#F2B705` · blue `#1E5AA8` · ink, all in small units |
| Müller-Brockmann — grid book | orange `#EE6B2F` field · paper hairlines · ink type |
| Hofmann — Basel | paper · ink · one red `#E30613` |
