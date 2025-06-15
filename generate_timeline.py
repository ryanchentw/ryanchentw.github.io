import os
import re
import yaml
from datetime import datetime

POSTS_DIR = "content/posts"
OUTPUT_FILE = "content/_index.md"

def extract_metadata(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    # Extract YAML front matter
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    meta = yaml.safe_load(match.group(1))
    # Get title and date
    title = meta.get("title")
    date = meta.get("date")
    # Always convert date to string in YYYY-MM-DD format
    if isinstance(date, datetime):
        date_str = date.strftime("%Y-%m-%d")
    elif isinstance(date, str):
        # Try to parse and reformat
        try:
            date_str = datetime.fromisoformat(date).strftime("%Y-%m-%d")
        except Exception:
            date_str = date[:10]
    else:
        date_str = str(date)
    return {
        "title": title,
        "date": date_str,
        "filename": os.path.basename(filepath)
    }

def main():
    posts = []
    for fname in os.listdir(POSTS_DIR):
        if fname.endswith(".md"):
            meta = extract_metadata(os.path.join(POSTS_DIR, fname))
            if meta and meta["title"] and meta["date"]:
                posts.append(meta)
    # Group by year
    posts_by_year = {}
    for post in posts:
        year = post["date"][:4]
        posts_by_year.setdefault(year, []).append(post)
    # Sort years descending, posts within year ascending
    years = sorted(posts_by_year.keys(), reverse=True)
    for year in years:
        posts_by_year[year].sort(key=lambda x: x["date"])
    # Write nested timeline
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Timeline\n\n")
        for year in years:
            f.write(f"## {year}\n\n")
            for post in posts_by_year[year]:
                date_str = post["date"][:10]
                link = post['filename']
                if link.endswith('.md'):
                    link = link[:-3]
                f.write(f"- {date_str} — [{post['title']}](/posts/{link})\n")
            f.write("\n")

if __name__ == "__main__":
    main() 
