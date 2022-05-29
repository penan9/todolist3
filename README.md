git clone https://github.com/penan9/todolist3.git

(myVenv) 8:16:57:~/PycharmProjects/pythonTodo
% docker build --no-cache -t mytododocker:latest .
% docker run -p 5001:5001 --rm mytododocker

to build docker compose:
% docker-compose up --build

to run docker compose:
% docker-compose up

to list out all todo list:
1) curl --location --request GET 'http://localhost:5001/todo?access_token=ya29.a0ARrdaM_bpzpN8vgANr4PLdFcnozwPz7BCX8JW7pkRDlIuohD-1K7YhhoSQ_YLr88YGLKYcpE-ZJfj0pSSqNbWA5zh5ZbXM1np91pi5ugMsKVpWn0aBfjGAJ3C8uX7ys7b6yX5KFRqKvGeo3qFNkRXkiKoYgD' \
--data-raw ''

2) curl \
--request GET \
--header "Authorization: Bearer ya29.a0ARrdaM_bpzpN8vgANr4PLdFcnozwPz7BCX8JW7pkRDlIuohD-1K7YhhoSQ_YLr88YGLKYcpE-ZJfj0pSSqNbWA5zh5ZbXM1np91pi5ugMsKVpWn0aBfjGAJ3C8uX7ys7b6yX5KFRqKvGeo3qFNkRXkiKoYgD" \
--header "Accept: application/json" \
--url "http://localhost:5001/todo"

todos: [{'id': 2, 'taskName': 'New task', 'markDone': True, 'description': 'Next week do'}, {'id': 3, 'taskName': 'Holiday tomorrow', 'markDone': False, 'description': 'Bring mother to see doc'}, {'id': 4, 'taskName': 'Go Alma', 'markDone': False, 'description': 'Bring little huanzhu '}, {'id': 5, 'taskName': 'ikat tepi again?', 'markDone': False, 'description': 'Bring little huanzhu also pa'}, {'id': 6, 'taskName': 'ikat tepi again? mau?', 'markDone': False, 'description': 'in little huanzhu apa pun mau?'}, {'id': 7, 'taskName': 'apa u mau?', 'markDone': False, 'description': 'whooo mau?'}, {'id': 8, 'taskName': 'try new one?', 'markDone': False, 'description': 'whooo, ok done!'}, {'id': 9, 'taskName': 'try new one again?', 'markDone': False, 'description': 'whooo, ok done wohooo!'}, {'id': 10, 'taskName': 'try new one again, ok?', 'markDone': False, 'description': 'whooo, ok done wohooo one!'}, {'id': 11, 'taskName': 'try new one again, ok, ok?', 'markDone': False, 'description': 'whooo, ok done wohooo one, ok!'}, {'id': 12, 'taskName': 'new week end again, haha!', 'markDone': False, 'description': 'whooo, tomorrow go bw!'}, {'id': 13, 'taskName': 'new week end again, wohoo!', 'markDone': False, 'description': 'whooo, tomorrow go or next day!'}, {'id': 14, 'taskName': 'new week ...', 'markDone': False, 'description': 'oowh,tomorrow back to work kay!'}, {'id': 15, 'taskName': 'new week holiday ...', 'markDone': False, 'description': 'ok,tomorrow back to work ya!'}, {'id': 16, 'taskName': 'new week 1 holiday ...', 'markDone': True, 'description': 'new, tomorrow back to work ya!'}, {'id': 18, 'taskName': 'new week 3 holiday ...', 'markDone': True, 'description': 'new 3, tomorrow back to work ya!'}]         <br> <a href='/logout'><button>logout</button></a>%

to list out a particular list:
1) (myVenv) 13:30:12:~/PycharmProjects/pythonTodo
% curl --location --request GET 'http://localhost:5001/todo/3?access_token=ya29.a0ARrdaM_bpzpN8vgANr4PLdFcnozwPz7BCX8JW7pkRDlIuohD-1K7YhhoSQ_YLr88YGLKYcpE-ZJfj0pSSqNbWA5zh5ZbXM1np91pi5ugMsKVpWn0aBfjGAJ3C8uX7ys7b6yX5KFRqKvGeo3qFNkRXkiKoYgD' \
--data-raw ''
{
  "description": "Bring mother to see doc",
  "id": 3,
  "markDone": false,
  "taskName": "Holiday tomorrow"
}

2) curl \
--request GET \
--header "Authorization: Bearer ya29.a0ARrdaM8S2ukLrOjo5QlKsEs3ZEEfvQYuZY7itYyZb5si4q8EcP0RKES5xU7A-9tLY7zzPR-_A0qLKq5lPz5l9CHYnOg1yDDsBhxoqzhFkwg_iTJkDwspDqpw8-QwHt_N3ywjLtyNFphmYMEdkbyGXoo31hX9" \
--header "Accept: application/json" \
--url "http://localhost:5001/todo/3"

{
  "description": "Bring mother to see doc",
  "id": 3,
  "markDone": false,
  "taskName": "Holiday tomorrow"
}

To add a new todo list:
1) curl --location --request POST 'http://localhost:5001/todo?access_token=ya29.a0ARrdaM_bpzpN8vgANr4PLdFcnozwPz7BCX8JW7pkRDlIuohD-1K7YhhoSQ_YLr88YGLKYcpE-ZJfj0pSSqNbWA5zh5ZbXM1np91pi5ugMsKVpWn0aBfjGAJ3C8uX7ys7b6yX5KFRqKvGeo3qFNkRXkiKoYgD' \
--header 'Content-Type: application/json' \
--data-raw '{
"taskName": "New task 3",
"description": "Next week do 2",
"markDone": false
}
'

2)curl --location --request POST 'http://127.0.0.1:5001/todo' \
--header 'Authorization: Bearer ya29.a0ARrdaM_bpzpN8vgANr4PLdFcnozwPz7BCX8JW7pkRDlIuohD-1K7YhhoSQ_YLr88YGLKYcpE-ZJfj0pSSqNbWA5zh5ZbXM1np91pi5ugMsKVpWn0aBfjGAJ3C8uX7ys7b6yX5KFRqKvGeo3qFNkRXkiKoYgD' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "Bring little girl along 13",
    "markDone": false,
    "taskName": "Go Alma ok 13"
}'

{
    "id": 21
}

To delete a todo list:curl --location --request POST 'http://127.0.0.1:5001/todo' \
--header 'Authorization: Bearer ya29.a0ARrdaM_bpzpN8vgANr4PLdFcnozwPz7BCX8JW7pkRDlIuohD-1K7YhhoSQ_YLr88YGLKYcpE-ZJfj0pSSqNbWA5zh5ZbXM1np91pi5ugMsKVpWn0aBfjGAJ3C8uX7ys7b6yX5KFRqKvGeo3qFNkRXkiKoYgD' \
--header 'Content-Type: application/json' \
--url "http://localhost:5001/todo"
--data-raw '{ "description": "Bring little girl along ", "markDone": false, "taskName": "Go Alma ok" }'

1) curl --location --request DELETE 'http://localhost:5001/todo/19?access_token=ya29.a0ARrdaM_bpzpN8vgANr4PLdFcnozwPz7BCX8JW7pkRDlIuohD-1K7YhhoSQ_YLr88YGLKYcpE-ZJfj0pSSqNbWA5zh5ZbXM1np91pi5ugMsKVpWn0aBfjGAJ3C8uX7ys7b6yX5KFRqKvGeo3qFNkRXkiKoYgD' \
--header 'Content-Type: application/json' \
--data-raw '
'

2) curl \
--request DELETE \
--header "Authorization: Bearer ya29.a0ARrdaM_bpzpN8vgANr4PLdFcnozwPz7BCX8JW7pkRDlIuohD-1K7YhhoSQ_YLr88YGLKYcpE-ZJfj0pSSqNbWA5zh5ZbXM1np91pi5ugMsKVpWn0aBfjGAJ3C8uX7ys7b6yX5KFRqKvGeo3qFNkRXkiKoYgD" \
--url "http://localhost:5001/todo/17"

{
  "message": "Done delete todo!"
}

To mark a complete task:
1) curl --location --request POST 'http://localhost:5001/todo_complete/18?access_token=ya29.a0ARrdaM_bpzpN8vgANr4PLdFcnozwPz7BCX8JW7pkRDlIuohD-1K7YhhoSQ_YLr88YGLKYcpE-ZJfj0pSSqNbWA5zh5ZbXM1np91pi5ugMsKVpWn0aBfjGAJ3C8uX7ys7b6yX5KFRqKvGeo3qFNkRXkiKoYgD' \
--header 'Content-Type: application/json' \
--data-raw '
'

2) curl \
--request POST \
--header "Authorization: Bearer ya29.a0ARrdaM_bpzpN8vgANr4PLdFcnozwPz7BCX8JW7pkRDlIuohD-1K7YhhoSQ_YLr88YGLKYcpE-ZJfj0pSSqNbWA5zh5ZbXM1np91pi5ugMsKVpWn0aBfjGAJ3C8uX7ys7b6yX5KFRqKvGeo3qFNkRXkiKoYgD" \
--url "http://localhost:5001/todo_complete/16"

{
  "id": 16,
  "message": "Marking done!"
}



