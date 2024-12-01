import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const articleApi = createApi({
  reducerPath: "articleApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000/api/article",
  }),
  endpoints: (builder) => ({
    getSummary: builder.query({
      query: (params) => ({
        url: "/summarize",
        method: "POST",
        headers: {
          "article-url": params.articleUrl,
        },
      }),
    }),
  }),
});

export const { useLazyGetSummaryQuery } = articleApi;
