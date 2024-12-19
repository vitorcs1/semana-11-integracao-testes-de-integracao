import unittest;
from aluno import AlunoClass; 
from turma import TurmaClass;
from conexao import ConexaoClass;
import mongomock; #Projeto: https://github.com/mongomock/mongomock


class alunoTest(unittest.TestCase):
  @mongomock.patch(servers=(('localhost.com', 27017),))
  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...');
    self.aluno = AlunoClass('Fabio', 'Teixeira', 10);
    self.turma = TurmaClass();
    self.turma.cadastrarAlunos([self.aluno]);
    self.conexao = ConexaoClass.conexaoMongoDB(self, url = 'localhost.com', banco = 'faculdade')

  def test_salvarAluno(self):
    resposta = self.aluno.salvar(conexao=self.conexao, colecao='alunos')
    
    colecao_mock = self.conexao['alunos']
    aluno_inserido = colecao_mock.find_one({'primeiro_nome': 'Fabio', 'sobrenome': 'Teixeira', 'nota': 10})
    
    self.assertIsNotNone(aluno_inserido, 'O aluno não foi salvo no banco de dados')
    self.assertEqual(aluno_inserido['primeiro_nome'], 'Fabio', 'O primeiro nome do aluno não foi salvo')
    self.assertEqual(aluno_inserido['sobrenome'], 'Teixeira', 'O sobrenome do aluno não foi salvo')
    self.assertEqual(aluno_inserido['nota'], 10, 'A nota do aluno não foi salva')
    self.assertEqual(resposta, True, 'O método salvar não retornou o valor esperado!')


  def test_salvarTurma(self):   
    resposta = self.turma.salvar(conexao = self.conexao, colecao = 'turma');  
    self.assertEqual(True, resposta, 'Turma cadastrada incorretamente!');

if __name__ == "__main__":
  unittest.main()