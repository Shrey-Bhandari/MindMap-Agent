from pathlib import Path
from ingest.ppt_parser import load_ppt
from ingest.context_builder import build_contextual_slides
import json


def run_phase_1(unit_id: str, ppt_paths: list, output_path: Path):
    all_slides = []
    global_index = 1

    for ppt_path in ppt_paths:
        ppt_path = Path(ppt_path)
        slides = load_ppt(ppt_path)

        contextual_slides, global_index = build_contextual_slides(
            unit_id=unit_id,
            ppt_name=ppt_path.name,
            slides=slides,
            start_global_index=global_index
        )

        all_slides.extend(contextual_slides)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_slides, f, indent=2, ensure_ascii=False)

    print(f"[RecallGraph] Phase 1 complete. Slides processed: {len(all_slides)}")


if __name__ == "__main__":
    run_phase_1(
        unit_id="UNIT_3",
        ppt_paths=[
            "data/raw_ppts/3_1.pptx",
            "data/raw_ppts/3_2.pptx",
            "data/raw_ppts/3_3.pptx"
        ],
        output_path=Path("data/normalized/unit_3_slides.json")
    )
