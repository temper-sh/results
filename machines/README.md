# Find your machine

Results lists only machines that actually ran the complete profile. Capacity
estimates and model-card claims stay out of this table.

## Witnessed setups

| Machine | Memory | Supported work | Current choice | Decisive evidence |
|---|---:|---|---|---|
| [Apple M5 / Mac17,3](apple-m5-32gb.md) | 32 GiB unified | Local coding | Qwen3.8 plain Q4_K_M at 131,072 for speed/context, or Dynamic 3.0 XL at 102,400 for quality first | Both passed 11/12 short and 4/4 practical gates; near-capacity fill/replay passed with zero swap growth |

Muse Glimmer is also measured on this machine, but remains `LAB` until real
visual and deliberate work qualifies a role.

## If your machine is not listed

Use the closest page to understand the method, not to copy its verdict.

- Memory changes with artifact, context, projector, drafter, helpers, and
  ordinary application load.
- Speed changes across chips and engines.
- Quality and tool behavior change with model, quantization, template,
  reasoning, sampling, and harness.
- A larger RAM number makes a profile plausible, not supported.

The [guide](../GUIDE.md#what-changes-on-another-machine) explains what transfers
and what needs a new witness.
