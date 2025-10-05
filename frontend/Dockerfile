FROM node:18-alpine AS builder

WORKDIR /app
COPY package.json ./
RUN npm install --legacy-peer-deps
COPY . .
RUN rm -rf .next/ dist/
RUN npm run build

FROM node:18-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/out ./out

USER nextjs

EXPOSE 3000
ENV PORT 3000

CMD ["node", "server.js"]