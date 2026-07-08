from datetime import datetime


def calcular_precisa_de_rega(ultima_rega, frequencia_rega_dias) -> bool:
    dias_desde_ultima_rega = (datetime.now() - ultima_rega).days
    return dias_desde_ultima_rega >= frequencia_rega_dias

def parser_id_mongo(documento):
    if documento is None:
        return None

    return {
        "id": str(documento.id),
        "nome": documento.nome,
        "especie": documento.especie,
        "frequencia_rega_dias": documento.frequencia_rega_dias,
        "exposicao_solar": documento.exposicao_solar,
        "ambiente": documento.ambiente,
        "observacoes": documento.observacoes,
        "criado_em": documento.criado_em.isoformat(),
        "atualizado_em": documento.atualizado_em.isoformat(),
        "precisa_de_rega": calcular_precisa_de_rega(documento.ultima_rega, documento.frequencia_rega_dias),
    }


def parser_lista_ids_mongo(documentos):
    return [parser_id_mongo(documento) for documento in documentos]