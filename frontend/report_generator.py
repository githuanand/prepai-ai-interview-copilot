from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    question,
    answer,
    evaluation,
    score
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "PrepAI Interview Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"<b>Interview Score:</b> {score}/10",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 10))

    elements.append(
        Paragraph(
            f"<b>Question:</b><br/>{question}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 10))

    elements.append(
        Paragraph(
            f"<b>Your Answer:</b><br/>{answer}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 10))

    elements.append(
        Paragraph(
            f"<b>AI Evaluation:</b><br/>{evaluation}",
            styles["BodyText"]
        )
    )

    doc.build(elements)