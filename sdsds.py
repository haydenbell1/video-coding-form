import json

# File paths
file_a_path = r"C:\Users\haydo\Downloads\dataset_tiktok-scraper_2024-10-01_23-40-20-990 (1).json"
file_b_path = r"C:\Users\haydo\Downloads\dataset_tiktok-comments-scraper_2024-10-02_00-08-36-917.json"
output_file_path = r"C:\Users\haydo\Downloads\combined_tiktok_data.json"

# Load File A (Expecting it to be a list of objects)
with open(file_a_path, 'r', encoding='utf-8') as file_a:
    file_a_data = json.load(file_a)

# Load File B (Expecting it to be a list of comment objects)
with open(file_b_path, 'r', encoding='utf-8') as file_b:
    file_b_data = json.load(file_b)

# Verify that both files contain lists
if not isinstance(file_a_data, list) or not isinstance(file_b_data, list):
    raise ValueError("Both files should contain a list of objects.")

# Create a new list to hold combined results for each video in File A
combined_data = []

# Iterate through each video object in File A
for item_a in file_a_data:
    # Extract only the specified fields from each item in File A
    filtered_item_a = {
        "id": item_a.get("id"),
        "text": item_a.get("text"),
        "createTime": item_a.get("createTime"),
        "createTimeISO": item_a.get("createTimeISO"),
        "diggCount": item_a.get("diggCount"),
        "shareCount": item_a.get("shareCount"),
        "playCount": item_a.get("playCount"),
        "collectCount": item_a.get("collectCount"),
        "commentCount": item_a.get("commentCount"),
        "mentions": item_a.get("mentions"),
        "hashtags": item_a.get("hashtags"),
        "searchQuery": item_a.get("searchQuery"),
        "mediaUrls": item_a.get("mediaUrls")  # Include mediaUrls from File A
    }

    # Ensure that the current item in File A has a valid 'id' value
    item_a_id = filtered_item_a.get("id")
    if not isinstance(item_a_id, str) or not item_a_id:
        continue  # Skip if 'id' is not a valid string

    # Find matching comments in File B where the videoWebUrl contains the ID from File A
    matching_comments = [
        {
            "videoWebUrl": comment.get("videoWebUrl"),
            "text": comment.get("text"),
            "diggCount": comment.get("diggCount"),
            "repliesToId": comment.get("repliesToId"),
            "replyCommentTotal": comment.get("replyCommentTotal")
        }
        for comment in file_b_data
        if isinstance(comment, dict) and isinstance(comment.get("videoWebUrl"), str) and item_a_id in comment.get("videoWebUrl", "")
    ]

    # Add matching comments to the filtered item
    filtered_item_a["comments"] = matching_comments

    # Append the combined item to the result list
    combined_data.append(filtered_item_a)

# Save the combined JSON for all objects to a new file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(combined_data, output_file, indent=4)

print(f"Combined JSON has been saved to: {output_file_path}")
