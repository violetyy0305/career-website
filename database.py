from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://ekpm9fcfuyubgabwu1nt:pscale_pw_sHjTCvTJOLiqzEvqhO1noa7taqDEilVXvJ7M1MRF03H@aws.connect.psdb.cloud/mindgenomics?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})
'''
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs
'''


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
