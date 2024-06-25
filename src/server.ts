import fastify, { FastifyReply, FastifyRequest } from "fastify";
import fjwt, { JWT } from "@fastify/jwt";
import userRoutes from "./modules/users/user.router";
import { userSchemas } from "./modules/users/user.schema";
import fastifySwagger from "@fastify/swagger";
import fastifySwaggerUi from "@fastify/swagger-ui";
import { jwtConstant } from "./configs";

declare module "fastify" {
  interface FastifyRequest {
    jwt: JWT;
  }
  export interface FastifyInstance {
    authenticate: any;
  }
}

function buildServer() {
  const server = fastify();

  server.get("/healthcheck", async function () {
    return { status: "OK" };
  });

  // server.addHook("preHandler", (req, reply, next) => {
  //   req.jwt = server.jwt;
  //   return next();
  // });

  for (const schema of [...userSchemas]) {
    server.addSchema(schema);
  }

  // server.register(fjwt, {
  //   secret: jwtConstant.secret,
  // });

  // server.decorate(
  //   "authenticate",
  //   async (request: FastifyRequest, reply: FastifyReply): Promise<void> => {
  //     try {
  //       await request.jwtVerify();
  //     } catch (e) {
  //       return reply.send(e);
  //     }
  //   }
  // );

  // build swagger
  const swaggerOptions = {
    swagger: {
      info: {
        title: "My Title",
        description: "My Description.",
        version: "1.0.0",
      },
      host: "localhost:3000",
      schemes: ["http", "https"],
      consumes: ["application/json"],
      produces: ["application/json"],
    },
  };

  const swaggerUiOptions = {
    routePrefix: "/docs",
    exposeRoute: true,
  };

  server.register(fastifySwagger, swaggerOptions);
  server.register(fastifySwaggerUi, swaggerUiOptions);

  server.register(userRoutes, { prefix: "api/users" });

  return server;
}

export default buildServer;
