import re

# Open the file containing the dataset
#input_file_path = "DutchFolkTunes/OriginalDataset.txt"
input_file_path = "Eurovision/OriginalDataset.txt"
output_file_path = "processed_songs.txt"

# Read the dataset from the file
with open(input_file_path, "r") as file:
    dataset = file.read()

# Regex pattern to separate songs and format each
pattern = r"(\[L:\d+/\d+\])\s*(\[M:\d+/\d+\])\s*(\[K:[^\]]+\])(.+?)(?=\[L:\d+/\d+\]|\Z)"
matches = re.findall(pattern, dataset, re.DOTALL)

# Process each match into the desired format
formatted_songs = []
for match in matches:
    # Strip brackets from headers
    header_l = match[0].strip().replace("[", "").replace("]", "")
    header_m = match[1].strip().replace("[", "").replace("]", "")
    header_k = match[2].strip().replace("[", "").replace("]", "")
    
    # body = re.sub(r"\s+", " ", match[3]).strip()

    # Remove any redefinitions of [M:*] in the song body
    body = re.sub(r"\[M:\d+/\d+\]", "", match[3]).strip()
    body = re.sub(r"\s+", " ", body)  # Normalize whitespace
    
    # Remove trailing empty brackets "[ ]" if they exist
    body = re.sub(r"\s*\[\s*\]\s*$", "", body)
    
    # Format the song
    formatted_songs.append("{}\n{}\n{}\n{}".format(header_l, header_m, header_k, body))

# Join all formatted songs with newlines for separation
result = "\n\n".join(formatted_songs)

# Save the formatted result to a new file
with open(output_file_path, "w") as file:
    file.write(result)

print("Processed songs with redefined [M:*] and empty brackets removed have been saved to {}".format(output_file_path))