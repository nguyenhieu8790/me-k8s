import yaml
import os

def split_yaml(input_file, output_dir="output"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, "r") as f:
        docs = list(yaml.safe_load_all(f))

    for doc in docs:
        if not doc:
            continue

        kind = doc.get("kind", "unknown")
        name = doc.get("metadata", {}).get("name", "noname")

        filename = f"{kind.lower()}-{name}.yaml"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w") as out:
            yaml.dump(doc, out, sort_keys=False)

        print(f"Created: {filepath}")

if __name__ == "__main__":
    # Example usage
    split_yaml("install.yaml")