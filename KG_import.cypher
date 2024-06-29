// Step 1: Create BELONGS_TO relationship for type
LOAD CSV WITH HEADERS FROM 'file:///KG_result.csv' AS row
WITH row
WHERE row.Predicate = 'type'
MERGE (entity:Entity {name: row.Subject})
MERGE (ontology:Category {name: row.Object})
MERGE (entity)-[:BELONGS_TO]->(ontology);

// Step 2: Create HAS_PROPERTY relationship for other predicates
LOAD CSV WITH HEADERS FROM 'file:///KG_result.csv' AS row
WITH row
WHERE row.Predicate <> 'type'
MERGE (entity:Entity {name: row.Subject})
MERGE (attribute:Attribute {name: row.Predicate, value: row.Object})
MERGE (entity)-[:HAS_PROPERTY {property: row.Predicate}]->(attribute);