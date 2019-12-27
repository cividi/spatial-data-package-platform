# alebmic (sqlalchemy migrations)

# register model

add to `alembic/env.py`

```python
from user.models import UserModel
target_metadata = [UserModel.metadata]
```

# create migration

```python
alembic revision --autogenerate -m "added user table"
```

# migrate

```bash
# create tables/changes from alembic
alembic upgrade head
```
