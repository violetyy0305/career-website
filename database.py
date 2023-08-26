from sqlalchemy import create_engine, text
#import os

#db_connection_string = os.environ['DB_CONNECTION_STRING']
db_connection_string = "mysql+pymysql://oz86mmb94z2zy9o6tlia:pscale_pw_R8IL4f2NSNKUaESeCeGP2bACuLioJaEUOx7k86lYwfH@aws.connect.psdb.cloud/mindgenomics?charset=utf8mb4"

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


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id=:val"),
                          {"val": id})
    row = result.all()
    if len(row) == 0:
      return None
    else:
      keys = list(result.keys())
      d = {}
      for i in range(len(row[0])):
        d[keys[i]] = row[0][i]
      return d

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query=text("insert into applications(job_id, full_name, email, education) values (:job_id, :full_name, :email, :education)")

    conn.execute(query,
                {"job_id":job_id,
                "full_name":data['full_name'],
                "email":data['email'],
                "education":data['education']})
    