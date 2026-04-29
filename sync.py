#!/usr/bin/env python3
"""
sync.py — Generates the CLASSES JavaScript array from module markdown files.

Makes the module .md files the single source of truth. Run this after
adding or editing modules, and it outputs the JavaScript to paste into
index.html's CLASSES array (or writes it directly with --write).

Usage:
    python3 sync.py              # Print CLASSES JS to stdout
    python3 sync.py --write      # Write directly into index.html
    python3 sync.py --check      # Check for drift between .md and index.html
"""

import os
import sys
import re
import json
import yaml
import glob
from datetime import datetime

# ─── Configuration ────────────────────────────────────────────────

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
SOURCES_YAML = os.path.join(WORKSPACE, "sources.yaml")
MODULES_DIR = os.path.join(WORKSPACE, "modules")
INDEX_HTML = os.path.join(WORKSPACE, "index.html")

# Fallback program definitions if sources.yaml doesn't exist
DEFAULT_PROGRAMS = [{
    "id": "bootcamp",
    "name": "Fundamentals Bootcamp",
    "description": "12 topic-based modules for new-hire onboarding",
    "module_dir": "modules/bootcamp/",
    "module_prefix": "M",
    "active": True,
}]

# ─── Markdown Parsing ─────────────────────────────────────────────

def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return None, content

    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        print(f"  WARNING: Bad YAML in {filepath}: {e}", file=sys.stderr)
        return None, content

    body = match.group(2)
    return meta, body


def extract_section(body, heading):
    """Extract content under a ## heading from markdown body."""
    pattern = rf'^## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, body, re.MULTILINE | re.DOTALL)
    if not match:
        return None
    return match.group(1).strip()


def extract_subsections(section_text):
    """Extract ### subsection titles from a section."""
    return re.findall(r'^### (.+)$', section_text, re.MULTILINE)


def extract_bullets(section_text):
    """Extract bullet points from a section, cleaning markdown."""
    bullets = []
    for line in section_text.split("\n"):
        line = line.strip()
        if line.startswith("- ") or line.startswith("* "):
            bullet = line[2:].strip()
            # Clean markdown formatting
            bullet = re.sub(r'\*\*(.+?)\*\*', r'\1', bullet)
            bullet = re.sub(r'\*(.+?)\*', r'\1', bullet)
            bullet = re.sub(r'`(.+?)`', r'\1', bullet)
            bullets.append(bullet)
    return bullets


def first_paragraph(text):
    """Get the first paragraph (up to first double newline or 300 chars)."""
    if not text:
        return None
    # Take up to first double newline
    para = text.split("\n\n")[0].strip()
    # Remove markdown formatting
    para = re.sub(r'\*\*(.+?)\*\*', r'\1', para)
    para = re.sub(r'\*(.+?)\*', r'\1', para)
    para = re.sub(r'^###?\s+.+\n', '', para)  # Remove headings
    para = para.strip()
    if not para:
        return None
    # Truncate if needed
    if len(para) > 300:
        # Cut at last sentence boundary before 300
        cut = para[:300]
        last_period = max(cut.rfind('. '), cut.rfind('? '), cut.rfind('! '))
        if last_period > 100:
            return cut[:last_period + 1]
        return cut + "..."
    return para

# ─── Module Processing ────────────────────────────────────────────

def process_module(filepath):
    """Parse a module .md file into a hub-compatible data object."""
    meta, body = parse_frontmatter(filepath)
    if not meta or "id" not in meta:
        return None

    # Extract body sections
    overview_text = extract_section(body, "Overview") or ""
    objectives_text = extract_section(body, "Learning Objectives") or ""
    key_elements_text = extract_section(body, "Key Elements") or ""
    activities_text = extract_section(body, "Activities") or ""
    pain_points_text = extract_section(body, "Pain Points Addressed") or ""

    # Build key elements: use ### subsection titles if available, else bullets
    key_elements = extract_subsections(key_elements_text)
    if not key_elements:
        key_elements = extract_bullets(key_elements_text)
    # Limit to first 6 for readability
    key_elements = key_elements[:6]

    # Build learning objectives
    objectives = extract_bullets(objectives_text)[:4]

    # Activity: first paragraph or sentence
    activity = None
    if activities_text and "no formal activities" not in activities_text.lower():
        activity = first_paragraph(activities_text)

    # Pain point: first sentence
    pain_point = None
    if pain_points_text:
        pain_point = first_paragraph(pain_points_text)

    # Features
    features = meta.get("postman_features", []) or []
    if isinstance(features, str):
        features = [features]

    # Update triggers
    triggers = meta.get("update_triggers", []) or []

    # Determine lastAffected from recent updates (leave null, set by review skill)
    module_data = {
        "id": meta["id"],
        "name": meta.get("title", meta["id"]),
        "sensitivity": meta.get("change_sensitivity", "medium"),
        "status": meta.get("status", "current"),
        "lastUpdated": str(meta.get("last_updated", "")),
        "lastAudited": str(meta.get("last_audited", "")),
        "sourceFile": os.path.basename(filepath),
        "features": features,
        "overview": overview_text.split("\n\n")[0] if overview_text else "",
        "learningObjectives": objectives,
        "keyElements": key_elements,
        "activity": activity,
        "painPoint": pain_point,
        "updateTriggers": triggers,
        "lastAffected": None,  # Set by the review/apply workflow
    }

    return module_data

# ─── Program Processing ───────────────────────────────────────────

def load_programs():
    """Load program definitions from sources.yaml or use defaults."""
    if os.path.exists(SOURCES_YAML):
        with open(SOURCES_YAML, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        programs = config.get("programs", DEFAULT_PROGRAMS)
        return [p for p in programs if p.get("active", True)]
    return DEFAULT_PROGRAMS


# Icon and display name mappings
PROGRAM_DISPLAY = {
    "bootcamp": {
        "shortName": "Bootcamp",
        "icon": "&#9670;",
        "slidesLink": "https://docs.google.com/presentation/d/your-slides-link",
    },
    "101": {
        "shortName": "101",
        "icon": "&#9679;",
        "slidesLink": "",
    },
    "201": {
        "shortName": "201",
        "icon": "&#9650;",
        "slidesLink": "",
    },
    "301": {
        "shortName": "301",
        "icon": "&#9632;",
        "slidesLink": "",
    },
}


def process_program(program):
    """Process all modules in a program directory."""
    module_dir = os.path.join(WORKSPACE, program["module_dir"])
    if not os.path.isdir(module_dir):
        print(f"  INFO: Directory {module_dir} doesn't exist yet (program '{program['id']}' has no modules)", file=sys.stderr)
        return None

    md_files = sorted(glob.glob(os.path.join(module_dir, "*.md")))
    if not md_files:
        print(f"  INFO: No .md files in {module_dir}", file=sys.stderr)
        return None

    modules = []
    for filepath in md_files:
        mod = process_module(filepath)
        if mod:
            modules.append(mod)

    if not modules:
        return None

    display = PROGRAM_DISPLAY.get(program["id"], {
        "shortName": program["id"].upper(),
        "icon": "&#9679;",
        "slidesLink": "",
    })

    return {
        "id": program["id"],
        "name": program.get("name", program["id"]),
        "shortName": display["shortName"],
        "icon": display["icon"],
        "description": program.get("description", ""),
        "slidesLink": display["slidesLink"],
        "sourceDir": program["module_dir"],
        "modules": modules,
    }

# ─── JavaScript Generation ────────────────────────────────────────

def to_js_string(value):
    """Convert a Python value to a JavaScript-safe string literal."""
    if value is None:
        return "null"
    # Use json.dumps for proper escaping of quotes, newlines, etc.
    return json.dumps(value, ensure_ascii=False)


def generate_module_js(mod, indent=6):
    """Generate JavaScript object literal for a module."""
    pad = " " * indent
    lines = ["{"]
    lines.append(f'{pad}  id: {to_js_string(mod["id"])}, name: {to_js_string(mod["name"])}, sensitivity: {to_js_string(mod["sensitivity"])},')
    lines.append(f'{pad}  status: {to_js_string(mod["status"])}, lastUpdated: {to_js_string(mod["lastUpdated"])}, lastAudited: {to_js_string(mod["lastAudited"])},')
    lines.append(f'{pad}  sourceFile: {to_js_string(mod["sourceFile"])},')
    lines.append(f'{pad}  features: {json.dumps(mod["features"], ensure_ascii=False)},')
    lines.append(f'{pad}  overview: {to_js_string(mod["overview"])},')
    lines.append(f'{pad}  learningObjectives: {json.dumps(mod["learningObjectives"], ensure_ascii=False)},')
    lines.append(f'{pad}  keyElements: {json.dumps(mod["keyElements"], ensure_ascii=False)},')
    lines.append(f'{pad}  activity: {to_js_string(mod["activity"])},')
    lines.append(f'{pad}  painPoint: {to_js_string(mod["pain_point"] if "pain_point" in mod else mod.get("painPoint"))},')
    lines.append(f'{pad}  updateTriggers: {json.dumps(mod["updateTriggers"], ensure_ascii=False)},')
    lines.append(f'{pad}  lastAffected: {to_js_string(mod["lastAffected"])}')
    lines.append(f'{pad}}}')
    return ("\n").join(lines)


def generate_class_js(cls, indent=2):
    """Generate JavaScript object literal for a class/program."""
    pad = " " * indent
    mod_pad = " " * (indent + 4)

    lines = [f'{pad}{{']
    lines.append(f'{pad}  id: {to_js_string(cls["id"])},')
    lines.append(f'{pad}  name: {to_js_string(cls["name"])},')
    lines.append(f'{pad}  shortName: {to_js_string(cls["shortName"])},')
    lines.append(f'{pad}  icon: {to_js_string(cls["icon"])},')
    lines.append(f'{pad}  description: {to_js_string(cls["description"])},')
    lines.append(f'{pad}  slidesLink: {to_js_string(cls["slidesLink"])},')
    lines.append(f'{pad}  sourceDir: {to_js_string(cls["sourceDir"])},')
    lines.append(f'{pad}  modules: [')

    for i, mod in enumerate(cls["modules"]):
        mod_js = generate_module_js(mod, indent=indent + 4)
        comma = "," if i < len(cls["modules"]) - 1 else ""
        lines.append(f'{mod_pad}{mod_js}{comma}')

    lines.append(f'{pad}  ]')
    lines.append(f'{pad}}}')
    return "\n".join(lines)


def generate_classes_js(classes):
    """Generate the full CLASSES array JavaScript."""
    lines = ["const CLASSES = ["]
    for i, cls in enumerate(classes):
        comma = "," if i < len(classes) - 1 else ""
        lines.append(f'{generate_class_js(cls)}{comma}')
    lines.append("  // To add a new program, create module files in modules/{program}/ following")
    lines.append("  // the schema in modules/SCHEMA.md, register the program in sources.yaml,")
    lines.append("  // then run: python3 sync.py --write")
    lines.append("];")
    return "\n".join(lines)

# ─── Index.html Writing ───────────────────────────────────────────

def write_to_index(classes_js):
    """Replace the CLASSES array in index.html."""
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # Find and replace the CLASSES array
    pattern = r'const CLASSES = \[.*?\n\];'
    match = re.search(pattern, html, re.DOTALL)
    if not match:
        print("ERROR: Could not find CLASSES array in index.html", file=sys.stderr)
        sys.exit(1)

    new_html = html[:match.start()] + classes_js + html[match.end():]

    with open(INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"  Written to {INDEX_HTML}")


def check_drift(classes):
    """Compare module counts and IDs between .md files and index.html."""
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # Extract module IDs from index.html
    html_ids = set(re.findall(r'id:\s*"(M\d+|101-\d+|201-\d+|301-\d+)"', html))

    # Extract module IDs from .md files
    md_ids = set()
    for cls in classes:
        for mod in cls["modules"]:
            md_ids.add(mod["id"])

    only_in_html = html_ids - md_ids
    only_in_md = md_ids - html_ids

    if only_in_html or only_in_md:
        print("DRIFT DETECTED:")
        if only_in_html:
            print(f"  In index.html but not in .md files: {sorted(only_in_html)}")
        if only_in_md:
            print(f"  In .md files but not in index.html: {sorted(only_in_md)}")
        return False
    else:
        print("No drift detected. index.html matches .md files.")
        return True

# ─── Main ─────────────────────────────────────────────────────────

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--print"

    print(f"sync.py — {datetime.now().strftime('%Y-%m-%d %H:%M')}", file=sys.stderr)
    print(f"  Workspace: {WORKSPACE}", file=sys.stderr)

    # Load programs
    programs = load_programs()
    print(f"  Programs found: {[p['id'] for p in programs]}", file=sys.stderr)

    # Process each program
    classes = []
    total_modules = 0
    total_features = set()

    for program in programs:
        cls = process_program(program)
        if cls:
            classes.append(cls)
            n = len(cls["modules"])
            total_modules += n
            for mod in cls["modules"]:
                for f in mod["features"]:
                    total_features.add(f)
            print(f"  {program['id']}: {n} modules, {sum(len(m['features']) for m in cls['modules'])} feature dependencies", file=sys.stderr)

    print(f"  Total: {total_modules} modules across {len(classes)} programs", file=sys.stderr)
    print(f"  Unique features tracked: {len(total_features)}", file=sys.stderr)

    if not classes:
        print("ERROR: No modules found in any program directory.", file=sys.stderr)
        sys.exit(1)

    if mode == "--check":
        success = check_drift(classes)
        sys.exit(0 if success else 1)

    # Generate JavaScript
    classes_js = generate_classes_js(classes)

    if mode == "--write":
        write_to_index(classes_js)
        print(f"  CLASSES array updated in index.html ({total_modules} modules)", file=sys.stderr)
    else:
        # Print to stdout for inspection
        print(classes_js)


if __name__ == "__main__":
    main()
