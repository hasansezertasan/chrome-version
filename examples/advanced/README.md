# Advanced example

Use `chrome_version` as a preflight gate: exit non-zero when Chrome is missing
or older than a required major version. Useful before launching browser-based
tooling in CI or automation.

## Run

```sh
uv run --locked python examples/advanced/main.py
echo "exit code: $?"
```

## Expected output

```text
Chrome 123.0.6312.86 satisfies the minimum major 120.
exit code: 0
```

When Chrome is missing or too old, it writes an explanation to `stderr` and
exits with code `1`.
