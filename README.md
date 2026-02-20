# Human-Like Creative Writer Assistant

This repository provides a lightweight assistant that generates robust prompts for writing:

- novels
- poetry
- dialogue
- lyrics
- movie scripts
- screenplay

The generated prompt is tuned for output that feels **real**, **authentic**, and grounded in **environmental detail**.

## Quick start

```bash
python writer_assistant.py novel "A doctor returns to her coastal hometown to uncover a family lie" \
  --tone "intimate, reflective" \
  --perspective "first person" \
  --environment "Monsoon-soaked fishing town, power cuts, salt-heavy air, crowded wharf" \
  --characters "Mira (doctor)" "Baba (estranged father)" "Ishaan (childhood friend)" \
  --constraints "900-1200 words" "show-dont-tell" "no deus ex machina"
```

## Why this works

The assistant prompt emphasizes:

1. sensory environment and lived-in setting
2. believable motivations and conflict
3. distinct voice per character
4. emotional truth over dramatic exaggeration

You can feed the generated prompt into your preferred LLM.
