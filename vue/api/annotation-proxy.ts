export const config = {
  runtime: 'experimental-edge',
};

type GraphQlData = { [key: string]: any, [index: number]: never };

interface GraphQlResponse<T extends GraphQlData> {
  data: T;
  errors?: Array<{ message: string }>;
}

interface Category {
  pk: Number;
  name: String;
  icon: String;
  color: String;
  commentsEnabled: Boolean;
}

interface State {
  pk: Number;
  name: String;
  decoration: String;
}

interface Attachement {
  document: String;
  myOrder: Number;
}

interface Annotations {
  id: String;
  pk: Number;
  kind: String;
  rating: Number;
  data: Object;
  category: Category;
  state: State;
  attachements: Attachement[];
}

async function graphQLFetch<T extends GraphQlData>(
  url: string,
  query: string,
  variables = {}
): Promise<T> {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query, variables }),
  });
  if (!res.ok) {
    throw new Error(`${res.status}: ${res.statusText}`);
  }

  const graphQlRes: GraphQlResponse<T> = await res.json();
  if (graphQlRes.errors) {
    throw new Error(graphQlRes.errors.map((err) => err.message).join("\n"));
  }
  return graphQlRes.data.workspace;
}

export default async (req) => {
  console.log(JSON.stringify(req));

  const url = "";
  const query = `query getworkspace($wshash: ID!, $lang: LanguageCodeEnum!) {
    workspace(id: $wshash) {
      annotations {
        id
        pk
        kind
        rating
        data
        category {
          pk
          name(languageCode: $lang)
          icon
          color
          commentsEnabled
        }
        state {
          pk
          name(languageCode: $lang)
          decoration
        }
        attachements {
          document
          myOrder
        }
      }
    }
  }`;
  const variables = {
      wshash: "V29ya3NwYWNlTm9kZTpZRjA2Wg==",
      lang: "de"
  }

  const { workspace } = await graphQLFetch<{ workspace: { annotations: Annotations[] } }>(
    url,
    query,
    variables
  );

  new Response(JSON.stringify(workspace));
}