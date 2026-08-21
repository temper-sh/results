# Muse Glimmer 30B live `LAB` profile

Disposition: **LAB** on the Apple M5 / 32 GiB witness.

## TL;DR

Muse's exact Unsloth Q4 XL target plus Q4 projector is installed and safe to
evaluate at 102,400 tokens. Text protocol, 96k synthesis, typed tool recovery,
synthetic vision, Pi routing, and Qwen/Muse swapping passed. It has not yet
earned a practical role: use real screenshots, research decisions, tool
recovery, and retained long synthesis to decide that.

## Profile

| Field | Value |
|---|---|
| Target | `Muse-Glimmer-30B-UD-Q4_K_XL.gguf`, revision `faa5b025…`, SHA-256 `82bece30…` |
| Projector | `mmproj-kquant.gguf`, SHA-256 `f48b4523…` |
| Template | official Meta revision `a4e59da5…`, SHA-256 `cfc67e5f…` |
| Runtime | llama.cpp b10470 / `34af94cd9`; llama-swap v250 |
| Window | one 102,400-token slot, Q8 K/V, 16 checkpoints, prompt-cache RAM off |
| Reasoning | medium, separated, 1,024-token reasoning budget |
| Sampling | temperature 1, top-p 0.95, top-k 64 for role work |
| Speculation | none; current Q4 DFlash rejected |

## What passed

| Gate | Result |
|---|---|
| Text protocol | control, reasoning, tools, history, and cancellation passed |
| Typed failure recovery | corrected the call and completed the synthetic task |
| Long synthesis | meaningful 96,165-token prompt, replay, and branch passed at a 102,400 server window |
| Vision | all 4 frozen dashboard facts, exact visible replay, image -> text -> image lifecycle |
| Live integration | llama-swap text/image, Pi model discovery/request, and mutual Qwen/Muse swapping passed |
| Deployed vision resources | 17.405 GiB peak observed RSS; swap stayed at 492 MiB; no thermal stop |

The 100k dashboard request used 1,266 prompt tokens at 89.60 tok/s and decoded
302 tokens at 7.86 tok/s. A cold routed replay including model load took 60.73
seconds and again returned all four facts.

A deliberately tiny 64-token text budget ended inside reasoning with no visible
answer; 256 tokens returned the exact answer normally. This is why the live Pi
profile advertises 4,096 output tokens.

## Directional evidence, not promotion evidence

Medium reasoning completed all 12 synthetic role cases in 589.15 seconds. The
frozen exact-label scorer passed 6/12, while a post-hoc semantic audit judged
all 12 decisions substantively correct. Because that audit was not predeclared,
it is useful direction but not a qualification score. High reasoning took
898.25 seconds for only six cases and is not the routine default.

The current Q4 DFlash also failed its useful-work gate: block maximum 15 was
19.67% slower and block maximum 5 was 16.90% slower than target-only across
three frozen tasks. It is absent from the installed profile.

## What real work should decide

1. A naturally occurring screenshot, chart, or dense document decision.
2. A multi-source research or product decision with evidence and uncertainty.
3. A tool-backed task with a natural or safely injected typed failure.
4. A real 20k+ retained synthesis with scattered constraints and a follow-up
   branch.

Score first-attempt completion, factual errors, quiet-wrong actions, correction
turns, tool validity, completed-work wall time, and owner preference. Compare
Qwen only on overlapping text/tool work; vision does not need a forced
text-only control.

## Evidence boundary

Muse is a model-dossier `LAB` profile, not a reviewed supported-role decision.
The copied [`evidence.json`](evidence.json) is byte-identical to the sanitized
live integration record, SHA-256 `004c4792…`. The direct 102,400 vision report
has SHA-256 `26a53386…`; its exact-PID process watcher has SHA-256 `203d9890…`
and remains in Labs rather than being copied here. Labs was based on revision
`ec22c368…` with the dossier and runs still in the working tree.

## Promotion gate

Promote only if retained work establishes at least one differentiated role
without quiet-wrong regressions. MLX, DSpark, higher projector precision, and
fine-tunes remain separate profiles and do not inherit this result.
