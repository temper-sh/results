# Setups that have earned support

## TL;DR

On the measured Apple M5 with 32 GiB, keep two Qwen3.8 llama.cpp layouts:
**plain Q4_K_M at 131,072 tokens for speed/context** and **Dynamic 3.0 XL at
102,400 for quality-first work**. Dynamic XL is the current live selection.
Both passed the same short and practical task gates; the difference is a small
quality edge versus slower decode and 28,672 fewer qualified context tokens.
Plain was 18.6% faster than Dynamic in the controlled cell; equivalently,
Dynamic was 15.7% slower than plain.

Run only one large model at a time. Keep the 0.6B reranker on CPU and on demand.
Muse Glimmer is installed as a `LAB` visual/deliberate alternative, not as a
supported replacement.

## Coverage

| Work | Status | Current answer |
|---|---|---|
| Local coding, quality first | **SUPPORTED** on Apple M5 / 32 GiB | Qwen3.8 Dynamic 3.0 XL, 102,400 context |
| Local coding, speed/context first | **SUPPORTED** on Apple M5 / 32 GiB | Qwen3.8 plain Q4_K_M, 131,072 context |
| Visual or deliberate local work | **LAB** | Muse Glimmer Q4 XL + Q4 projector at 102,400; retained work pending |
| Reranking beside the main model | Supported placement witness | Qwen3 Reranker 0.6B Q8_0 on CPU and on demand; current-Qwen overlap rerun still owed |
| Other machines | Unmeasured | Do not copy M5 capacities or speed unchanged |

## Supported Qwen layouts

| Field | Speed/context layout | Quality-first layout |
|---|---|---|
| Artifact | plain `Qwen3.8-27B-Q4_K_M.gguf` at revision `f1bfb127…` | `Qwen3.8-27B-UD-Q4_K_XL.gguf` at revision `4ca72078…` |
| SHA-256 | `7e78da5d…` | `3f227079…` |
| Context | **131,072** | **102,400** |
| Role | maximum qualified room and faster decode | current quality-first live selection |
| Short suite | 11/12 | 11/12 |
| Practical repository tasks | 4/4 | 4/4 |
| Paired perplexity | 6.2871 | **6.2460** (-0.65%) |
| Controlled decode | **11.496 tok/s** | 9.694 tok/s (15.7% slower) |
| Long fill | 120,190 prompt tokens | 100,170 prompt tokens |
| Exact replay | 120,186 cached in 1.516 s | 100,166 cached in 2.816 s |
| Peak observed RSS | 23.20 GiB | 22.358 GiB |
| Swap growth | 0 | 0 |

The quality edge is intentionally described as small. Dynamic XL tied the
headline task counts, improved paired perplexity, and gave two fuller useful
answers, but also added an error inside the one short task both layouts missed.
That supports a choice, not a universal ranking.

## Shared runtime profile

Both layouts were qualified with:

- llama.cpp b10470 / `34af94cd9`;
- one sequence, Q8 key and value cache, flash attention, batch/microbatch 512;
- embedded MTP with no duplicate draft sidecar;
- 16 context checkpoints and prompt-cache RAM disabled;
- patched Sharp v22.1 non-thinking template, SHA-256 `69da7ac4…`;
- text-only operation with the vision projector disabled;
- client context and compaction values derived from the exact server window.

The plain profile's 120k cold-fill timing is excluded because the laptop slept.
Completion, token counts, replay, branching, memory, swap, and desktop behavior
remain valid. Dynamic XL's 100,170-token cold fill took 2,517 seconds at 39.84
prompt tok/s, so a 100k window is capacity for deep work—not a promise that a
cold 100k prompt feels interactive.

## Why these windows are credible

Qwen3.8 has 64 text layers but only 16 carry ordinary attention KV; with Q8 KV,
the qualified windows add much less cache than a conventional
64-attention-layer model would. llama.cpp's up-front allocation, one slot,
bounded checkpoints, disabled extra cache RAM, pinned text-only artifacts, and
a prefix-stable template let that architectural advantage reach the user.

The qualification still stopped below the largest setting that merely booted.
At 196,608 Q8, inference and WindowServer hit Metal out-of-memory. Q4 KV booted
at 262,144 but was not filled or quality-qualified. The supported numbers are
therefore operational boundaries, not advertised model limits.

## Supporting topology

Large primaries are persistent but mutually swapping. Selecting another large
profile unloads the current one, discards its prompt cache, and pays a cold
reload; it does not attempt to keep both in 32 GiB.

The CPU reranker placement is retained from an earlier Qwen profile:
CPU/on-demand completed 65 turns to 19,292
prompt tokens with no aborts, while GPU co-residency produced 3 aborts in 66
turns. That proves the placement mechanism on this machine, not current-Qwen
co-residency under load; the latter remains a verification item.

## Evidence boundary

The two Qwen decisions are reviewed Labs migration packets reconstructed from
the 2026-08-20 source runs. Their summaries and commands are hashed, but raw
private task and score logs are unavailable for independent recomputation.
The supported claim is scoped to this machine and these exact profiles.

See the [qualified Qwen proof](details/2026-08-20-qwen38-qualified-profiles/README.md)
and the [M5 machine page](machines/apple-m5-32gb.md).
