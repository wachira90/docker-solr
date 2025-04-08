Sure! Here's a step-by-step guide to setting up **Apache Solr 9.8.1** with **JWT Authentication** using Docker, including a sample `docker-compose.yml` and `security.json` file.

---

## ✅ Step-by-step Setup for Solr JWT Auth (Docker)

### 🧩 Step 1: Create your project directory
```bash
mkdir solr-jwt-auth
cd solr-jwt-auth
```

---

### 🗂️ Step 2: Create `docker-compose.yml`

```yaml
version: '3.8'

services:
  solr:
    image: public.ecr.aws/docker/library/solr:9.8.1
    container_name: solr
    ports:
      - "8983:8983"
    volumes:
      - ./security.json:/var/solr/data/security.json
    environment:
      - SOLR_AUTH_TYPE=basic
    command:
      - solr-precreate
      - mycore
```

🔹 This launches Solr and loads the `security.json` for configuring JWT authentication.

---

### 🛡️ Step 3: Create `security.json`

Create a file called `security.json` in the same directory:

```json
{
  "authentication": {
    "class": "solr.JWTAuthPlugin",
    "jwt": {
      "issuer": "my-issuer",
      "jwksUrl": "https://your-auth-domain.com/.well-known/jwks.json",
      "audiences": ["solr"],
      "required": true
    }
  },
  "authorization": {
    "class": "solr.RuleBasedAuthorizationPlugin",
    "user-role": {
      "admin-user": ["admin"]
    },
    "permissions": [
      {
        "name": "security-edit",
        "role": "admin"
      },
      {
        "name": "all",
        "role": "admin"
      }
    ]
  }
}
```

🔸 Notes:
- Replace `"https://your-auth-domain.com/.well-known/jwks.json"` with the URL to your public JWT keys (JWKS endpoint).
- Replace `"my-issuer"` with your JWT's `iss` claim.
- `"audiences"` should match the `aud` claim in your JWT.
- `admin-user` is the subject (`sub`) claim in the JWT that has admin rights.

---

### 🚀 Step 4: Start the container

```bash
docker-compose up
```

Solr should now be running at: [http://localhost:8983](http://localhost:8983)

You will need to include a **valid JWT token** in the `Authorization` header when accessing the Solr UI or API:

```
Authorization: Bearer <your-jwt-token>
```

---

### 🔍 Step 5: Testing the JWT Auth

Use `curl` with a valid token:

```bash
curl -H "Authorization: Bearer <your-jwt-token>" http://localhost:8983/solr/admin/info/system
```

---

Would you like a simple JWKS server mock setup (for testing), or a working JWT token generation example as well?
