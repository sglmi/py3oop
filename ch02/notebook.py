import datetime


last_id = 0

class Note:
	def __init__(self, memo, tags=""):
		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id

	def match(self, term):
		""" Determine if this note matches the term text.
			Return True if it matches, False otherwise.

		Search is case sensitive and matches both text and tags."""

		return term in self.memo or term in self.tags 



class Notebook:
	def __init__(self):
		self.notes = []

	def new_note(self, memo, tags=""):
		""" Create new note and add it to the list."""
		self.notes.append(Note(memo, tags))

	def _find_note(self, note_id: str,) -> str:
		for note in self.notes:
			if str(note.id) == str(note_id):
				return note
		return ""

	def modify_memo(self, note_id, memo):
		""" Find the note with the given id and change its memo to the given value."""
		note = self._find_note(note_id)
		if note:
			note.memo = memo
			return True
		return False
	def modify_tags(self, note_id, tags):
		note = self._find_note(note_id)
		if note:
			note.tags = tags
			return True
		return False

	def search(self, term):
		return [note for note in self.notes if note.match(term)]



