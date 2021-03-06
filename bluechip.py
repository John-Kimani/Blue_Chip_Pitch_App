from app import create_app,db
from app.models import Pitch, User


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User, Pitch=Pitch)
