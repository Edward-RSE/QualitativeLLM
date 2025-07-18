import argparse

import requests


base_url = "http://localhost:11434"


def get_server_health():
    response = requests.get(f"{base_url}")
    return response.status_code == 200


def post_completion(model, context, user_input):
    prompt = f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>{context}<|eot_id|><|start_header_id|>user<|end_header_id|>{user_input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    data = {
        "model": model,
        "prompt": prompt,
        "options": {
            "temperature": 0.9,
            "top_k": 35,
            "top_p": 0.95,
            "stop": ["</s>", "Assistant:", "User:", "<|eot_id|>"],
        },
        "stream": False,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{base_url}/api/generate", json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "Error processing your request. Please try again."


def proxy_post_completion(context, user_input):
    return context + "\n" + user_input


def update_context(context, user_input, assistant_response):
    return f"{context}\nUser: {user_input}\nAssistant: {assistant_response}"


def main(model, input_filename, prompt_filename, out_file, n):
    healthy = get_server_health()
    print(f"Server Health: {healthy}")

    if not healthy:
        print("Server is not ready for requests.")
        return

    with open(prompt_filename, "r", encoding="utf8") as f:
        prompt = f.read()

    in_text = []
    with open(input_filename, "r", encoding="utf8") as f:
        for line in f.readlines():
            in_text.append(line.strip("\n"))

    chunks = [in_text[i : i + n] for i in range(0, len(in_text), n)]

    print(f"Input file read. Chunk size {n}\nNumber of chunks: {len(chunks)}")

    with open(out_file, "w", encoding="utf8") as f:
        for i, chunk in enumerate(chunks):
            print(f"Processing chunk {i + 1}/{len(chunks)}")
            chunk = "\n".join(chunk)
            output = post_completion(model, prompt, chunk)

            f.write(f"{output}\n\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="AI-Navigator Interaction",
        description="Splits file up into chunks of size n and puts those into an LLM with a given prompt, then puts "
        "the output into a file",
    )

    parser.add_argument("model")
    parser.add_argument("input_filename")
    parser.add_argument("prompt_filename")
    parser.add_argument("-o", "--output_filename")
    parser.add_argument("-n", "--number_in_chunks")

    args = parser.parse_args()

    output_filename = "out.txt" if args.output_filename is None else args.output_filename
    number_in_chunks = 100 if args.number_in_chunks is None else int(args.number_in_chunks)

    main(args.model, args.input_filename, args.prompt_filename, output_filename, number_in_chunks)
