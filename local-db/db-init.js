db = db.getSiblingDB("forte-db");

db.createCollection("transactions", {
    validator: {
       $jsonSchema: {
          bsonType: "object",
          required: [ "transaction_id", "customer_id", "amount", "category", "date", "type", "deactivated"],
          properties: {
            transaction_id: {
                bsonType: "string",
                description: "must be a string and is required"
             },
             customer_id: {
                bsonType: "string",
                description: "must be a string and is required"
             },
             amount: {
                bsonType: "decimal",
                description: "must be a float if the field exists"
             },
             category: {
                bsonType: "string",
                description: "must be a string and is required"
             },
             date: {
               bsonType: "date",
               description: "must be a date and is required"
            },
             type: {
                enum: [ "income", "expense"],
                description: "must be income or expense"
             },
             deactivated: {
               bsonType: "bool",
            }
          }
       }
    }
 });

 db.transactions.createIndex( { transaction_id: 1 }, { unique: true } );

 db.transactions.insertMany([
    { "transaction_id": "bd7b69fa-9207-4996-91cd-b7eec3fce21b", "customer_id": "bd7b69fa-9207-4996-91cd-b7eec3fce21a", "amount": Decimal128("50.1"), "category": "c1",  "type": "income",
      "deactivated": false, "date": ISODate("2025-01-16T18:28:55Z") },
    { "transaction_id": "8c002a9b-6532-4125-8b58-e2af55a7d60e", "customer_id": "bd7b69fa-9207-4996-91cd-b7eec3fce21a", "amount": Decimal128("100.1"), "category": "c2", "type": "expense",
      "deactivated": false, "date": ISODate("2025-02-16T18:28:55Z") },
    { "transaction_id": "70032cd2-0c22-41cf-bf02-b77f52dcdb76", "customer_id": "70032cd2-0c22-41cf-bf02-b77f52dcdb76", "amount": Decimal128("50.1"), "category": "c1", "type": "income",
      "deactivated": false, "date": ISODate("2025-01-16T18:28:55Z") },
    { "transaction_id": "88d9655b-8364-4062-9153-ad35766d3eb9", "customer_id": "70032cd2-0c22-41cf-bf02-b77f52dcdb76", "amount": Decimal128("100.1"), "category": "c2", "type": "expense",
      "deactivated": false, "date": ISODate("2025-02-16T18:28:55Z") },
    { "transaction_id": "6dddde02-02fa-4027-b469-ab2e3e7dea62", "customer_id": "70032cd2-0c22-41cf-bf02-b77f52dcdb76", "amount": Decimal128("150.1"), "category": "c2", "type": "expense",
      "deactivated": false, "date": ISODate("2025-03-16T18:28:55Z") }
]);
