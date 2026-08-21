# Other paths: measured, rejected, or still open

## TL;DR

The current M5/32 GiB recommendation is the two-layout Qwen3.8 llama.cpp set in
[Current choices](CURRENT.md). Muse is a genuine `LAB` alternative for visual
and deliberate work. Rapid-MLX is parked, not recommended. Older Qwen setup
conclusions were invalidated after a full context/template/cache requalification and
do not remain as competing current rows.

## Measured choices

| Candidate | Status | What the evidence says | Next gate |
|---|---|---|---|
| Muse Glimmer UD-Q4_K_XL + Q4 projector, llama.cpp, 102,400 | **LAB**, installed | Text protocol, typed tool recovery, 96,165-token synthesis, 4/4 synthetic visual facts, Pi routing, and 17.405 GiB peak observed RSS passed. Synthetic role direction was promising, not qualifying. | Real screenshot/document decisions, multi-source research, tool recovery, and retained 20k+ synthesis with frozen semantic rubrics. |
| Muse Q4 DFlash on b10470/M5 | **REJECTED for this profile** | `n_max=15` was 19.67% slower and `n_max=5` was 16.90% slower than target-only across three frozen tasks; neither arm matched all target hashes. | A materially newer runtime or drafter, tested against target-only completed work. |
| Rapid-MLX 0.12.15 Qwen3.8 fixed-K1 at 32,768 | **PARKED** | Deterministic MTP reached 10.597 tok/s, but Pi's sampled posture did not engage it and only 1/4 practical tasks passed versus Dynamic XL's 4/4. Auto-K3 produced three hashes in five identical seeded requests. | Maintained lossless MTP under the actual sampled client plus the same 4/4 practical gate. |
| Qwen Q4 KV at 262,144 | **UNQUALIFIED** | The server answered a small probe, but the window was not filled and Q4 KV quality was not evaluated; desktop margin was already unsafe. | Controlled Q4-versus-Q8 quality plus full fill/replay/branch and desktop-safety qualification. |
| 0.6B reranker on GPU beside a large main model | **REJECTED placement on this M5/32 profile** | 3 aborts in 66 turns versus 0/65 with CPU/on-demand placement. | A lower-memory main profile or a new overlap witness with safe headroom. |

## Watch and deferred work

| Candidate | Status | Why it stays here |
|---|---|---|
| Muse MLX profile | **WATCH** | Different weights, template packaging, memory behavior, and engine; it cannot inherit the GGUF result. Parked until the retained Muse roles justify another whole-profile comparison. |
| Muse DSpark | **WATCH** | Requires conversion and a new fit/useful-work qualification. It is not a remedy for the rejected Q4 DFlash by assumption. |
| Ornith 1.5 35B-A3B | **WATCH** | Added to the Labs portfolio queue after Muse; no local artifact or role witness yet. |
| Qwen3.6 retest | **PLANNED FRESH** | Earlier branch conclusions are not inherited. A new run must use current artifact pinning, template, KV, context, MTP, cache, safety, and practical-work knowledge. |
| Higher-precision Qwen or Muse | **WATCH on larger memory** | File arithmetic can justify a probe, not quality or safe co-residency. |
| Router/classifier model | **DEFERRED** | Direct profile choice is simpler until real usage shows routing errors worth another model and failure surface. |

## Historical reset

Results previously carried a long chain of early Qwen engine, sampling,
speculation, cache, and candidate-memory conclusions. They were measured, but
their setup posture was materially wrong for the question now being answered.
They have been removed from current guidance and public history, then replaced
with a compact
[reset record](details/2026-08-21-qwen-publication-reset/README.md). The CPU
reranker placement is the explicit surviving exception.

Statuses and publication boundaries are defined in [Method](METHOD.md).
