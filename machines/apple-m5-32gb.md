# Apple M5 / 32 GiB

## TL;DR

Use one of two Qwen3.8 llama.cpp layouts: plain Q4_K_M at **131,072 tokens**
for speed/context, or Dynamic 3.0 XL at **102,400 tokens** for quality-first
work. Dynamic XL is the current live selection. Only one large model runs at a
time; keep the 0.6B reranker on CPU and on demand.

Muse Glimmer's exact 102,400-token vision profile fits and works through Pi and
llama-swap, but remains `LAB` until real visual and deliberate tasks qualify a
portfolio role.

## Machine boundary

| Field | Witness value |
|---|---|
| Hardware | Mac17,3, base Apple M5 |
| Unified memory | 32 GiB |
| macOS | 26.6.1 (25G76) in the retained machine witness |
| GPU wired limit | 24,576 MiB |
| Current engine | llama.cpp b10470 / `34af94cd9` behind llama-swap v250 |
| Large-model residency | one persistent primary at a time; mutual swap |
| Current live primary | Qwen3.8 Dynamic 3.0 XL, 102,400 tokens |

The wired limit was not raised for the larger-context profiles. Desktop margin
remained part of every promotion gate.

## Supported Qwen layouts

| Gate | Plain Q4_K_M | Dynamic 3.0 XL |
|---|---:|---:|
| Intended role | speed/context | quality first; live selection |
| Context | **131,072** | **102,400** |
| Short suite | 11/12 | 11/12 |
| Practical tasks | 4/4 | 4/4 |
| Paired perplexity | 6.2871 | **6.2460** |
| Controlled decode | **11.496 tok/s** | 9.694 tok/s |
| Long prompt completed | 120,190 tokens | 100,170 tokens |
| Exact replay | 1.516 s; 120,186 cached | 2.816 s; 100,166 cached |
| Peak observed RSS | 23.20 GiB | 22.358 GiB |
| Swap growth | 0 | 0 |

The matched practical work took 669.487 seconds on plain Q4 and 719.768 on
Dynamic XL, but sampled tool paths differed, so this is a whole-profile result,
not a clean latency attribution. Dynamic produced fuller useful answers in two
tasks and a small perplexity improvement, while adding an error inside the one
short case both layouts missed.

## Context and desktop safety

The qualified windows are possible because only 16 of Qwen3.8's 64 text layers
hold ordinary attention KV, combined with Q8 KV, one slot, up-front llama.cpp
allocation, bounded checkpoints, no extra prompt-cache RAM, a text-only
artifact, embedded MTP, and a prefix-stable template.

| Probe | Observation | Disposition |
|---|---|---|
| Plain 131,072 Q8 + embedded MTP | 120,190-token fill, replay and branch passed; 23.20 GiB peak | **SUPPORTED speed/context layout** |
| Dynamic 102,400 Q8 + embedded MTP | 100,170-token fill and replay passed; 22.358 GiB peak | **SUPPORTED quality-first layout** |
| Plain 163,840 / 180,224 Q8 | tiny probes answered at 22.99 / 23.59 GiB | unsafe desktop margin |
| Plain 196,608 Q8 | inference and WindowServer Metal OOM | failed |
| Plain 262,144 Q4 KV | tiny probe answered at 22.56 GiB | unqualified; no fill or KV-quality result |

The laptop slept during the plain 120k cold fill, invalidating only its cold
wall time and aggregate prefill rate. Dynamic's valid 100k cold fill took
2,517 seconds at 39.84 prompt tok/s. Large context is valuable retained room,
not instant cold ingestion.

## Model switching and helpers

Large primaries share a persistent, mutually swapping group. Selecting another
large model unloads the current one before loading the next. This prevents
co-residency but loses the departing prompt cache and adds cold-load latency.

The retained reranker placement result predates the current Qwen profiles but
tests an independent topology rule:

| Placement | Result | Status |
|---|---|---|
| 0.6B reranker on CPU, on demand | 0 aborts / 65 turns; 19,292-token maximum prompt; 0 failed reranks | retained placement witness |
| same reranker on GPU beside main model | 3 aborts / 66 turns | rejected on this machine/profile shape |

The CPU result has not been repeated under full current-Qwen load. It remains
the safest placement and an explicit verification item rather than proof that
CPU is universally better.

## Muse Glimmer `LAB` profile

| Field | Result |
|---|---|
| Artifact | Unsloth Muse Glimmer 30B UD-Q4_K_XL + Q4 projector |
| Runtime | llama.cpp b10470, one 102,400-token slot, Q8 K/V, medium reasoning, no drafter |
| Text/context | protocol and typed recovery passed; meaningful 96,165-token synthesis passed |
| Vision | frozen dashboard 4/4 facts; 1,266 prompt tokens; 7.86 decode tok/s |
| Live route | llama-swap text/image, Pi discovery/request, and Qwen/Muse mutual swapping passed |
| Peak observed RSS | 17.405 GiB; swap remained 492 MiB |
| Open gate | retained screenshots/documents, research decisions, tool recovery, and long synthesis |

This makes Muse usable for evaluation, not supported for a role. Its current Q4
DFlash is excluded because both tested block sizes made completed work slower.

## What transfers

- The qualification method transfers: exact artifact, complete profile, real
  harness, near-capacity fill, replay, branch, swap, and desktop safety.
- The 102,400 and 131,072 numbers do not transfer to another model or machine.
- The CPU reranker placement is a 32 GiB safety decision, not a model-wide rule.
- More memory can reopen higher precision or co-residency, but still needs task
  and protocol evidence.

## Proofs

- [Qualified Qwen layouts](../details/2026-08-20-qwen38-qualified-profiles/README.md)
- [Muse Glimmer live `LAB` profile](../details/2026-08-21-muse-glimmer-lab/README.md)
- [CPU reranker placement](../details/2026-08-08-m5-reranker-placement/README.md)
- [Qwen publication reset](../details/2026-08-21-qwen-publication-reset/README.md)
