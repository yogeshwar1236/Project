#!/usr/bin/env python3
"""Writer assistant prompt builder for human-like creative writing."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from typing import List

SUPPORTED_FORMATS = {
    "novel": "Long-form narrative with deep character arcs and scene transitions.",
    "poetry": "Evocative imagery, rhythm, and layered meaning.",
    "dialogue": "Conversation-first writing with voice distinction and subtext.",
    "lyrics": "Musical phrasing, emotional hooks, and memorable lines.",
    "movie-script": "Screen-ready scene/action/dialogue formatting with cinematic pacing.",
    "screenplay": "Industry-style visual storytelling with tight scene intent.",
}


@dataclass
class WritingRequest:
    form: str
    topic: str
    tone: str = "authentic, emotionally grounded"
    perspective: str = "third person"
    audience: str = "general adult"
    environment: str = ""
    characters: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)


class WriterAssistant:
    """Builds rich prompts for creative writing tasks."""

    def build_prompt(self, request: WritingRequest) -> str:
        form_key = request.form.lower().strip()
        if form_key not in SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported format '{request.form}'. Choose from: {', '.join(SUPPORTED_FORMATS)}"
            )

        characters = ", ".join(request.characters) if request.characters else "Not specified"
        constraints = (
            "\n".join(f"- {item}" for item in request.constraints)
            if request.constraints
            else "- Keep the language natural and believable."
        )
        environment = request.environment or "Ground scenes in sensory details tied to location, weather, and atmosphere."

        return f"""You are an elite creative writing assistant.

TASK
Write a {request.form} about: {request.topic}

STYLE PROFILE
- Creative form guidance: {SUPPORTED_FORMATS[form_key]}
- Tone: {request.tone}
- Perspective: {request.perspective}
- Audience: {request.audience}

WORLD & ENVIRONMENT
- Setting direction: {environment}
- Use concrete sensory details (sound, texture, smell, temperature, light).
- Make character choices reflect social and physical environment.

CHARACTERS
- Primary figures: {characters}
- Give each voice a distinct rhythm, vocabulary, and emotional logic.

AUTHENTICITY RULES
- Avoid clichés unless intentionally subverted.
- Prioritize emotionally truthful reactions over melodrama.
- Include subtle imperfections in speech/behavior to feel human.
- Let conflict emerge from values, fears, and desire.

CONSTRAINTS
{constraints}

DELIVERY
- Start with a compelling opening.
- Keep pacing appropriate for the chosen form.
- End with resonance (image, line, or emotional beat that lingers).
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a high-quality creative-writing prompt for any major writing form."
    )
    parser.add_argument("form", choices=list(SUPPORTED_FORMATS), help="Type of writing to generate")
    parser.add_argument("topic", help="Central idea, premise, or storyline")
    parser.add_argument("--tone", default="authentic, emotionally grounded")
    parser.add_argument("--perspective", default="third person")
    parser.add_argument("--audience", default="general adult")
    parser.add_argument("--environment", default="")
    parser.add_argument(
        "--characters",
        nargs="*",
        default=[],
        help="Character names or short role tags",
    )
    parser.add_argument(
        "--constraints",
        nargs="*",
        default=[],
        help="Extra constraints (e.g., word-count<300, no profanity)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    request = WritingRequest(
        form=args.form,
        topic=args.topic,
        tone=args.tone,
        perspective=args.perspective,
        audience=args.audience,
        environment=args.environment,
        characters=args.characters,
        constraints=args.constraints,
    )

    assistant = WriterAssistant()
    print(assistant.build_prompt(request))


if __name__ == "__main__":
    main()
