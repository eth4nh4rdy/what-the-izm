# what_the_izm_master_roadmap.md
## What the Izm? — Theory & Philosophy Worksheet Generator
## Primo English · Primo Curriculum Manager

*Version: 0.1 — Approved foundation. Modify only when build direction changes.*
*Created: 2026-09-02 by MODE: DEV*

---

## What This Is

**What the Izm?** is a theory and philosophy ESL worksheet generator. The student or teacher selects a theory from the theory bank and a stage within that theory's arc. The program fetches information on the theory at that stage from multiple data sources, passes it through an LLM pipeline, and generates an 8-page classroom worksheet in DOCX format.

The program has two equal goals: make difficult ideas genuinely understandable, and provoke real intellectual discussion in the classroom. Page 4 explains. Page 5 attacks. The exercises are language-focused, topic-aware, and satirical. The audience is Korean adults who are genuinely curious about ideas.

Each theory is not one class — it is a structured arc of classes. Stoicism is not one worksheet. It is Hellenic Origins, then Roman Stoicism, then Neo-Stoicism. Students move through a theory the way they would move through a course, building vocabulary and comprehension at each stage before the next one opens up.

---

## Tone & Identity

- Intellectually serious. Occasionally brutal. Funny when it serves the content.
- Page 4 is the teacher: clear, accessible, level-calibrated explanation of the theory at its current stage.
- Page 5 is the provocateur: real historical critiques, devil's advocate reframings, classroom debate prompts with no clean answers. This page is allowed to be rude, aggressive, and genuinely challenging.
- Exercises are language-first but philosophy-flavored. Satire and humor are tools, not decoration.
- The program respects the student's intelligence. It does not condescend. It does not hedge.

---

## Repository

- **Repo name:** `what-the-izm`
- **Remote:** `https://github.com/eth4nh4rdy/what-the-izm`
- **Local path:** `C:/users/smeefer/primo_english/what-the-izm/`
- **Platform:** Windows 11, Python 3.10+, Miniconda
- **Git initialized before any code is written — no exceptions**
- **Branch strategy:** `main` (stable) + feature branches per phase
- **Standalone repo — not a fork of any existing Primo program**

---

## Page Structure

| Page | Content |
|---|---|
| 1 | What the Izm? header · Name/Date · Theory name · Stage · 3 warm-up questions |
| 2 | Keywords 1–3 — word, POS, EN def, KO def, synonyms, My sentence blank |
| 3 | Keywords 4–6 — same format |
| 4 | Theory summary — stage-aware, level-calibrated, 400–600 words, all keywords in bold |
| 5 | Controversy & Debate — real critiques, devil's advocate prompts, classroom debate questions |
| 6 | Exercises — izm exercise bank |
| 7 | Exercises continued |
| 8 | Writing homework — LLM-generated prompt + 20 blank writing lines |

---

## Keyword Block Format (Pages 2–3)

One block per keyword, 3 blocks per page:

```
**[word] ([part of speech])**
**English:** [one clear sentence definition]
**Korean:** [한국어로 한 문장]
**Synonyms:** [synonym1] · [synonym2] · [synonym3]
**My sentence:** __________________________

______________________________________________________________________________________________
```

Keywords are selected from the fetched theory content. Selection criteria:
- Philosophical or academic vocabulary the student is unlikely to know
- Terms that are central to understanding the theory at this stage
- Words with real utility beyond the worksheet — usable in academic writing and discussion

---

## Page 4 — Theory Summary

- 400–600 words minimum
- Written at the target Primo level — vocabulary and sentence complexity calibrated accordingly
- Stage-aware: content covers only what is relevant to the current stage of the theory's arc
- All 6 keywords appear in the body text, wrapped in `**double asterisks**` for bold rendering
- Tone: clear, engaging, written as if explaining to a curious and intelligent friend
- No academic hedging. No passive-voice fog. No "scholars argue that."

---

## Page 5 — Controversy & Debate

This is the sharpest page in the program. It contains three components:

**1. The Attack**
A real historical critique of the theory at its current stage — sourced from an actual philosopher, school of thought, or intellectual tradition that opposed it. Named, specific, and not softened. The LLM is instructed to present this critique as the critic would — with full force, not as a balanced summary.

**2. Devil's Advocate**
2–3 reframings that challenge the student's likely assumptions about the theory. These are designed to be uncomfortable. They may be provocative, counterintuitive, or deliberately one-sided. The goal is to make the student defend or abandon their position.

**3. Classroom Debate Prompts**
2–3 open questions with no clean answers. Designed to generate disagreement in the room. These are not comprehension checks — they are genuine philosophical disputes that the theory itself has not resolved.

---

## Theory Bank Structure

Stored in `theories/theories.yaml`. Each entry contains:

```yaml
theories:
  - id: stoicism
    name: Stoicism
    slug: stoicism
    description: >
      A Hellenistic philosophy founded in Athens by Zeno of Citium, teaching that virtue
      is the only true good and that destructive emotions result from errors in judgment.
    data_sources:
      - wikipedia
      - sep
    stages:
      - id: 1
        name: Hellenic Origins
        focus: Zeno of Citium and the founding of the Stoa. Early doctrine on logos, virtue, and the good life.
        key_figures: ["Zeno of Citium", "Cleanthes", "Chrysippus"]
        key_texts: ["Discourses (Epictetus — later)", "Fragments of Zeno"]
        key_controversies:
          - "Is virtue truly sufficient for happiness regardless of external circumstances?"
          - "Stoic determinism vs. human agency — are we free or just pretending?"
      - id: 2
        name: Roman Stoicism
        focus: The Stoic tradition adapted and expanded by Roman thinkers under empire.
        key_figures: ["Seneca", "Epictetus", "Marcus Aurelius"]
        key_texts: ["Meditations", "Letters to Lucilius", "Enchiridion"]
        key_controversies:
          - "Can a slave philosopher be free? Epictetus and the contradiction of Stoic slavery."
          - "Seneca's wealth versus Stoic poverty — hypocrisy or pragmatism?"
      - id: 3
        name: Neo-Stoicism and Modern Revival
        focus: The rediscovery and reapplication of Stoic ideas in contemporary philosophy and popular culture.
        key_figures: ["Justus Lipsius", "Ryan Holiday", "Massimo Pigliucci"]
        key_texts: ["De Constantia", "The Obstacle Is the Way", "How to Be a Stoic"]
        key_controversies:
          - "Is modern Stoicism a philosophy or a self-help brand?"
          - "Has the revival stripped Stoicism of its political and cosmological dimensions?"
```

The bank is seeded with 5–8 theories in Phase 0 and grows over time. Adding a theory requires a full stage definition — no entry is added without stages, key figures, key texts, and key controversies for every stage.

---

## Exercise Bank

Dedicated `exercises/izm_exercise_bank.yaml`. Designed in Phase 2 — operator session required before generator is built.

Exercise types are:
- **Language-first:** vocabulary in context, argumentation structures, hedging language, academic register
- **Topic-aware:** content draws on the theory, its figures, and its controversies
- **Satirical and humorous:** the frames are funny; the language practice is real

Example exercise directions (to be fully specified in Phase 2):
- Rewrite this philosopher's argument so your grandmother could understand it
- Match the theory to the modern situation it would handle worst
- This philosopher just posted this tweet. Is it based or embarrassing? Defend your answer.
- Fill in the blank with the correct hedging phrase — the philosopher is not sure and needs to sound like it
- Identify the logical fallacy in this argument against the theory

Exercise types are not finalized here. Phase 2 defines them.

---

## Architecture

```
what-the-izm/
    ├── izm.py                         # CLI entry point
    ├── generator.py                   # LLM — 8-page content generation
    ├── formatter.py                   # DOCX renderer — 8-page structure
    ├── aggregator.py                  # Combines fetcher output into single payload
    ├── requirements.txt
    ├── .env
    ├── .env.example
    ├── .gitignore
    ├── README.md
    ├── config/
    │     ├── sources.yaml             # LLM provider config + data source config
    │     └── levels.yaml              # Primo Scale 1–10 (copied from existing program)
    ├── fetchers/
    │     ├── __init__.py
    │     ├── base_fetcher.py          # Abstract base — interface all fetchers implement
    │     ├── wikipedia_fetcher.py     # Primary source
    │     └── sep_fetcher.py          # Stanford Encyclopedia of Philosophy — secondary source
    ├── theories/
    │     └── theories.yaml            # Theory bank — grows over time
    ├── exercises/
    │     └── izm_exercise_bank.yaml   # Exercise bank — defined in Phase 2
    └── output/
          └── .gitkeep
```

---

## CLI

```bash
python izm.py --theory stoicism --stage 1 --level 6
```

**Arguments:**
- `--theory` — slug from `theories.yaml` (required)
- `--stage` — integer stage number (required)
- `--level` — integer 1–10, Primo Scale (required)
- `--list-theories` — prints all valid theory slugs and exits
- `--list-stages <theory>` — prints all stages for a given theory and exits

**Validation:**
- `--theory` must match a slug in `theories.yaml` — exit with error if not found
- `--stage` must be a valid stage number for the selected theory — exit with error if out of range
- `--level` must be an integer between 1 and 10

**Output filename pattern:**
```
output/izm_[theory]_stage[N]_L[level]_[YYYYMMDD].docx
```

---

## LLM Provider

OpenRouter only. Same config pattern as News Noodle, Brainrot, and Carry-On Confidence. `sources.yaml` contains a single LLM block for OpenRouter. `get_llm_client()` in `generator.py` reads OpenRouter config and raises `RuntimeError` if `OPENROUTER_API_KEY` is missing.

`max_tokens` set to 8000 — philosophical content on Page 5 is dense, and the full 8-page prompt requires headroom.

---

## Phase Sequence

---

### Phase 0 — Foundation

**Goal:** Repo exists. Git initialized. Directory scaffold complete. All config files in place. Theory bank seeded with 5–8 theories. No code written.

**Deliverables:**
- GitHub repo `eth4nh4rdy/what-the-izm` initialized
- Full directory scaffold committed
- `config/levels.yaml` copied from an existing Primo program
- `config/sources.yaml` skeleton created — LLM block for OpenRouter, data source stubs
- `theories/theories.yaml` seeded with 5–8 theories, each with full stage definitions
- `.env.example`, `.gitignore`, `requirements.txt` skeleton, `README.md` stub committed
- `output/.gitkeep` committed

**Phase 0 complete when:** `git log` shows a clean initial commit and `theories.yaml` contains at least 5 fully defined theories.

---

### Phase 1 — Fetchers

**Goal:** `wikipedia_fetcher.py` and `sep_fetcher.py` built and tested in isolation. `aggregator.py` combines their output into a single enriched content dict ready for the generator.

**Architecture:**
- `base_fetcher.py` defines the abstract interface — `fetch(theory_name, stage)` returns a standardized dict
- `wikipedia_fetcher.py` implements `base_fetcher.py` — fetches the Wikipedia article for the theory, extracts relevant sections based on the current stage's key figures and focus
- `sep_fetcher.py` implements `base_fetcher.py` — fetches the SEP entry for the theory. SEP uses structured URLs (`https://plato.stanford.edu/entries/[slug]/`) — fetcher parses HTML and extracts the relevant section text
- `aggregator.py` calls both fetchers, merges output, deduplicates overlapping content, and returns a single dict with keys: `theory`, `stage`, `summary_text`, `key_figures`, `key_texts`, `controversies`, `raw_sources`

**Isolation test:**
```bash
python -c "from fetchers.wikipedia_fetcher import WikipediaFetcher; f = WikipediaFetcher(); print(f.fetch('stoicism', 1))"
python -c "from fetchers.sep_fetcher import SEPFetcher; f = SEPFetcher(); print(f.fetch('stoicism', 1))"
python -c "from aggregator import aggregate; print(aggregate('stoicism', 1))"
```

**Phase 1 complete when:** Both fetchers and the aggregator run cleanly against at least 3 theories across different stages with no unhandled exceptions.

---

### Phase 2 — Exercise Bank

**Goal:** `exercises/izm_exercise_bank.yaml` designed, confirmed by operator, and committed. Generator cannot begin until this file is locked.

**Process:** Same as Carry-On Confidence Phase 2 and Corporate Survival Phase 2 — operator session required. MODE: DEV proposes exercise types. Operator confirms, rejects, or modifies. Format specs, difficulty ranges, instruction lines, tone notes, and answer key formats locked before YAML is written.

**Target:** 8–12 exercise types. Enough variety that no two worksheets feel the same. Every type must be:
- Executable by an LLM from a format spec
- Printable and solvable on the page without additional materials
- Language-focused at its core — philosophy is the frame, not the product

**Phase 2 complete when:** `izm_exercise_bank.yaml` is committed and operator has approved the final file.

---

### Phase 3 — Generator

**Goal:** `generator.py` built. Takes the aggregator payload, theory metadata, stage config, level config, and exercise bank as input. Produces a complete 8-page content dict via a single LLM call to OpenRouter.

**Section markers:**
```
===PAGE1===
===PAGE2===
===PAGE3===
===PAGE4===
===PAGE5===
===PAGE6===
===PAGE7===
===PAGE8===
===END===
```

**Page 5 prompt engineering — critical:**
The LLM must be instructed explicitly to:
- Name the real critic or school of thought making The Attack — no anonymous "some argue"
- Present the critique at full force — not as a balanced summary
- Write the devil's advocate prompts to be genuinely uncomfortable
- Ensure debate questions have no clean answer — if one side is obviously correct, rewrite the question

**Page 4 prompt engineering:**
- Minimum 400 words — LLM instructed to count before submitting
- No academic hedging, no passive voice, no news-report framing
- Level calibration: sentence length, vocabulary complexity, and conceptual density all scale with `--level`
- All 6 keywords must appear in the body, wrapped in `**double asterisks**`

**Isolation test:**
```bash
python -c "
from aggregator import aggregate
from generator import generate_worksheet
import yaml
levels = yaml.safe_load(open('config/levels.yaml', encoding='utf-8'))
payload = aggregate('stoicism', 1)
result = generate_worksheet(payload, 'stoicism', 1, levels['levels'][6])
print('pages:', list(result.keys()))
print('page4 words:', len(result['page4'].split()))
print('page5 preview:', result['page5'][:300])
"
```

**Phase 3 complete when:** Isolation test produces a valid 8-page content dict for at least 2 theories at different levels. Page 4 is 400+ words. Page 5 contains a named critic, devil's advocate prompts, and debate questions.

---

### Phase 4 — Formatter

**Goal:** `formatter.py` built. Consumes the generator content dict. Produces a DOCX student worksheet using python-docx.

**Branding:**
- Page 1 header: `What the Izm? · Primo English`
- Primo English QR code inserted bottom-right of Page 1 (`primo_english_qr.png`)
- Consistent typography: Calibri body 11pt, headings bold 18pt, Korean text Malgun Gothic
- Name and Date fields on Page 1
- Theory name and Stage name printed below header on Page 1

**Page rendering notes:**
- Pages 2–3: keyword block renderer — same pattern as News Noodle and Brainrot
- Page 4: line-by-line rendering with `**keyword**` bold marker detection
- Page 5: rendered as structured sections — The Attack, Devil's Advocate, Debate Prompts — each with a bold section label
- Pages 6–7: exercise block rendering — answer keys suppressed from student DOCX
- Page 8: writing homework prompt + 20 blank writing lines (`'_' * 100`, two per line slot)

**Self-test:**
```bash
python izm.py --theory stoicism --stage 1 --level 6
```
Open DOCX and confirm all 8 pages present, branding correct, Korean text renders, keywords bold in Page 4, Page 5 sections labeled.

**Phase 4 complete when:** Full DOCX opens correctly for at least 2 theories at different levels with no rendering errors.

---

### Phase 5 — CLI + End-to-End

**Goal:** `izm.py` wiring complete. Full pipeline runs from a single CLI command to a DOCX file in `/output`.

**Argument parsing:** `argparse`. Arguments: `--theory`, `--stage`, `--level`, `--list-theories`, `--list-stages`.

**Validation logic:**
- Load `theories.yaml` at startup
- Validate `--theory` against slug list — print available slugs and exit on failure
- Validate `--stage` against stage count for selected theory — print available stages and exit on failure
- Validate `--level` is integer 1–10 — exit on failure

**Pipeline wiring:**
```
parse args → validate → load configs → aggregate() → generate_worksheet() → format_worksheet_docx() → save → print output path
```

**Self-test:**
```bash
python izm.py --theory stoicism --stage 1 --level 6
python izm.py --theory utilitarianism --stage 2 --level 4
python izm.py --theory existentialism --stage 1 --level 8
python izm.py --list-theories
python izm.py --list-stages stoicism
```

**Phase 5 complete when:** All self-test commands run without errors and produce correct output.

---

### Phase Scale — Quality & Expansion

**Goal:** Stabilize, improve, and expand. No fixed completion point — minimum bar is classroom-ready output across all seeded theories at all stages.

**Quality audit:**
- Page 4 summary fills the page at all levels — density calibrated correctly
- Page 5 is genuinely provocative — not diplomatic, not hedged
- Keywords are well-chosen — not too easy, not obscure for obscurity's sake
- Exercises are varied across a run — no worksheet feels like the last one
- Korean text renders correctly in all DOCX outputs

**Expansion:**
- Theory bank reviewed and expanded — target 15–20 theories before classroom launch
- Additional data sources researched and added — candidates include PhilPapers, Internet Encyclopedia of Philosophy, Project Gutenberg (primary texts)
- Each new data source gets its own fetcher implementing `base_fetcher.py`

**Branding review:**
- Page 1 visual reviewed against other Primo programs
- Output filename pattern confirmed correct

---

## Git Conventions

- Feature branches per phase: `phase-0-foundation`, `phase-1-fetchers`, etc.
- Merge to `main` only after phase self-test passes
- Commit messages are detailed and descriptive — no single-line commits on phase completions
- No commits directly to `main` during active development

---

## Self-Test (Full Pipeline — Run After Phase 5)

```bash
python izm.py --theory stoicism --stage 1 --level 6
python izm.py --theory stoicism --stage 2 --level 6
python izm.py --theory utilitarianism --stage 1 --level 4
python izm.py --theory existentialism --stage 3 --level 8
python izm.py --list-theories
python izm.py --list-stages stoicism
```

For each worksheet run confirm:
- No errors
- All 8 pages present and correctly formatted
- Korean text renders correctly
- Exactly 3 warm-up questions on Page 1
- Theory name and stage printed on Page 1
- 6 keywords across Pages 2–3, all formatted correctly
- Page 4 summary 400+ words, all keywords bold
- Page 5 contains named critic, devil's advocate prompts, and debate questions
- Pages 6–7 contain exercises from the izm exercise bank — no answer keys visible
- Page 8 contains writing prompt and 20 blank writing lines
- What the Izm? header and QR code on Page 1
- Output file saved to `/output` with correct filename pattern

---

*End of what_the_izm_master_roadmap.md*
*Version: 0.1 — 2026-09-02*
