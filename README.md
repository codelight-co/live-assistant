- Create a Virtual Environment using

```bash
sudo pip install virtualenv
virtualenv env
```

- Activate the virtualenv

```bash
env\Scripts\activate # for windows
source env/bin/activate # for linux and mac
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Setting up environment variables

| Key     | Value |
| ----------- | ----------- |
| DATABASE_URL   | postgresql://user:password@host:port/db|

- To run the project

```bash
uvicorn main:app
```