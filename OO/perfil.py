from datetime import date

class Perfil:

    quantidade_usuarios = 0
    def __init__(self, nome: str, sobrenome: str, nascimento: date,
                 endereco: str, telefone: str, email: str, estado_civil: str,
                 etnia: str, profissao: str, renda:float, habilitacao:bool):
        try:
            if isinstance(nome, str):
                if len(nome) < 2 or len(nome) > 20:
                    raise ValueError("Nome deve conter entre 2 e 20 caracteres")

            else:
                raise TypeError("Nome deve ser um texto!")

            if isinstance(sobrenome, str):
                if len(sobrenome) < 2 or len(sobrenome) > 150:
                    raise ValueError("Sobrenome deve conter entre 2 e 150 caracteres")

            else:
                raise TypeError("Sobrenome deve ser um texto!")

            if isinstance(nascimento, date):
                limite = date.today()
                if nascimento > limite.replace(year=limite.year - 18):
                    raise ValueError("A idade mínima é de 18 anos")
                elif nascimento < limite.replace(year=limite.year - 100):
                    raise ValueError("A idade máxima é de 100 anos completos")

            else:
                raise TypeError("Sobrenome deve ser um texto!")

            if isinstance(telefone, str):
                if len(telefone) < 10 or len(telefone) > 16:
                    raise ValueError("Telefone deve conter entre 10 e 16 caracteres")

            else:
                raise TypeError("Telefone deve ser um texto!")


        except Exception as error:
            raise error

        else:
            self.nome = nome
            self.sobrenome = sobrenome
            self.nascimento = nascimento
            self.endereco = endereco
            self.telefone = telefone
            self.email = email
            self.estado_civil = estado_civil
            self.etnia = etnia
            self.profissao = profissao
            self.renda = renda
            self.habilitacao = habilitacao
            Perfil.quantidade_usuarios = Perfil.quantidade_usuarios + 1
            self.id = Perfil.quantidade_usuarios

    def __str__(self) -> str:
        saida = (f"ID: {self.id}"
                 f"\nNome: {self.nome} {self.sobrenome}"
                 f"\nData de nascimento: {self.nascimento} "
                 f"\nEndereço: {self.endereco}, telefone: {self.telefone}"
                 f"\nEmail: {self.email}"
                 f"\nEstado civil: {self.estado_civil}"
                 f"\nEtnia: {self.etnia}"
                 f"\nProfissão: {self.profissao}, renda: R${self.renda}"
                 f"\nHabilitação: {self.habilitacao}")
        return saida
