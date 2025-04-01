import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def encode_profile(blood_type, hla_typing, organ_type):
    blood_map = {"O": 0, "A": 1, "B": 2, "AB": 3}
    organ_map = {"kidney": 0, "liver": 1, "heart": 2, "lung": 3, "pancreas": 4}
    hla_vector = [int(x) for x in hla_typing.split()]  # Simplified encoding
    return [blood_map[blood_type], organ_map[organ_type]] + hla_vector

def match_donors_recipients(donors, recipients):
    best_match = None
    highest_score = -1
    
    for donor_id, donor_profile in donors.items():
        for recipient_id, recipient_profile in recipients.items():
            # Ensure same organ type
            if donor_profile[1] != recipient_profile[1]:
                continue
            
            score = cosine_similarity([donor_profile], [recipient_profile])[0][0]
            if score > highest_score:
                highest_score = score
                best_match = (donor_id, recipient_id)
    
    if best_match:
        return {"donor": best_match[0], "recipient": best_match[1], "score": highest_score}
    return {"message": "No match found"}