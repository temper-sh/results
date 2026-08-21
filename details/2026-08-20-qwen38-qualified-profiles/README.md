# Qualified Qwen3.8 layouts

Disposition: **SUPPORTED** as two layouts on the Apple M5 / 32 GiB witness.

## TL;DR

Keep plain Q4_K_M at 131,072 tokens for speed/context and Dynamic 3.0 XL at
102,400 for quality-first work. Both passed 11/12 short and 4/4 practical
tasks. Plain decoded 18.6% faster than Dynamic—equivalently, Dynamic was 15.7%
slower than plain—while retaining 28,672 more qualified context tokens.
Dynamic improved paired perplexity by 0.65%. Rapid-MLX passed only 1/4 practical
tasks and remains parked.

## Profile identity

| Field | Shared value |
|---|---|
| Machine | Apple M5 / 32 GiB unified memory |
| Engine | llama.cpp b10470 / `34af94cd9` |
| Runtime | one slot; Q8 K/V; flash attention; batch/microbatch 512 |
| Context controls | 16 checkpoints; prompt-cache RAM disabled |
| Speculation | MTP embedded in each target; no duplicate draft sidecar |
| Template | patched Sharp v22.1, SHA-256 `69da7ac41de69defd62c98aa553b4b0eadda9c4ed5698770c957521c9c7e055b` |
| Mode | text-only, non-thinking, projector disabled |

The artifact is the intended difference. Plain Q4_K_M is revision
`f1bfb127c64f7072bdd2cad55f258b9c8b2910fe`, SHA-256 `7e78da5d…`.
Dynamic 3.0 XL is revision
`4ca720788d1e01f1bff70c033e0d0028fd02e502`, SHA-256 `3f227079…`.

## Quality and useful work

| Gate | Plain Q4_K_M | Dynamic 3.0 XL |
|---|---:|---:|
| Short suite | 11/12 | 11/12 |
| Practical repository tasks | 4/4 | 4/4 |
| Paired perplexity | 6.2871 | **6.2460** (-0.65%) |
| Controlled decode | **11.496 tok/s** | 9.694 tok/s (15.7% slower) |
| Practical wall | 669.487 s | 719.768 s |
| Tool calls | 27 | 21 |

The practical runs sampled different tool paths, so the wall-time difference
is a whole-profile observation rather than a clean artifact-speed measurement.
Dynamic gave fuller useful answers in two tasks but added a touching-range
error inside the short case both layouts missed. The quality result is small
and mixed, which is why both layouts remain recommended.

The reviewed packet stores `candidate_delta_percent: -18.6`, which uses the
reverse comparison (plain divided by Dynamic). Results publishes both bases
explicitly: plain is 18.6% faster relative to Dynamic; Dynamic is 15.7% slower
relative to plain.

## Context and safety

Qwen3.8 has 64 text layers, but 48 are recurrent and only 16 hold ordinary
attention KV. With Q8 KV, moving from a 24,576 to 131,072 window adds about
3.45 GiB rather than the cost expected from 64 full-attention layers.

| Gate | Plain 131,072 | Dynamic 102,400 |
|---|---:|---:|
| Long prompt | 120,190 tokens | 100,170 tokens |
| Exact replay | 120,186 cached in 1.516 s | 100,166 cached in 2.816 s |
| Peak observed RSS | 23.20 GiB | 22.358 GiB |
| Swap growth | 0 | 0 |
| Desktop event | none at selected window | none |

The laptop slept during the plain cold fill, so its cold wall time and
aggregate prefill rate are excluded. Dynamic's valid cold fill took 2,517.153
seconds at 39.84 prompt tok/s.

Plain Q8 answered tiny probes at 163,840 and 180,224 with too little desktop
margin. At 196,608, inference and WindowServer hit Metal OOM. Q4 KV answered at
262,144 but was not filled or quality-qualified. The supported values are the
largest operational candidates, not the largest listening servers.

## Why Rapid-MLX stays parked

Rapid-MLX 0.12.15 fixed-K1 safely served 32,768 tokens and produced 5/5
byte-identical deterministic outputs at 10.597 tok/s. Pi's sampled requests did
not engage that MTP path, however, and the practical gate passed only 1/4.
Auto-K3 returned three substantive hashes across five identical seeded greedy
requests. Synthetic capacity and component speed did not earn a third layout.

## Evidence boundary

These are reviewed Labs migration packets reconstructed after the source runs,
not preregistered experiments. The source summaries and commands are hashed,
but private prompts, outputs, and raw scored logs are unavailable here. The
plain sleep exclusion and Dynamic counterevidence are retained above.

Byte-identical reviewed packets:

- [`context-evidence.json`](context-evidence.json), SHA-256 `203b9c48…`;
- [`dynamic-evidence.json`](dynamic-evidence.json), SHA-256 `bdbf830f…`;
- [`engine-evidence.json`](engine-evidence.json), SHA-256 `ec161659…`.

The Labs source working tree was based on revision `ec22c368…`; the migrated
source runs themselves record local-ai-setup base revision `da9b070d…` and
their exact summary hashes.

## Reopen

Recheck after an artifact, engine, or template revision; a contradictory public
role corpus; another machine witness; a safe higher-precision layout; or a
maintained MLX sampled-client MTP path that passes the same 4/4 practical gate.
