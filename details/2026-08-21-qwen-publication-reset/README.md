# Qwen publication reset

Disposition: **correction** effective 2026-08-21.

## TL;DR

Results no longer treats the earlier context-constrained Qwen setup, Qwen3.6
branch, speculation, cache, sampling, or candidate-memory records as current
evidence. The 2026-08-20 work showed that context, template, artifact pinning,
cache, checkpoints, MTP packaging, and client settings had been materially
wrong for the question. Current guidance starts from the reviewed 100k/128k
profiles. CPU reranker placement is the explicit retained exception.

## What changed

The old publication mixed measurements from different model branches, engines,
templates, context limits, cache policies, auxiliary artifacts, and harness
postures. Those measurements were real observations, but their conclusions do
not answer the current setup question.

The corrected baseline now requires:

- an exact artifact and template pin;
- one slot with Q8 K/V;
- embedded MTP without a duplicate sidecar;
- bounded checkpoints and prompt-cache RAM disabled;
- text-only serving for coding;
- matching client window and compaction values;
- compute, near-capacity fill, replay, branch, swap, and desktop-safety gates;
- practical work and quality tests before promotion.

## Removed from the current proof path

The detailed 2026-07-31 through 2026-08-20 publication directories covering
shell compression, Qwen3.6 engine/sampling/support, earlier candidate
memory, OptiQ/DSpark, Qwen3.8 accelerators, the 24k bridge, old MTP sidecar, and
local edit formats were removed from the current tree. The rewritten public
branch no longer carries those files or commits; an archive checkout created
during the reset retains the previous tip and was deliberately not published.

This is not a claim that every local observation inside them was false. It is a
claim that their combined setup assumptions are no longer suitable for choosing
the current Qwen profile, and keeping them in the main proof index created more
confusion than useful caution.

## Retained exception

The CPU/on-demand versus GPU-co-resident reranker comparison tests a placement
mechanism that remains relevant and was explicitly preserved by Labs. It now
has a focused [reranker record](../2026-08-08-m5-reranker-placement/README.md)
without the retired main-model recommendation around it.

## Replacement

The reviewed replacement is the
[qualified Qwen record](../2026-08-20-qwen38-qualified-profiles/README.md):
plain Q4_K_M at 131,072 for speed/context and Dynamic 3.0 XL at 102,400 for
quality-first use. Future Qwen3.6 work begins with a fresh plan and inherits
the method, not the old verdicts.
