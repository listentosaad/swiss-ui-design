# swiss-ui-design

A Claude skill for designing website and app interfaces in the Swiss / International Typographic Style, so the result reads as the work of a disciplined human designer rather than a generic AI template.

## What it does

- Starts from the content and finds a concept specific to the product.
- Builds on a grid derived from the type (after Müller-Brockmann's *Grid Systems*).
- Composes asymmetric, flush-start layouts with type as the main image.
- Adds a "poster layer" of signature moves drawn from Keller, Ballmer, Müller-Brockmann, Hofmann, the Basel object poster and Matter's photomontage.
- Chooses a **Look** before the layout (ground, color scheme, picture treatment): five systems sampled from real posters, with the ground covering most of the first screen, not a cream page with an accent.
- Uses full-strength flat color as planes, with every text/background pair checked against WCAG.
- Ships tested CSS for the poster techniques: equal-width lockups, color bands, halftone and duotone pictures, overprint, module stacks.
- Measures the color power of a screenshot (`scripts/color_power.py`).
- Reviews the result against a checklist of common AI-template tells.
- Supports Arabic (RTL) and English interfaces.

## Structure

```
swiss-ui-design/
├── SKILL.md                 # the skill: workflow, grid/type/color, Arabic & RTL, components, review checklist, sources
├── README.md
├── references/
│   └── looks.md             # five Looks (ground, palette, contrast pairs), the posters' measured anatomy, tested CSS
├── scripts/
│   └── color_power.py       # share of the first viewport that is strong flat color or ink (needs Pillow)
└── evals/                   # test cases for checking the skill after each change
    ├── arabic-coworking-landing/     # Arabic RTL landing page (prompt in Arabic)
    └── english-roastery-dashboard/   # English orders dashboard
```

Each test case has a `prompt.md` (the user request), a `case.yaml` (what a good result looks like) and a `graders/` folder with one checkable statement per file.

## Install

- **Claude Code:** copy the `swiss-ui-design` folder into `~/.claude/skills/` (or your project's `.claude/skills/`).
- **Claude apps:** upload the zipped folder as a custom skill.

## Testing

Run the test cases after editing the skill, to check that a change improved the output and didn't break anything. With Claude Code (v2.1.269 or later), from inside the `swiss-ui-design` folder:

```bash
claude plugin eval . --allow-tools Write,Edit,Bash
```

It runs each case with and without the skill and writes a report under `evals/results/`. These are real, billed model runs. You can also ask Claude to run the cases with the skill-creator skill and review the screenshots.

## Sources

Built from the Arabic booklet *The Swiss School of Design* and the references it cites: Hollis, *Swiss Graphic Design*; Meggs, *A History of Graphic Design*; Müller-Brockmann, *Grid Systems in Graphic Design*; Hitchcock & Johnson, *The International Style*; Hofmann, *Graphic Design Manual*; Smashing Magazine; Print Magazine; Aristova & Vasilieva on flat design and the International Style.
