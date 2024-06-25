# Fastify-Typescript
## How to use

### 1. install dependencies

Install Node dependencies:

`npm install`

### 2. Set up the database

This uses [Postgres database](https://www.postgresql.org/).

To set up your database, run:

```sh
npm run prisma:save
npm run prisma:dep
```

### 3. Generate Prisma Client (type-safe database client)

Run the following command to generate [Prisma Client](https://www.prisma.io/docs/reference/tools-and-interfaces/prisma-client/generating-prisma-client):

```sh
npx prisma migrate dev --name <name>
npm run prisma:gen
```

### 4. Start the Fastify server

Launch your Fastify server with this command:

```sh
npm run dev
```

## For Build Generation

Build server with command: 

```sh
npm run build
```

## Prisma documentation
- Check out the [Prisma docs](https://www.prisma.io/docs/)
- Check out the [Fastify docs](https://www.fastify.io/docs/latest/)
