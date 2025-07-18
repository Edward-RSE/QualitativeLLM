import argparse

from openai import OpenAI


def post_completion(context, user_input):
    response = client.chat.completions.create(
        model="gpt-4o", messages=[{"role": "developer", "content": context}, {"role": "user", "content": user_input}]
    )

    return response.choices[0].message.content


def main(input_filename, prompt_filename, out_file, n):
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
            output = post_completion(prompt, chunk)

            f.write(f"{output}\n\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="AI-Navigator Interaction",
        description="Splits file up into chunks of size n and puts those into an LLM with a given prompt, then puts "
        "the output into a file",
    )

    parser.add_argument("model_name")  # Unused, kept kept for consistency with other scripts
    parser.add_argument("input_filename")
    parser.add_argument("prompt_filename")
    parser.add_argument("-o", "--output_filename")
    parser.add_argument("-n", "--number_in_chunks")
    parser.add_argument("-k", "--key")

    args = parser.parse_args()

    output_filename = "out.txt" if args.output_filename is None else args.output_filename
    number_in_chunks = 100 if args.number_in_chunks is None else int(args.number_in_chunks)

    client = OpenAI(api_key=args.key)

    main(args.input_filename, args.prompt_filename, output_filename, number_in_chunks)
