class AlunoClass:
  def __init__(self, nome, sobrenome, nota):    
    self.nome = nome;
    self.sobrenome = sobrenome;
    self.nota = nota;

  def mostrarAluno(self):
    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota);    

  def salvar(self, conexao, colecao):    
    try:
        db_colecao = conexao[colecao]
        
        db_colecao.insert_one({
            'primeiro_nome': self.nome,
            'sobrenome': self.sobrenome,
            'nota': self.nota
        })
        
        return True
    except Exception as e:
        print(f"Erro ao salvar aluno: {e}")
        return False