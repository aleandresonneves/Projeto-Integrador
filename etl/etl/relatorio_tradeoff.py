import json
from pathlib import Path

def gerar_relatorio(resumo):

    pasta = Path("relatorios")
    pasta.mkdir(exist_ok=True)

    total = resumo["clientes"]
    revisao = resumo["revisao_manual"]

    percentual = (
        ((total - revisao) / total) * 100
        if total else 0
    )

    relatorio = {
        "total_clientes": total,
        "revisao_manual": revisao,
        "sem_revisao_manual": total - revisao,
        "percentual_sem_revisao": round(percentual, 2),
        "divergencias_cep_bairro":
            resumo["divergencias_cep_bairro"],
        "cnpj_invalidos":
            resumo["cnpj_dv_invalido"],
        "telefones_invalidos":
            resumo["telefones_invalidos"],
        "emails_invalidos":
            resumo["emails_invalidos"]
    }

    caminho = pasta / "indicadores_tradeoff.json"

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            relatorio,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

    print("Relatório de trade-off gerado!")