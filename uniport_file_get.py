
from Bio import ExPASy
from Bio import SwissProt
import pandas as pd

protein_id = "Q9UHB7"
def get_uniport_protein_sequence(uniprot_id):
    informations=[]

    with ExPASy.get_sprot_raw(uniprot_id) as handle:
        record = SwissProt.read(handle)
        informations.append({"description":record.description,
                                 "features":record.features,
                                 "protein_existence":record.protein_existence,
                                 "sequence":record.sequence,
                                 "accessions":record.accessions,
                                 "entry_name":record.entry_name,
                                 "cross_references":record.cross_references,
                                 "seqinfo":record.seqinfo ,
                                 "sequence_length":record.sequence_length ,
                                 "host_taxonomy_id":record.host_taxonomy_id,"orgclss":record.organism_classification})
        return informations

def multi_get_uniport_protein_sequence(protein_id_list=[]):
    data = []

    for protein_id in protein_id_list:
        handle = ExPASy.get_sprot_raw(protein_id)
        record = SwissProt.read(handle)
        protein_sequence = record
        data.append({
            "Protein ID": protein_id,
            "Protein Sequence": protein_sequence.sequence,
            "description":protein_sequence.description,
            "features": protein_sequence.features,
            "protein_existence": protein_sequence.protein_existence,
            "accessions": protein_sequence.accessions,
            "entry_name": protein_sequence.entry_name,
            "cross_references": protein_sequence.cross_references,
            "seqinfo": protein_sequence.seqinfo,
            "sequence_length": protein_sequence.sequence_length,
            "host_taxonomy_id": protein_sequence.host_taxonomy_id
        })
    df = pd.DataFrame(data)
    return df


a=multi_get_uniport_protein_sequence(protein_id_list = ["P04637","Q9UHB7"]  )
print(a)