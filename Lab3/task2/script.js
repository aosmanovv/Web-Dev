const inputField = document.getElementById('todoInput');
const addBtn = document.getElementById('addBtn');
const todoList = document.getElementById('todoList');



function addTask() {
  const taskValue = inputField.value.trim();
  if (taskValue === '') return;

  const li = document.createElement('li');

  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.addEventListener('change', () => {
    span.classList.toggle('done');
  });

  const span = document.createElement('span');
  span.className = 'todo-text';
  span.textContent = taskValue;

  const deleteButton = document.createElement('button');
  deleteButton.textContent = 'x';
  deleteButton.className = 'delete-btn';
  deleteButton.onclick = () => {
    todoList.removeChild(li); 
  };

  li.appendChild(checkbox);
  li.appendChild(span);
  li.appendChild(deleteButton);
  
  todoList.appendChild(li);

  inputField.value = '';
}


addBtn.addEventListener('click', addTask);
inputField.addEventListener('keypress', (pressed) => {
  if (pressed.key === 'Enter') addTask();
});