import json
import re
import sys

def get_entities(data):
    """Get entity spans from doccano line"""
    return data.get("label") or data.get("labels") or data.get("entities") or []

def tokenize(text):
    """Split text into tokens, preserving punctuation"""
    return re.findall(r"\w+|[^\w\s]", text, re.UNICODE)

def doccano_to_conll(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            if not line.strip():
                continue

            data = json.loads(line)
            text = data.get("text") or data.get("content", "")
            entities = get_entities(data)

            # Create tag array for each char in text
            tags = ["O"] * len(text)
            for ent in entities:
                try:
                    start, end, label = ent
                except ValueError:
                    continue  # skip invalid entities
                if start < 0 or end > len(text):
                    continue
                tags[start] = f"B-{label.upper()}"
                for i in range(start + 1, end):
                    tags[i] = f"I-{label.upper()}"

            # Tokenize and map back
            idx = 0
            for token in tokenize(text):
                start = text.find(token, idx)
                end = start + len(token)
                idx = end
                tag_slice = tags[start:end]
                tag = "O"
                for t in tag_slice:
                    if t != "O":
                        tag = t
                        break
                outfile.write(f"{token}\t{tag}\n")

            outfile.write("\n")  # separate samples
        
        print(f"✅ Conversion complete! Output saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python doccano_resume_to_conll.py input.jsonl output.conll")
    else:
        doccano_to_conll(sys.argv[1], sys.argv[2])
