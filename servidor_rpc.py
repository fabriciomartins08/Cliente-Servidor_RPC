import xmlrpc.server
import sqlite3

class ContatosServer:
    def __init__(self):
        self.conn = sqlite3.connect('contatos.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS contatos
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         client_id INTEGER,
                         name TEXT,
                         phone TEXT,
                         email TEXT)''')

    def adicionar_contato(self, client_id, name, phone, email):
        self.c.execute("INSERT INTO contatos (client_id, name, phone, email) VALUES (?, ?, ?, ?)",
                       (client_id, name, phone, email))
        self.conn.commit()
        return self.c.lastrowid

    def remover_contato(self, client_id, contact_id):
        self.c.execute("DELETE FROM contatos WHERE client_id = ? AND id = ?", (client_id, contact_id))
        self.conn.commit()

    def procurar_por_letra(self, client_id, letter):
        self.c.execute("SELECT * FROM contatos WHERE client_id = ? AND name LIKE ?", (client_id, letter + '%'))
        return self.c.fetchall()

    def procurar_por_nome(self, client_id, name):
        self.c.execute("SELECT * FROM contatos WHERE client_id = ? AND name = ?", (client_id, name))
        return self.c.fetchall()

    def pegue_proximo_contato(self, client_id):
        self.c.execute("SELECT * FROM contatos WHERE client_id = ? ORDER BY name LIMIT 1", (client_id,))
        return self.c.fetchone()

    def pegue_proxima_letra(self, client_id, letter):
        self.c.execute("SELECT name FROM contatos WHERE client_id = ? AND name > ? ORDER BY name LIMIT 1",
                       (client_id, letter))
        result = self.c.fetchone()
        if result is not None:
            return result[0][0]
        else:
            return None

    def pegue_contato_index_do_id(self, client_id, contact_id):
        self.c.execute("SELECT id FROM contatos WHERE client_id = ? AND id = ?", (client_id, contact_id))
        result = self.c.fetchone()
        if result is not None:
            return result[0]
        else:
            return None

    def carregar_contatos(self):
        self.c.execute("SELECT * FROM contatos")
        return self.c.fetchall()

    def salvar_contatos(self):
        self.conn.commit()

# Cria um objeto que representa o servidor
server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))
server.register_instance(ContatosServer())

# Aguarda por chamadas de função
server.serve_forever()
