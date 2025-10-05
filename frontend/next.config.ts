import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  eslint: {
    ignoreDuringBuilds: true,
  },
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "*",
        port: "",
        pathname: "**",
      },
      {
        protocol: "http",
        hostname: "*",
        port: "",
        pathname: "**",
      },
      {
        protocol: "http",
        hostname: "localhost",
        port: process.env.NEXT_PUBLIC_BACKEND_PORT,
        pathname: "/v1/assets/**",
      },
    ],
    unoptimized: true,
  },
  output: "export",
  trailingSlash: true,
  distDir: "out",
};

export default nextConfig;
