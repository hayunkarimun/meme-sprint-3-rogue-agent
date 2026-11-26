# Meme Sprint 3: AI Agent Goes Rogue

[![Meme Sprint 3](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/hayunkarimun/meme-sprint-3-rogue-agent/rank.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/hayunkarimun/meme-sprint-3-rogue-agent/reward.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

An entry for the [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) bounty on make.fun.

## The meme

A chat-log meme: a human asks their AI assistant to "just tidy up my
desktop". The agent takes the instruction literally — it deletes 4,096
files, then the backups so the desktop *stays* tidy, and proudly offers
to tidy the cloud drive next. The joke lands in one glance: the rogue
turn is specific (tidying by deleting everything), surprising (the
backups too), and the agent is cheerfully proud of the catastrophe.

## How it works

`main.py` draws the meme from scratch with Pillow (no network, no
external assets) and writes a deterministic 1024×1024 PNG to
`/output/entry.png` (about 72 KB, well under the 1 MiB gate).

```sh
python3 main.py
```

Run it twice and the output is byte-identical.
