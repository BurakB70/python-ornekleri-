from Bio import SeqIO
from Bio.SeqUtils import molecular_weight ,IsoelectricPoint,CheckSum
from  Bio.SeqUtils import ProtParamData,MeltingTemp
import pandas as pd

class prtoeomic:
    parse_file =" "
    formatt =" "
    sequences = []
    dfframe_or_dict=True
    response=[]
    def __init__(self, parser_file,formatt,dfframe_or_dict):
        self.parse_file = parser_file
        self.formatt=formatt
        self.dfframe_or_dict =dfframe_or_dict

    def parse_to_dataframe(self):
        self.response
        sequences =[]
        self.sequences = sequences
        with open(self.parse_file, "r") as handle:
            for record in SeqIO.parse(handle,self.formatt):
                sequences.append({
                    "id": record.id,
                    "description": record.description,
                    "sequence":str( record.seq),
                    "annotations":record.annotations,
                    "dbxrefs":record.dbxrefs

                })
        if  self.dfframe_or_dict== True:
            df = pd.DataFrame(sequences,)
            self.response=df
            return self.response
        else:
            self.response=sequences
            return self.response
    def some_analiz(self):
        if self.dfframe_or_dict==True:
            copy_data=self.response
            for data in copy_data["sequence"]:
                weight =molecular_weight(data,seq_type="protein")
                copy_data["molecular_weight"]=weight


                self.lastdata =copy_data.copy()
                return self.lastdata
        else:
            self.dfframe_or_dict = True
            return self.some_analiz()
  



# sp|O00257|CBX4_HUMAN E3 SUMO-protein ligase CBX4 OS=Homo sapiens OX=9606 GN=CBX4 PE=1 SV=3

fasta_file = "uniprotkb_p53_AND_proteins_with_27_2024_02_04.fasta"
parser_read = prtoeomic(fasta_file,"fasta",True)
df = parser_read.parse_to_dataframe()
som=parser_read.some_analiz()
print(som)