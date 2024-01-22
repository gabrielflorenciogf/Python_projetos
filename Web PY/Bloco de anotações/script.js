document.addEventListener('DOMContentLoaded', function () {
    loadNotes();
});

function loadNotes() {
    const notesContainer = document.getElementById('notes-container');
    const notes = getSavedNotes();

    notes.forEach(function (note, index) {
        const noteElement = createNoteElement(note, index);
        notesContainer.appendChild(noteElement);
    });
}

function getSavedNotes() {
    const notes = JSON.parse(localStorage.getItem('notes')) || [];
    return notes;
}

function saveNotes() {
    const notesContainer = document.getElementById('notes-container');
    const notes = [];
    const noteElements = notesContainer.getElementsByClassName('note');

    for (let i = 0; i < noteElements.length; i++) {
        notes.push(noteElements[i].textContent);
    }

    localStorage.setItem('notes', JSON.stringify(notes));
    alert('Anotações salvas com sucesso!');
}

function createNoteElement(note, index) {
    const noteElement = document.createElement('div');
    noteElement.classList.add('note');
    noteElement.textContent = note;

    const actionButtons = document.createElement('div');
    actionButtons.classList.add('action-buttons');

    const editButton = document.createElement('button');
    editButton.textContent = 'Editar';
    editButton.onclick = function () {
        editNote(index);
    };

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Excluir';
    deleteButton.onclick = function () {
        deleteNote(index);
    };

    actionButtons.appendChild(editButton);
    actionButtons.appendChild(deleteButton);

    noteElement.appendChild(actionButtons);

    return noteElement;
}

function addNote() {
    const noteInput = document.getElementById('note-input');
    const noteText = noteInput.value.trim();

    if (noteText !== '') {
        const notesContainer = document.getElementById('notes-container');
        const noteElement = createNoteElement(noteText, notesContainer.childElementCount);
        notesContainer.appendChild(noteElement);

        noteInput.value = '';
    }
}

function editNote(index) {
    const notesContainer = document.getElementById('notes-container');
    const noteElement = notesContainer.children[index];
    const currentNoteText = noteElement.textContent;

    const newNoteText = prompt('Editar anotação:', currentNoteText);

    if (newNoteText !== null) {
        noteElement.textContent = newNoteText;
    }
}

function deleteNote(index) {
    const notesContainer = document.getElementById('notes-container');
    const noteElement = notesContainer.children[index];

    const confirmDelete = confirm('Tem certeza de que deseja excluir esta anotação?');

    if (confirmDelete) {
        notesContainer.removeChild(noteElement);
    }
}
