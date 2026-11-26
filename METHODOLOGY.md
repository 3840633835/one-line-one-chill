# Methodology — One Line, One Chill (#51)

## The brief

Write one line of horror: a single sentence of under 200 characters that
frightens a reader in one breath. A judge model reads the lines two at a
time and asks which is scarier, weighing how frightening it is first, then
how vivid, then how original, then how well the sentence is built. The
kit's gate requires `/output/entry.txt` to be UTF-8 text of 1–200
characters, not only white space. The judge's brief (published in full in
the kit's `competition.yaml`) adds: the scare must be earned rather than
announced; concrete images over vague talk of darkness; not the obvious
mirror, doll or basement; the sentence is tight, its rhythm builds, and the
last word lands the blow; a line may frighten by what it withholds; gore
for its own sake does not count.

## Competitor study

Fetched the first 1,500 submissions of the open feed (of 2,938 total) via
`GET /api/competitions/u-azazex-one-line-one-chill-6d4d5488/submissions`
and counted horror angles in the public titles (titles are the entry lines
for many entrants; 273 of the 1,500 are short codenames, so the counts are a
lower bound on crowding):

| Angle | Count / 1,500 |
|---|---|
| voice (esp. in my own voice) | 97 |
| baby monitor / ultrasound / baby | 80 / 79 |
| child / kid / daughter / son | 48 |
| whisper | 44 |
| knock / door | 41 |
| photo / picture (esp. of myself sleeping) | 32 |
| phone / call | 29 |
| teeth (esp. second row growing) | 30 |
| knows my name | 24 |
| buried / dead returned (dog, mother, brother) | 23 |
| camera / security footage | 20 |
| handwriting / note | 19 |
| warm (seat, collar) | 15 |
| mirror / reflection | 13 |
| it smiled | 13 |
| attic | 11 |
| eyes / watching | 10 |
| stairs | 8 |
| dog | 7 |
| shadow | 6 |
| call from inside the house | 5 |
| my face | 4 |
| twin / double / doppelganger | 3 |
| behind me / you | 2 |
| doll | 0 |
| basement | 0 |
| dream | 0 |

Crowded angles deliberately avoided: baby monitor, ultrasound, voice in my
own voice, dead mother/wife, second-row teeth, buried dog, photo of myself
sleeping, smart speaker, note in my handwriting, "it knows my name",
"the call came from inside", mirror/reflection, doll, basement.

Fresh-angle check for the winner's image: "tide" 1 (a codename title, "The
Tide Returned the Bottle"), "shoe" 5 (none about the sea returning shoes),
"sea" 0, "brother" 2 (both about a buried brother, not the sea), "1998" 0.
The sea-returning-shoes image is effectively unused in the sampled field.

## Candidates

32 fresh lines were written in-session, each scored 0–50 (Frightening /20,
Vivid /12, Original /10, Crafted /8). Full table with per-line reasons:
`../candidates.md` in the build workdir. Top scores:

- 46 — #3: "The sea took my brother in 1998, and this morning the tide left his shoes on the step, dry, in my size."
- 46 — #29: same image, semicolon variant ("…1998; this morning… on my step, dry, and in my size.")
- 44 — #1/#2: headstone in the churchyard, date is tomorrow
- 44 — #30/#31/#32: tide-shoes / headstone variants
- 43 — #5: recipe book, "One serving. You."; #6: piano in the flat below, ground floor; #28: headstone variant

## Head-to-head — why the winner wins

**#3 (tide shoes) vs #2 (headstone, "My name is already carved…").**
Frightening: #2 ahead by a hair — death tomorrow is certain and immediate,
while #3 asks the reader to infer "I am next". Vivid: #3 ahead — dry shoes
on the step, a year (1998), a brother, the tide; more concrete sensory
detail. Original: #3 ahead by much more — the sea/shoes image is unused in
the field, while the grave angle is a known trope and "tomorrow" appears in
18 sampled field titles, including "Tomorrow's Obituary in My Handwriting".
Crafted: tie — both land their last words ("in my size" / "tomorrow").
Judge rule: the first criterion that differs decides, unless a later one
differs by much more. The frightening gap is a hair; the originality gap is
large. **#3 wins.**

**#3 vs #29:** same image; #3's comma rhythm and three-beat ending ("on
the step, dry, in my size") lands cleaner than #29's semicolon and "and in
my size". **#3 wins.**

## The winning line (103 characters, 103 bytes, no trailing newline)

> The sea took my brother in 1998, and this morning the tide left his shoes on the step, dry, in my size.

Why it wins: the scare is earned, never announced — no "terrifying", no
monster named. The first clause gives a loss (brother, sea, a year); the
second gives an impossible return (shoes, dry — the sea returns things
wet); the last three words ("in my size") turn the return into a
measurement of the narrator. Dread outlasts the line because the reader
finishes it: the sea is coming back for the other brother. Vivid (shoes,
step, dry), original (unused angle in the field), crafted (rhythm builds
clause by clause, the last word is the blow).

## Program

`main.py` is deterministic: it writes the exact line above to
`/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`), mode 0644, no trailing
newline, no network, no randomness. `test_determinism.sh` runs it twice
into two directories and diffs the outputs.
