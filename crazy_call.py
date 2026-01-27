#!/usr/bin/env python3
"""
Crazy Call - Customer Notes & Funny Moments Tracker
Track wild Zoom interactions, customer notes, and funny work moments.
"""

import json
from datetime import datetime

NOTES_FILE = "customer_notes.json"


def load_notes():
    """Load notes from file."""
    try:
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_notes(notes):
    """Save notes to file."""
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)
    print(f"\nSaved {len(notes)} notes to {NOTES_FILE}")


def add_note(notes):
    """Add a new note."""
    print("\n--- Add New Note ---")
    print("Categories:")
    print("  1. Customer Note")
    print("  2. Wild Zoom Interaction")
    print("  3. Funny Work Moment")

    choice = input("\nSelect category (1-3): ").strip()
    categories = {"1": "Customer Note", "2": "Wild Zoom Interaction", "3": "Funny Work Moment"}

    category = categories.get(choice)
    if not category:
        print("Invalid category.")
        return

    customer = input("Customer/Person name (or press Enter to skip): ").strip()
    title = input("Brief title: ").strip()
    if not title:
        print("Title is required.")
        return

    print("Enter your note (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            if lines:
                break
        else:
            lines.append(line)

    content = "\n".join(lines)
    if not content:
        print("Note content is required.")
        return

    note = {
        "id": len(notes) + 1,
        "category": category,
        "customer": customer if customer else "N/A",
        "title": title,
        "content": content,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    notes.append(note)
    print(f"\nNote added: '{title}'")


def view_notes(notes):
    """View all notes."""
    if not notes:
        print("\nNo notes yet. Add some!")
        return

    print(f"\n{'='*60}")
    print(f"  ALL NOTES ({len(notes)} total)")
    print(f"{'='*60}")

    for note in notes:
        print(f"\n[{note['id']}] {note['category'].upper()}")
        print(f"    Title: {note['title']}")
        print(f"    Customer: {note['customer']}")
        print(f"    Date: {note['timestamp']}")
        print(f"    ---")
        for line in note['content'].split('\n'):
            print(f"    {line}")
        print(f"{'-'*60}")


def view_by_category(notes):
    """View notes filtered by category."""
    if not notes:
        print("\nNo notes yet.")
        return

    print("\n--- View by Category ---")
    print("  1. Customer Notes")
    print("  2. Wild Zoom Interactions")
    print("  3. Funny Work Moments")

    choice = input("\nSelect category (1-3): ").strip()
    categories = {"1": "Customer Note", "2": "Wild Zoom Interaction", "3": "Funny Work Moment"}

    category = categories.get(choice)
    if not category:
        print("Invalid category.")
        return

    filtered = [n for n in notes if n['category'] == category]

    if not filtered:
        print(f"\nNo notes in '{category}' category.")
        return

    print(f"\n{'='*60}")
    print(f"  {category.upper()} ({len(filtered)} notes)")
    print(f"{'='*60}")

    for note in filtered:
        print(f"\n[{note['id']}] {note['title']}")
        print(f"    Customer: {note['customer']}")
        print(f"    Date: {note['timestamp']}")
        print(f"    ---")
        for line in note['content'].split('\n'):
            print(f"    {line}")
        print(f"{'-'*60}")


def delete_note(notes):
    """Delete a note by ID."""
    if not notes:
        print("\nNo notes to delete.")
        return

    view_notes(notes)
    try:
        note_id = int(input("\nEnter note ID to delete (0 to cancel): "))
        if note_id == 0:
            return

        for i, note in enumerate(notes):
            if note['id'] == note_id:
                removed = notes.pop(i)
                print(f"\nDeleted: '{removed['title']}'")
                return

        print("Note not found.")
    except ValueError:
        print("Invalid ID.")


def main():
    """Main menu loop."""
    print("\n" + "="*40)
    print("   CRAZY CALL - Notes Tracker")
    print("="*40)

    notes = load_notes()
    print(f"Loaded {len(notes)} existing notes.")

    while True:
        print("\n--- MENU ---")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. View by Category")
        print("4. Delete Note")
        print("5. Save Notes")
        print("6. Exit")

        choice = input("\nChoice (1-6): ").strip()

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            view_by_category(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            save_notes(notes)
        elif choice == "6":
            save_choice = input("Save before exiting? (y/n): ").strip().lower()
            if save_choice == 'y':
                save_notes(notes)
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Try 1-6.")


if __name__ == "__main__":
    main()
