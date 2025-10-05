const baseUrl = process.env.NEXT_PUBLIC_BACKEND_URL as string;
const port = process.env.NEXT_PUBLIC_BACKEND_PORT as string;

let rawUrl = baseUrl.replace(/\/+$/, "");

if (!rawUrl.match(/:\d+$/) && !rawUrl.startsWith("https://")) {
  rawUrl = `${rawUrl}:${port}`;
}

if (
  rawUrl &&
  !rawUrl.startsWith("http://localhost") &&
  !rawUrl.startsWith("https://localhost")
) {
  if (!rawUrl.startsWith("http://") && !rawUrl.startsWith("https://")) {
    rawUrl = `https://${rawUrl}`;
  }
}

if (!rawUrl.endsWith("/v1")) {
  rawUrl = rawUrl.replace(/\/+$/, "") + "/v1";
}

export const API_URL = rawUrl;
