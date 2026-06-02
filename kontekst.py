class DbConnection:
    def __enter__(self):
        self.conn = connect_db()
        return self.conn
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        return False

with DbConnection() as db:
    db.execute('SELECT 1')
