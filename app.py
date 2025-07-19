from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'segredo_super_secreto'
DB_NAME = 'emails.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def login():
    return render_template('TELA DE LOGIN - SAFEMIND.html')

@app.route('/login', methods=['POST'])
def do_login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    print(f"Tentativa de login com email: {email}")  # DEBUG

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE email = ? AND senha = ?', (email, senha))
    user = cursor.fetchone()
    conn.close()

    if user:
        session['usuario'] = email
        print(f"Login bem-sucedido: {email}")  # DEBUG
        return redirect(url_for('inicio'))
    else:
        print("Login falhou: email ou senha inválidos")  # DEBUG
        return render_template('TELA DE LOGIN - SAFEMIND.html', erro='Email ou senha inválidos')

@app.route('/inicio')
def inicio():
    print(f"Usuário na sessão: {session.get('usuario')}")  # DEBUG
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('TELA DE INICIO - SAFEMIND.html', usuario=session['usuario'])

@app.route('/pesquisa')
def pesquisa():
    return render_template('TELA DE PESQUISA - SAFEMIND.html')

@app.route('/explorar')
def explorar():
    return render_template('TELA EXPLORAR - SAFEMIND.html')

@app.route('/configuracoes')
def configuracoes():
    return render_template('TELA DE CONFIGURAÇÕES - SAFEMIND.html')

@app.route('/conta')
def conta():
    return render_template('TELA DE CONTA - SAFEMIND.html')

@app.route('/teste-temperamento')
def teste_temperamento():
    return render_template('TELA DE TESTES - SAFEMIND.html')

@app.route('/teste-linguagem-amor')
def teste_linguagem_amor():
    return render_template('TELA DE TESTES 5 LINGUAGEM DO AMOR - SAFEMIND.html')

@app.route('/dra-jaqueline')
def dra_jaqueline():
    return render_template('TELA DRA. JAQUELINE - SAFEMIND.html')

@app.route('/dr-lucas')
def dr_lucas():
    return render_template('TELA DR. LUCAS - SAFEMIND.html')

@app.route('/dra-priscila')
def dra_priscila():
    return render_template('TELA DRA. PRISCILA - SAFEMIND.html')

@app.route('/dra-janaina')
def dra_janaina():
    return render_template('TELA DRA. JANAINA - SAFEMIND.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)