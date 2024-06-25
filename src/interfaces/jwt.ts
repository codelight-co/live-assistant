import { JWT } from "@fastify/jwt";

export interface FastifyJWT {
  user: {
    id: number;
    email: string;
    name: string;
  };
}

export interface FastifyRequest {
  jwt: JWT;
}

export interface FastifyInstance {
  authenticate: any;
}
