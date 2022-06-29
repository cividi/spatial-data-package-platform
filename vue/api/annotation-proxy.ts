import type { VercelRequest, VercelResponse } from '@vercel/node';
import fetch from 'node-fetch';

type GraphQlData = { [key: string]: any, [index: number]: never };

interface GraphQlResponse<T extends GraphQlData> {
  data: T;
  errors?: Array<{ message: string }>;
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
  const graphQlRes: GraphQlResponse<T> = (await res.json() as GraphQlResponse<T>);
  if (graphQlRes.errors) {
    throw new Error(graphQlRes.errors.map((err) => err.message).join("\n"));
  }
  return graphQlRes.data;
}

export default async (req: VercelRequest, res: VercelResponse) => {
  const url = `${process.env.VUE_APP_GRAPHQL_URI}`;
  const wshash = `WorkspaceNode:${req.query.workspace}` || null;
  const lang = req.query.lang || 'de';

  if(url && wshash && lang) {
    const wshash_base64 = Buffer.from(wshash).toString('base64');

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
        wshash: wshash_base64,
        lang
    }

    const { workspace } = await graphQLFetch<{ workspace: Object }>(
      url,
      query,
      variables
    );
    
    res.setHeader('Cache-Control', 'max-age=0, s-maxage=900, stale-while-revalidate');
    return res.status(200).json({ workspace });
  }
}