# Method

## Publication layers

Results separates explanation from proof without separating claims from their
evidence:

| Layer | Reader question | Contents |
|---|---|---|
| [Philosophy](PHILOSOPHY.md) | What are we optimizing for, and why? | The case for local work, completed-task speed, and evidence before recommendation |
| [Guide](GUIDE.md) | How should I think about a good local-AI system? | Durable concepts, everyday mechanics, and links to decisive proofs |
| [Current choices](CURRENT.md) | What can I responsibly use today? | Exact supported recipes and gaps |
| [Machines](machines/README.md) | Does that answer apply to my hardware? | One page per witnessed machine; no imaginary benchmark rows |
| [Other paths](CONSIDERED.md) | Why not this attractive alternative? | Rejections, incomplete candidates, estimates, and reopen conditions |
| [Proof library](details/README.md) | Show me the evidence. | Dated methods, measurements, limitations, profile identity, and provenance |

The philosophy explains the objective; the guide explains how to pursue it.
The guide is organized around what a person needs to understand, not around the
chronology of lab runs. A new machine normally adds a machine page and dated
proof. It changes the guide only when it changes a portable explanation or
reveals an important new boundary.

## Reader contract

Results is written first for the person choosing what to run, not for an AI
infrastructure specialist. Every dated proof should still work from top to
bottom:

1. **TL;DR:** what to do, the decisive reason, and where the advice applies.
2. **Why:** the mechanism in ordinary language, especially when a faster
   component made the complete job slower.
3. **Evidence:** enough numbers, failures and limitations to judge the claim.
4. **Technical identity and provenance:** exact reproducibility details for
   readers who need them.

Do not make a reader decode an acronym to learn the recommendation. Introduce
the ordinary-language meaning first, then the technical name where it helps:

| Term | Plain meaning |
|---|---|
| Prompt processing / prefill | Reading the existing instructions and conversation before writing the next answer. |
| Decode | Writing the new answer, one token at a time. |
| Draft acceptance | How often speculative decoding's guesses save work instead of adding overhead. |
| Peak memory | The highest measured model-engine allocation during the run—not model file size or total machine RAM. |
| Prefix cache | Reusing work from the unchanged beginning of a conversation instead of reading it all again. |

When a benchmark and an everyday task disagree, show the time or work ledger
that explains the disagreement. Clearly label observed correlation versus a
demonstrated cause. Keep the exact technical material, but place it after the
answer rather than making it the entrance fee.

## What a result describes

The unit of evidence is a **runtime profile**:

> machine + model revision + quantization + template + engine + flags +
> context/cache policy + sampling + placement + residency + tool/harness

Changing any load-bearing field creates a new row. A result for the same model
on another engine, with another template, or with a GPU reranker is not the
same result.

## Decision order

1. First-attempt task quality and quiet-wrong-answer risk.
2. Protocol correctness: roles, tool calls, streaming, and structured output.
3. Fit and stability under realistic co-residents and growing context.
4. User-perceived latency: prefill, warm turns, and decode separately.
5. Convenience and maintenance cost.

A faster arm cannot compensate for a quality, protocol, or stability failure.

## Evidence labels

| Label | Meaning |
|---|---|
| **SUPPORTED** | The exact profile passed its declared field gates on the named machine. |
| **LAB** | Measured and promising, but at least one promotion gate is still open. |
| **REJECTED** | A measured failure crossed a declared stop rule for that profile. |
| **JUDGMENT** | A decision from sustained use without a controlled scored comparison. |
| **WATCH** | Research, artifact inspection, or capacity arithmetic only; no qualifying run. |
| **UNMEASURED** | A design decision, explicitly not presented as benchmark evidence. |

## Publication boundary

This repository keeps conclusions, machine tables, exact summary rows,
artifact revisions, source hashes, limitations, and failed arms. Labs keeps
the harnesses and potentially sensitive raw transcripts: source code, absolute
paths, prompts, and captured model output do not become public merely because
they were measured.

A detailed record should contain enough information to audit the conclusion
and locate the source snapshot. Promotion requires a sanitized, immutable
evidence artifact; raw logs can remain access-controlled.

## Minimum record

Every new result records:

- date and disposition;
- exact machine and memory limits;
- artifact and template revisions;
- engine and dependency versions where available;
- full profile identity or hash;
- corpus, repetitions, metrics, stop rules, and every failed run;
- what was measured, what was inferred, and what remains unknown.

Run `python3 tests/check.py` before publishing. It validates JSON, local links,
required entry points, and publication-safe paths.

Labs keeps the reusable review workflow in `prompts/update-data.md`. It audits
profile identity, source hashes, calculations, sanitization, conflicts,
corrections and every affected Results surface before invoking this validator.
