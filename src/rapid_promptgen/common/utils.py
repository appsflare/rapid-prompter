def parse_response(response: str):
    prompt_response_list = []

    # Split the response into prompt-response pairs
    pairs = [pair.strip() for pair in response.split("**Prompt:**")]

    for pair in filter(lambda p: p != "", pairs):
        contents = pair.split("**Response:**")
        prompt_response_list.append({"prompt": contents[0], "response": contents[1]})

    return prompt_response_list
