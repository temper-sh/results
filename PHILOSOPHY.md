# The speed of finished work

Imagine two local models sitting beside each other on the same desk.

The first begins answering immediately and writes twenty tokens every second.
The second pauses, then writes only ten. If the scoreboard stops there, the
first model wins by a distance. It looks like the obvious recommendation.

Now give the faster one a real job.

During this project's field work, the owner used a fast local profile to
investigate a bug in a commercial codebase. Early turns felt responsive: files
were read, hypotheses arrived quickly, and the investigation appeared to be
moving. As the work deepened across the repository, the profile spent more of
that speed reacquiring context, revisiting ground, and recovering the thread.
Repeated attempts never reached a verified fix.

This was a field observation, not a controlled comparison, so it does not
prove that every slower profile would have solved the bug. It establishes the
important part without overclaiming: the raw speed was real, and the completed-
task throughput was still zero. There was no successful task time to put in the
other column.

That difference is the reason for this project. Temper does not try to find the
largest model that will launch or the most exciting number a benchmark can
print. It tries to find local systems that complete useful work reliably on
hardware a person can actually own.

## Local does not have to mean frontier

A consumer machine is not going to reproduce the strongest frontier service
for every task. That is the wrong promise and, increasingly, the wrong
comparison.

Everyday work contains a wide range of difficulty. Some jobs genuinely benefit
from frontier reasoning, enormous scale, or a hosted research system. Others
need a dependable editor, a private document reader, a visual second opinion,
or a small utility that follows a narrow procedure well. Not everyone needs
frontier capability for every turn, and no one benefits from paying frontier
costs for work a local profile can complete correctly.

Local execution also buys something a capability leaderboard does not measure.
It can keep the entire job offline. It does not depend on a provider's uptime,
quota, policy, or decision to change a model's behavior while retaining its
name and price. The exact artifact can be pinned, hashed, and run again. That
does not make it permanently correct, but it makes the system inspectable and
the change boundary yours.

The useful strategy is therefore a portfolio, not a declaration that local has
defeated the frontier. Use a frontier model when the task earns it. Use a
quality-first local model when privacy, independence, or a stable long-running
workspace matters. Offload simpler utility work when a smaller local profile
can do it without creating cleanup. The right model is the least expensive and
most independent one that can finish the particular job to the required
standard.

## Start the clock when the job starts

Tokens per second measures one visible part of one turn. A person experiences
a longer clock:

> load + read + think + act + verify + correct + recover

Decode speed matters. So do prompt processing, cache reuse, tool latency,
context growth, memory pressure, and the number of attempts needed before the
answer is safe to use. A profile that writes quickly but needs supervision and
repair is borrowing time from the person operating it.

This is why first-attempt quality sits above component speed in the decision
order. A wrong answer is not merely a low score. In real work it can create a
second investigation, contaminate later context, or look convincing enough to
survive until the cost of correcting it is much higher. Quietly wrong work is
often worse than an explicit refusal or crash because it moves the burden of
detection to the user.

The same principle applies even when two profiles produce equally good short
answers. Momentary speed can become long-run slowness. A small context window
may feel quick until it repeatedly compacts away facts the task still needs. A
lazy memory strategy may look efficient at startup and then grow until the
desktop swaps or the model dies deep into the session. A speculative decoder
may accelerate clean prose but add overhead on tool-heavy or unpredictable
output. A fast helper placed beside the main model may steal the memory margin
that kept the larger job alive.

The honest unit is not a token and not even a response. It is a completed task
over the length and conditions in which that task will actually be performed.

## A listening socket is not a working system

Local AI is unusually good at producing convincing partial victories. A server
starts with a huge context flag, so the window appears supported. A model emits
one valid tool call, so the integration appears finished. A quantized file is
smaller, so it appears strictly better for the machine. An acceleration method
has sound mathematics and an impressive average, so it appears certain to
help.

Each statement can be technically true and operationally misleading.

We learned this at the seams between real components. Profiles reached
“ready” while streamed tool calls arrived as ordinary text or a request stayed
open without delivering the tokens it had generated. A chat template changed
the serialized bytes of earlier history and defeated prefix reuse on every
turn. A package manager installed a dependency combination that passed a tiny
smoke test but made long-prompt processing roughly three times slower. Other
acceleration paths started successfully, then regressed complete-task time or
failed when the draft was rejected. Harness and model combinations sometimes
proved incompatible before the model received a request at all.

Some of those findings travelled back upstream. The unbounded Rapid-MLX
tool-streaming hang was [reported as issue
#1359](https://github.com/raullenchai/Rapid-MLX/issues/1359) and fixed by
[pull request #1391](https://github.com/raullenchai/Rapid-MLX/pull/1391). The
Qwen non-thinking template defect that broke prefix invariance became
[Froggeric discussion
#80](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates/discussions/80),
where the one-line repair was accepted upstream. Other problems remained local
patches, rejected profiles, documented dependency conflicts, or open retest
gates. A server being alive never told us which category we were looking at.

The current 100k–128k profiles illustrate how many layers stand behind one
apparently simple context number. The architecture makes those windows
plausible; the matching engine, cache, template, artifact, client policy, and
full-window testing make them usable. No single benchmark trick establishes
the result.

The reverse lesson matters too. A larger window that allocates and answers a
greeting has not passed. It must perform real compute near capacity, replay the
prefix, branch from changed history, survive its ordinary co-residents, and
leave the desktop usable. In these results, some larger configurations started
successfully and still failed under the conditions that mattered. “It boots”
was an observation, not a recommendation.

## Plausible claims are hypotheses

Most setup mistakes do not begin with foolish ideas. They begin with claims
that are solid, reasonable, and incomplete.

A model card may accurately state the architecture's maximum context without
showing that a particular quantization, runtime, and laptop can sustain it. An
engine flag may do what its documentation says while interacting badly with
checkpoint storage or a client cache. A model repository may contain both an
embedded acceleration head and a separate sidecar, making the apparently
careful act of loading both waste memory. A template may look like formatting
glue while quietly deciding whether history, reasoning, and tools remain
correct. A community result may be genuine on its author's machine and still
depend on a different batch shape, background load, or definition of success.

The response is not cynicism. It is to turn every important claim into a test:

- identify the exact artifact, revision, template, runtime, and machine;
- separate what documentation claims from what the run observes;
- test the failure boundary, not only the happy-path greeting;
- exercise actual tools and inspect their effects, not just their syntax;
- measure growing and changed history, not only isolated prompts;
- keep failures and negative arms long enough to explain the decision;
- repeat quality checks after any change to a load-bearing part of the profile.

Tool use deserves special suspicion because a believable transcript can hide a
broken action. A model can name the right tool with the wrong arguments. A
parser can accept malformed output. A harness can report a call that never
changed the intended file. Verification must reach the world outside the
model's prose: inspect the diff, read the returned data, run the check, and
confirm that the requested state actually exists.

One editing tool was an almost perfect paper tiger. Instead of asking the model
to repeat the old text around a change, it let the model identify lines with
short hashes and send a compact replacement. The design made complete sense:
fewer generated tokens, precise anchors, and less ambiguous matching should
have meant faster, safer edits.

In practice, the hash solved only where to edit. The model still had to
reconstruct the fragile seam around the replacement—indentation, blank lines,
and the exact bytes joining old code to new. Calls could be valid and accepted
while the resulting file was wrong. The compact request saved work in the part
that was easy to count, then returned the cost as inspection, retries, and
correction. For this local workflow it was not a faster editing tool; it was a
faster way to submit an edit that still needed policing.

Fact-checking also applies to our own explanation. A measured correlation is
not automatically a mechanism. A single success is not a reliability claim.
An estimate is not a result. When the evidence cannot distinguish those
categories, the honest label is `LAB`, `WATCH`, or `UNMEASURED`, followed by a
clear test that could change it.

## Evidence is how the setup becomes dependable

Evidence-based setup can look slower than copying the most popular command and
starting work. At the beginning, it is slower. It requires frozen artifacts,
matched comparisons, realistic prompts, memory observation, failure records,
and reruns after changes.

The repayment arrives later. When a long task reaches 80k of history, the
context window is no longer a hope. When a model calls a tool, the integration
has known behavior and visible failure modes. When an attractive new runtime
appears, it can be compared against a preserved baseline instead of against a
memory of how the old setup felt. When something regresses, the profile has an
identity precise enough to investigate.

That is also why these results recommend complete profiles rather than model
names. The weights do not work alone. Quantization, template, engine, cache,
context policy, helpers, harness, hardware, and the rest of the running machine
all participate in the outcome. Change a load-bearing part and the old evidence
becomes a lead, not a guarantee.

The aim is not to eliminate judgment. Real work will always be broader than a
test suite. The aim is to make judgment answerable to reality: declare what the
system is for, measure the places it can fail, preserve enough evidence to
audit the conclusion, and reopen the decision when new evidence arrives.

Raw speed is useful. Finished-work speed is what gives the machine a job.

For operational advice, continue with [the guide](GUIDE.md). For the labels,
profile identity, and publication boundary behind the evidence, see
[the method](METHOD.md).
