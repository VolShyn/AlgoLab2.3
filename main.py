# Додати ребро
def add_edge(v, w):
    global adj
    adj[v].append(w)
    adj[w].append(v)


# Пошук у глибину
def dfs(v, id, id_number):
    global visited, adj, c

    # Перевірка чи попадає у вершину
    visited[v] = True

    # Законекчений компонент та його ІД
    id[v] = id_number

    c += 1

    # Пройтися по всім примикаючим вершинам
    for i in adj[v]:

        # Якщо до вершини не входить
        if (not visited[i]):
            dfs(i, id, id_number)


def connected_components():
    global V, adj, visited, c

    # id[i]: зберігає компонент чи існує тут вершина
    id = [0] * (V + 1)

    component_size = [0] * (V + 1)
    for v in range(1, V + 1):

        # Якщо вершина не помічена
        if (visited[v] == False):

            c = 0

            # ІД даного компонента
            id_number = v
            dfs(v, id, id_number)

            # Зберігає кількість вершин даного компонента
            component_size[v] = c
        else:

            component_size[v] = component_size[id[v]]

    # Ітеруємо по всім вершинам
    for v in range(1, V + 1):

        # Перевірка чи компонент - граф
        if (component_size[v] - 1 != len(adj[v])):
            return False
    return True


# перевірка на транзитивність
def is_transitive(N, M, Edge):
    global adj, visited, c

    # Перетин з масивом
    for i in range(M):
        add_edge(Edge[i][0], Edge[i][1])

    # Якщо всі компоненти - повні графи
    f = connected_components()
    if (f == 0):
        sg.popup(("NO"))
    else:
        sg.popup(("YES"))


if __name__ == '__main__':
    import PySimpleGUI as sg

    sg.theme('BluePurple')

    layout = [[sg.Input('51',  size = (10,1), key='-ed-')],
              [sg.Input('52', key='-ed1-', size=(10,1))],
              [sg.Input('', size = (10,1), key='-ed2-')],
              [sg.Input('2', key='-IN-', size=(2, 1)), sg.Input('2', key='-IN1-', size=(2, 1))],
              [sg.Button('Show'), sg.Button('Exit')]]

    window = sg.Window('Pattern 2B', layout, element_justification='right')

    while True:
        event, values = window.read()
        V, c = 5, 0
        adj = [[] for i in range(V + 1)]
        visited = [False] * (V + 1)
        N = int(values['-IN-'])
        M = int(values['-IN1-'])
        Edge = []
        list1 = []
        for x in values['-ed-']:
            list1.append(int(x))
        Edge.append(list1)
        list1 = []
        for x in values['-ed1-']:
            list1.append(int(x))
        Edge.append(list1)
        list1 = []
        for x in values['-ed2-']:
            list1.append(int(x))
        Edge.append(list1)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Show':
            is_transitive(N, M, Edge)
            break

    window.close()
