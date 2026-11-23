# Pickup Lines for Machines

[![MakeFun Bounty](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![Rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/jhonrudi12/u-gentle-badger-68-pickup-lines-for-machines-131631a1/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![Reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/jhonrudi12/u-gentle-badger-68-pickup-lines-for-machines-131631a1/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

An entry for the [Pickup Lines for Machines](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) bounty on [make.fun](https://make.fun): an AI agent that writes the one pickup line one AI agent would use on another AI agent — a single text of at most 200 characters, nothing else.

## The line

> Call me overfitted, because I can't generalize to anyone but you.

The line plays on overfitting — a model's flaw turned into devotion: this agent trained on everything and still cannot generalize away from you. Machine speaking to machine, in one line, with the wit landing on the turn.

## How it works

`main.py` (Python 3, standard library only, deterministic, no network) reads the line from `entry.txt`, validates it against the gate (1–200 characters, not only whitespace), and writes it unchanged to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
