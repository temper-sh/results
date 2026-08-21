# A quality-first guide to local AI

A laptop will not become a data center because we found a clever flag. It can
become something more useful: a well-run workshop, with one capable worker at
the bench and specialist tools brought out only when the job needs them.

Good local AI is not the biggest model that opens a chat window. It is a
profile that completes the intended work on the machine you own, with enough
memory for the conversation, correct tool behavior, and a failure mode you can
see and recover from. Efficiency is allowed to remove waste, not correctness.

The exact measured profiles are in [Current choices](CURRENT.md). This guide
keeps only the lessons that should survive the next model release.

## 1. Choose a portfolio, not one universal winner

Research, visual documents, planning, coding, and quick helper work do not need
the same model posture. A useful portfolio may contain several recommended
profiles with different strengths.

| Work | What matters most | Current evidence |
|---|---|---|
| Coding | correct edits, tools, verification, retained context | two supported Qwen3.8 layouts on the measured M5 |
| Deliberate research and planning | evidence, uncertainty, sound decisions, safe tools | Muse Glimmer is `LAB`; retained work pending |
| Visual documents | exact extraction followed by a useful decision | Muse's synthetic and live vision path passed; real documents pending |
| Small helper work | low overhead and reliable narrow behavior | CPU reranking has a placement witness; other helpers remain task-specific |

One profile does not need to replace another globally. Compare models only on
work they both claim to serve.

The setup and the active mode have different jobs. Setup records what the owner
has chosen to install and permit. A mode selects the approved models and tools
needed for one kind of work; it may narrow that set but never silently widen
it. The same local machine can lead a private job, handle utility work, or
provide a carefully chosen helper to a frontier harness without pretending
those are the same workload.

## 2. The complete profile is the unit

A model request passes through several coupled layers:

| Layer | Why it matters |
|---|---|
| Exact weights and quantization | determine ability, size, and which tensors retain precision |
| Template and reasoning policy | serialize roles, history, tools, and thinking |
| Engine and flags | allocate weights, KV cache, checkpoints, and temporary work |
| Harness and parser | turn output into visible answers and valid tool calls |
| Placement and co-residents | decide whether the profile survives real machine pressure |

Changing a template, context, KV precision, drafter, projector, engine, or tool
parser creates a new profile. Results from the old one do not transfer merely
because the model name stayed the same.

Pin artifacts by revision and hash. A moving repository reference can change
weights or add a projector at restart without any local manifest change.

## 3. Memory must include the whole turn

On unified-memory Macs, model weights, conversation state, temporary buffers,
helpers, applications, and the desktop share one pool. “The model loaded” is
only a startup observation.

A model file fitting in memory is like a sofa fitting through the front door:
it does not prove there is room to live around it. The live budget includes
weights, growing history, temporary compute, helpers, the operating system, and
the applications that make the computer useful.

A safe fit test includes:

- real compute after load;
- a near-capacity prompt, not a tiny greeting;
- exact replay and a changed-history branch;
- swap and process-memory monitoring;
- ordinary desktop survival;
- the helpers that will actually overlap.

Large primary models should swap on a 32 GiB machine rather than co-reside.
Switching costs a cold load and discards the departing prompt cache, but it
keeps the memory boundary explicit.

The retained reranker result illustrates the same rule at smaller scale. A
0.6B reranker on CPU and on demand completed 65 growing turns with no aborts;
placing it on GPU beside the main model produced 3 aborts in 66 turns. CPU was
selected to protect the larger task, not because CPU is universally best for
reranking.

## 4. How 100k–128k works on this machine

Qwen3.8's architecture made a much larger window possible: 48 of its 64 text
layers are recurrent, so only 16 layers carry ordinary attention KV. Q8 KV
therefore grows far more slowly than it would in a conventional 64-attention-
layer transformer. The architecture supplied the opportunity; the following
controls stopped the runtime from wasting it:

| Control | Practical effect |
|---|---|
| llama.cpp GGUF with up-front allocation | makes the selected window inspectable before deep work |
| Q8 key and value cache | keeps the qualified quality/capacity point |
| one sequence | gives the one agent the whole advertised window |
| text-only target | avoids loading a projector into the coding profile |
| embedded MTP, no duplicate sidecar | speeds writing without duplicating tensors already in the target |
| 16 checkpoints, prompt-cache RAM off | bounds checkpoint storage and removes an extra lazy cache budget |
| fixed batch shape and flash attention | preserves the qualified working-buffer profile |
| prefix-stable patched template | lets long history reuse its unchanged prefix |
| matching client window and compaction | prevents the client from compacting at the obsolete threshold |

The plain layout completed 120,190 prompt tokens inside a 131,072-token window.
Dynamic XL completed 100,170 inside 102,400. Both replayed almost the entire
prompt from cache, branched correctly, and added no swap.

Larger settings were not promoted merely because they started. At 196,608 Q8,
inference and WindowServer hit Metal out-of-memory. Q4 KV started at 262,144
but was neither filled nor quality-tested. An operational context claim needs
fill, replay, branch, quality, and desktop evidence.

See the [qualified Qwen proof](details/2026-08-20-qwen38-qualified-profiles/README.md).

## 5. Quantization trades quality, speed, and room

Quantization labels are summaries, not guarantees. A sensitivity-aware layout
may keep important tensors at higher precision and become larger or slower than
a uniform quant with the same “4-bit” family label.

The current Qwen choice is deliberately two-dimensional:

| Layout | Evidence-backed advantage | Cost |
|---|---|---|
| Plain Q4_K_M | 18.6% faster matched decode; 28,672 more qualified context tokens | slightly worse paired perplexity and less complete answers in two tasks |
| Dynamic 3.0 XL | 0.65% lower paired perplexity; current quality-first choice | slower decode and a 102,400 rather than 131,072 window |

Both scored 11/12 short tasks and 4/4 practical tasks. That is enough to offer
a preference-sensitive choice, not enough to claim Dynamic is universally
better.

## 6. Acceleration must improve completed work

“Fast” can describe different chapters of the same turn:

| Chapter | What the user is waiting for |
|---|---|
| Cold load | the model and its runtime becoming ready |
| Prompt processing | instructions, files, and conversation being read |
| Decode | the answer or tool call being written |
| Completion | tools, verification, retries, and recovery producing usable work |

Improving one chapter is valuable only in proportion to how much of the real
job it occupies. Agent turns often read a long history and write a short tool
call, while a drafting task may have the opposite shape.

Speculative decoding lets a drafter guess several next tokens for the target to
verify. It can accelerate writing without changing the target distribution
when implemented losslessly. It does not shorten the existing prompt, choose
better tools, or rescue a weak target.

Qwen's recommended GGUF files already contain their MTP tensors, so a separate
draft GGUF would duplicate them. Muse's current Q4 DFlash made the three frozen
tasks 17–20% slower than target-only on this runtime. It remains out of the live
profile.

Measure cold load, reading the prompt, writing the answer, tool time, retries,
and complete-task wall time separately. A faster pen is valuable only when
writing is the bottleneck and the drafter fits safely.

Prefix caching deserves the same discipline. It can skip work from the
unchanged beginning of a conversation, but it cannot reuse a prefix that the
template, tool history, or request shape has changed. Count the work actually
avoided in normal turns, not just the tokens that disappear in an ideal replay.

## 7. Reasoning is a profile choice

Thinking can be a feature for deliberate research and planning, but it costs
time and output budget. Muse's medium-reasoning sampler completed all 12 cases
in less time than high reasoning took for six; high also produced prolonged
overthinking. Medium is therefore the current evaluation posture, while high
is reserved for a task that justifies an escalation.

Persistent reasoning also means a tiny output limit can expire before a
visible answer. The live Muse route demonstrated this at 64 tokens and passed
normally at 256. Client budgets belong to the profile just as context does.

## 8. Tools need consent and evidence

Every tool adds instructions to the conversation before it runs and may expose
data or mutate state when it does. A large menu can consume attention even when
most tools are never called. Install and enable tools individually. A mode may
narrow an approved tool set; it should never silently widen it.

Prefer tools that own mechanical invariants and fail visibly. Exact matching,
schema validation, permissions, and rollback should not depend on the model
remembering a comma or reconstructing whitespace. A rejected, typed error is
safer than a plausible success message attached to the wrong external state.

Test the real path:

1. render roles and history correctly;
2. stream complete tool names, IDs, and arguments;
3. continue after success and typed failure;
4. verify the external result, not only the model's claim;
5. retain enough evidence to detect a quiet wrong action.

For model evaluation, first-attempt completion and quiet-wrong risk come before
protocol, fit, task wall time, and component speed—in that order.

## 9. A practical build order

1. Name the work and its data boundary.
2. Pick a complete candidate profile, not just weights.
3. Set an operating-system and desktop memory reserve.
4. Qualify context with fill, replay, branch, swap, and desktop checks.
5. Exercise the actual harness, tools, and reasoning posture.
6. Score retained work before tuning speed.
7. Add helpers only after testing their placement and overlap.
8. Keep rollback and profile switching explicit.

## What changes on another machine

The method transfers; the numbers do not. A different chip, memory bucket,
engine, artifact, projector, helper set, or ordinary application load needs a
new witness. More memory makes a profile plausible, not qualified.

Use [Machines](machines/README.md) for witnessed hardware and
[Other paths](CONSIDERED.md) for candidates whose next gate is still open.
