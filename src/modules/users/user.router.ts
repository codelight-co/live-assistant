import { FastifyInstance } from "fastify";
import { $ref } from "./user.schema";
import { getUsersHandler, registerUserHandler } from "./user.controller";

async function userRoutes(server: FastifyInstance) {
  server.post(
    "/",
    {
      schema: {
        tags: ["User"],
        body: $ref("createUserSchema"),
        response: {
          201: $ref("createUserResponseSchema"),
        },
      },
    },
    registerUserHandler
  );

  server.get(
    "/",
    {
      // preHandler: [server.authenticate],
      schema: {
        tags: ["User"],
      },
    },
    getUsersHandler
  );
}

export default userRoutes;
