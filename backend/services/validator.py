import json
import re


def clean_json(response: str):

    response = response.strip()

    # Remove markdown JSON blocks
    response = re.sub(
        r"```json",
        "",
        response
    )

    response = re.sub(
        r"```",
        "",
        response
    )

    return response.strip()



def validate_response(response: str):

    try:

        cleaned = clean_json(response)

        data = json.loads(cleaned)

        return data


    except Exception as e:

        return {
            "match_score": 0,
            "missing_keywords": [],
            "suggestions": [
                f"Invalid AI response: {str(e)}"
            ]
        }