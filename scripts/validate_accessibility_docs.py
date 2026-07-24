from __future__ import annotations

import json
import math
import os
import re
from pathlib import Path
from typing import Any

STATUS = "ACCESSIBILITY_REVIEW_PROTOCOL_DOCUMENTED_SITE_NOT_CERTIFIED"
EXPECTED_STATES = {
    "NOT_REVIEWED",
    "AUTOMATED_CHECKS_ONLY",
    "MANUAL_REVIEW_INCOMPLETE",
    "REVIEWED_WITH_OPEN_FINDINGS",
    "REVIEWED_NO_KNOWN_BLOCKERS",
    "SUPERSEDED",
    "WITHDRAWN",
    "UNKNOWN",
}


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON value: {value}")


def assert_finite(value: Any, location: str = "$") -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"non-finite number at {location}")
    if isinstance(value, dict):
        for key, child in value.items():
            assert_finite(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            assert_finite(child, f"{location}[{index}]")


def heading_levels(text: str) -> list[int]:
    levels: list[int] = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            match = re.match(r"^(#{1,6})\s+\S", line)
            if match:
                levels.append(len(match.group(1)))
    return levels


def validate() -> list[str]:
    required = [
        Path("README.md"),
        Path("mkdocs.yml"),
        Path("taskchain.md"),
        Path("punchlist.md"),
        Path("release.md"),
        Path("changelog.md"),
        Path("docs/index.md"),
        Path("docs/accessibility-review-evidence.md"),
        Path("docs/accessibility-review-profile-v1.json"),
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise SystemExit(f"missing accessibility documentation: {missing}")

    profile = json.loads(
        Path("docs/accessibility-review-profile-v1.json").read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_constant,
    )
    assert_finite(profile)

    if profile.get("schema_version") != "qsio.documentation-accessibility-review.v1":
        raise SystemExit("unexpected accessibility profile schema version")
    if profile.get("status") != STATUS:
        raise SystemExit("accessibility profile does not preserve non-certification status")
    if profile.get("safe_default") != "NOT_REVIEWED":
        raise SystemExit("accessibility safe default must remain NOT_REVIEWED")
    if set(profile.get("review_states", [])) != EXPECTED_STATES:
        raise SystemExit("accessibility review states are incomplete or changed")
    denials = profile.get("authority_denials", {})
    if not denials or any(value is not False for value in denials.values()):
        raise SystemExit("every accessibility authority field must remain denied")
    gap = profile.get("fysa_120", {}).get("proposed_gap", {})
    if gap.get("id") != "019-R" or gap.get("authoritative") is not False:
        raise SystemExit("FYSA-120 accessibility refinement metadata is invalid")

    guide_path = Path("docs/accessibility-review-evidence.md")
    guide = guide_path.read_text(encoding="utf-8")
    markers = [
        STATUS,
        "The safe default is `NOT_REVIEWED` or `UNKNOWN`",
        "### Prose equivalent",
        "## Automated checks",
        "## Manual review matrix",
        "## Required review packet",
        "## Publication, withdrawal, and rollback boundary",
        "019-R — Exact-generation technical-site accessibility evidence",
    ]
    absent = [marker for marker in markers if marker not in guide]
    if absent:
        raise SystemExit(f"accessibility guide is missing markers: {absent}")

    nav = Path("mkdocs.yml").read_text(encoding="utf-8")
    if "accessibility-review-evidence.md" not in nav:
        raise SystemExit("MkDocs navigation omits accessibility review")

    controlled = [
        Path("README.md"),
        Path("taskchain.md"),
        Path("release.md"),
        Path("docs/index.md"),
        guide_path,
    ]
    for path in controlled:
        if STATUS not in path.read_text(encoding="utf-8"):
            raise SystemExit(f"{path} omits governing accessibility status")

    for path in [Path("docs/index.md"), guide_path]:
        levels = heading_levels(path.read_text(encoding="utf-8"))
        if not levels or levels[0] != 1:
            raise SystemExit(f"{path} must begin with a level-one heading")
        for previous, current in zip(levels, levels[1:]):
            if current > previous + 1:
                raise SystemExit(f"{path} skips heading levels: {previous} to {current}")

    lines = guide.splitlines()
    table_headers = sum(
        1
        for first, second in zip(lines, lines[1:])
        if first.lstrip().startswith("|")
        and second.lstrip().startswith("|")
        and not second.replace("|", "").replace(":", "").replace("-", "").strip()
    )
    if table_headers < 2:
        raise SystemExit("review-state and severity tables require headers")

    if guide.count("```mermaid") != guide.count("### Prose equivalent"):
        raise SystemExit("every Mermaid diagram requires one prose equivalent")

    weak_pattern = re.compile(r"\[(here|click here|link|more)\]\(", re.IGNORECASE)
    weak = [
        str(path)
        for path in [Path("README.md"), *sorted(Path("docs").rglob("*.md"))]
        if weak_pattern.search(path.read_text(encoding="utf-8"))
    ]
    if weak:
        raise SystemExit(f"weak standalone link text found: {weak}")

    return [
        "required_files=pass",
        "strict_json=pass",
        "profile_invariants=pass",
        "heading_order=pass",
        "table_headers=pass",
        "diagram_prose_equivalence=pass",
        "meaningful_link_text=pass",
        "manual_review_completed=false",
        "certification=false",
        "publication_authority=false",
    ]


if __name__ == "__main__":
    results = validate()
    output = Path(
        os.environ.get("ACCESSIBILITY_VALIDATION_OUTPUT", "accessibility-structural-validation.txt")
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(results) + "\n", encoding="utf-8")
    print("\n".join(results))
