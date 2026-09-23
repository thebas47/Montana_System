from dataclasses import dataclass

@dataclass
class Nf_doc:
    week: str
    state: str
    nf_num: str
    cnpj: str
    provider: str
    competency: str
    value: str

    def __str__(self):
        return(
            f"\nSemana: {self.week}\n"
            f"Estado: {self.state}\n"
            f"N° NF: {self.nf_num}\n"
            f"CNPJ: {self.cnpj}\n"
            f"Prestador: {self.provider}\n"
            f"Competência: {self.competency}\n"
            f"Valor: {self.value}\n"
        )
