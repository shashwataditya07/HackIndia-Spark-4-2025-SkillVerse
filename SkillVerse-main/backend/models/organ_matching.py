import random

def ai_match_donor(donor, recipients):
    """
    AI-based donor matching logic.
    """
    matched_recipients = []
    for recipient in recipients:
        # Matching logic (blood type, organ, health conditions)
        if donor["blood_type"] == recipient["blood_type"] and donor["organ"] == recipient["organ"]:
            match_score = random.uniform(0.7, 1.0)  # Simulating AI model score
            if match_score > 0.8:
                matched_recipients.append(recipient)

    return matched_recipients