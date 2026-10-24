import json

class WikiEntry:
    def __init__(self, title, content, source_type, source_detail):
        self.title = title
        self.content = content
        self.source_type = source_type  # e.g., 'game_observation', 'dev_note', 'patch_log'
        self.source_detail = source_detail # e.g., 'v0.1.2', 'Player observation 2023-10-27', 'Dev Blog Post #5'

    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'source_type': self.source_type,
            'source_detail': self.source_detail
        }

class Wiki:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_entries_by_source_type(self, source_type):
        return [entry for entry in self.entries if entry.source_type == source_type]

    def get_all_entries(self):
        return self.entries

    def save_to_json(self, filename='wiki_data.json'):
        data = [entry.to_dict() for entry in self.entries]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Wiki saved to {filename}")

    def load_from_json(self, filename='wiki_data.json'):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.entries = [WikiEntry(d['title'], d['content'], d['source_type'], d['source_detail']) for d in data]
            print(f"Wiki loaded from {filename}")
        except FileNotFoundError:
            print(f"{filename} not found, starting with an empty wiki.")

# --- Example Usage ---

if __name__ == "__main__":
    my_wiki = Wiki()

    # Add some example entries with resource tags
    my_wiki.add_entry(WikiEntry(
        title="Iron Sword",
        content="A basic sword crafted from iron. Deals moderate damage.",
        source_type="game_observation",
        source_detail="Player found at level 1"
    ))

    my_wiki.add_entry(WikiEntry(
        title="Iron Sword",
        content="Iron Sword damage increased by 10% in patch v0.2.0.",
        source_type="patch_log",
        source_detail="v0.2.0"
    ))

    my_wiki.add_entry(WikiEntry(
        title="Goblin Camp Location",
        content="The first goblin camp is located north of the starting village.",
        source_type="dev_note",
        source_detail="Early access dev stream Q&A"
    ))

    # Save the wiki
    my_wiki.save_to_json()

    # Load the wiki and query it
    loaded_wiki = Wiki()
    loaded_wiki.load_from_json()

    print("\n--- All Entries ---")
    for entry in loaded_wiki.get_all_entries():
        print(f"- {entry.title} ({entry.source_type}: {entry.source_detail})")

    print("\n--- Entries from Game Observations ---")
    for entry in loaded_wiki.get_entries_by_source_type("game_observation"):
        print(f"- {entry.title}: {entry.content}")
