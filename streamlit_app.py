"""I&I BIM Tools - searchable catalogue of Dynamo graphs (.dyn) for Revit.

The app reads every .dyn file in this folder, shows its description and
lets you download it. The graphs themselves run only inside Revit / Dynamo.
"""

import json
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).parent

CATEGORIES = {
    "A": "Setup",
    "B": "Model",
    "C": "Interior",
    "D": "Drawings",
    "E": "Issue",
}

CATEGORY_HELP = {
    "A": "Project start-up: units, levels, worksets, view templates, schedules",
    "B": "Modelling: grids, walls, doors, stairs, slabs, structure from CAD or plan",
    "C": "Interiors: rooms, ceilings, skirting, door/window numbering",
    "D": "Drawings: sheets, annotation, tile and RCP plans, details",
    "E": "Issue: QA check, PDF / DWG / IFC export, transmittals",
}

st.set_page_config(page_title="I&I BIM Tools", page_icon=":triangular_ruler:", layout="wide")


@st.cache_data
def load_tools():
    """Read every .dyn file in the repo and collect its basic information."""
    tools = []
    for path in sorted(ROOT.glob("*.dyn")):
        parts = path.stem.split("_")
        code = parts[0]
        letter = code[:1].upper()
        title = " ".join(parts[2:]) if len(parts) > 2 else path.stem

        description, nodes = "", None
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig"))
            description = (data.get("Description") or "").strip()
            nodes = len(data.get("Nodes", []))
        except (OSError, ValueError):
            description = "Could not read the description from this file."

        tools.append(
            {
                "file": path.name,
                "path": path,
                "code": code,
                "letter": letter,
                "category": CATEGORIES.get(letter, "Other"),
                "title": title,
                "description": description,
                "nodes": nodes,
                "size_kb": round(path.stat().st_size / 1024),
            }
        )
    return tools


tools = load_tools()

# ----------------------------------------------------------------------------
# Header

st.title(":triangular_ruler: I&I BIM Tools")
st.caption("Dynamo graphs for Revit - setup, modelling, interiors, drawings and issue.")

c1, c2, c3 = st.columns(3)
c1.metric("Dynamo graphs", len(tools))
c2.metric("Categories", len({t["letter"] for t in tools}))
c3.metric("Works with", "Revit 2026 + Dynamo 3.x")

with st.expander("How to use"):
    st.markdown(
        """
1. Find the tool you need with the search box or the category filter.
2. Click **Download** to save the `.dyn` file.
3. In Revit, open **Manage > Dynamo**, then **Open** and pick the file.
4. Read the description, set the inputs (many graphs use an Excel list or a linked CAD file) and press **Run**.

The graphs run only inside Revit. This page is the library, not an online runner.
        """
    )

# ----------------------------------------------------------------------------
# Filters

with st.sidebar:
    st.header("Find a tool")
    query = st.text_input("Search", placeholder="e.g. tile, stairs, export")
    chosen = st.multiselect(
        "Category",
        options=list(CATEGORIES.keys()),
        default=list(CATEGORIES.keys()),
        format_func=lambda k: f"{k} - {CATEGORIES[k]}",
    )
    st.markdown("---")
    for key, text in CATEGORY_HELP.items():
        st.caption(f"**{key} - {CATEGORIES[key]}**: {text}")

q = query.strip().lower()
shown = [
    t
    for t in tools
    if t["letter"] in chosen
    and (not q or q in (t["file"] + " " + t["description"]).lower())
]

st.subheader(f"{len(shown)} tool{'s' if len(shown) != 1 else ''}")

if not shown:
    st.info("No tools match. Try a different word or select more categories.")

# ----------------------------------------------------------------------------
# Tool list

for t in shown:
    label = f"{t['code']} - {t['title']}"
    with st.expander(label):
        st.markdown(f"**Category:** {t['category']}")
        st.write(t["description"] or "No description saved in this graph.")
        meta = [f"File size: {t['size_kb']} KB"]
        if t["nodes"] is not None:
            meta.append(f"Top-level nodes: {t['nodes']}")
        st.caption(" | ".join(meta))
        st.download_button(
            "Download .dyn",
            data=t["path"].read_bytes(),
            file_name=t["file"],
            mime="application/json",
            key=f"dl_{t['file']}",
        )

# ----------------------------------------------------------------------------
# Extras

pattern = ROOT / "RANDOM_RUBBLE_STONE.pat"
if pattern.exists():
    st.subheader("Revit fill pattern")
    st.write("Random rubble stone hatch, used by the compound wall details (D07).")
    st.download_button(
        "Download RANDOM_RUBBLE_STONE.pat",
        data=pattern.read_bytes(),
        file_name=pattern.name,
        mime="text/plain",
        key="dl_pattern",
    )

st.markdown("---")
st.caption("I&I BIM Engineering Consultant - licensed under Apache 2.0.")
