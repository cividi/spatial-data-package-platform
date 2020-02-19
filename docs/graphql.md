# graphql

go to '/graphql/' which opens the GraphiQL browser

## sample queries

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


