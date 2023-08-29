from typing import Any, Dict
import argilla as rg
from dotenv import load_dotenv

load_dotenv()

rg.init(workspace="aria")


def create_dataset():
    feedback_dataset = rg.FeedbackDataset(
        fields=[
            rg.TextField(name="prompt", required=True),
            rg.TextField(name="response", required=True, use_markdown=True),
        ],
        questions=[
            rg.LabelQuestion(
                name="quality",
                title="Content Quality",
                description="Rank this submission",
                required=True,
                labels={
                    "optimal": "Optimal",
                    "too-much-content": "Too Much Content",
                    "vague": "Vague",
                },
            ),
            rg.TextQuestion(
                name="final-prompt",
                title="Final Prompt",
                description="Final Prompt",
                use_markdown=False,
                required=False,
            ),
            rg.TextQuestion(
                name="final-response",
                title="Final Response",
                description="Final Response",
                use_markdown=True,
                required=False,
            ),
        ],
        guidelines="These are the annotation guidelines.",
    )
    feedback_dataset.push_to_argilla("aria_eform_generated")


def add_records(items: Dict[str, Any]):
    feedback_dataset = rg.FeedbackDataset.from_argilla("aria_eform_generated")
    records = []
    for item in items:
        records.append(rg.FeedbackRecord(fields=item))
    feedback_dataset.add_records(records=records)
    # feedback_dataset.push_to_argilla()
