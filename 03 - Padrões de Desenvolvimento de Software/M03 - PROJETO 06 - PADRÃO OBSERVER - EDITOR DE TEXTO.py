# Classe Observer
class Observer:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

# Classe Subject
class Subject:
    def __init__(self):
        self._observers = Observer()

    def attach(self, observer):
        self._observers.attach(observer)

    def detach(self, observer):
        self._observers.detach(observer)

    def notify(self):
        self._observers.notify()

# Classe Editor
class Editor(Subject):
    def __init__(self):
        super().__init__()
        self._content = []

    def insertLine(self, lineNumber, text):
        self._content.insert(lineNumber, text)
        self.notify()

    def removeLine(self, lineNumber):
        del self._content[lineNumber]
        self.notify()

    def getContent(self):
        return self._content

# Subclasse TextEditor
class TextEditor(Editor):
    def __init__(self, filePath):
        super().__init__()
        self._filePath = filePath

    def openFile(self):
        with open(self._filePath, 'r') as f:
            for line in f:
                self._content.append(line.strip())
        self.notify()

    def saveFile(self):
        with open(self._filePath, 'w') as f:
            f.write('\n'.join(self._content))

# Classe ConsoleListener
class ConsoleListener:
    def __init__(self, editor):
        self._editor = editor

    def update(self):
        print("Conteúdo atual do arquivo:")
        for line in self._editor.getContent():
            print(line)

# Criando um objeto TextEditor e adicionando um listener
textEditor = TextEditor('arquivo.txt')
consoleListener = ConsoleListener(textEditor)
textEditor.attach(consoleListener)

# Abrindo o arquivo e adicionando linhas de texto
textEditor.openFile()
while True:
    line = input("Digite uma linha de texto (ou 'EOF' para finalizar): ")
    if line == 'EOF':
        break
    textEditor.insertLine(len(textEditor.getContent()), line)

# Salvando o arquivo
textEditor.saveFile()
