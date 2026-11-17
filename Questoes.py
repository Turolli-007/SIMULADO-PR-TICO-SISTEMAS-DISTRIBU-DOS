Problema A
A empresa estabeleceu que apenas dois pedidos podem estar em processamento
simultaneamente.
Entretanto, o código está configurado para permitir três.
Localize a configuração responsável por esse limite e faça a correção necessária.

# Controle de concorrência
MAXIMO_SIMULTANEO = 2 #Foi realizado a troca do numero 3 pelo numero 2 
semaforo = threading.Semaphore(
    MAXIMO_SIMULTANEO
)

Problema B 

Após o processamento dos pedidos, o estoque do servidor principal passa de 10 para 7
unidades.
Entretanto, a réplica continua informando 10 unidades.
Localize a função responsável pela sincronização e corrija o código para que a réplica
receba o estoque atualizado do servidor principal.

def sincronizar():
    replica["estoque"] = principal["estoque"] #estava para a replica copiar a propria funcao, alterei de replica para principal 
def consultar_estoque():
    if principal["online"]:
        return (
            "PRINCIPAL",
            principal["estoque"]

Problema C

O sistema precisa continuar funcionando quando o servidor principal estiver indisponível.
Entretanto, após a simulação de falha, o programa apresenta: "Consulta após falha: INDISPONIVEL None"
Localize a condição incorreta na função de consulta e faça a alteração para que o sistema
utilize a réplica quando o principal estiver offline.

def consultar_estoque():
    if principal["online"]:
        return (
            "PRINCIPAL",
            principal["estoque"]
        )
    if replica["online"]: #no original estava Principal e nao replica 
        return (
            "REPLICA",
            replica["estoque"]
        )
    return "INDISPONIVEL", None


