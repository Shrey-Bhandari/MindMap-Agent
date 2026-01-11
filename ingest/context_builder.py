from typing import List, Dict, Optional


def build_contextual_slides(
    unit_id: str,
    ppt_name: str,
    slides: List[Dict],
    start_global_index: int
) -> List[Dict]:
    """
    Attach previous and next slide context.
    """
    normalized = []
    global_index = start_global_index

    def join_text(text_list: List[str]) -> Optional[str]:
        return " ".join(text_list) if text_list else None

    for i, slide in enumerate(slides):
        prev_slide = slides[i - 1] if i > 0 else None
        next_slide = slides[i + 1] if i < len(slides) - 1 else None

        record = {
            "unit_id": unit_id,
            "global_slide_index": global_index,
            "ppt_name": ppt_name,
            "slide_number": slide["slide_number"],
            "title": slide["title"],
            "current_text": join_text(slide["raw_text"]),
            "previous_context": join_text(prev_slide["raw_text"]) if prev_slide else None,
            "next_context": join_text(next_slide["raw_text"]) if next_slide else None,
            "raw_metadata": {
                "has_image": slide["has_image"],
                "bullet_count": len(slide["raw_text"]),
            },
        }

        normalized.append(record)
        global_index += 1

    return normalized, global_index
