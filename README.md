# Temper Results

## Local AI measured as complete work

Temper Results is the readable evidence layer for the local-AI project. It
answers three practical questions: what works now, on which machine, and why a
plausible alternative was not selected.

The unit of advice is a complete profile: model artifact, template, engine,
context and cache policy, tools, placement, harness, and hardware. A model name
or tokens-per-second result is never enough by itself.

## Why this exists

Local AI on consumer hardware is not a toy anymore. It does not match frontier
models at the limits of their ability, but it can already do useful everyday
work entirely offline. That means private work can remain private, a provider's
outage cannot stop the job, and a model cannot be silently weakened or reshaped
behind the same product name and price. Many tasks do not need frontier-model
ability at all. A dependable local utility profile can handle those tasks while
reserving expensive frontier subscriptions for the work that benefits from
them.

The important word is **work**. The fastest token stream is not necessarily the
fastest route to a correct result. [The speed of finished work](PHILOSOPHY.md)
explains why this project measures complete jobs, distrusts attractive paper
claims until they survive the real setup, and treats evidence as part of the
product rather than benchmark decoration.

## Start here

1. [Current choices](CURRENT.md) contains the profiles that have earned support.
2. [The philosophy](PHILOSOPHY.md) explains what the project is optimizing for
   and why evidence matters.
3. [The guide](GUIDE.md) explains the few mechanics that matter in practice.
4. [Machines](machines/README.md) keeps every recommendation tied to witnessed
   hardware.
5. [Other paths](CONSIDERED.md) lists measured `LAB` profiles, rejections, and
   watch items with their next gate.
6. [Proofs](details/README.md) contains the compact, dated evidence.

## Current measured machine

On the Apple M5 with 32 GiB unified memory, Qwen3.8-27B has two supported
llama.cpp layouts:

| Layout | Context | Use it when | Measured trade-off |
|---|---:|---|---|
| Plain Q4_K_M | 131,072 | speed and maximum qualified context matter most | 11.50 tok/s in the matched decode test; 120,190-token fill passed |
| Dynamic 3.0 UD-Q4_K_XL | 102,400 | quality is the first priority | same 11/12 short and 4/4 practical gates; 0.65% lower paired perplexity; 9.69 tok/s |

Dynamic XL is the current live selection. Plain Q4 remains recommended rather
than being treated as an obsolete control. Both use one slot, Q8 K/V cache,
embedded MTP, bounded checkpoints, no extra prompt-cache RAM, a pinned patched
template, and no vision projector.

The largest measured systems gain was usable context, not a new model.
Matching the engine, KV, slot, checkpoint, cache, template, artifact, and
client-window posture produced fully exercised 100k–128k profiles on this
machine.

The 0.6B reranker remains CPU-only and on demand. Its placement witness is
historical but intentionally preserved: CPU placement completed 65 growing
turns with no aborts; GPU co-residency produced 3 aborts in 66 turns.

## A useful `LAB` alternative

Muse Glimmer 30B is installed as an optional, mutually swapping profile for
deliberate and visual work. Its exact 102,400-token Q4-projector profile passed
text, Pi, image, routing, and memory-safety checks, including all four facts in
the frozen dashboard task at 17.405 GiB peak observed RSS. It is still `LAB`:
real screenshots, research decisions, tool recovery, and retained synthesis
must establish whether it deserves a portfolio role.

## Publication rules

- Correct first-attempt work outranks component speed.
- Context is qualified by real compute, near-capacity fill, replay, branching,
  swap, and desktop survival—not by a listening socket.
- Large local models swap; they do not co-reside on this 32 GiB profile.
- Tools and harness integrations remain explicit owner choices.
- A result stays attached to its artifact, runtime, machine, and date.
- Failures remain visible, but invalidated setup-era detail does not remain in
  the current path merely because it was once measured.

[Method](METHOD.md) defines the status labels and evidence boundary.

Last reviewed: **2026-08-21**.
