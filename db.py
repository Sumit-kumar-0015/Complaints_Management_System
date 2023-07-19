import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS students(
           id Integer Primary Key,
           enroll_id text,
           student_name text,
           course_name text,
           email text,
           course text,
           college_name text,
           complaint text
         )
         """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self,enroll_id,student_name,course_name,email,course,college_name,complaint):
        self.cur.execute("insert into students values (NULL,?,?,?,?,?,?,?)",
                         (enroll_id,student_name,course_name,email,course,college_name,complaint))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from students")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self,id):
        self.cur.execute("delete from students where id=?",(id,))
        self.con.commit()

    # Update a Record in DB
    def update(self,id,enroll_id,student_name,course_name,email,course,college_name,complaint):
        self.cur.execute("update students set enroll_id=?,student_name=?,course_name=?,email=?,course=?,college_name=?,complaint=? where id=?",
                         (enroll_id,student_name,course_name,email,course,college_name,complaint,id))
        self.con.commit()
