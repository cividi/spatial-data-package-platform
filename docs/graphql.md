# GraphQL

_Notes on our usage of the GraphQL-based query API._

## sample queries

go to '/graphql/' which opens the GraphiQL browser

### gemeinden

```graphql
{
  municipalities {
    edges {
      node {
        bfsNumber
        name
      }
    }
  }
}
```

The `MunicipalityNode` has the fields
- id: ID!, The ID of the object.
- name: String!
- canton: MunicipalityCanton!, enum
- bfsNumber: Int

### snapshots

#### all

```graphql
{
  snapshots {
    edges {
      node {
        id
        data
        slugHash
        screenshot {
          url
        }
      }
    }
  }
}
```
