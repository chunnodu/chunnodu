from rdflib import Graph

g = Graph()
g.parse("content/foaf.rdf")

print(f"Graph loaded successfully with {len(g)} statements.")

# Example: Print all people you know
from rdflib.namespace import FOAF
print("\nPeople you know:")
for person in g.subjects(FOAF.knows, None):
    for known in g.objects(person, FOAF.knows):
        name = g.value(known, FOAF.name)
        print(f"- {name}")
