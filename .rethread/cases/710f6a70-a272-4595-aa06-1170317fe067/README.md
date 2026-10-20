# Reproduce this Case

Use a disposable isolated environment. Install the hashed requirements.lock.
Run the reproduction command and unchanged pytest/Ruff suite listed in manifest.json.
The additive guard fails at the recorded base and passes on this repair.
Verification is scoped to these checks, not all possible behavior.
