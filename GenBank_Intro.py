"""GenBank intro demonstrates how to get organism, gene or nucleotide
    information by using Bio module."""

"""The Bio.Entrez.esearch() function will search any of the NCBI databases. This function takes the following arguments:
db : The database to search. For example, this field can be nucleotide for GenBank or pubmed for PubMed.
term: The search term for the "Query" field. You can use search tags here."""



from Bio import Entrez

# email for any problems for contact
Entrez.email = "jacob.elvig@gmail.com"

# write out the query for clear visualization
query = '"Isopyrum"[Organism] AND ("2007/12/20"[Publication Date] : "2011/11/06"[Publication Date])'

# Store the query results
handle = Entrez.esearch(db='nucleotide', term=query)

# read the return
record = Entrez.read(handle)

# for this question only count the rows
count = record['Count']
print(count)            # -> 14
