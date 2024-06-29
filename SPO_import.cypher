// Create RELATION relationship for entities
LOAD CSV WITH HEADERS FROM 'file:///SPO_result.csv' AS row
MERGE (subject:Entity {name: row.Subject})
MERGE (object:Entity {name: row.Object})
MERGE (subject)-[:RELATION {type: row.Predicate}]->(object)