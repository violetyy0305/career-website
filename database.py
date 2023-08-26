from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []

    keys = list(result.keys())

    for job in result.all():
      d = {}
      for i in range(len(job)):
        d[keys[i]] = job[i]
      jobs.append(d)
  return jobs
