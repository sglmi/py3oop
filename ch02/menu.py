import sys

from notebook import Notebook


class Menu:
	def __init__(self):
		self.notebook = Notebook()

		self.choices = {
			"1": self.show_notes,
			"2": self.search_notes,
			"3": self.add_note,
			"4": self.modify_note,
			"5": self.quit,
		}

	def display_menu(self):
		msg = """
		Notebook Menu
		---------------
		1. Show all Notes
		2. Search Notes
		3. Add Notes
		4. Modify Note
		5. Quit
		""".strip()
		print(msg)

	def run(self):
		while True:
			self.display_menu()
			choice = input("Enter an option: ")
			action = self.choices.get(choice)
			if action is not None:
				action()
			else:
				print(f"{choice} is not a valid choice.")

	def show_notes(self, notes=None):
		if not notes:
			notes = self.notebook.notes
		for note in self.notebook.notes:
				print(f"{note.id} {note.tags} {note.memo}" )

	def search_notes(self):
		term = input("Search for: ")
		notes = self.notebook.search(term)
		self.show_notes(notes)

	def add_note(self):
		memo = input("Enter a memo: ")
		self.notebook.new_note(memo)
		print("Your note has been added.")

	def modify_note(self):
		note_id = input("Enter a note id: ")
		memo = input("Enter a memo: ")
		tags = input("Enter tags: ")
		if memo:
			self.notebook.modify_memo(note_id, memo)
		if tags:
			self.notebook.modify_tags(note_id, tags)

	def quit(self):
		print("Thank you for using your notebook today.")
		sys.exit(0)

if __name__ == "__main__":
	Menu().run()