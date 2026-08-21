# CPU reranker placement on the M5 / 32 GiB

Disposition: **retained placement witness**.

## TL;DR

Keep the Qwen3 Reranker 0.6B Q8_0 on CPU and load it only when needed. In the
retained machine witness, CPU placement completed 65 growing turns to 19,292
prompt tokens with no aborts or failed reranks. GPU co-residency produced 3
aborted turns in 66. This is the explicit surviving result from the
earlier Qwen profile era.

## Result

| Placement | Turns | Largest prompt | Aborts | Failed reranks | Disposition |
|---|---:|---:|---:|---:|---|
| CPU, on demand (`-ngl 0`) | 65 | 19,292 | 0 | 0 | retain |
| GPU beside the large main model | 66 | 19,313 | 3 | 0 recorded extraction failures | reject on this machine/profile shape |

The reranker is not intrinsically better on CPU. The placement protected the
larger model's unified-memory margin, trading occasional helper latency for
fewer lost main-model turns.

## Evidence boundary

The CPU witness used an older Qwen3.6/Rapid-MLX main profile. It establishes the
placement mechanism on this 32 GiB machine, not current-Qwen co-residency under
load. Repeating the overlap with the current 100k/128k profiles remains useful.

Source field-kit records:

- GPU-co-resident report SHA-256
  `280537d784df2333276f97783af7e777e2ddf68772e6ccc710f15404d7e9d46d`;
- CPU/on-demand report SHA-256
  `d862abc17d1f4c7ae968d03a8e8f2a3ee1abb4402b2ab54b95176174ecb79328`;
- machine report SHA-256
  `ece80e4e2a9f91e0e65e2dceb048a7bdeef72c8bd1276d2515c5e2b90c198672`;
- CPU fit rows SHA-256
  `5b3fb4ce8dbec484a90c08ab82fd1e7846ab9d5a6306968f1f08660472712a36`.

Labs preserves this result as the indexed-only `m5-helper-placement` exception.

## Reopen

Reconsider GPU placement only after a changed main profile or memory class
passes a growing-context overlap run without reducing quality or desktop
margin.
