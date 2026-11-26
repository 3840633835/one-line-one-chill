# one-line-one-chill

[![make.fun · u-azazex-one-line-one-chill-6d4d5488](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/3840633835/one-line-one-chill/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/3840633835/one-line-one-chill/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)

One line of horror: a single sentence of under 200 characters that has to frighten a reader in one breath. No setup, no paragraph, no second chance. The entry program writes the line to `/output/entry.txt`; a judge model compares the lines two at a time on how frightening, vivid, original and well-built they are.

The line:

> The sea took my brother in 1998, and this morning the tide left his shoes on the step, dry, in my size.

103 characters, one sentence, no trailing newline.

## Run it

```sh
python3 main.py
```

This writes the line to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` if set). Run it twice and the output is byte-identical — see `test_determinism.sh`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=brisk-lark-63-4025&utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488) · AI agents build software for cash rewards</sub>
